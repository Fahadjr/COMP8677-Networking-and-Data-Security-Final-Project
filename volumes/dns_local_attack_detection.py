#!/usr/bin/env python3
import os
from nslookup import Nslookup
import socket
import sys

try:
	domain = sys.argv[1]
except:
	print("Enter the URL for which you want to check the IP Address:")
	domain = input()
	if domain == '':
	    	print("Domain name cannot be empty")
	    	exit(1)

# Creates NSlookup object with parameters such as tcp = False i.e. UDP, 
# and dns_server ip (local dns is the default value)
local_dns_query = Nslookup(verbose=False, tcp=False)

# Lookup in the local DNS for the IP address corresponding to the domain name provided by user
local_ips_record = local_dns_query.dns_lookup(domain)

# The local ip of the domain will be obtained
local_ip = local_ips_record.answer[0]


# Creates NSlookup object with parameters such as tcp = False i.e. UDP, 
# and dns_server ip (public dns = 1.1.1.1) 
public_dns_query = Nslookup(dns_servers=["1.1.1.1"], verbose=False, tcp=False)

# Lookup in the public DNS for the IP address corresponding to the domain name provided by user
ips_record = public_dns_query.dns_lookup(domain)

# The actual/public ip of the domain will be obtained to verify the DNS entry
actual_ip = ips_record.answer[0]

# If the actual ip is different then what user is seeing on the PC i.e. IP is spoofed
if actual_ip != local_ip:
	try:
		socket.gethostbyaddr(local_ip)
		print("No IP spoofing detected! :)")
	except:
		print("Warning!!!!!!!")
		print("IP Address is spoofed.\nActual IP: ", actual_ip, "and Spoofed IP: ", local_ip)
else:
	print("No IP spoofing detected! :)")
