---
alias:
tag: IT/DevOps IT/technologies CodeNotebook
---

# Grafana

You can quickly spin up Grafana instance from cli:

```bash
docker run -d -p 3000:3000 --name=grafana \
    --user "$(id -u)" \
    --volume "absolute/path-to/place:/var/lib/grafana" \
    -e "GF_FEATURE_TOGGLES_ENABLE=publicDashboards" \
    grafana/grafana-oss
```

Example compose:

```yaml
version: "3.8"
services:
  grafana:
    image: grafana/grafana-oss
    container_name: grafana
    restart: unless-stopped
    environment:
     - GF_SERVER_ROOT_URL=http://my.grafana.server/
     - GF_INSTALL_PLUGINS=grafana-clock-panel
    ports:
     - '3000:3000'
    # bind mount, note the docker needs read-write access to that place
    volumes:
      - 'absolute/path-to/place:/var/lib/grafana'
```

Run it with `docker compose up -d`

## Node exporter

Installation on bare metal, find appropriate version on [Github](https://github.com/prometheus/node_exporter/releases) and then run:

```bash
wget <link>
tar xvfz node_exporter-*.*-amd64.tar.gz
cd node_exporter-*.*-amd64
./node_exporter
```


You may verify metrics are accessible with `curl http://localhost:9100/metrics`

Node Exporter will stop working once you exit the terminal. To make it run 24/7 even after reboot, write the following into `/etc/systemd/system/node-exporter.service`

```ini
[Unit]
Description=Node Exporter Agent
[Service]
#user with execute privileges
User=your-user
ExecStart=/home/ubuntu/node_exporter-1.6.1.linux-arm64/node_exporter
Restart=always
[Install]
WantedBy=multi-user.target
```

Save the file and run to enable the service and start it up.

```bash
systemctl daemon-reload
systemctl enable --now node-exporter.service
```

Alternatively, you may run it from docker:

```yml
version: '3.8'

services:
  node_exporter:
    image: quay.io/prometheus/node-exporter:latest
    container_name: node_exporter
    command:
      - '--path.rootfs=/host'
    network_mode: host
    pid: host
    restart: unless-stopped
    volumes:
      - '/:/host:ro,rslave'
```

## Source

- [Official](https://grafana.com/docs/grafana/latest/)
- [Medium Guide Node+Prom+Graf #1](https://shashanksrivastava.medium.com/set-up-a-linux-server-monitoring-system-using-grafana-prometheus-bb3448f585b8)
- [Medium Guide Node+Prom+Graf #2](https://towardsdev.com/how-to-monitor-a-linux-server-using-prometheus-grafana-f436c724c9c9)
