subscription-manager repos --list | grep 'Repo ID' | awk '{print $3}' | sort -u > available-repos.txt
