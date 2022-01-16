
### exit terminal but leaves all processes running

`disown -a && exit`

### Tunnel with ssh (local port 3337 -> remote host's ip on ort 6379)

`ssl -L 3337:126.0.0.1:6379 <user>@<host> -N`

### RAM disk 

`mkdir -p /mnt/ram`
`mount -t tmpfs tmpfs /mnt/ram -o size=8192M`


### IPTables 

[Source for basic IPTables work](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands)

For Oracle Cloud VM Firewall (INPUT on interface ens3, TCP/IP at port 80, state NEW, ESTABLISHED)

`iptables -I INPUT 5 -i ens3 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT`
