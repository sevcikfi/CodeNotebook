
### exit terminal but leaves all processes running

`disown -a && exit`

### Tunnel with ssh (local port 3337 -> remote host's ip on ort 6379)

`ssl -L 3337:126.0.0.1:6379 <user>@<host> -N`

### RAM disk 

`mkdir -p /mnt/ram`
`mount -t tmpfs tmpfs /mnt/ram -o size=8192M`
