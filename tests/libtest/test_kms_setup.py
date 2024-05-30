import logging
import time

from ocs_ci.framework.testlib import libtest
from ocs_ci.utility import kms as KMS

logger = logging.getLogger(__name__)


@libtest
def test_setup_kms():
    """
    Test of RHV get_vm_status() method implementation
    VM  of healthy OCS Cluster has 'up' status by default.
    """
    kms = KMS.get_kms_deployment()
    kms.deploy()
