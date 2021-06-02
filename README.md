# From  Aleksa Tamburkovski: https://www.youtube.com/watch?v=0NQ2aMxBYNE

# ARP Spoofer tool 2021, automated loop

## To forward traffic(so target machine can access internet) in terminal before spoof, enter:
##                  ""  echo 1 >> /proc/sys/net/ipv4/ip forward        ""
## Run command:     ""  python3 arpspoofer.py <router IP> <target IP>  ""
###        e.g.         python3 arpspoofer.py 192.168.1.1 192.168.1.4
