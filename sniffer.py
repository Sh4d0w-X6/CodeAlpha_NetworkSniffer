import os
import platform
from scapy.all import sniff, conf

# Fix for Windows
if platform.system() == "Windows":
    conf.use_pcap = True

def packet_callback(packet):
    print("\n📦 Packet Captured!")

    if packet.haslayer("IP"):
        ip = packet["IP"]
        print(f"Source IP: {ip.src}")
        print(f"Destination IP: {ip.dst}")

    if packet.haslayer("TCP"):
        tcp = packet["TCP"]
        print("Protocol: TCP")
        print(f"Source Port: {tcp.sport}")
        print(f"Destination Port: {tcp.dport}")

    elif packet.haslayer("UDP"):
        udp = packet["UDP"]
        print("Protocol: UDP")
        print(f"Source Port: {udp.sport}")
        print(f"Destination Port: {udp.dport}")

    print(f"Packet Size: {len(packet)} bytes")
    print("-" * 40)

def start_sniffing():
    print(f"Running on: {platform.system()}")

    try:
        sniff(prn=packet_callback, count=20)
    except PermissionError:
        print("❌ Permission denied! Run as Administrator / root.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    start_sniffing()