import random
import string

class Packet:
    def __init__(self, source_ip, dest_ip, protocol, payload):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.protocol = protocol
        self.payload = payload

    def __str__(self):
        return (f"Source IP: {self.source_ip}\n"
                f"Destination IP: {self.dest_ip}\n"
                f"Protocol: {self.protocol}\n"
                f"Payload (sample): {self.payload[:20]}...")

def generate_packet(source_ip, dest_ip, protocol):
    """Simulates a network packet with random data."""
    payload = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(100))
    return Packet(source_ip, dest_ip, protocol, payload)

def analyze_packet(packet):
    """Analyzes a simulated packet and displays relevant information."""
    print(packet)

def main():
    """Simulates network traffic and analyzes packets."""
    packets = [
        generate_packet("122.139.1.11", "8.8.8.8", "TCP"),
        generate_packet("10.0.0.1", "172.16.0.2", "UDP"),
        generate_packet("137.0.0.1", "localhost", "HTTP")
    ]

    for packet in packets:
        analyze_packet(packet)

if __name__ == "__main__":
    main()
