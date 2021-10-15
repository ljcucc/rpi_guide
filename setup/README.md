# Setup ansible playbook

## Reqiurements

* Your Raspberry pi * 1
* Installation of ansible on your computer is reqiured.

## how to start?

1. create `hosts` file in this folder

like this:
```
[pi]
raspberrypi.local ansible_connection=ssh ansible_user=pi
```

2. run `ansible-playbook (playbook you want to try).yml -i hosts`

here are some playbook you can run to install packages:

* `setup_with_opencv.yml`