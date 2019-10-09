# RedHat-Repo-Download
Documentation and scripts for syncing content from a Redhat Subscribed system for offline use.


> ️⚠ **WARNING** scripts not listed in this `README.md` are for personal use, and you dont have to pay attention to them.


This repo will implement [RedHats 2nd approach](https://access.redhat.com/solutions/29269) for updating disconnected systems.
If you wanted to sync content for RedHat 7 servers, and workstations you would need to create two machines that perform the syncing; one system for syncing workstation content, and one system for syncing server content.

This guide makes the following assumptions:

1. You are starting with a fresh Redhat install.
1. You have a RedHat account.
1. The account has at least one valid subscription that can be attached to the system.


# Downloading Patches

## Process
1. Register the system to Redhat.
```
subscription-manager register
```

2. Temporarily auto attach a subscription to allow us to install packages.
```
subscription-manager attach --auto
```

3. Install Git and clone this repository to your target system.
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

6. Dependening on how many subscriptions you have, there may be a large amount of repositories, and you likely won't want to sync all the content. Copy the `available-repos.txt` file, and manually delete any repositories that you don't want. Name this file to something appropriate such as `enabled-repos.txt`.

7. Sync all of the repositories to the local system using this repos `sync-repos.sh` script. The first argument is the file that contains the repositories that you want to sync and the second argument is the directory they will be synced to.
```
bash sync-repos.sh enabled-repos.txt repositories
```

## Conclusion

Your system should now have all of the desired content synced locally, and you can move the content to your disconnected systems, and make it available.

# Syncing patches to offline Satellite server (optional)

If you run an offline Satellite server and host your own CDN, then you can use this repos ansible playbook at `sync_patches/main.yml`.
The playbook is risky since it depends on an implementation detail of Satellite by querying the Postgresql database to get repository information.
*WARNING* This playbook will only work for a yum `releasever` value of either `7Workstation` or `7Server`.

1. Ensure you have `ansible` installed on the system that contains the patches.
2. Execute the playbook. You will be prompted for three values: 
  * The Satellite server hostname to connect to.
  * The directory containing the patches.
  * The base directory on the Satellite server where the files will be copied to. 
  
The playbook will synchronize all the content, update the repository metadata, and set proper permissions so Apache can access the files.
```
cd sync_patches
ansible-playbook main.yml
```
3. Synchronize all the repositories in the web UI (This could be automated but the web app does this best).
4. Publish new content views.

Your clients should now see the new content:
`yum clean all && yum makecache && yum update`
