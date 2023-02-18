# SSH stuff

## Basics

Most basic usage `ssh user@host` where host can be IPv4, IPv6 or DNS address, including utf-8 characters and no top-level-domain for local machines. (It's called FQDN xd)

### Specify port

`ssh -p number user@host`

### Specify key files

If your keys don't live in expected places e.g. `.ssh/key name` or aren't made aware to `ssh-agent`, you may specify them wih `-i path/to/key` e.g.:

`ssh -i ~/.ssh/key user@host`

### Tunnel through to another host

`ssh -J host1 host2`

### Generating keys

`ssh-keygen` generates private & public key, optional to add passphrase, option `-t`, `-b`, `-f` for cypher, bytes, filename

Private: either no extension or `.ppk`

- different formats e.g. OpenSSH, OpenSSL, Putty (Puttygen keys can be converted to OpenSSH)
- perms: 600 i.e. ugo -wr------

Public: `.pub`, `.cert`, `.pem`

- various formats i.e. Putty but standard is `[cypher-type] [key-string] [some comment]  [more comment]`
- perms: *public means public*

usually saved in `$HOME/.ssh/"cypher-name"` or name of your private key file

### Existing keys

 If you wanna use some other specially named key files without `-i` all the time, they have to be added to agent with `ssh-add [file]` where options are:

- `-v` for verbose
- `-l/L` list fingerprint, List full *public key*
- `-d/L` , delete specified key, Delete all.

To start the agent, use ``eval `ssh-agent` ``

### Fingerprint

If you wanna find the fingerprint of particular key, use `ssh-keygen -lvf key/path`, remove `-v` if you don't like pretty art `:c`

### Putting public keys on other machine

Public keys need to be added (appended on one new line) to .ssh/authorized_key or special place on particular website e.g. *Github/SSH&GPG keys*, easiest done with `ssh-copy-id [-i /key/location] user@host`. If you don't have `copy-id` module installed, you may use the following command for UNIX and Windows respectively:

```bash
`ssh-keygen && cat $envuserprofile/.ssh/id_rsa.pub | ssh user@linuxserver 'cat >> .ssh/authorized_keys'`
```

```powershell
type C:\Users\user\.ssh\id_rsa.pub | ssh user@host 'cat >> .ssh/authorized_keys'
```

### Securing SSH

Disabling direct root logins usually default options in most distros. However, it's highly advised to enable *asymmetric keys* based exclusive authentication. It's important to note that key management can get quite messy quite fast if thorough housekeeping isn't performed and medium and large organizations should be using CA *certificate authority* issued revocable keys along with TOTP (*time-based one-time password*).
For reducing the number of bot bruteforcing and amount of logs, it's recommended to change default port and install *fail2ban* and utilizing reverse proxy (e.g. Cloudflare) with IP filtering allowing only connections from said proxy.

### X11 Forwarding

in `/etc/ssh/sshd_config`

```bash
X11Forwarding yes
```

pass `export DISPLAY=localhost:10.0` connect to remote with `ssh -[X|Y] user@host`. For *Putty*, enable ticker box in *forwarding tab*

VS Code env variable:

```json
"terminal.integrated.env.linux": {
    "DISPLAY": "localhost:10.0",
}
```

## Config

Client config files are in `~/.ssh/ssh_config` (user) or `/etc/ssh/ssh_config`(global). For daemon, edit `/etc/ssh/sshd_config` where popular options to change include:

```bash
Port 22

PermitRootLogin yes #allows directly to login as root fully
PermitRootLogin prohibit-password (default) #disallows passwords
PermitRootLogin without-password #prohibits completely

PubkeyAuthentication yes #allows keys
PasswordAuthentication yes #enables password auth
PermitEmptyPasswords no #disables empty password

ForwardAgent yes
AllowAgentForwarding yes #for ssh-agent forwarding allowing SSO over multiple connections
```

**NOTE:** old Putty version doesn't work with some openSSH server after autumn 2022 due to deprecations of oldest RSA, if you wanna use it for some reason add `PubkeyAcceptedAlgorithms=+ssh-rsa` into `/etc/ssh/sshd_config`. Preferably use cmd/powershell built in `ssh` command (nearly same functionality as on unix machines).

## Sources

- [keygen](https://www.ssh.com/academy/ssh/keygen) and [add](https://www.ssh.com/academy/ssh/add) from ssh.com
- [copy-id](https://www.ssh.com/academy/ssh/copy-id)
- [copy-id-eq](https://chrisjhart.com/Windows-10-ssh-copy-id/) and [Scott](https://www.hanselman.com/blog/how-to-use-windows-10s-builtin-openssh-to-automatically-ssh-into-a-remote-linux-machine)
