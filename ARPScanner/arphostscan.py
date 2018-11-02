import sys
from datetime import datetime
from scapy.all import *


iface = "eth0"
ips = raw_input("Range of IPs : ")


print "\nScanning..!"
start_time = datetime.now()


conf.verb = 0
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2, iface=iface,inter=0.1,verbose=0)

print "MAC - IP\n"
for snd,rcv in ans:
	print rcv.sprintf(r"%Ether.src% - %ARP.psrc%") 
stop_time = datetime.now()
total_time = stop_time - start_time
print "\n Scan Complete!"
print (" Scan Duration: %s" %(total_time))