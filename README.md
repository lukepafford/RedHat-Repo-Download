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

2. Temporarily auto attach a subscription to allow us to install packages
```
subscription-manager attach --auto
```

3. Install Git and clone this repository to your target system
```
yum -y install git
git clone https://github.com/lukepafford/RedHat-Repo-Download.git
cd RedHat-Repo-Download
```

4. Attach all available subscriptions to the system. Execute this repos `subscribe-all.sh` script to quickly attach subscriptions to the system.
```
bash subscribe-all.sh
```

5. Execute `create-available-repos-file.sh` to create the file `available-repos.txt`. This file will contain all available repositories (one repository ID per line) that you can sync from. 
```
bash create-available-repos-file.sh
```

6. Dependening on how many subscriptions you have, there may be a large amount of repositories, and you likely won't want to sync all the content. Copy the `available-repos.txt` file, and manually delete any repositories that you don't want. Name this file to something appropriate such as `enabled-repos.txt`

7. Sync all of the repositories to the local system using this repos `sync-repos.sh` script. The first argument is the file that contains the repositories that you want to sync and the second argument is the directory they will be synced to
```
bash sync-repos.sh enabled-repos.txt repositories
```

## Conclusion

Your system should now have all of the desired content synced locally, and you can move the content to your disconnected systems, and make it available.
