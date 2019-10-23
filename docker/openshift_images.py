#!/usr/bin/python3
from typing import List, Dict, NewType, Union

system_tag_version: str = 'v3.11.135'
registry = 'registry.redhat.io'

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


user_images: List[str] = []
for namespace, repositories in image_map.items():
	for repository, tags in repositories.items():
		user_image = [ f'{registry}/{namespace}/{repository}:{tag}' for tag in tags ]
		user_images.extend(user_image)
