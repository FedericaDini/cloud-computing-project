# Ceph-based file manager

## How to run the application
Run the backend instance for each Ceph-mon module:

* `172.16.3.226`

``` sh
lxc exec juju-f254bd-1-lxd-0 /bin/bash
python3 backend.py
```
* `172.16.3.180`

``` sh
lxc exec juju-f254bd-2-lxd-0 /bin/bash
python3 backend.py
```

* `172.16.3.197`

``` sh
lxc exec juju-f254bd-3-lxd-0 /bin/bash
python3 backend.py
```

The dispatcher is already up and running inside a Docker container exposed on `172.16.3.190:8080`

Run the client instance on `172.16.3.247`

```sh
python3 client.py
```



   
