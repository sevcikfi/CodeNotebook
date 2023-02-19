---
alias:
tag: IT/DevOps CodeNotebook 
---


# Docker

Summary::*le container hellscape*

## Building image

`docker build -t myApp /path/to/dockerfile` or `docker-compose build`

- \-t for "name tag"

`docker images` to list images

`docker image rm <full:name or id>` to rm image

## Composing image

`docker-compose up` for running docker-compose on current dir, use with `-d` to detach from STDIN and `--build` to rebuild the image before trying to run

`docker-compose down` to shutdown the containers

## Running it

`docker ps` to list containers (`-a` for all)

`docker pull` pulls image from remote repo

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

`docker start <name or ID>` to start specific container, to run image, `-a` to attach STDOUT, `-i` for STDIN

`docker restart <name or ID>` to restart

`docker stop <name or ID>` to stop running container safely

`docker kill` to stop immediately

`docker rm <name or ID>` to remove

`docker exec -it <name> <command>` for getting inside, 99.9% times with bash

### Docker hub

`docker login` to login docker, `docker commit <container-id> <username(repo)/image-name>` and `docker push` to push it there - very similar to git

---

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

`ENTRYPOINT ["command"]` - makes the container into a *binary*, e.g. *`ENTRYPOINT ["/bin/cat"]`* and *`docker run img /etc/passwd`* would cat out the content of `passwd`

`CMD ["execute", "params", "paramsX"]` runs this command on start up

Note: command from (docker-)compose.yml **overrides** *CMD*, similar to after image name on cli

---

## docker-compose.yml

Example compose:

```yaml
services:
  service-without-modifs:
    image: some-image-name
    volumes:
      - ./path/in/host:/path/in/container
    environment:
      - some_var=for-the-image
      - some_other_var=for-the-image
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

### Volumes

from *Compose docs*:

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

examples from docs:

#### Basic

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

#### Aliases

> **Note**: A network-wide alias can be shared by multiple containers, and even by multiple services. If it is, then exactly which container the name resolves to is not guaranteed.

As such, it is **HIGHLY RECOMMEND** to use *aliases* over *static IPs*.

> In the example below, service `frontend` will be able to reach the `backend` service at the hostname `backend` or `database` on the `back-tier` network, and service `monitoring` will be able to reach same `backend` service at `db` or `mysql` on the `admin` network.

```yaml
services:
  frontend:
    image: awesome/webapp
    networks:
      - front-tier
      - back-tier

  monitoring:
    image: awesome/monitoring
    networks:
      - admin

  backend:
    image: awesome/backend
    networks:
      back-tier:
        aliases:
          - database
      admin:
        aliases:
          - mysql

networks:
  front-tier:
  back-tier:
  admin:
```

#### Static IPs

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

1. [Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
2. [Dockerfile docs](https://docs.docker.com/engine/reference/builder/)
3. [Compose docs](https://docs.docker.com/compose/compose-file/compose-file-v3/#volumes)
4. [Networking](https://docs.docker.com/compose/networking/)
5. [Docker build](https://docs.docker.com/engine/reference/commandline/compose_build/)
6. [text](https://docs.docker.com/engine/reference/commandline/compose_up/)
7. [YT](https://www.youtube.com/watch?v=pTFZFxd4hOI)
