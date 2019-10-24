#!/usr/bin/env python3
""" 
Purpose
========

This module does nothing other than generate lists which contain URLS
of container images that can be downloaded from RedHats registry.

This module was created so that it would be easy to modify and extend any images to these lists
with minimal hassle.



Variables
==========
User code only needs to concern itself with `component_images`, and `user_images`.

`component_images` contains a list of all image URLs that are required to perform an 
offline installation.
`user_images` is the list of images that Openshift expects to have access to once the install is 
complete. These are the images developers will actually use to build apps.


* `component_images` and `component_images_no_changes` lists are created from
  https://docs.openshift.com/container-platform/3.11/install/disconnected_install.html#disconnected-syncing-images

  `component_images_no_changes` contains images that don't have a tag specified from the link, and etcd, which
  looks like it requires its own specific version

* `system_tag_version` is the shared tag used by all required OpenShift component images

* `registry` is the domain name of the image registry

* `user_images` is a list of image URLs that OpenShift expects to have in its registry

* `image_map` is the dictionary that is used to build the URLs in `user_images`

"""
from typing import List, Dict, NewType, Union

system_tag_version: str = 'v3.11.146'
registry = 'registry.redhat.io'


component_images_no_tag: List[str] = [
	'registry.redhat.io/openshift3/apb-base',
	'registry.redhat.io/openshift3/apb-tools',
	'registry.redhat.io/openshift3/automation-broker-apb',
	'registry.redhat.io/openshift3/csi-attacher',
	'registry.redhat.io/openshift3/csi-driver-registrar',
	'registry.redhat.io/openshift3/csi-livenessprobe',
	'registry.redhat.io/openshift3/csi-provisioner',
	'registry.redhat.io/openshift3/grafana',
	'registry.redhat.io/openshift3/local-storage-provisioner',
	'registry.redhat.io/openshift3/manila-provisioner',
	'registry.redhat.io/openshift3/mariadb-apb',
	'registry.redhat.io/openshift3/mediawiki',
	'registry.redhat.io/openshift3/mediawiki-apb',
	'registry.redhat.io/openshift3/mysql-apb',
	'registry.redhat.io/openshift3/ose-ansible-service-broker',
	'registry.redhat.io/openshift3/ose-cli',
	'registry.redhat.io/openshift3/ose-cluster-autoscaler',
	'registry.redhat.io/openshift3/ose-cluster-capacity',
	'registry.redhat.io/openshift3/ose-cluster-monitoring-operator',
	'registry.redhat.io/openshift3/ose-console',
	'registry.redhat.io/openshift3/ose-configmap-reloader',
	'registry.redhat.io/openshift3/ose-control-plane',
	'registry.redhat.io/openshift3/ose-deployer',
	'registry.redhat.io/openshift3/ose-descheduler',
	'registry.redhat.io/openshift3/ose-docker-builder',
	'registry.redhat.io/openshift3/ose-docker-registry',
	'registry.redhat.io/openshift3/ose-efs-provisioner',
	'registry.redhat.io/openshift3/ose-egress-dns-proxy',
	'registry.redhat.io/openshift3/ose-egress-http-proxy',
	'registry.redhat.io/openshift3/ose-egress-router',
	'registry.redhat.io/openshift3/ose-haproxy-router',
	'registry.redhat.io/openshift3/ose-hyperkube',
	'registry.redhat.io/openshift3/ose-hypershift',
	'registry.redhat.io/openshift3/ose-keepalived-ipfailover',
	'registry.redhat.io/openshift3/ose-kube-rbac-proxy',
	'registry.redhat.io/openshift3/ose-kube-state-metrics',
	'registry.redhat.io/openshift3/ose-metrics-server',
	'registry.redhat.io/openshift3/ose-node',
	'registry.redhat.io/openshift3/ose-node-problem-detector',
	'registry.redhat.io/openshift3/ose-operator-lifecycle-manager',
	'registry.redhat.io/openshift3/ose-ovn-kubernetes',
	'registry.redhat.io/openshift3/ose-pod',
	'registry.redhat.io/openshift3/ose-prometheus-config-reloader',
	'registry.redhat.io/openshift3/ose-prometheus-operator',
	'registry.redhat.io/openshift3/ose-recycler',
	'registry.redhat.io/openshift3/ose-service-catalog',
	'registry.redhat.io/openshift3/ose-template-service-broker',
	'registry.redhat.io/openshift3/ose-tests',
	'registry.redhat.io/openshift3/ose-web-console',
	'registry.redhat.io/openshift3/postgresql-apb',
	'registry.redhat.io/openshift3/registry-console',
	'registry.redhat.io/openshift3/snapshot-controller',
	'registry.redhat.io/openshift3/snapshot-provisioner',
	'registry.redhat.io/openshift3/ose-efs-provisioner',
	'registry.redhat.io/openshift3/metrics-cassandra',
	'registry.redhat.io/openshift3/metrics-hawkular-metrics',
	'registry.redhat.io/openshift3/metrics-hawkular-openshift-agent',
	'registry.redhat.io/openshift3/metrics-heapster',
	'registry.redhat.io/openshift3/metrics-schema-installer',
	'registry.redhat.io/openshift3/oauth-proxy',
	'registry.redhat.io/openshift3/ose-logging-curator5',
	'registry.redhat.io/openshift3/ose-logging-elasticsearch5',
	'registry.redhat.io/openshift3/ose-logging-eventrouter',
	'registry.redhat.io/openshift3/ose-logging-fluentd',
	'registry.redhat.io/openshift3/ose-logging-kibana5',
	'registry.redhat.io/openshift3/prometheus',
	'registry.redhat.io/openshift3/prometheus-alertmanager',
	'registry.redhat.io/openshift3/prometheus-node-exporter',
	'registry.redhat.io/jboss-amq-6/amq63-openshift',
	'registry.redhat.io/jboss-datagrid-7/datagrid71-openshift',
	'registry.redhat.io/jboss-datagrid-7/datagrid71-client-openshift',
	'registry.redhat.io/jboss-datavirt-6/datavirt63-openshift',
	'registry.redhat.io/jboss-datavirt-6/datavirt63-driver-openshift',
	'registry.redhat.io/jboss-decisionserver-6/decisionserver64-openshift',
	'registry.redhat.io/jboss-processserver-6/processserver64-openshift',
	'registry.redhat.io/jboss-eap-6/eap64-openshift',
	'registry.redhat.io/jboss-eap-7/eap71-openshift',
	'registry.redhat.io/jboss-webserver-3/webserver31-tomcat7-openshift',
	'registry.redhat.io/jboss-webserver-3/webserver31-tomcat8-openshift',
	'registry.redhat.io/openshift3/jenkins-2-rhel7',
	'registry.redhat.io/openshift3/jenkins-agent-maven-35-rhel7',
	'registry.redhat.io/openshift3/jenkins-agent-nodejs-8-rhel7',
	'registry.redhat.io/openshift3/jenkins-slave-base-rhel7',
	'registry.redhat.io/openshift3/jenkins-slave-maven-rhel7',
	'registry.redhat.io/openshift3/jenkins-slave-nodejs-rhel7',
	'registry.redhat.io/rhscl/mongodb-32-rhel7',
	'registry.redhat.io/rhscl/mysql-57-rhel7',
	'registry.redhat.io/rhscl/perl-524-rhel7',
	'registry.redhat.io/rhscl/php-56-rhel7',
	'registry.redhat.io/rhscl/postgresql-95-rhel7',
	'registry.redhat.io/rhscl/python-35-rhel7',
	'registry.redhat.io/redhat-sso-7/sso70-openshift',
	'registry.redhat.io/rhscl/ruby-24-rhel7',
	'registry.redhat.io/redhat-openjdk-18/openjdk18-openshift',
	'registry.redhat.io/redhat-sso-7/sso71-openshift',
	'registry.redhat.io/rhscl/nodejs-6-rhel7',
	'registry.redhat.io/rhscl/mariadb-101-rhel7',
]

component_images_no_changes: List[str] = [
	'registry.redhat.io/rhel7/etcd:3.2.22',
	'registry.redhat.io/cloudforms46/cfme-openshift-postgresql',
	'registry.redhat.io/cloudforms46/cfme-openshift-memcached',
	'registry.redhat.io/cloudforms46/cfme-openshift-app-ui',
	'registry.redhat.io/cloudforms46/cfme-openshift-app',
	'registry.redhat.io/cloudforms46/cfme-openshift-embedded-ansible',
	'registry.redhat.io/cloudforms46/cfme-openshift-httpd',
	'registry.redhat.io/cloudforms46/cfme-httpd-configmap-generator',
	'registry.redhat.io/rhgs3/rhgs-server-rhel7',
	'registry.redhat.io/rhgs3/rhgs-volmanager-rhel7',
	'registry.redhat.io/rhgs3/rhgs-gluster-block-prov-rhel7',
	'registry.redhat.io/rhgs3/rhgs-s3-server-rhel7',
]

component_images: List[str] = [ f'{url}:{system_tag_version}' for url in component_images_no_tag ]
component_images.extend(component_images_no_changes)



Namespace = str
Repository = str
Tags = List[str]

image_map: Dict[Namespace, Dict[Repository, Tags]] = {
	'fuse7': {
		'fuse-apicurito': ['1.2','1.3'],
		'fuse-apicurito-generator': ['1.2', '1.3'],
		'fuse-console': [
			'1.0', '1.1', '1.3', '1.4'
		],
		'fuse-eap-openshift': [
			'1.0', '1.1', '1.2', '1.3'
		],
		'fuse-java-openshift': [
			'1.0', '1.1', '1.2', '1.3'
		],
		'fuse-karaf-openshift': [
			'1.0', '1.1', '1.2', '1.3'
		]
	},
	'dotnet': {
		'dotnetcore-10-rhel7': ['1.0'],
		'dotnetcore-10-rhel7': ['1.1'],
		'dotnetcore-20-rhel7': ['2.0'],
		'dotnetcore-21-rhel7': ['2.1'],
		'dotnetcore-22-rhel7': ['2.2'],
		'dotnet-20-runtime-rhel7': ['2.0'],
		'dotnet-21-runtime-rhel7': ['2.1'],
		'dotnet-22-runtime-rhel7': ['2.2'],
	},
	'jboss-eap-7-tech-preview': {
		'eap-cd-openshift': [
			'12.0', '13.0', '14.0', '15.0',
			'16.0'
		]
	},
	'jboss-fuse-6': {
		'fis-java-openshift': ['1.0', '2.0'],
		'fis-karaf-openshift': ['1.0', '2.0']
	},
	'rhscl': {
		'httpd-24-rhel7': ['latest'],
		'mariadb-101-rhel7': ['latest'],
		'mariadb-102-rhel7': ['latest'],
		'mysql-55-rhel7': ['latest'],
		'mysql-56-rhel7': ['latest'],
		'mysql-57-rhel7': ['latest'],
		'nginx-110-rhel7': ['latest'],
		'nginx-112-rhel7': ['latest'],
		'nginx-18-rhel7': ['latest'],
		'nodejs-4-rhel7': ['latest'],
		'nodejs-6-rhel7': ['latest'],
		'nodejs8-rhel7': ['latest'],
		'php-56-rhel7': ['latest'],
		'php-70-rhel7': ['latest'],
		'php-71-rhel7': ['latest'],
		'postgresql-10-rhel7': ['latest'],
		'postgresql-94-rhel7': ['latest'],
		'postgresql-95-rhel7': ['latest'],
		'postgresql-96-rhel7': ['latest'],
		'python-27-rhel7': ['latest'],
		'python-34-rhel7': ['latest'],
		'python-35-rhel7': ['latest'],
		'python-36-rhel7': ['latest'],
		'redis-32-rhel7': ['latest'],
		'ruby-22-rhel7': ['latest'],
		'ruby-23-rhel7': ['latest'],
		'ruby-24-rhel7': ['latest'],
		'ruby-25-rhel7': ['latest']
	},
	'redhat-openjdk-18': {
		'openjdk18-openshift': [
			'1.0', '1.1', '1.2', '1.3',
			'1.4', 'latest'],
	},
	'jboss-amq-6': {
		'amq62-openshift': [
			'1.1', '1.2', '1.3', '1.4',
			'1.5', '1.6', '1.7'
		],
		'amq63-openshift': [
			'1.0', '1.1', '1.2', '1.3'
		]
	},
	'jboss-datagrid-7': {
		'datagrid73-openshift': ['1.0']
	},
	'jboss-datavirt-6': {
		'datavirt63-driver-openshift': ['1.0', '1.1'],
		'datavirt63-openshift': [
			'1.0', '1.1', '1.2', '1.3',
			'1.4'
		]
	},
	'jboss-decisionserver-6': {
		'decisionserver64-openshift': [
			'1.0', '1.1', '1.2', '1.3',
			'1.4', '1.5', '1.6'
		]
	},
	'jboss-eap-6': {
		'eap64-openshift': [
			'1.1', '1.2', '1.3', '1.4',
			'1.5', '1.6', '1.7', '1.8',
			'1.9', 'latest'
		]
	},
	'jboss-eap-7': {
		'eap70-openshift': [
			'1.3', '1.4', '1.5', '1.6',
			'1.7'
		],
		'eap71-openshift': [
			'1.1', '1.2', '1.3', '1.4',
			'latest'
		],
		'eap72-openshift': ['1.0', 'latest']
	},
	'jboss-processserver-6': {
		'processserver64-openshift': [
			'1.0', '1.1', '1.2', '1.3',
			'1.4', '1.5', '1.6'
		]
	},
	'jboss-webserver-3': {
		'webserver30-tomcat7-openshift': [
			'1.1', '1.2', '1.3'
		],
		'webserver30-tomcat8-openshift': [
			'1.1', '1.2', '1.3'
		],
		'webserver31-tomcat7-openshift': [
			'1.1', '1.2', '1.3'
		],
		'webserver31-tomcat8-openshift': [
			'1.1', '1.2', '1.3'
		],
	},
	'openshift3': {
		'jenkins-1-rhel7': ['latest'],
		'jenkins-2-rhel7': ['v3.11'],
		'mongodb-24-rhel7': ['latest'],
		'mongodb-26-rhel7': ['latest'],
		'mongodb-32-rhel7': ['latest'],
		'mongodb-36-rhel7': ['latest'],
		'nodejs-010-rhel7': ['latest'],
		'perl-516-rhel7': ['latest'],
		'perl-520-rhel7': ['latest'],
		'perl-524-rhel7': ['latest'],
		'perl-526-rhel7': ['latest'],
		'php-55-rhel7': ['latest'],
		'postgresql-92-rhel7': ['latest'],
		'python-33-rhel7': ['latest'],
		'ruby-20-rhel7': ['latest'],
	},
	'rhoar-nodejs': {
		'nodejs-10': ['latest'],
		'nodejs-8': ['latest'],
	},
	'redhat-sso-7': {
		'sso70-openshift': ['1.3', '1.4'],
		'sso71-openshift': [
			'1.0', '1.1', '1.2', '1.3'
		],
		'sso72-openshift': [
			'1.0', '1.1', '1.2'
		],
	},
	'rhdm-7': {
		'rhdm70-decisioncentral-openshift': ['1.1'],
		'rhdm70-kieserver-openshift': ['1.0', '1.1'],
		'rhdm71-controller-openshift': ['1.0', '1.1'],
		'rhdm71-decisioncentral-openshift': ['1.0', '1.1'],
		'rhdm71-kieserver-openshift': ['1.0', '1.1'],
		'rhdm72-controller-openshift': ['1.0', '1.1'],
		'rhdm72-decisioncentral-openshift': ['1.0', '1.1'],
		'rhdm72-kieserver-openshift': ['1.0', '1.1'],
		'rhdm73-controller-openshift': ['1.0', '1.1'],
		'rhdm73-decisioncentral-openshift': ['1.0', '1.1'],
		'rhdm73-kieserver-openshift': ['1.0', '1.1'],
	},
	'rhdm-7-tech-preview': {
		'rhdm71-decisioncentral-indexing-openshift': ['1.0', '1.1'],
		'rhdm71-optaweb-employee-rostering-openshift': ['1.0', '1.1'],
		'rhdm72-decisioncentral-indexing-openshift': ['1.0', '1.1'],
		'rhdm72-optaweb-employee-rostering-openshift': ['1.0', '1.1'],
		'rhdm73-decisioncentral-indexing-openshift': ['1.0', '1.1'],
		'rhdm73-optaweb-employee-rostering-openshift': ['1.0', '1.1'],
	},
	'rhpam-7-tech-preview': {
		'rhpam70-businesscentral-indexing-openshift': [
			'1.0', '1.1', '1.2'
		],
		'rhpam71-businesscentral-indexing-openshift': ['1.0', '1.1'],
		'rhpam72-businesscentral-indexing-openshift': ['1.0', '1.1'],
		'rhpam73-businesscentral-indexing-openshift': ['1.0', '1.1'],
	},
	'rhpam-7': {
		'rhpam70-businesscentral-monitoring-openshift': ['1.0', '1.1', '1.2'],
		'rhpam70-businesscentral-openshift': ['1.0', '1.1', '1.2'],
		'rhpam70-controller-openshift': ['1.0', '1.1', '1.2'],
		'rhpam70-kiserver-openshift': ['1.0', '1.1', '1.2'],	
		'rhpam70-smartrouter-openshift': ['1.0', '1.1', '1.2'],
		'rhpam71-businesscentral-monitoring-openshift': ['1.0', '1.1'],
		'rhpam71-businesscentral-openshift': ['1.0', '1.1'],
		'rhpam71-controller-openshift': ['1.0', '1.1'],
		'rhpam71-kiserver-openshift': ['1.0', '1.1'],	
		'rhpam71-smartrouter-openshift': ['1.0', '1.1'],
		'rhpam72-businesscentral-monitoring-openshift': ['1.0', '1.1'],
		'rhpam72-businesscentral-openshift': ['1.0', '1.1'],
		'rhpam72-controller-openshift': ['1.0', '1.1'],
		'rhpam72-kiserver-openshift': ['1.0', '1.1'],	
		'rhpam72-smartrouter-openshift': ['1.0', '1.1'],
		'rhpam73-businesscentral-monitoring-openshift': ['1.0', '1.1'],
		'rhpam73-businesscentral-openshift': ['1.0', '1.1'],
		'rhpam72-controller-openshift': ['1.0', '1.1'],
		'rhpam73-kiserver-openshift': ['1.0', '1.1'],	
		'rhpam73-smartrouter-openshift': ['1.0', '1.1'],
	}
}


# Build the fqdn for the user images
user_images: List[str] = []
for namespace, repositories in image_map.items():
	for repository, tags in repositories.items():
		user_image = [ f'{registry}/{namespace}/{repository}:{tag}' for tag in tags ]
		user_images.extend(user_image)
