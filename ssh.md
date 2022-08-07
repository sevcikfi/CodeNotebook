# SSH stuff

## Baiscs

### generate keys

`ssh-keygen` generates private & public key, optional to add passphrase, option -t, -b, -f for cypher, bytes, filename

Public: either no extention or .ppk

- different formats e.g. OpenSSH, OpenSSL, Putty (Puttygen keys can be converted to OpenSSH)
- perms: 600 i.e. ugo -wr------

Private: .pub, .cert, .pem

- various formats i.e. Putty but standard is `[cypher type] [key itself] [comment]`
- perms: public means public

usually saved in $HOME/.ssh/*cypher name* or name of your private key file

IMPORTANT: if you add **specially named** key files, they have to be added to agent with `ssh-add [file]`, option -v, -l/L -d/L for verbose, list, List all, delete one, Delete all

Public keys need to be added (appended on one new line) to .ssh/authorized_key or special place on particular website e.g. Github/SSH&GPG keys, easiest done with `ssh-copy-id [-i /key/location] user@host`

TODO: format better
TODO: command examples

### Securing SSH

Disabling direct root logins usually default options in most distros. However, it's higly advised to enable *asymetric keys* based exclusive authentication. It's important to note that key managment can get quite messy quite fast if thorough housekeeping isn't performed and medium and large organisations should be using CA *certificate authority* issued revocable keys along with TOTP *time-based one-time password*.
For reducing the number of bot brutoforcing and amount of logs, it's recommended to change default port and install *fail2ban* and utilizing reverse proxy (e.g. Cloudfare) with IP filtering allowing only connections from said proxy.

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

## Sources

[keygen](https://www.ssh.com/academy/ssh/keygen) and [add](https://www.ssh.com/academy/ssh/add) from ssh.com
