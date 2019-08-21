#!/bin/bash
if [[ "$#" -ne 2 ]]; then
        echo "$0 repoFile destination"
        exit 1
fi

if ! rpm -q yum-utils > /dev/null 2>&1; then
        yum -y install yum-utils
fi

repoFile="$1"
dest="$2"

for repoId in $(cat "$repoFile"); do
        reposync --repoid=$repoId --downloadcomps --download-metadata --newest-only --download_path=$dest
done
