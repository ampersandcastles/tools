from scapy.all import send, IP, UDP

destination_ip = '255.255.255.255'
source_ip = '192.168.1.121'
source_port = 14236
destination_port = 14235

packet = IP(src=source_ip, dst=destination_ip) / UDP(sport=source_port, dport=destination_port)

send(packet)