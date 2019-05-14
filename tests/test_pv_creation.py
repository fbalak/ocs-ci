"""
A test for creating a PV
"""


import logging
from pdb import set_trace
import ocs.defaults as defaults
from ocs import exceptions

from utility.utils import run_oc_cmd

import yaml
import string
import os


from ocsci.enums import TestStatus


log = logging.getLogger(__name__)

PV_YAML = os.path.join("templates/ocs-deployment", "PersistentVolume.yaml")


def create_pv():
    """
    Create a new Persistent Volume
    """
    ret = run_oc_cmd(f"oc create -f {PV_YAML} -o yaml")
    if ret.status.phase == "Pending":
        return True
    return False


def delete_pv(pv_name):
    """
    Delete a Persistent Volume by given name
    """
    stat = run_oc_cmd(f"oc delete -f {PV_YAML}")
    if stat in defaults.VOLUME_DELETED.format(volume_name=pv_name):
        return True
    return False


def verify_pv_exist(pv_name):
    """
    Verify a Persistent Volume exists by a given name
    """
    try:
        run_oc_cmd(f"oc get PersistentVolume {pv_name} -o yaml")
        set_trace()
    except exceptions.CommandFailed:
        log.info(f"PV {pv_name} doesn't exist")
        return False
    log.info(f"PV {pv_name} exist")
    return True


def run(**kwargs):
    """
    A simple function to exercise a resource creation through api-client
    """
    pv_name = "example"
    assert create_pv()
    assert verify_pv_exist(pv_name)
    assert delete_pv(pv_name)
    assert not verify_pv_exist(pv_name)
    return TestStatus.PASSED

