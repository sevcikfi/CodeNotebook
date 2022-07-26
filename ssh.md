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

## Sources

[keygen](https://www.ssh.com/academy/ssh/keygen) and [add](https://www.ssh.com/academy/ssh/add) from ssh.com
