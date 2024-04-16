---
alias:
tag: CodeNotebook
---

# Basics stuff one looks up all the time

## Moving around system

`cd path/to/dir` to change directory, `cd ..` to move one dir up

`pwd` to write out current absolute path e.g. `/home/user/.ssh`

`ls` to write out the content of current dir (possible append with path `ls some/place`), popular options include:

- `-a` for all, `-A` for all without `.` and `..`
- `-l` for long format, `-g` just without author, `-G` without group
- `-F` to append one of `*/=>@|)` to entries
- `--color=always` to show colours
- `-h` for man-readable, useful with `-l` and `-s`
- `-s` print size in blocks
- `-r` to reverse order
- `-S` sort by size, descending
- `-t` sort by time creation, descending
- `-clt` sort by ctime (modification), descending
- `-ut` sort by access time, descending
- `-U` no sorting
- `-X` sort by extensions
- `-R` for recursive listing
- `-n` is like `-l` but numbers instead of strings

## Info and find stuff

### uname

to find software info about current OS `uname -a`

### lsb_release

to find info about current release `lsb_release -a`

### neofetch

Install neofetch for pretty print of basic HW and SW info `neofetch`

### which

`which command` to find the path to command

### type

`type command` to find what kind of command is, whether programme, executable or shell built-in

### find

Utilized by `find <starting-directory> <options> <search term>` and most basic being:

```bash
find . -name my-file
```

Other options are:

- `-iname` for case-insensitivity
- `-not` for negation
- `-type` followed by `d`irectory, `f`ile, `l`ink, `c`haracter and `b`lock device
- `-delete` to delete the found files
- `-size <size> <unit>`, possible use `ckMG` for byte, kilo, mega, giga `10M`
- `-user` by user
- `-group` by group
- `-perm` by perm (alternative `-empty` for empty files, `-exec` for executables and `-read`  for readable)

### locate

Alternative to `find` is `locate` which indexes your whole system and runs the command on the database. You may install it and run it via following:

```bash
sudo apt-get update
sudo apt-get install mlocate
sudo updatedb
```

## File rights + ownership

TODO: write a bit more about these

`chmod`

`chown -Rv user[:group] FILE`

`chgrg`

## Multiple TTYs

### exit terminal but leaves all processes running

`disown -a && exit`

### Screen

For simple command persistence, use `screen`, then run your command and leave with `CTRL+A D`. To come back, use `screen -r`. If you have more screens running, it'll list all of them with last command and let you choose one of them.

### Tmux

*it certainly exists*.

## systemd

### Basic command

For system state:

- `systemctl status` show current status
- `systemctl --failed` show failed units

Checking *unit* status:

- `systemctl status unit` includes whether it's running
- `systemctl is-enabled unit`

Management, all requires root/sudo:

- `systemctl start unit`
- `systemctl stop unit`
- `systemctl restart unit`
- `systemctl reload unit` (reloads unit's config)
- `systemctl daemon-reload` (scan for changes)

Enabling units i.e. starting at boot

- `systemctl enable unit`
- `systemctl enable --now unit` to enable and start right away
- `systemctl disable unit`

### adding a service

In `etc/systemd/system/your.service` we write following

```ini
[Unit]
Description=Your service here
After=network.target #what part of system is required
StartLimitIntervalSec=0
[Service]
Type=simple
Restart=always #on-failure option
RestartSec=1 #interval before restarting
User=YourUser #important for file access
ExecStart=/path/to/bin command args

[Install]
WantedBy=multi-user.target
```

and start it with `systemctl start your.service`.

## Disks and Drives

`df -HT`,`lsblk` (no SU), `fdisk -l`, `blkid`

### Partitions

**!BE CAREFUL!** Altho fdisk need confirm to write, use print to triple check
`sudo fdisk /dev/sdx`

### Filesystems

`mkfs.<type> [-j] /dev/sdxn`
`e2label /dev/sdxn "label name"`

### Mounting

to mount `sudo mount /dev/sdxn /where/to`

in `/etc/fstab` add entry and do `mount -a`

```text
#FS,LABEL= or UUID=  /mnt/pnt/  fstype  options  dump  pass
LABEL=MY_BACKUP    /mount/point  ext4  defaults   1     2
```

### RAM disk

`mkdir -p /mnt/ram`
`mount -t tmpfs tmpfs /mnt/ram -o size=8192M`

## Network stuff

### Network Manager CLI

`nmcli` with one of the following allows you to list, modify, manage connections & device or even allows you to use wifi to scan network, set hotspots or show password

- g[eneral]       NetworkManager's general status and operations
- n[etworking]    overall networking control
- r[adio]         NetworkManager radio switches
- c[onnection]    NetworkManager's connections
- d[evice]        devices managed by NetworkManager
- a[gent]         NetworkManager secret agent or polkit agent
- m[onitor]       monitor NetworkManager changes

E.g. to set wifi to connect automatically, do following:

```bash
nmcli connection modify NAME/UUID connection.autoconnect yes
```

## Firewalls

TODO: write a bit more about how to use either of them

All firewall manipulation will require **admin privileges**.

### ufw

### IPTables

Printing current rules is done via `iptables -L`, add `-v` for more verbosity; `iptables -S` for exact command wording

To save the rules, use:

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

### Oracle Cloud

If you're setting up service in Oracle Cloud, do not **forget** to allow particular ports and ips in secure list via webUI. However each Ubuntu and like other image with IPTables need to run following commands to make it work since the defaults make traffic into arbitrary REJECT jump. If you wanna do it ***right*** way, add the rules with `-I FLOW 5 <rest-of-rule>` (or any number before the jump rule specified bellow).

```bash
iptables -D INPUT -j REJECT --reject-with icmp-host-prohibited
iptables -D FORWARD -j REJECT --reject-with icmp-host-prohibited
```

**FIXME:** wording
To add traffic through, modify following; for Oracle Cloud VM Firewall (INPUT on interface ens3, TCP/IP at port 80, state NEW, ESTABLISHED)

```bash
iptables -A INPUT -i ens3 (NIC) -p tcp (protocol) --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
```

### terminal colours

- https://docs.rockylinux.org/gemstones/string_color/
- https://opensource.com/article/19/9/linux-terminal-colors
- https://blog.icod.de/2023/11/26/how-to-have-a-nice-looking-prompt-in-rocky-linux/
- https://unix.stackexchange.com/questions/148/colorizing-your-terminal-and-shell-environment
- https://student.cs.uwaterloo.ca/~cs452/terminal.html

```bash
#custom
    PS1='\e[33;1m\u\[\033[00m\]@\[\033[01;32m\]\h\[\033[00m\]: \[\033[01;34m\]\W\e[0m\$ '
#default deb
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
```


## Source

- [Source for basic IPTables work](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands)
- [IPtables guide](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/)
- [Systemd from arch wiki](https://wiki.archlinux.org/title/systemd)
