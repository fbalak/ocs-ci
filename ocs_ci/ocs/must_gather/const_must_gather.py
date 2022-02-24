"""
The Procedure to add new version:
1.New Version created
2.Add the new version to GATHER_COMMANDS_VERSION dictionary
3.Ask the developer about new files on new version
4.Add file names to relevant list

OCS4.6 Link:
https://github.com/openshift/ocs-operator/blob/fefc8a0e04e314801809df2e5292a20fae8456b8/must-gather/collection-scripts/

OCS4.5 Link:
https://github.com/openshift/ocs-operator/blob/de48c9c00f8964f0f8813d7b3ddd25f7bc318449/must-gather/collection-scripts/

"""
from ocs_ci.framework import config
from ocs_ci.ocs import constants


GATHER_COMMANDS_CEPH = [
    "ceph_auth_list",
    "ceph_balancer_status",
    "ceph_config-key_ls",
    "ceph_config_dump",
    "ceph_crash_stat",
    "ceph_device_ls",
    "ceph_fs_dump",
    "ceph_fs_ls",
    "ceph_fs_status",
    "ceph_fs_subvolumegroup_ls_ocs-storagecluster-cephfilesystem",
    "ceph_health_detail",
    "ceph_mds_stat",
    "ceph_mgr_dump",
    "ceph_mgr_module_ls",
    "ceph_mgr_services",
    "ceph_mon_dump",
    "ceph_mon_stat",
    "ceph_osd_blocked-by",
    "ceph_osd_crush_class_ls",
    "ceph_osd_crush_dump",
    "ceph_osd_crush_rule_dump",
    "ceph_osd_crush_rule_ls",
    "ceph_osd_crush_show-tunables",
    "ceph_osd_crush_weight-set_dump",
    "ceph_osd_df",
    "ceph_osd_df_tree",
    "ceph_osd_dump",
    "ceph_osd_getmaxosd",
    "ceph_osd_lspools",
    "ceph_osd_numa-status",
    "ceph_osd_perf",
    "ceph_osd_pool_ls_detail",
    "ceph_osd_stat",
    "ceph_osd_tree",
    "ceph_osd_utilization",
    "ceph_pg_dump",
    "ceph_pg_stat",
    "ceph_quorum_status",
    "ceph_report",
    "ceph_service_dump",
    "ceph_status",
    "ceph_time-sync-status",
    "ceph_versions",
]

GATHER_COMMANDS_JSON = [
    "ceph_auth_list_--format_json-pretty",
    "ceph_balancer_pool_ls_--format_json-pretty",
    "ceph_balancer_status_--format_json-pretty",
    "ceph_config-key_ls_--format_json-pretty",
    "ceph_config_dump_--format_json-pretty",
    "ceph_crash_ls_--format_json-pretty",
    "ceph_crash_stat_--format_json-pretty",
    "ceph_device_ls_--format_json-pretty",
    "ceph_fs_dump_--format_json-pretty",
    "ceph_fs_ls_--format_json-pretty",
    "ceph_fs_status_--format_json-pretty",
    "ceph_fs_subvolumegroup_ls_ocs-storagecluster-cephfilesystem_--format_json-pretty",
    "ceph_health_detail_--format_json-pretty",
    "ceph_mds_stat_--format_json-pretty",
    "ceph_mgr_dump_--format_json-pretty",
    "ceph_mgr_module_ls_--format_json-pretty",
    "ceph_mgr_services_--format_json-pretty",
    "ceph_mon_dump_--format_json-pretty",
    "ceph_mon_stat_--format_json-pretty",
    "ceph_osd_blacklist_ls_--format_json-pretty",
    "ceph_osd_blocked-by_--format_json-pretty",
    "ceph_osd_crush_class_ls_--format_json-pretty",
    "ceph_osd_crush_dump_--format_json-pretty",
    "ceph_osd_crush_rule_dump_--format_json-pretty",
    "ceph_osd_crush_rule_ls_--format_json-pretty",
    "ceph_osd_crush_show-tunables_--format_json-pretty",
    "ceph_osd_crush_weight-set_dump_--format_json-pretty",
    "ceph_osd_crush_weight-set_ls_--format_json-pretty",
    "ceph_osd_df_--format_json-pretty",
    "ceph_osd_df_tree_--format_json-pretty",
    "ceph_osd_dump_--format_json-pretty",
    "ceph_osd_getmaxosd_--format_json-pretty",
    "ceph_osd_lspools_--format_json-pretty",
    "ceph_osd_numa-status_--format_json-pretty",
    "ceph_osd_perf_--format_json-pretty",
    "ceph_osd_pool_ls_detail_--format_json-pretty",
    "ceph_osd_stat_--format_json-pretty",
    "ceph_osd_tree_--format_json-pretty",
    "ceph_osd_utilization_--format_json-pretty",
    "ceph_pg_dump_--format_json-pretty",
    "ceph_pg_stat_--format_json-pretty",
    "ceph_progress_--format_json-pretty",
    "ceph_progress_json",
    "ceph_progress_json_--format_json-pretty",
    "ceph_quorum_status_--format_json-pretty",
    "ceph_report_--format_json-pretty",
    "ceph_service_dump_--format_json-pretty",
    "ceph_status_--format_json-pretty",
    "ceph_time-sync-status_--format_json-pretty",
    "ceph_versions_--format_json-pretty",
]

GATHER_COMMANDS_OTHERS = [
    "buildconfigs.yaml",
    "builds.yaml",
    "configmaps.yaml",
    "cronjobs.yaml",
    "daemonsets.yaml",
    "deploymentconfigs.yaml",
    "deployments.yaml",
    "endpoints.yaml",
    "events.yaml",
    "horizontalpodautoscalers.yaml",
    "imagestreams.yaml",
    "jobs.yaml",
    "noobaa-core-0.log",
    "noobaa-core-0.yaml",
    "noobaa-default-backing-store.yaml",
    "noobaa-default-bucket-class.yaml",
    "noobaa.yaml",
    "ocs-storagecluster-cephblockpool.yaml",
    "ocs-storagecluster-cephcluster.yaml",
    "ocs-storagecluster-cephfilesystem.yaml",
    "openshift-storage.yaml",
    "persistentvolumeclaims.yaml",
    "pods.yaml",
    "pools_rbd_ocs-storagecluster-cephblockpool",
    "replicasets.yaml",
    "replicationcontrollers.yaml",
    "routes.yaml",
    "secrets.yaml",
    "services.yaml",
    "statefulsets.yaml",
    "storagecluster.yaml",
]

GATHER_COMMANDS_OPENSHIFT_DEDICATED_EXCLUDE = [
    "db-noobaa-db-0.yaml",
    "my-alertmanager-claim-alertmanager-main-0.yaml",
    "my-alertmanager-claim-alertmanager-main-1.yaml",
    "my-alertmanager-claim-alertmanager-main-2.yaml",
    "my-prometheus-claim-prometheus-k8s-0.yaml",
    "my-prometheus-claim-prometheus-k8s-1.yaml",
    "noobaa-core-0.log",
    "noobaa-core-0.yaml",
    "noobaa-db-0.log",
    "noobaa-db-0.yaml",
    "noobaa-default-backing-store.yaml",
    "noobaa-default-bucket-class.yaml",
    "noobaa.yaml",
    "pools_rbd_ocs-storagecluster-cephblockpool",
    "registry-cephfs-rwx-pvc.yaml",
]

GATHER_COMMANDS_OPENSHIFT_DEDICATED_EXCLUDE_4_6 = [
    "openshift-storage-operatorgroup-admin.yaml",
    "openshift-storage-operatorgroup-edit.yaml",
    "openshift-storage-operatorgroup-view.yaml",
    "openshift-storage.noobaa.io.yaml",
]

GATHER_COMMANDS_CEPH_4_5 = [
    "ceph_osd_blacklist_ls",
    "ceph_df",
    "ceph_fs_subvolume_ls_ocs-storagecluster-cephfilesystem_csi",
    "ceph_progress",
]

GATHER_COMMANDS_JSON_4_5 = [
    "ceph_df_--format_json-pretty",
    "ceph_fs_subvolume_ls_ocs-storagecluster-cephfilesystem_csi_--format_json-pretty",
]

GATHER_COMMANDS_OTHERS_4_5 = [
    "describe_nodes",
    "describe_pods_-n_openshift-storage",
    "get_clusterversion_-oyaml",
    "get_csv_-n_openshift-storage",
    "get_events_-n_openshift-storage",
    "get_infrastructures.config_-oyaml",
    "get_installplan_-n_openshift-storage",
    "get_nodes_--show-labels",
    "get_pods_-owide_-n_openshift-storage",
    "get_pv",
    "get_pvc_--all-namespaces",
    "get_sc",
    "get_subscription_-n_openshift-storage",
    "db-noobaa-db-0.yaml",
    "my-alertmanager-claim-alertmanager-main-0.yaml",
    "my-alertmanager-claim-alertmanager-main-1.yaml",
    "my-alertmanager-claim-alertmanager-main-2.yaml",
    "my-prometheus-claim-prometheus-k8s-0.yaml",
    "my-prometheus-claim-prometheus-k8s-1.yaml",
    "noobaa-db-0.log",
    "noobaa-db-0.yaml",
    "registry-cephfs-rwx-pvc.yaml",
]

GATHER_COMMANDS_CEPH_4_6 = [
    "ceph_df",
    "ceph_fs_subvolume_ls_ocs-storagecluster-cephfilesystem_csi",
]

GATHER_COMMANDS_JSON_4_6 = [
    "ceph_df_--format_json-pretty",
    "ceph_fs_subvolume_ls_ocs-storagecluster-cephfilesystem_csi_--format_json-pretty",
    "ceph_progress",
]

GATHER_COMMANDS_OTHERS_4_6 = [
    "volumesnapshotclass",
    "storagecluster",
    "get_clusterrole",
    "desc_clusterrole",
    "desc_nodes",
    "get_infrastructures.config",
    "get_clusterrolebinding",
    "desc_pv",
    "get_clusterversion",
    "get_sc",
    "desc_clusterrolebinding",
    "get_nodes_-o_wide_--show-labels",
    "desc_clusterversion",
    "get_pv",
    "desc_sc",
    "desc_infrastructures.config",
    "csv",
    "rolebinding",
    "all",
    "role",
    "storagecluster.yaml",
    "admin.yaml",
    "aggregate-olm-edit.yaml",
    "aggregate-olm-view.yaml",
    "alertmanager-main.yaml",
    "alertmanager-main.yaml",
    "backingstores.noobaa.io-v1alpha1-admin.yaml",
    "backingstores.noobaa.io-v1alpha1-crdview.yaml",
    "backingstores.noobaa.io-v1alpha1-edit.yaml",
    "backingstores.noobaa.io-v1alpha1-view.yaml",
    "basic-user.yaml",
    "basic-users.yaml",
    "bucketclasses.noobaa.io-v1alpha1-admin.yaml",
    "bucketclasses.noobaa.io-v1alpha1-crdview.yaml",
    "bucketclasses.noobaa.io-v1alpha1-edit.yaml",
    "bucketclasses.noobaa.io-v1alpha1-view.yaml",
    "cephblockpools.ceph.rook.io-v1-admin.yaml",
    "cephblockpools.ceph.rook.io-v1-crdview.yaml",
    "cephblockpools.ceph.rook.io-v1-edit.yaml",
    "cephblockpools.ceph.rook.io-v1-view.yaml",
    "cephclients.ceph.rook.io-v1-admin.yaml",
    "cephclients.ceph.rook.io-v1-crdview.yaml",
    "cephclients.ceph.rook.io-v1-edit.yaml",
    "cephclients.ceph.rook.io-v1-view.yaml",
    "cephclusters.ceph.rook.io-v1-admin.yaml",
    "cephclusters.ceph.rook.io-v1-crdview.yaml",
    "cephclusters.ceph.rook.io-v1-edit.yaml",
    "cephclusters.ceph.rook.io-v1-view.yaml",
    "cephfilesystems.ceph.rook.io-v1-admin.yaml",
    "cephfilesystems.ceph.rook.io-v1-crdview.yaml",
    "cephfilesystems.ceph.rook.io-v1-edit.yaml",
    "cephfilesystems.ceph.rook.io-v1-view.yaml",
    "cephnfses.ceph.rook.io-v1-admin.yaml",
    "cephnfses.ceph.rook.io-v1-crdview.yaml",
    "cephnfses.ceph.rook.io-v1-edit.yaml",
    "cephnfses.ceph.rook.io-v1-view.yaml",
    "cephobjectrealms.ceph.rook.io-v1-admin.yaml",
    "cephobjectrealms.ceph.rook.io-v1-crdview.yaml",
    "cephobjectrealms.ceph.rook.io-v1-edit.yaml",
    "cephobjectrealms.ceph.rook.io-v1-view.yaml",
    "cephobjectstores.ceph.rook.io-v1-admin.yaml",
    "cephobjectstores.ceph.rook.io-v1-crdview.yaml",
    "cephobjectstores.ceph.rook.io-v1-edit.yaml",
    "cephobjectstores.ceph.rook.io-v1-view.yaml",
    "cephobjectstoreusers.ceph.rook.io-v1-admin.yaml",
    "cephobjectstoreusers.ceph.rook.io-v1-crdview.yaml",
    "cephobjectstoreusers.ceph.rook.io-v1-edit.yaml",
    "cephobjectstoreusers.ceph.rook.io-v1-view.yaml",
    "cephobjectzonegroups.ceph.rook.io-v1-admin.yaml",
    "cephobjectzonegroups.ceph.rook.io-v1-crdview.yaml",
    "cephobjectzonegroups.ceph.rook.io-v1-edit.yaml",
    "cephobjectzonegroups.ceph.rook.io-v1-view.yaml",
    "cephobjectzones.ceph.rook.io-v1-admin.yaml",
    "cephobjectzones.ceph.rook.io-v1-crdview.yaml",
    "cephobjectzones.ceph.rook.io-v1-edit.yaml",
    "cephobjectzones.ceph.rook.io-v1-view.yaml",
    "cephrbdmirrors.ceph.rook.io-v1-admin.yaml",
    "cephrbdmirrors.ceph.rook.io-v1-crdview.yaml",
    "cephrbdmirrors.ceph.rook.io-v1-edit.yaml",
    "cephrbdmirrors.ceph.rook.io-v1-view.yaml",
    "cloud-credential-operator-role.yaml",
    "cloud-credential-operator-rolebinding.yaml",
    "cluster-admin.yaml",
    "cluster-admin.yaml",
    "cluster-admins.yaml",
    "cluster-autoscaler-operator.yaml",
    "cluster-autoscaler-operator.yaml",
    "cluster-autoscaler-operator:cluster-reader.yaml",
    "cluster-autoscaler.yaml",
    "cluster-autoscaler.yaml",
    "cluster-debugger.yaml",
    "cluster-image-registry-operator.yaml",
    "cluster-monitoring-operator.yaml",
    "cluster-monitoring-operator.yaml",
    "cluster-monitoring-view.yaml",
    "cluster-node-tuning-operator.yaml",
    "cluster-node-tuning-operator.yaml",
    "cluster-node-tuning:tuned.yaml",
    "cluster-node-tuning:tuned.yaml",
    "cluster-reader.yaml",
    "cluster-readers.yaml",
    "cluster-samples-operator-proxy-reader.yaml",
    "cluster-samples-operator-proxy-reader.yaml",
    "cluster-samples-operator.yaml",
    "cluster-samples-operator.yaml",
    "cluster-status-binding.yaml",
    "cluster-status.yaml",
    "cluster-storage-operator-role.yaml",
    "cluster-version-operator.yaml",
    "cluster.yaml",
    "console-extensions-reader.yaml",
    "console-extensions-reader.yaml",
    "console-operator-auth-delegator.yaml",
    "console-operator.yaml",
    "console-operator.yaml",
    "console.yaml",
    "console.yaml",
    "default-account-cluster-image-registry-operator.yaml",
    "default-account-cluster-network-operator.yaml",
    "default-account-openshift-machine-config-operator.yaml",
    "endpointslices.yaml",
    "events",
    "insights-operator-auth.yaml",
    "insights-operator-gather-reader.yaml",
    "insights-operator-gather.yaml",
    "insights-operator-gather.yaml",
    "insights-operator.yaml",
    "insights-operator.yaml",
    "installplan",
    "node-exporter.yaml",
    "node-exporter.yaml",
    "ocs-storagecluster-cephfs.yaml",
    "ocs-storagecluster-cephfsplugin-snapclass.yaml",
    "ocs-storagecluster-rbdplugin-snapclass.yaml",
    "ocsinitializations.ocs.openshift.io-v1-admin.yaml",
    "ocsinitializations.ocs.openshift.io-v1-crdview.yaml",
    "ocsinitializations.ocs.openshift.io-v1-edit.yaml",
    "ocsinitializations.ocs.openshift.io-v1-view.yaml",
    "olm-operator-binding-openshift-operator-lifecycle-manager.yaml",
    "olm-operators-admin.yaml",
    "olm-operators-edit.yaml",
    "olm-operators-view.yaml",
    "openshift-cluster-monitoring-admin.yaml",
    "openshift-cluster-monitoring-edit.yaml",
    "openshift-cluster-monitoring-view.yaml",
    "openshift-csi-snapshot-controller-role.yaml",
    "openshift-csi-snapshot-controller-runner.yaml",
    "openshift-dns-operator.yaml",
    "openshift-dns-operator.yaml",
    "openshift-dns.yaml",
    "openshift-dns.yaml",
    "openshift-image-registry-pruner.yaml",
    "openshift-ingress-operator.yaml",
    "openshift-ingress-operator.yaml",
    "openshift-ingress-router.yaml",
    "openshift-ingress-router.yaml",
    "openshift-sdn-controller.yaml",
    "openshift-sdn-controller.yaml",
    "openshift-sdn.yaml",
    "openshift-sdn.yaml",
    "openshift-state-metrics.yaml",
    "openshift-state-metrics.yaml",
    "openshift-storage-operatorgroup-admin.yaml",
    "openshift-storage-operatorgroup-edit.yaml",
    "openshift-storage-operatorgroup-view.yaml",
    "openshift-storage.noobaa.io.yaml",
    "operatorhub-config-reader.yaml",
    "packagemanifests-v1-admin.yaml",
    "packagemanifests-v1-edit.yaml",
    "packagemanifests-v1-view.yaml",
    "packageserver-service-system:auth-delegator.yaml",
    "pods",
    "pods_-owide",
    "prometheus-adapter-view.yaml",
    "prometheus-adapter.yaml",
    "prometheus-k8s.yaml",
    "prometheus-k8s.yaml",
    "prometheus-operator.yaml",
    "prometheus-operator.yaml",
    "pvc_all_namespaces",
    "registry-admin.yaml",
    "registry-editor.yaml",
    "registry-monitoring.yaml",
    "registry-monitoring.yaml",
    "registry-registry-role.yaml",
    "registry-viewer.yaml",
    "self-access-reviewer.yaml",
    "self-access-reviewers.yaml",
    "self-provisioner.yaml",
    "self-provisioners.yaml",
    "storage-admin.yaml",
    "storage-version-migration-migrator.yaml",
    "storagecluster",
    "storageclusters.ocs.openshift.io-v1-admin.yaml",
    "storageclusters.ocs.openshift.io-v1-crdview.yaml",
    "storageclusters.ocs.openshift.io-v1-edit.yaml",
    "storageclusters.ocs.openshift.io-v1-view.yaml",
    "subscription",
    "sudoer.yaml",
    "system-bootstrap-node-bootstrapper.yaml",
    "system-bootstrap-node-renewal.yaml",
    "system:aggregate-to-admin.yaml",
    "system:aggregate-to-edit.yaml",
    "system:aggregate-to-view.yaml",
    "system:aggregated-metrics-reader.yaml",
    "system:auth-delegator.yaml",
    "system:basic-user.yaml",
    "system:basic-user.yaml",
    "system:build-strategy-custom.yaml",
    "system:build-strategy-docker-binding.yaml",
    "system:build-strategy-docker.yaml",
    "system:build-strategy-jenkinspipeline-binding.yaml",
    "system:build-strategy-jenkinspipeline.yaml",
    "system:build-strategy-source-binding.yaml",
    "system:build-strategy-source.yaml",
    "system:certificates.k8s.io:certificatesigningrequests:nodeclient.yaml",
    "system:certificates.k8s.io:certificatesigningrequests:selfnodeclient.yaml",
    "system:certificates.k8s.io:kube-apiserver-client-approver.yaml",
    "system:certificates.k8s.io:kube-apiserver-client-kubelet-approver.yaml",
    "system:certificates.k8s.io:kubelet-serving-approver.yaml",
    "system:certificates.k8s.io:legacy-unknown-approver.yaml",
    "system:controller:attachdetach-controller.yaml",
    "system:controller:attachdetach-controller.yaml",
    "system:controller:certificate-controller.yaml",
    "system:controller:certificate-controller.yaml",
    "system:controller:clusterrole-aggregation-controller.yaml",
    "system:controller:clusterrole-aggregation-controller.yaml",
    "system:controller:cronjob-controller.yaml",
    "system:controller:cronjob-controller.yaml",
    "system:controller:daemon-set-controller.yaml",
    "system:controller:daemon-set-controller.yaml",
    "system:controller:deployment-controller.yaml",
    "system:controller:deployment-controller.yaml",
    "system:controller:disruption-controller.yaml",
    "system:controller:disruption-controller.yaml",
    "system:controller:endpoint-controller.yaml",
    "system:controller:endpoint-controller.yaml",
    "system:controller:endpointslice-controller.yaml",
    "system:controller:endpointslice-controller.yaml",
    "system:controller:endpointslicemirroring-controller.yaml",
    "system:controller:endpointslicemirroring-controller.yaml",
    "system:controller:expand-controller.yaml",
    "system:controller:expand-controller.yaml",
    "system:controller:generic-garbage-collector.yaml",
    "system:controller:generic-garbage-collector.yaml",
    "system:controller:horizontal-pod-autoscaler.yaml",
    "system:controller:horizontal-pod-autoscaler.yaml",
    "system:controller:job-controller.yaml",
    "system:controller:job-controller.yaml",
    "system:controller:namespace-controller.yaml",
    "system:controller:namespace-controller.yaml",
    "system:controller:node-controller.yaml",
    "system:controller:node-controller.yaml",
    "system:controller:operator-lifecycle-manager.yaml",
    "system:controller:persistent-volume-binder.yaml",
    "system:controller:persistent-volume-binder.yaml",
    "system:controller:pod-garbage-collector.yaml",
    "system:controller:pod-garbage-collector.yaml",
    "system:controller:pv-protection-controller.yaml",
    "system:controller:pv-protection-controller.yaml",
    "system:controller:pvc-protection-controller.yaml",
    "system:controller:pvc-protection-controller.yaml",
    "system:controller:replicaset-controller.yaml",
    "system:controller:replicaset-controller.yaml",
    "system:controller:replication-controller.yaml",
    "system:controller:replication-controller.yaml",
    "system:controller:resourcequota-controller.yaml",
    "system:controller:resourcequota-controller.yaml",
    "system:controller:route-controller.yaml",
    "system:controller:route-controller.yaml",
    "system:controller:service-account-controller.yaml",
    "system:controller:service-account-controller.yaml",
    "system:controller:service-controller.yaml",
    "system:controller:service-controller.yaml",
    "system:controller:statefulset-controller.yaml",
    "system:controller:statefulset-controller.yaml",
    "system:controller:ttl-controller.yaml",
    "system:controller:ttl-controller.yaml",
    "system:deployer.yaml",
    "system:deployer.yaml",
    "system:discovery.yaml",
    "system:discovery.yaml",
    "system:heapster.yaml",
    "system:image-auditor.yaml",
    "system:image-builder.yaml",
    "system:image-builder.yaml",
    "system:image-pruner.yaml",
    "system:image-puller.yaml",
    "system:image-puller.yaml",
    "system:image-pusher.yaml",
    "system:image-signer.yaml",
    "system:kube-aggregator.yaml",
    "system:kube-controller-manager.yaml",
    "system:kube-controller-manager.yaml",
    "system:kube-dns.yaml",
    "system:kube-dns.yaml",
    "system:kube-scheduler.yaml",
    "system:kube-scheduler.yaml",
    "system:kubelet-api-admin.yaml",
    "system:master.yaml",
    "system:masters.yaml",
    "system:node-admin.yaml",
    "system:node-admin.yaml",
    "system:node-admins.yaml",
    "system:node-bootstrapper.yaml",
    "system:node-bootstrapper.yaml",
    "system:node-problem-detector.yaml",
    "system:node-proxier.yaml",
    "system:node-proxier.yaml",
    "system:node-proxiers.yaml",
    "system:node-reader.yaml",
    "system:node.yaml",
    "system:node.yaml",
    "system:oauth-token-deleter.yaml",
    "system:oauth-token-deleters.yaml",
    "system:openshift:aggregate-snapshots-to-admin.yaml",
    "system:openshift:aggregate-snapshots-to-basic-user.yaml",
    "system:openshift:aggregate-snapshots-to-storage-admin.yaml",
    "system:openshift:aggregate-snapshots-to-view.yaml",
    "system:openshift:aggregate-to-admin.yaml",
    "system:openshift:aggregate-to-basic-user.yaml",
    "system:openshift:aggregate-to-cluster-reader.yaml",
    "system:openshift:aggregate-to-edit.yaml",
    "system:openshift:aggregate-to-storage-admin.yaml",
    "system:openshift:aggregate-to-view.yaml",
    "system:openshift:cloud-credential-operator:cluster-reader.yaml",
    "system:openshift:cluster-config-operator:cluster-reader.yaml",
    "system:openshift:cluster-samples-operator:cluster-reader.yaml",
    "system:openshift:controller:build-config-change-controller.yaml",
    "system:openshift:controller:build-config-change-controller.yaml",
    "system:openshift:controller:build-controller.yaml",
    "system:openshift:controller:build-controller.yaml",
    "system:openshift:controller:check-endpoints-crd-reader.yaml",
    "system:openshift:controller:check-endpoints-node-reader.yaml",
    "system:openshift:controller:check-endpoints.yaml",
    "system:openshift:controller:cluster-quota-reconciliation-controller.yaml",
    "system:openshift:controller:cluster-quota-reconciliation-controller.yaml",
    "system:openshift:controller:default-rolebindings-controller.yaml",
    "system:openshift:controller:default-rolebindings-controller.yaml",
    "system:openshift:controller:deployer-controller.yaml",
    "system:openshift:controller:deployer-controller.yaml",
    "system:openshift:controller:deploymentconfig-controller.yaml",
    "system:openshift:controller:deploymentconfig-controller.yaml",
    "system:openshift:controller:horizontal-pod-autoscaler.yaml",
    "system:openshift:controller:horizontal-pod-autoscaler.yaml",
    "system:openshift:controller:image-import-controller.yaml",
    "system:openshift:controller:image-import-controller.yaml",
    "system:openshift:controller:image-trigger-controller.yaml",
    "system:openshift:controller:image-trigger-controller.yaml",
    "system:openshift:controller:kube-apiserver-check-endpoints-auth-delegator.yaml",
    "system:openshift:controller:kube-apiserver-check-endpoints-crd-reader.yaml",
    "system:openshift:controller:kube-apiserver-check-endpoints-node-reader.yaml",
    "system:openshift:controller:machine-approver.yaml",
    "system:openshift:controller:machine-approver.yaml",
    "system:openshift:controller:namespace-security-allocation-controller.yaml",
    "system:openshift:controller:namespace-security-allocation-controller.yaml",
    "system:openshift:controller:origin-namespace-controller.yaml",
    "system:openshift:controller:origin-namespace-controller.yaml",
    "system:openshift:controller:pv-recycler-controller.yaml",
    "system:openshift:controller:pv-recycler-controller.yaml",
    "system:openshift:controller:resourcequota-controller.yaml",
    "system:openshift:controller:resourcequota-controller.yaml",
    "system:openshift:controller:service-ca.yaml",
    "system:openshift:controller:service-ca.yaml",
    "system:openshift:controller:service-ingress-ip-controller.yaml",
    "system:openshift:controller:service-ingress-ip-controller.yaml",
    "system:openshift:controller:service-serving-cert-controller.yaml",
    "system:openshift:controller:service-serving-cert-controller.yaml",
    "system:openshift:controller:serviceaccount-controller.yaml",
    "system:openshift:controller:serviceaccount-controller.yaml",
    "system:openshift:controller:serviceaccount-pull-secrets-controller.yaml",
    "system:openshift:controller:serviceaccount-pull-secrets-controller.yaml",
    "system:openshift:controller:template-instance-controller.yaml",
    "system:openshift:controller:template-instance-controller.yaml",
    "system:openshift:controller:template-instance-controller:admin.yaml",
    "system:openshift:controller:template-instance-finalizer-controller.yaml",
    "system:openshift:controller:template-instance-finalizer-controller.yaml",
    "system:openshift:controller:template-instance-finalizer-controller:admin.yaml",
    "system:openshift:controller:template-service-broker.yaml",
    "system:openshift:controller:template-service-broker.yaml",
    "system:openshift:controller:unidling-controller.yaml",
    "system:openshift:controller:unidling-controller.yaml",
    "system:openshift:discovery.yaml",
    "system:openshift:discovery.yaml",
    "system:openshift:kube-controller-manager:gce-cloud-provider.yaml",
    "system:openshift:kube-controller-manager:gce-cloud-provider.yaml",
    "system:openshift:machine-config-operator:cluster-reader.yaml",
    "system:openshift:oauth-apiserver.yaml",
    "system:openshift:openshift-apiserver.yaml",
    "system:openshift:openshift-authentication.yaml",
    "system:openshift:openshift-controller-manager.yaml",
    "system:openshift:openshift-controller-manager.yaml",
    "system:openshift:openshift-controller-manager:ingress-to-route-controller.yaml",
    "system:openshift:openshift-controller-manager:ingress-to-route-controller.yaml",
    "system:openshift:operator:authentication.yaml",
    "system:openshift:operator:cluster-kube-scheduler-operator.yaml",
    "system:openshift:operator:etcd-operator.yaml",
    "system:openshift:operator:kube-apiserver-operator.yaml",
    "system:openshift:operator:kube-apiserver-recovery.yaml",
    "system:openshift:operator:kube-controller-manager-operator.yaml",
    "system:openshift:operator:kube-controller-manager-recovery.yaml",
    "system:openshift:operator:kube-scheduler-recovery.yaml",
    "system:openshift:operator:kube-scheduler:public-2.yaml",
    "system:openshift:operator:kube-storage-version-migrator-operator.yaml",
    "system:openshift:operator:openshift-apiserver-operator.yaml",
    "system:openshift:operator:openshift-config-operator.yaml",
    "system:openshift:operator:openshift-controller-manager-operator.yaml",
    "system:openshift:operator:openshift-etcd-installer.yaml",
    "system:openshift:operator:openshift-kube-apiserver-installer.yaml",
    "system:openshift:operator:openshift-kube-controller-manager-installer.yaml",
    "system:openshift:operator:openshift-kube-scheduler-installer.yaml",
    "system:openshift:operator:service-ca-operator.yaml",
    "system:openshift:public-info-viewer.yaml",
    "system:openshift:public-info-viewer.yaml",
    "system:openshift:scc:anyuid.yaml",
    "system:openshift:scc:hostaccess.yaml",
    "system:openshift:scc:hostmount.yaml",
    "system:openshift:scc:hostnetwork.yaml",
    "system:openshift:scc:nonroot.yaml",
    "system:openshift:scc:privileged.yaml",
    "system:openshift:scc:restricted.yaml",
    "system:openshift:templateservicebroker-client.yaml",
    "system:openshift:tokenreview-openshift-controller-manager.yaml",
    "system:openshift:tokenreview-openshift-controller-manager.yaml",
    "system:persistent-volume-provisioner.yaml",
    "system:public-info-viewer.yaml",
    "system:public-info-viewer.yaml",
    "system:registry.yaml",
    "system:router.yaml",
    "system:scope-impersonation.yaml",
    "system:scope-impersonation.yaml",
    "system:sdn-manager.yaml",
    "system:sdn-reader.yaml",
    "system:sdn-readers.yaml",
    "system:volume-scheduler.yaml",
    "system:volume-scheduler.yaml",
    "system:webhook.yaml",
    "system:webhooks.yaml",
    "telemeter-client-view.yaml",
    "telemeter-client.yaml",
    "telemeter-client.yaml",
    "thanos-querier.yaml",
    "thanos-querier.yaml",
    "version.yaml",
    "view.yaml",
    "volumesnapshotclass",
    "whereabouts-cni.yaml",
    "db-noobaa-db-0.yaml",
    "my-alertmanager-claim-alertmanager-main-0.yaml",
    "my-alertmanager-claim-alertmanager-main-1.yaml",
    "my-alertmanager-claim-alertmanager-main-2.yaml",
    "my-prometheus-claim-prometheus-k8s-0.yaml",
    "my-prometheus-claim-prometheus-k8s-1.yaml",
    "noobaa-db-0.log",
    "noobaa-db-0.yaml",
    "registry-cephfs-rwx-pvc.yaml",
]

GATHER_COMMANDS_CEPH_4_7 = [
    "ceph_df_detail",
]

GATHER_COMMANDS_JSON_4_7 = [
    "ceph_df_detail_--format_json-pretty",
]

GATHER_COMMANDS_OTHERS_4_7 = [
    "noobaa-db-pg-0.yaml",
    "db-noobaa-db-pg-0.yaml",
    "noobaa-db-pg-0.log",
    "namespacestores.noobaa.io-v1alpha1-view.yaml",
    "namespacestores.noobaa.io-v1alpha1-edit.yaml",
    "namespacestores.noobaa.io-v1alpha1-crdview.yaml",
    "namespacestores.noobaa.io-v1alpha1-admin.yaml",
    "alertmanager-main.yaml",
    "prometheus-operator.yaml",
    "prometheus-k8s.yaml",
    "prometheus-k8s-scheduler-resources.yaml",
    "prometheus-adapter.yaml",
    "prometheus-operator.yaml",
    "prometheus-k8s.yaml",
    "prometheus-k8s-scheduler-resources.yaml",
    "prometheus-adapter.yaml",
    "prometheus-adapter-view.yaml",
]

GATHER_COMMANDS_OTHERS_EXTERNAL = GATHER_COMMANDS_OTHERS + [
    "ocs-external-storagecluster-ceph-rbd.yaml",
    "ocs-external-storagecluster-ceph-rgw.yaml",
    "ocs-external-storagecluster-cephfs.yaml",
]

GATHER_COMMANDS_OTHERS_EXTERNAL_4_6 = GATHER_COMMANDS_OTHERS_4_6 + [
    "ocs-external-storagecluster-cephfsplugin-snapclass.yaml",
    "ocs-external-storagecluster-rbdplugin-snapclass.yaml",
]

GATHER_COMMANDS_OTHERS_EXTERNAL_4_8 = GATHER_COMMANDS_OTHERS_4_7 + [
    "noobaa-ceph-objectstore-user.yaml",
    "ocs-external-storagecluster-cephcluster.yaml",
    "ocs-external-storagecluster-cephobjectstore.yaml",
]

GATHER_COMMANDS_OTHERS_EXTERNAL_EXCLUDE = [
    "ocs-storagecluster-cephblockpool.yaml",
    "ocs-storagecluster-cephcluster.yaml",
    "ocs-storagecluster-cephfilesystem.yaml",
    "pools_rbd_ocs-storagecluster-cephblockpool",
    "ocs-storagecluster-ceph-rbd.yaml",
    "ocs-storagecluster-ceph-rgw.yaml",
    "ocs-storagecluster-cephfs.yaml",
    "ocs-storagecluster-cephfsplugin-snapclass.yaml",
    "ocs-storagecluster-rbdplugin-snapclass.yaml",
]

if config.ENV_DATA["platform"].lower() in constants.MANAGED_SERVICE_PLATFORMS:
    GATHER_COMMANDS_OTHERS = list(
        set(GATHER_COMMANDS_OTHERS) - set(GATHER_COMMANDS_OPENSHIFT_DEDICATED_EXCLUDE)
    )
    GATHER_COMMANDS_OTHERS_4_6 = list(
        set(GATHER_COMMANDS_OTHERS_4_6)
        - set(GATHER_COMMANDS_OPENSHIFT_DEDICATED_EXCLUDE_4_6)
    )

GATHER_COMMANDS_VERSION = {
    4.5: {
        "CEPH": GATHER_COMMANDS_CEPH + GATHER_COMMANDS_CEPH_4_5,
        "JSON": GATHER_COMMANDS_JSON + GATHER_COMMANDS_JSON_4_5,
        "OTHERS": GATHER_COMMANDS_OTHERS + GATHER_COMMANDS_OTHERS_4_5,
        "OTHERS_EXTERNAL": list(
            set(GATHER_COMMANDS_OTHERS_EXTERNAL + GATHER_COMMANDS_OTHERS_4_5)
            - set(GATHER_COMMANDS_OTHERS_EXTERNAL_EXCLUDE)
        ),
    },
    4.6: {
        "CEPH": GATHER_COMMANDS_CEPH + GATHER_COMMANDS_CEPH_4_6,
        "JSON": GATHER_COMMANDS_JSON + GATHER_COMMANDS_JSON_4_6,
        "OTHERS": GATHER_COMMANDS_OTHERS + GATHER_COMMANDS_OTHERS_4_6,
        "OTHERS_EXTERNAL": list(
            set(GATHER_COMMANDS_OTHERS_EXTERNAL + GATHER_COMMANDS_OTHERS_EXTERNAL_4_6)
            - set(GATHER_COMMANDS_OTHERS_EXTERNAL_EXCLUDE)
        ),
    },
    4.7: {
        "CEPH": GATHER_COMMANDS_CEPH + GATHER_COMMANDS_CEPH_4_7,
        "JSON": GATHER_COMMANDS_JSON + GATHER_COMMANDS_JSON_4_7,
        "OTHERS": GATHER_COMMANDS_OTHERS + GATHER_COMMANDS_OTHERS_4_7,
        "OTHERS_EXTERNAL": list(
            set(GATHER_COMMANDS_OTHERS_EXTERNAL + GATHER_COMMANDS_OTHERS_4_7)
            - set(GATHER_COMMANDS_OTHERS_EXTERNAL_EXCLUDE)
        ),
    },
    4.8: {
        "CEPH": GATHER_COMMANDS_CEPH + GATHER_COMMANDS_CEPH_4_7,
        "JSON": GATHER_COMMANDS_JSON + GATHER_COMMANDS_JSON_4_7,
        "OTHERS": GATHER_COMMANDS_OTHERS + GATHER_COMMANDS_OTHERS_4_7,
        "OTHERS_EXTERNAL": list(
            set(GATHER_COMMANDS_OTHERS_EXTERNAL + GATHER_COMMANDS_OTHERS_EXTERNAL_4_8)
            - set(GATHER_COMMANDS_OTHERS_EXTERNAL_EXCLUDE)
        ),
    },
    4.9: {
        "CEPH": GATHER_COMMANDS_CEPH + GATHER_COMMANDS_CEPH_4_7,
        "JSON": GATHER_COMMANDS_JSON + GATHER_COMMANDS_JSON_4_7,
        "OTHERS": GATHER_COMMANDS_OTHERS + GATHER_COMMANDS_OTHERS_4_7,
        "OTHERS_EXTERNAL": list(
            set(GATHER_COMMANDS_OTHERS_EXTERNAL + GATHER_COMMANDS_OTHERS_EXTERNAL_4_8)
            - set(GATHER_COMMANDS_OTHERS_EXTERNAL_EXCLUDE)
        ),
    },
    4.10: {
        "CEPH": GATHER_COMMANDS_CEPH + GATHER_COMMANDS_CEPH_4_7,
        "JSON": GATHER_COMMANDS_JSON + GATHER_COMMANDS_JSON_4_7,
        "OTHERS": GATHER_COMMANDS_OTHERS + GATHER_COMMANDS_OTHERS_4_7,
        "OTHERS_EXTERNAL": list(
            set(GATHER_COMMANDS_OTHERS_EXTERNAL + GATHER_COMMANDS_OTHERS_EXTERNAL_4_8)
            - set(GATHER_COMMANDS_OTHERS_EXTERNAL_EXCLUDE)
        ),
    },
}
