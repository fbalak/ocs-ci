"""
A test for creating a CephFS
"""
import logging
from pdb import set_trace
from kubernetes import config
from openshift.dynamic import DynamicClient, exceptions
import ocs.defaults as defaults
import yaml
from ocsci.enums import TestStatus
from utility.utils import run_cmd

k8s_client = config.new_client_from_config()
dyn_client = DynamicClient(k8s_client)
log = logging.getLogger(__name__)


def create_ceph_fs(client, fs_name, active_count):
    """
    Create a new Ceph File System
    """

    fs_body = (
        f"""
        apiVersion: ceph.rook.io/v1
        kind: CephFilesystem
        metadata:
          name: {fs_name}
          namespace: {defaults.ROOK_CLUSTER_NAMESPACE}
        spec:
          # The metadata pool spec. Must use replication.
          metadataPool:
            replicated:
              size: 3
          # The list of data pool specs. Can use replication or erasure coding.
          dataPools:
            - failureDomain: host
              replicated:
                size: 3
          # The metadata service (mds) configuration
          metadataServer:
            # The number of active MDS instances
            activeCount: {active_count}
            # Whether each active MDS instance will have an active standby
            # with a warm metadata cache for faster failover.
            # If false, standbys will be available, but will not have
            # a warm cache.
            activeStandby: true
            # The affinity rules to apply to the mds deployment
            placement:
            #  nodeAffinity:
            #    requiredDuringSchedulingIgnoredDuringExecution:
            #      nodeSelectorTerms:
            #      - matchExpressions:
            #        - key: role
            #          operator: In
            #          values:
            #          - mds-node
            #  tolerations:
            #  - key: mds-node
            #    operator: Exists
            #  podAffinity:
            #  podAntiAffinity:
            # A key/value list of annotations
            annotations:
            #  key: value
            resources:
            # The requests and limits set here, allow the filesystem MDS
            # Pod(s) to use half of one CPU core and 1 gigabyte of memory
            #  limits:
            #    cpu: "500m"
            #    memory: "1024Mi"
            #  requests:
            #    cpu: "500m"
            #    memory: "1024Mi"
        """
    )

    fs_dict = yaml.safe_load(fs_body)
    log.info(f"Creating a new Ceph FileSystem")
    ret = client.create(body=fs_dict)
    set_trace()
    log.info(f"Return value is:\n{ret}")
    return ret


def modify_fs(client, dict_to_modify, new_active_count):
    """
    """
    dict_to_modify['spec']['metadataServer']['activeCount'] = new_active_count
    log.info(f"Change the active_count to {new_active_count}")
    ret = client.replace(body=dict_to_modify)
    log.info(f"The updated return value is:\n{ret}")
    return ret


def delete_fs(client, fs_name):
    """
    """
    log.info(f"Deleting the file system")
    ret = client.delete(
        name=fs_name, namespace=defaults.ROOK_CLUSTER_NAMESPACE
    )
    if ret.status == "Success":
        return True
    return False


def verify_fs_exist(client, fs_name):
    """
    """
    try:
        log.info(f"Verifying if the filesystem exist or not")
        client.get(name=fs_name, namespace=defaults.ROOK_CLUSTER_NAMESPACE)
    except exceptions.ApiException:
        log.info(f"Ceph FS {fs_name} doesn't exist")
        return False
    log.info(f"Ceph FS {fs_name} exist")
    return True


def run(**kwargs):
    """
    A simple function to exercise a resource creation through api-client
    """
    fs_name = 'my-cephfs'
    active_count = '1'
    new_active_count = '2'
    ceph_fs_resource = dyn_client.resources.get(
        api_version='v1', kind='CephFilesystem'
    )
    set_trace()
    ret = create_ceph_fs(ceph_fs_resource, fs_name, active_count)
    set_trace()
    assert verify_fs_exist(ceph_fs_resource, fs_name)
    set_trace()
    assert modify_fs(ceph_fs_resource, ret.to_dict(), new_active_count)
    set_trace()
    assert delete_fs(ceph_fs_resource, fs_name)
    set_trace()
    assert not verify_fs_exist(ceph_fs_resource, fs_name)
    set_trace()
    return TestStatus.PASSED

