# Network Sniffer: Technical Logic & Explanation

**Project:** CodeAlpha Cybersecurity Internship  
**Module:** Network Traffic Analysis  

This document provides a technical walkthrough of the **Network Sniffer** implementation. The script utilizes the **Scapy** library to interact with the Network Interface Card (NIC) and process packets in real-time.

---
## 1. Importing Libraries

```python
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from colorama import init, Fore
```

sniff: The main function from Scapy that actually listens to the network.

IP, TCP, UDP, ICMP: Specific "layers" of a network packet. Think of these as templates we use to read the data.

colorama: A library used to make the terminal text colored (Red, Blue, Green) so it is easier to read.

## 2. Setting Up Colors

```python
init()
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
RESET = Fore.RESET
```

init(): Initializes the color settings for Windows compatibility.

Variables: We store color codes in variables (like RED or BLUE) so we don't have to type Fore.RED every time we want to print something.

## 3. Helper Function: Identifying Protocols

```python
def get_protocol_name(packet):
    if packet.haslayer(TCP):
        return "TCP", RED
    elif packet.haslayer(UDP):
        return "UDP", BLUE
    elif packet.haslayer(ICMP):
        return "ICMP", GREEN
    else:
        return "Other", YELLOW
```

Goal: This function looks at a packet and decides what "Type" it is.

Logic:

If it has a TCP layer (Web browsing, file transfers), label it Red.

If it has a UDP layer (Streaming, DNS), label it Blue.

If it is ICMP (Ping), label it Green.

Everything else is Yellow.

## 4. The Core Logic: Processing Each Packet

```python
def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol_name, color = get_protocol_name(packet)
```

packet_callback: This is a custom function that runs every single time a packet is captured.

if packet.haslayer(IP): This is a filter. We only care about Internet Protocol (IP) packets. We ignore local noise like ARP packets.

src / dst: We extract the Source IP (who sent it) and Destination IP (where it is going).

## 5. Extracting Port Numbers

```python
        sport = "N/A"
        dport = "N/A"
        if packet.haslayer(TCP):
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif packet.haslayer(UDP):
            sport = packet[UDP].sport
            dport = packet[UDP].dport
```

Context: IP addresses tell us the computer, but Ports tell us the application (e.g., Port 80 is Web, Port 53 is DNS).

Logic: Since only TCP and UDP use ports (ICMP does not), we check for those layers specifically. If found, we extract the Source Port (sport) and Destination Port (dport).

## 6. Printing the Output

```python
        print(f"{color}[*] {src_ip}:{sport} --> {dst_ip}:{dport} | Protocol: {protocol_name}{RESET}")
```

This line combines everything we found into a clean, readable string.

It uses the color variable we determined earlier to print the line in Red, Blue, or Green.

RESET: Crucial—this turns the color back to white at the end of the line so the whole terminal doesn't stay red.

## 7. Inspecting the Payload (The Data)

```python
        if packet.haslayer('Raw'):
            try:
                payload = packet['Raw'].load.decode('utf-8', errors='ignore')
                if payload:
                    print(f"    {YELLOW}Payload Snippet: {payload[:50]}...{RESET}")
            except:
                pass
```

packet.haslayer('Raw'): This checks if the packet carries data (the "Payload").

.decode('utf-8'): Network data is sent in bytes (numbers). We try to turn it into readable text.

errors='ignore': If the data is encrypted (gibberish), Python might crash trying to read it. This command tells Python to skip unreadable characters instead of crashing.

[:50]: We only print the first 50 characters to keep the screen clean.

## 8. Starting the Sniffer

```python
def start_sniffer():
    print(f"{GREEN}Starting Network Sniffer...{RESET}")
    sniff(prn=packet_callback, store=0)
```

sniff(...): This is the engine starter.

prn=packet_callback: Tells Scapy, "Every time you catch a packet, send it to my packet_callback function."

store=0: Tells Scapy not to save packets in RAM. Without this, your computer would run out of memory if you left the sniffer running for a long time.