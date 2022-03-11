# Tor 

## Usage

TODO: basic browser usage

## Setup node

TODO: write config hint for setting up a node

### Add official Tor repo

```
code here
```

and install keyring for auto-updating **those** keys

```
apt install tor deb.torproject.org-keyring
```

Config file is located at `/set/tor/torrc`

### Node settings

ORPort, DirPort, Control port + nyx

To apply setting:

```
systemctl restart tor
```

and enjoy!

### Hidden service settings

```
HiddenServiceDir /var/lib/tor/service1/
HiddenServiceVersion 3
HiddenServicePort 443 127.0.0.1:443
HiddenServiceNonAnonymousMode 1
HiddenServiceSingleHopMode 1
SafeLogging 1
```

To apply setting:

```
systemctl restart tor
```

and enjoy!

### HTTP header for `.onion` address[5]

Add the following into `server { ... }` block in Nginx (or alternative webserver):

```
add_header Alt-Svc 
  'h2="2tjcxjzxgql6wilo3bu777pkvigx2wqwauxf7lyvvmsotjgrqiwwg7id.onion:443";
  ma=86400;
  persist=1';
```

- h2 - hostname (url address)
- ma - max age in seconds
- persists - "persist indicates whether alternative service cache should be cleared when the network is interrupted."

Finish by reloading your server and enjoy!

```
systemctl reload nginx
```

---

[1] Official tor website

[2] some other sos

[3] Kenny vid

[4] Kenny vid

[5] https://medium.com/privacyguides/securing-services-with-tor-and-alt-svc-43ebf43dd5e2
