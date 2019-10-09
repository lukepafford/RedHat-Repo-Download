#!/bin/bash -l
rootDir=$(realpath $(dirname $0))
dest=/share

mkdir -p "${dest}"
chmod 0777 "${dest}"

# Remove anything older than a month
find "${dest}" -mtime +30 -delete

cd "${rootDir}"
bash sync-repos.sh enabled-repos.txt repositories
bash archive-files.sh repositories "${dest}/rhel7-server-patches-$(date --iso-8601).tar.gz" 7
