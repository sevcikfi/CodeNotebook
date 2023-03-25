---
alias:
tag: IT/cybersecurity CodeNotebook 
---

# Tor

## Usage

TODO: basic browser usage

## Setup node

TODO: write config hint for setting up a node

### Add official Tor repo

```shell
code here
```

and install keyring for auto-updating **those** keys

```shell
apt install tor deb.torproject.org-keyring
```

Config file is located at `/set/tor/torrc`

### Node settings

ORPort, DirPort, Control port + nyx

To apply setting:

```shell
systemctl restart tor
```

and enjoy!

### Hidden service settings

```shell
HiddenServiceDir /var/lib/tor/service1/
HiddenServiceVersion 3
HiddenServicePort 443 127.0.0.1:443
HiddenServiceNonAnonymousMode 1
HiddenServiceSingleHopMode 1
SafeLogging 1
```

To apply setting:

```shell
systemctl restart tor
```

and enjoy!

### HTTP header for `.onion` address[5]

Add the following into `server { ... }` block in Nginx (or alternative webserver):

```json
add_header Alt-Svc 
  'h2="2tjcxjzxgql6wilo3bu777pkvigx2wqwauxf7lyvvmsotjgrqiwwg7id.onion:443";
  ma=86400;
  persist=1';
```

- h2 - hostname (url address)
- ma - max age in seconds
- persists - "persist indicates whether alternative service cache should be cleared when the network is interrupted."

Finish by reloading your server and enjoy!

```shell
systemctl reload nginx
```

---

## Sources

01. Official tor website
02. some other sos
03. Kenny vid#1
04. Kenny vid#2
05. [Guide](https://medium.com/privacyguides/securing-services-with-tor-and-alt-svc-43ebf43dd5e2) on .onion forward
06. [Vanity url tutorial](https://opensource.com/article/19/8/how-create-vanity-tor-onion-address)
