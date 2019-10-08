#!/bin/bash
if [[ "$#" -lt 2 ]]; then
        echo "$0: src archive [days=7]"
        exit 1
fi

src="$1"
archive="$2"
days="${3:-7}"


find "${src}" -mtime -"${days}" -type f -print0 | tar -czvf "${archive}" --null --files-from=-
