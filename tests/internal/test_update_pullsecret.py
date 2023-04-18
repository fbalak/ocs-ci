from ocs_ci.framework.testlib import managed_service_required
from ocs_ci.ocs.managedservice import update_pull_secret


@managed_service_required
def test_update_pull_secret():
    """
    Perform update of pull secret to to get access to ocs-registry to access
    quay.io/rhceph-dev/ocs-registry:latest
    """
    update_pull_secret()
