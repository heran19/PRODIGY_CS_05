from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        proto_name = {6: "TCP", 17: "UDP", 1: "ICMP"}.get(proto, str(proto))

        print(f"\nSource IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {proto_name}")

        if TCP in packet:
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        if packet.haslayer('Raw'):
            payload = bytes(packet['Raw'].load)
            print(f"Payload (first 50 bytes): {payload[:50]}")

print("Starting packet sniffer... (Ctrl+C to stop)")
print("Note: Requires admin/root privileges. For educational use on your own network only.")

sniff(prn=process_packet, store=False, count=20)
