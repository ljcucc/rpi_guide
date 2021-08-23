#!/usr/local/bin/python3

ssid = input("wifi ssid: ")
passwd = input("wifi password: ")

template = """country=TW
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="%s"
    psk="%s"
    key_mgmt=WPA-PSK
}""" % (ssid, passwd)

with open("wpa_supplicant.conf", "w") as f:
    f.write(template)
