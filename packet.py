from scapy.all import send, IP, UDP

# Define the destination IP address and UDP ports
destination_ip = '255.255.255.255'  # Destination IP address
source_ip = '192.168.1.111'         # Source IP address (change as needed)
source_port = 14236                 # Source port
destination_port = 14235            # Destination port

# Construct the packet
packet = IP(src=source_ip, dst=destination_ip) / UDP(sport=source_port, dport=destination_port)

# Send the packet
send(packet)
