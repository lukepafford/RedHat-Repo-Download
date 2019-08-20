# RedHat-Repo-Download
Documentation and scripts for syncing content from a Redhat Subscribed system for offline use

This repo will implement [RedHats 2nd approach](https://access.redhat.com/solutions/29269) for updating disconnected systems.
If you wanted to sync content for RedHat 7 servers, and workstations you would need to create two machines that perform the syncing; one system for syncing workstation content, and one system for syncing server content.

This guide makes the following assumptions:

1. You are starting with a fresh Redhat install.
1. You have a RedHat account.
1. The account has at least one valid subscription that can be attached to the system.


## Process
1. Register the system to Redhat.
```
subscription-manager register
```

2. Attach all available subscriptions to the system. Execute this repos helper script to quickly attach subscriptions to the system.
```
./subscribe-all.sh
```

3. Generate a list of all repository IDs and save these to a file.
```
subscription-manager repos --list | grep 'Repo ID' | awk '{print $3}' | sort -u > available-repos.txt
```

4. Dependening on how many subscriptions you have, there may be a large amount of repositories, and you likely won't want to sync all the content. Copy the file, and manually delete any repositories that you don't want. Name this file to something appropriate such as `enabled-repos.txt`

5. Sync all of the repositories to the local system using this repos helper sync script. The first argument is the file that contains the repositories that you want to sync (one repo ID for each line) and the second argument is the directory they will be synced to
```
./sync-repos.sh enabled-repos.txt repositories
```

## Conclusion

Your system should now have all of the desired content synced locally, and you can move the content to your disconnected systems, and make it available.
