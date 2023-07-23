# mac-changer
A Python script to change your MAC address to a random value or specify a new one.

## Installation
```
git clone https://github.com/milesrack/mac-changer
cd mac-changer
sudo python3 setup.py install
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