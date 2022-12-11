import scapy.all as scapy
from python_arptable import ARPTABLE

def mac(ipadd):
    arp_r = scapy.ARP(pdst=ipadd)
    br = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    list_1 = scapy.srp((br / arp_r), timeout=5, verbose=False)[0]
    return list_1[0][1].hwsrc


def sniff(interface):
    f = "tcp and src host 10.0.2.10 and dst 10.0.2.8"
    scapy.sniff(iface=interface, filter=f, store=False, prn=pr_packets)


def pr_packets(packet):
	print(packet.show())
	server = None

	for arp in ARPTABLE:
		if arp['IP address'] == packet[scapy.IP].src:
			server = arp['HW address']
    
	if packet[scapy.Ether].src != server:
		print(packet[scapy.Ether].src, server)
		print('MAC has been spoofed from this:' + str(packet[scapy.Ether].src) + '\n Packets have been spoofed')
	else:
		print('Recieved from the Trusted Server')

sniff(interface="eth0")