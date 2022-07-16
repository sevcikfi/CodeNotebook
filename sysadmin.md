# Basics stuff one looks up all the time

## File rights + ownership

`chmod`

`chown -Rv user[:group] FILE`

## Disks and Drives

`df -HT`,`lsblk` (no SU), `fdisk -l`, `blkid`
### Partitions

**!BE CAREFUL!** altho fdisk need confirm to write, use print to triple check
`sudo fdisk /dev/sdx`
### Filesystems

`mkfs.<type> [-j] /dev/sdxn`
`e2label /dev/sdxn "label name"`

### Mounting

to mount `sudo mount /dev/sdxn /where/to`

in `fstabl/` add entry and do `mount -a`
```
#FS,LABEL= or UUID=  /mnt/pnt/  fstype  options  dump  pass 
LABEL=MY_BACKUP    /mount/point  ext4  defaults   1     2
```

### exit terminal but leaves all processes running

`disown -a && exit`

### Tunnel with ssh (local port 3337 -> remote host's ip on port 6379)

`ssl -L 3337:126.0.0.1:6379 <user>@<host> -N`

### RAM disk 

`mkdir -p /mnt/ram`
`mount -t tmpfs tmpfs /mnt/ram -o size=8192M`


### IPTables 

[Source for basic IPTables work](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands)

For Oracle Cloud VM Firewall (INPUT on interface ens3, TCP/IP at port 80, state NEW, ESTABLISHED)

`iptables -I INPUT 5 -i ens3 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT`
