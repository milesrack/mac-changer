# mac-changer
A Python script to change your MAC address to a random value or specify a new one.

## Installation
```
git clone https://github.com/milesrack/mac-changer
cd mac-changer
pipx install .
```

## Usage
```
usage: mac-changer [-h] [-i INTERFACE] [-r] [-a ADDRESS] [-l]

Change your MAC address to a random address or specify a new one.

options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Network interface to modify MAC address (default all)
  -r, --random          Generate a random MAC address (default)
  -a ADDRESS, --address ADDRESS
                        New MAC address
  -l, --list            List available interfaces
```

## Examples
Random MAC address for all valid wireless and ethernet network interfaces:
```
sudo mac-changer
```
List available network interfaces:
```
sudo mac-changer --list
```
Random MAC address for `wlan0` interface:
```
sudo mac-changer -i wlan0
```
Set MAC address `12:34:56:78:9a:bc` for `wlan0` interface:
```
sudo mac-changer -i wlan0 -a 12:34:56:78:9a:bc
```
