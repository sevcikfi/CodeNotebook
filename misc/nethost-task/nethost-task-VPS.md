---
alias:
tag: meta
---

# nethost task VPS

Summary::

## Task

```text
IP: 178.238.47.126 
NMASK: 255.255.255.0 
GW: 178.238.47.1 
NAMESERVERY: 81.31.33.19, 80.79.16.5

IP: 2a01:430:13e::ffff:FA15:19 
NMASK: 64 GW: 2a01:430:13e::1 
NAMESERVERY: 2a01:430:0:5::5, 2a01:430:0:30::3

Zadání testovacího úkolu:
1. nainstalujte Debian/Ubuntu  
2. nainstalujte Apache 2, MySQL, PHP  
3. zprovozněte testovací Wordpress na Vámi zřízeném webovém serveru (počítám že bude dostupný přímo na veřejné IP adrese VPS)  
4. nastavte vhodně firewall a zabezpečte server (podrobně popište co je jak nastaveno, a proč)  
5. na serveru mějte SSH server a ke správě užívejte SSH  
6. neužívejte grafické rozhraní, ani jej neinstalujte   
Popište pak prosím co jste jak nastavil a proč, zároveň pak pošlete heslo do systému ať se na to můžeme podívat.  
  
Úkoly navíc (čím více splníte tím lépe):  
1. Vytvořte soubor etc.txt v /, jehož obsahem bude sloupcový výpis adresáře /etc, ovšem budou tu vypsané pouze adresáře a pouze jejich jména.  
2. Vytvořte soubor space.txt v /, jehož obsahem bude výpis využití místa na disku. Pod výpisem bude uveden soubor, který na serveru zabírá nejvíc místa.  
3. Přeřaďte před Vámi nainstalovaný Worpdress HAproxy a provoz směrujte přes ni. Tj. HAproxy bude předražená proxy skrze ní bude veden veškerý provoz, Apache samotný bude poslouchat pouze lokálně (localhost), na veřejné IP adrese bude poslouchat HAproxy.  
4. Implicitní mod_php nahraďte implementací PHP FPM
```

## Reasoning

### Basics

User: `kiriko:kiriko123`

Mysql: `root:kiriko123, wordpress@localhost:Kiriko-123`

1. Selected debian image and installed via ncurses w/o DE and manually configured network during the installation (ip4, gw, DNS) and run update/upgrade

   ```bash
   sudo apt update && sudo apt upgrade
   ```

2. Installed apache, php along wordpress dependencian and mysql from Oracle. We should see apache debian default page at our ip in browser.

   ```bash
    sudo apt install apache2 ghostscript php libapache2-mod-php php-mysql php-curl php-gd php-mbstring php-xml php-xmlrpc php-soap php-intl php-zip  php-imagick php-bcmath gnupg
    cd /tmp && sudo wget https://dev.mysql.com/get/mysql-apt-config_0.8.24-1_all.deb
    sudo dpkg -i mysql-apt-config*
    sudo apt update && sudo apt install mysql-server
    sudo mysql_secure_installation
    sudo mysql -u root -p
    mysql> CREATE DATABASE wordpress;
    mysql> CREATE USER wordpress@localhost IDENTIFIED BY 'Kiriko-123';
    mysql> GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,ALTER ON wordpress.* TO wordpress@localhost;
    mysql> FLUSH PRIVILEGES;
    mysql> exit;
    ```

3. Wordpress install: make `/var/www` where all web files live, change owner to `www-date` user, download wordpress and *unzip* it into the folder. We make wordpress site config as per `[1]` and enable it along with some module, disable the default one. Now we should see wordpress welcome first start page and finish the config here. (fill out db name, db user)

   ```bash
    sudo mkdir -p /var/www
    sudo chown www-data: /var/www
    wget -qO- https://wordpress.org/latest.tar.gz | sudo -u www-data tar zx -C /var/www
    echo "[1]" > /etc/apache2/sites-available/wordpress.conf #[1] reference to codeblock below
    sudo a2ensite wordpress && sudo a2enmod rewrite && sudo a2dissite 000-default && sudo systemctl reload apache2
    ```

4. Installing firewall - why ufw instead of iptables? Because i didn't feel the adiitonal complexity and more granular options were worth it in our case. Commands below allows OpenSSH (22/tcp), web (80/tcp) and localhost to localhost for working proxy.

    ```bash
    sudo apt install ufw
    #defaults> deny incoming, allow outgoing
    sudo ufw allow OpenSSH #ssh
    sudo ufw allow WWW #allow 80/tcp
    sudo ufw allow from 127.0.0.1 to 127.0.0.1 #allow localhost for proxy
    ```

5. SSH keys - we can easily generate keys and move them to the server and use as specified below (RSA is compatible with 99% however for future proofing, we should use instead ed25519). If we want to disallow non-key ssh connection, we have to change `PasswordAuthentication yes` to `no` in `/etc/ssh/sshd_config`. You may use the same key as i used when setting up the VM below at `[3]`. However, **NEVER EVER SEND ANYONE PRIVATE KEY IN PLAINTEXT PUBLICLY OVER THE INTERNET**! This is only for the purpose of this task.

   ```bash
    ssh-keygen -t rsa -b 4096 -C "nethost task" -f "nethost_RSA"
    chmod 400 nethost_RSA
    ssh-copy-id -i nethost_RSA.pub kiriko@178.238.47.126
    ssh -i nethost_RSA kiriko@178.238.47.126
   ```

6. As mentioned in 1., no DE was ever instaleld, everything was done via SSH, wordpress finished via webUI.

### Advanced

1. `ls -1F | grep "/" | sed 's/.$//' > /etc.txt` gets fles with classifiers, greps only folders, removes the classifier and redirects in into `/etc.txt`
2. `df -H | grep /dev/sd > space.txt && find / -type f -printf "%s\t%p\n" | sort -n | tail -1 >> space.txt` gets info about current disk and pushes it into `/space.txt`; search recursively from root, only files, print to STDOU as "size \tab name", pipes it into sort by number ascending, pipes it into tail to get last item and appends it to the file.
3. Haproxy - installed via commands shown below. Gets HProxy, changes apache and site to be on port 8000, binds the proxy on any IP port 80 and tells our server is at localhost (we could have multiple servers)

   ```bash
    sudo apt install haproxy
    #change 's/Listen 80/Listen 8000/' in /etc/apache2/ports.conf
    #change 's/<VirtualHost: *:80>/<VirtualHost: *:8000>/' /etc/apache2/sites-available/wordpress.conf
    echo "[2]" >> /etc/haproxy/haproxy.cfg #[2] reference to codeblock below
    sudo systemctl restart haproxy
   ```

4. mod_php -> PHP-FPM - uhhh turns off apache, install PHP-FPM, enables it, disables mod_php (old php install) and some prefork (i have no idea what those are whatsoever), enables the other better php, restarts the server, *Magically works*.

   ```bash
    sudo systemctl stop apache2.service && sudo systemctl disable apache2.service
    sudo apt install php-fpm
    sudo systemctl start php-fpm && sudo systemctl enable php-fpm
    sudo a2dismod php7.4 mpm_prefork && a2enmod proxy_fcgi setenvif mpm_event && sudo a2enconf php7.4-fpm protect-user-inis
    sudo systemctl start apache2.service && sudo systemctl enable apache2.service
   ```

### Sources

I'm not imniscient and use Google. To accomplish my task i used the following online tutorials:

- <https://blog.runcloud.io/install-wordpress-with-apache-on-ubuntu/>
- <https://www.digitalocean.com/community/tutorials/how-to-install-the-latest-mysql-on-debian-10>
- <https://ubuntu.com/tutorials/install-and-configure-wordpress#4-configure-apache-for-wordpress>
- <https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands#allow-apache-http-https>
- <https://www.linuxquestions.org/questions/ubuntu-63/what-ufw-rule-will-allow-port-80-to-localhost-but-only-from-localhost-4175595450/>
- <https://www.ssh.com/academy/ssh/keygen>
- <https://www.ssh.com/academy/ssh/copy-id>

- <https://www.geeksforgeeks.org/remove-last-character-from-string-in-linux/>
- <https://www.cyberciti.biz/faq/linux-find-largest-file-in-directory-recursively-using-find-du/>
- <https://www.haproxy.com/blog/haproxy-configuration-basics-load-balance-your-servers/>
- <https://medium.com/@jacksonpauls/moving-from-mod-php-to-php-fpm-914125a7f336>
- <https://www.cloudbooklet.com/how-to-install-php-fpm-with-apache-on-ubuntu-20-04/>
- <https://notes.licomonch.net/2020/02/07/convert-from-mod_php-and-apache-mpm-prefork-to-php-fpm-and-mpm-event-at-debian-10-buster/>

### **[1]** Apache config

```text
<VirtualHost *:80>
    DocumentRoot /var/www/wordpress
    <Directory /var/www/wordpress>
        Options FollowSymLinks
        AllowOverride Limit Options FileInfo
        DirectoryIndex index.php
        Require all granted
    </Directory>
    <Directory /var/www/wordpress/wp-content>
        Options FollowSymLinks
        Require all granted
    </Directory>
</VirtualHost>
```

### **[2]** HProxy config

```text
frontend myfrontend
  bind :80
  default_backend myservers

backend myservers
  server apache1 127.0.0.1:8000
```

### **[3]** RSA-private key for testing - note: NEVER EVER SEND ANYONE PRIVATE KEY LIKE THIS

```text
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
```
