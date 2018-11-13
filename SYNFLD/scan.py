from scapy.all import *

for x in range (1, 127):
	syn = IP(dst = "10.0.2.5") / TCP (sport = RandShort (), dport = x, flags = "S")
	rst = sr1 (syn, verbose = 0, timeout = 0.5)
	if rst:
		if rst [TCP] . flags == "SA":
			print (str (x) + "is open")


