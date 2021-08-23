# headless setup your RPi

> tested on macOS (intel)

1. Build a sdcard with a lite version of Raspbian
2. after finished, run `main.py` setup your wifi
3. after enter your wifi ssid and password, `main.py` will create a `wpa_supplicant.conf`
4. run `run.sh` to create files to `/Volumns/boot` (if not detected, try put out and in to sdcard reader again)
5. boot RPi and connect it with ssh domain: `ssh pi@raspberrypi.local`
6. enter default password `raspberry` and you're good to go.