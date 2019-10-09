#!/bin/bash
rootDir=$(realpath $(dirname $0))
dest="${rootDir}/anaconda_packages"
days="${1:-7}"
newerThan=$(date -u -d "${days} days ago" +"%a, %d %b %Y %H:%M:%S GMT")

mkdir -p "${dest}"
wget --input-file="${rootDir}/anaconda_urls.txt" \
--mirror \
--header="If-Modified-Since: ${newerThan}" \
--directory-prefix="${dest}"
