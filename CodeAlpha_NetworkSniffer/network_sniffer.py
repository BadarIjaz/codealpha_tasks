from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from colorama import init, Fore

# Initialize colorama
init()

# Define colors for different protocols
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
RESET = Fore.RESET

def get_protocol_name(packet):
    if packet.haslayer(TCP):
        return "TCP", RED
    elif packet.haslayer(UDP):
        return "UDP", BLUE
    elif packet.haslayer(ICMP):
        return "ICMP", GREEN
    else:
        return "Other", YELLOW

def packet_callback(packet):
    # Only process packets with an IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol_name, color = get_protocol_name(packet)
        
        # Try to get Port numbers (only for TCP/UDP)
        sport = "N/A"
        dport = "N/A"
        if packet.haslayer(TCP):
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif packet.haslayer(UDP):
            sport = packet[UDP].sport
            dport = packet[UDP].dport

        # Print the packet info in a clean, color-coded format
        print(f"{color}[*] {src_ip}:{sport} --> {dst_ip}:{dport} | Protocol: {protocol_name}{RESET}")

        # Show Payload Data (if available and interesting)
        if packet.haslayer('Raw'):
            try:
                # Try to decode as text, otherwise just show raw bytes
                payload = packet['Raw'].load.decode('utf-8', errors='ignore')
                # Only print if payload is not empty
                if payload:
                    print(f"    {YELLOW}Payload Snippet: {payload[:50]}...{RESET}")
            except:
                pass

def start_sniffer():
    print(f"{GREEN}Starting Network Sniffer...{RESET}")
    print(f"{GREEN}Press Ctrl+C to stop.{RESET}")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    start_sniffer()