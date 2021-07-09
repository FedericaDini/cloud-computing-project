# CLOUD COMPUTING PROJECT

## Ceph-based file manager

## How to run the application
   run the backend instance for each Ceph-mon module on:
   172.16.3.226
   > lxc exec juju-f254bd-1-lxd-0 /bin/bash
   > python3 backend.py
   172.16.3.180
   > lxc exec juju-f254bd-2-lxd-0 /bin/bash
   > python3 backend.py
   172.16.3.197
   > lxc exec juju-f254bd-3-lxd-0 /bin/bash
   > python3 backend.py


   
