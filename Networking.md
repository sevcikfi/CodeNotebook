---
alias:
tag: IT/DevOps IT/networking CodeNotebook 
---

# Networking

## Scanning network

### ARP

arp -na | grep -i b8:27:eb

### nmap

sudo nmap -sP 192.168.1.0/24 | awk '/^Nmap/{ip=$NF}/B8:27:EB/{print ip}'
nmap -Pn 192.168.1.0/24
nmap -Sn 192.168.1.0/24
