#!/bin/bash -l
rootDir=$(realpath $(dirname $0))
dest=/share

mkdir -p "${dest}"
chmod 0777 "${dest}"

# Remove anything older than a month
find "${dest}" -mtime +30 -delete

cd "${rootDir}"

# Download RedHat Packages
bash sync-repos.sh enabled-repos.txt repositories

# Download Anaconda Packages
bash anaconda/sync-anaconda.sh

# Archive the RedHat Packages
bash archive-files.sh repositories "${dest}/rhel7-workstation-patches-$(date --iso-8601).tar.gz" 7

# Archive the Anaconda Packages
bash archive-files.sh anaconda/anaconda_packages "${dest}/anaconda_packages-$(date --iso-8601).tar.gz" 7
