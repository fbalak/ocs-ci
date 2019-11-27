import logging
import pytest

from ocs_ci.ocs import constants, resources

log = logging.getLogger(__name__)


def create_pods(
    interface,
    pvc_factory,
    pod_factory,
    storageclass,
    count,
    access_mode,
):
    """
    Create pods for upgrade testing. pvc_factory and pod_factory have to be
    in the same scope.

    Args:
        interface (str): CephBlockPool or CephFileSystem
        pvc_factory (function): Function for creating PVCs
        pod_factory (function): Function for creating pods
        storageclass (obj): Storageclass to use
        count (int): Number of pods to create
        access_mode (str): ReadWriteOnce, ReadOnlyMany or ReadWriteMany.
            This decides the access mode to be used for the PVC

    Return:
        list: List of generated pods
    """
    # TODO(fbalak): Use proper constants after
    # https://github.com/red-hat-storage/ocs-ci/issues/1056
    # is resolved
    if interface == constants.CEPHBLOCKPOOL:
        sc_name = 'ocs-storagecluster-ceph-rbd'
    elif interface == constants.CEPHFILESYSTEM:
        sc_name = 'ocs-storagecluster-cephfs'
    else:
        raise AttributeError(f"Interface '{interface}' is invalid")

    log.info(
        f"Creating {count} pods via {interface} using {access_mode}"
        f" access mode and {sc_name} storageclass")
    metadata = {'name': sc_name}
    pvcs = [
        pvc_factory(
            storageclass=storageclass,
            access_mode=access_mode,
        ) for _ in range(count)
    ]
    pods = [
        pod_factory(
            interface=interface,
            pvc=pvc
        ) for pvc in pvcs
    ]
    return pods


@pytest.fixture(scope='session')
def default_storageclasses(request, teardown_factory_session):
    """
    Returns dictionary with storageclasses. Keys represent reclaim policy of
    storageclass. There are two storageclasses for each key. First is RBD based
    and the second one is CephFS based.
    """
    scs = {
        constants.RECLAIM_POLICY_DELETE: [],
        constants.RECLAIM_POLICY_RETAIN: []
    }
    for sc_name in (
        'ocs-storagecluster-ceph-rbd',
        'ocs-storagecluster-cephfs'
    ):
        sc = resources.ocs.OCS(
            kind=constants.STORAGECLASS,
            metadata={'name': sc_name}
        )
        sc.reload()
        scs[constants.RECLAIM_POLICY_DELETE].append(sc)
        sc.data['reclaimPolicy'] = constants.RECLAIM_POLICY_RETAIN
        sc.data['metadata']['name'] += '-retain'
        sc._name = sc.data['metadata']['name']
        sc.create()
        teardown_factory_session(sc)
        scs[constants.RECLAIM_POLICY_RETAIN].append(sc)
    return scs


@pytest.fixture(scope='session')
def pre_upgrade_pods(
    request,
    pvc_factory_session,
    pod_factory_session,
    default_storageclasses
):
    """
    Generate RBD and CephFS pods for tests before upgrade is executed.

    Returns:
        list: List of pods with RBD interface
    """
    pods = []

    for reclaim_policy in (
        constants.RECLAIM_POLICY_DELETE,
        constants.RECLAIM_POLICY_RETAIN
    ):
        for access_mode in [
            constants.ACCESS_MODE_RWO,
        ]:
            rbd_pods = create_pods(
                interface=constants.CEPHBLOCKPOOL,
                pvc_factory=pvc_factory_session,
                pod_factory=pod_factory_session,
                storageclass=default_storageclasses.get(reclaim_policy)[0],
                count=1,
                access_mode=access_mode,
            )
            pods.extend(rbd_pods)

        for access_mode in [
            constants.ACCESS_MODE_RWO,
            constants.ACCESS_MODE_RWX
        ]:
            cephfs_pods = create_pods(
                interface=constants.CEPHFILESYSTEM,
                pvc_factory=pvc_factory_session,
                pod_factory=pod_factory_session,
                storageclass=default_storageclasses.get(reclaim_policy)[1],
                count=1,
                access_mode=access_mode,
            )
            pods.extend(cephfs_pods)

    return pods


@pytest.fixture
def post_upgrade_pods(pvc_factory, pod_factory, default_storageclasses):
    """
    Generate pods for tests.

    Returns:
        list: List of pods with RBD and CephFS interface
    """
    pods = []
    for reclaim_policy in (
        constants.RECLAIM_POLICY_DELETE,
        constants.RECLAIM_POLICY_RETAIN
    ):
        for access_mode in [
            constants.ACCESS_MODE_RWO,
        ]:
            rbd_pods = create_pods(
                interface=constants.CEPHBLOCKPOOL,
                pvc_factory=pvc_factory,
                pod_factory=pod_factory,
                storageclass=default_storageclasses.get(reclaim_policy)[0],
                count=1,
                access_mode=access_mode,
            )
            pods.extend(rbd_pods)

        for access_mode in [
            constants.ACCESS_MODE_RWO,
            constants.ACCESS_MODE_RWX
        ]:
            cephfs_pods = create_pods(
                interface=constants.CEPHFILESYSTEM,
                pvc_factory=pvc_factory,
                pod_factory=pod_factory,
                storageclass=default_storageclasses.get(reclaim_policy)[1],
                count=1,
                access_mode=access_mode,
            )
            pods.extend(cephfs_pods)

    return pods
