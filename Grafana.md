---
alias:
tag: IT/languages CodeNotebook 
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

## Source

- [Official](https://grafana.com/docs/grafana/latest/)