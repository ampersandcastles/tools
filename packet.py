from scapy.all import sendp, Ether, IP, UDP

destination_ip = '255.255.255.255'
source_ip = '192.168.100.223'
source_mac = '8c:16:45:68:54:80'
destination_mac = 'ff:ff:ff:ff:ff:ff'  # Broadcast MAC address
source_port = 14236
destination_port = 14235

packet = Ether(src=source_mac, dst=destination_mac) / IP(src=source_ip, dst=destination_ip) / UDP(sport=source_port, dport=destination_port)

sendp(packet)
