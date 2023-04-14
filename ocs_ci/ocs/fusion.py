import os
import logging
import yaml

from ocs_ci.ocs.exceptions import ConfigurationError
from ocs_ci.framework import config
from ocs_ci.helpers import helpers
from ocs_ci.utility.managedservice import remove_header_footer_from_key
from ocs_ci.utility.templating import load_yaml, Templating
from ocs_ci.utility.utils import get_ocp_version, exec_cmd
from ocs_ci.ocs import constants
from ocs_ci.ocs.resources.catalog_source import CatalogSource

logger = logging.getLogger(name=__file__)

FUSION_TEMPLATE_DIR = os.path.join(constants.TEMPLATE_DIR, "fusion-aas")


def create_fusion_monitoring_resources():
    """
    Create resources used for Managed Fusion aaS Monitoring
    """
    templating = Templating(base_path=FUSION_TEMPLATE_DIR)
    project_name = "managed-fusion"
    logger.info(f"Creating {project_name} project")
    helpers.create_project(project_name=project_name)
    logger.info("Creating an OperatorGroup")
    og_path = os.path.join(FUSION_TEMPLATE_DIR, "operatorgroup.yaml")
    og_data = load_yaml(og_path)
    helpers.create_resource(**og_data)
    logger.info("Creating a CatalogSource")
    catsource_data = dict()
    catsource_data["image"] = config.ENV_DATA["fusion_catalogsource"]
    template = templating.render_template(
        "catalogsource.yaml.j2",
        catsource_data,
    )
    template = yaml.load(template, Loader=yaml.Loader)
    helpers.create_resource(**template)
    logger.info("Creating a Subscription")
    og_path = os.path.join(FUSION_TEMPLATE_DIR, "subscription.yaml")
    og_data = load_yaml(og_path)
    helpers.create_resource(**og_data)
    logger.info("Waiting for catalogsource")
    catalog_source = CatalogSource(
        resource_name="managed-fusion-catsrc",
        namespace="managed-fusion",
    )
    catalog_source.wait_for_state("READY")
    logger.info("Creating a monitoring secret")
    secret_data = dict()
    secret_data["pagerduty_config"] = config.ENV_DATA["pagerduty_config"]
    secret_data["smtp_config"] = config.ENV_DATA["smtp_config"]
    template = templating.render_template(
        "monitoringsecret.yaml.j2",
        secret_data,
    )
    template = yaml.load(template, Loader=yaml.Loader)
    helpers.create_resource(**template)


def deploy_odf():
    """
    Create openshift-storage namespace and deploy managedFusionOffering CR there.
    """
    templating = Templating(base_path=FUSION_TEMPLATE_DIR)
    ns_name = "openshift-storage"
    logger.info(f"Creating {ns_name} namespace")
    exec_cmd(["oc", "create", "ns", ns_name])
    logger.info("Creating the offering CRD")
    offering_data = dict()
    offering_data["ocp_version"] = get_ocp_version()
    offering_data["size"] = config.ENV_DATA["size"]
    public_key = config.AUTH.get("managed_service", {}).get("public_key", "")
    if not public_key:
        raise ConfigurationError(
            "Public key for Managed Service not defined.\n"
            "Expected following configuration in auth.yaml file:\n"
            "managed_service:\n"
            '  private_key: "..."\n'
            '  public_key: "..."'
        )
    public_key_only = remove_header_footer_from_key(public_key)
    offering_data["onboarding_validation_key"] = public_key_only
    template = templating.render_template(
        "managedfusionoffering.yaml.j2",
        offering_data,
    )
    template = yaml.load(template, Loader=yaml.Loader)
    helpers.create_resource(**template)