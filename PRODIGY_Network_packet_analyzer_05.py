from scapy.all import sniff #pip install scapy
from scapy.layers.inet import IP

log_file = "packet_traffic.log"

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ip_layer.proto
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        # Determine protocol name
        if protocol == 1:
            protocol_name = "ICMP"
        elif protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        else:
            protocol_name = "Unknown"

        payload = bytes(ip_layer.payload)
        output = (f"Protocol: {protocol_name}\n"
                  f"Source IP: {src_ip}\n"
                  f"Destination IP: {dst_ip}\n"
                  f"Payload: {payload[:100]}\n" 
                  + "-"*50 + "\n")

        print(output)
        with open(log_file, "a") as f:
            f.write(output)

def main():
    print("Starting packet sniffing... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, filter="ip", store=0) 

if __name__ == "__main__":
    main()
