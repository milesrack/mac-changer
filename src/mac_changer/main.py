#!/usr/bin/env python3
import argparse
import random
import subprocess
import os

def check_uid():
	if os.getuid() != 0:
		print("[!] This script must be run as root!")
		exit()
	elif os.name != "posix":
		print("[!] Exiting due to fatal error!")
		exit()

def get_interfaces():
	p = subprocess.run(["ls","/sys/class/net/"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	interfaces = p.stdout.decode().splitlines()
	return interfaces

def random_mac():
	address = [random.randint(0,255) for i in range(6)]
	address[0] |= 0x02
	address[0] &= ~0x01
	address = ":".join([format(b,"02x") for b in address])
	return address

def get_mac(interface):
	with open(f"/sys/class/net/{interface}/address","r") as f:
		address=f.read().strip()
	return address

def change_mac(interface,address):
	old_address = get_mac(interface)
	p1 = subprocess.run(["ip","link","set","dev",interface,"down"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	p2 = subprocess.run(["ip","link","set","dev",interface,"address",address],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	p3 = subprocess.run(["rfkill","unblock","all"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	p4 = subprocess.run(["ip","link","set","dev",interface,"up"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	if p1.stderr or p2.stderr or p3.stderr or p4.stderr:
		print(f"[!] Failed to change MAC address for {interface}")
	else:
		print(f"[+] {interface}: {old_address} => {address}")

def parse_args():
	parser = argparse.ArgumentParser(prog="mac-changer",description="Change your MAC address to a random address or specify a new one.")
	parser.add_argument("-i","--interface",help="Network interface to modify MAC address (default all)")
	parser.add_argument("-r","--random",action="store_false",default=True,help="Generate a random MAC address (default)")
	parser.add_argument("-a","--address",help="New MAC address")
	parser.add_argument("-l","--list",action="store_true",default=False,help="List available interfaces")
	return parser.parse_args()

def main():
	args = parse_args()
	check_uid()
	interfaces = get_interfaces()
	if args.list:
		for interface in interfaces:
			address = get_mac(interface)
			print(f"[+] {interface}: {address}")
	elif args.interface in interfaces:
		address = args.address if args.address else random_mac()
		change_mac(args.interface,address)
	else:
		prefixes = ["eth","enp","wlan","wlp"]
		for interface in interfaces:
			if any(interface.startswith(prefix) for prefix in prefixes):
				address = random_mac()
				change_mac(interface,address)

if __name__ == "__main__":
	main()
