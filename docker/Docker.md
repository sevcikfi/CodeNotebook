---
alias:
tag: IT/DevOps CodeNotebook 
---


# Docker

- *le container hellscape*

## Building image

`docker build -t myApp /path/to/dockerfile`

- \-t for "name tag"

`docker images` to list images
`docker image rm <full:name or id>` to rm image

## Composing image

`docker-compose up` for running docker-compose on current dir
`docker-compose down` to shutdown the containers

## Running it

`docker ps` to list containers (`-a` for all)

`docker run myApp-image`

- \-d for detached mode
- \-e for env vars
- \-i for interactive (keep STDIN)
- \-l for label metadata (relative weight)
- \-c for cpu share
- \--cpus for number of cores
- \-m memory
- \--name for the container (`docker rename oldName newName` to rename)
- \-p outside:inside, out2:int2 to publish ports
- \-t allocate pseudo-TTY
- \-u
- \-w workdir inside the container

`docker start <name or ID>` to start specific container
`docker restart <name or ID>` to restart
`docker stop <name or ID>` to stop
`docker rm <name or ID>` to remove

`docker exec -it <name>` for getting inside

## Dockerfile

`FROM "image:version"`

`RUN "command -params`

`WORKDIR "path/to/dir"` - quick way to change to dir and create it if doesn't exist

`USER <user>[:<group>] (| <UID>[:<GID>])`

### ADD vs COPY

`ADD /local/file /inside/path`

`COPY /local/file /inside/path`

### ARG vs ENV

`ENV ENV-STUFF=XYZ`
`ARG BUILD-ARG`

### ENTRYPOINT vs CMD

`ENTRYPOINT`

`CMD ["execute", "params", "paramsX"]`

Note: command from (docker-)compose.yml **overrides** *CMD*

## docker-compose.yml

Example compose:

```yaml
services:
  service-without-modifs:
    image: some-image-name
    volumes:
      - ./path/in/host:/path/in/container
    environment:
      - MYSQL_DATABASE=db
      - MYSQL_USER=django
      - MYSQL_PASSWORD=test
      - MARIADB_ROOT_PASSWORD=root
  web:
    build:
      context: where/docker/file
      dockerfile: "name-of-the-file"
      args:
        some_variable_name: a_value
    command: "some command starting the app"
    volumes:
      - type: bind
        source: host/path
        target: container/path
    ports:
      - "host-port:container-port"
    restart: unless-stopped
    #restart: on-failure:3 (tries to restart only 3 times)
    #tty: true (keeps open tty in container)
    depends_on:
      - "name-of-service"
```

### volumes

from *Compose docs*

```yaml
volumes:
  # Just specify a path and let the Engine create a volume
  - /var/lib/mysql
  # Specify an absolute path mapping
  - /opt/data:/var/lib/mysql
  # Path on the host, relative to the Compose file
  - ./cache:/tmp/cache
  # User-relative path
  - ~/configs:/etc/configs/:ro
  # Named volume
  - datavolume:/var/lib/mysql
```

### Networking

Some examples:

### Basic

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
  db:
    image: postgres
    ports:
      - "8001:5432"
```

```yaml
services:
  app:
    image: nginx:alpine
    networks:
      app_net:
        ipv4_address: 172.16.238.10
        ipv6_address: 2001:3984:3989::10

networks:
  app_net:
    ipam:
      driver: default
      config:
        - subnet: "172.16.238.0/24"
        - subnet: "2001:3984:3989::/64"
```

## Sources

1. [Dockerfile docs](https://docs.docker.com/engine/reference/builder/)
2. [Compose docs](https://docs.docker.com/compose/compose-file/compose-file-v3/#volumes)
