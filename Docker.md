---
alias:
tag: IT/DevOps IT/technologies CodeNotebook 
---

# Docker

Summary::*le container hellscape*

## Building image

`docker build -t myApp /path/to/dockerfile` or `docker-compose build`

- \-t for "name tag"

`docker images` to list images

`docker image rm <full:name or id>` to rm image

## Composing image

`docker-compose build` to build all services

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

`docker rm <name or ID>` to remove container

`docker image prune -a` to clean images

`docker system prune` prunes everything

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

### EXPOSE port

`EXPOSE 3306` - expose ports without publishing them to the host machine - they’ll only be accessible to linked services. Only the internal port can be specified or in compose as following:

```yaml
expose: 3306
```

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

### Environment variable and reusing settings

```yaml
version: '3.7'
services:
 redis: &service_default
   image: redis:4.0.9-alpine
   init: true
   restart: always
   container_name: redis
   extra_hosts:
     - 'redis:172.20.0.2'
     - 'nginx:172.20.0.3'
   networks:
     dockernet:
      ipv4_address: 172.20.0.2
nginx:
   <<: *service_default
   image: nginx:1.14-alpine
   container_name: nginx
   networks:
     dockernet:
      ipv4_address: 172.20.0.3
   ports:
     - 80:80
     - 443:443
networks:
 dockernet:
  driver: bridge
  ipam:
   config:
   - subnet: 172.20.0.0/16
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

## Installation

### Deb repo

Cleaning old version

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt update
```

Dependencies

```bash
sudo apt-get install ca-certificates curl gnupg lsb-release
```

```bash
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Script (for Rasbian)

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### Post-install setup

To use docker without `sudo`, do following and then relog into the system.

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

### Uninstallation  

Uninstall the Docker Engine, CLI, containerd, and Docker Compose packages:

```bash
sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
```

Images, containers, volumes, or custom configuration files on your host aren’t automatically removed. To delete all images, containers, and volumes:

```bash
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```

## Caveats for use-cases

maybe move to language/technology specific doc.

### Dotnet and `.csproj` clusterfuck

Basic app build:

```Dockerfile
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS publish
WORKDIR /src
COPY . .
RUN dotnet publish -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:6.0 as final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "WebApi.dll"]
```

Caching dependencies (might've gotten improved so that only `dotnet restore` is enough?)

```Dockerfile
# https://hub.docker.com/_/microsoft-dotnet
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /source

# copy csproj and restore as distinct layers
COPY *.sln .
COPY aspnetapp/*.csproj ./aspnetapp/
RUN dotnet restore

# copy everything else and build app
COPY aspnetapp/. ./aspnetapp/
WORKDIR /source/aspnetapp
RUN dotnet publish -c release -o /app --no-restore

# final stage/image
FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
COPY --from=build /app ./
ENTRYPOINT ["dotnet", "aspnetapp.dll"]
```

Complex app issue:

```Dockerfile
# https://hub.docker.com/_/microsoft-dotnet
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /source

# copy csproj and restore as distinct layers
COPY complexapp/*.csproj complexapp/
COPY libfoo/*.csproj libfoo/
COPY libbar/*.csproj libbar/
RUN dotnet restore complexapp/complexapp.csproj

# copy and build app and libraries
COPY complexapp/ complexapp/
COPY libfoo/ libfoo/
COPY libbar/ libbar/
WORKDIR /source/complexapp
RUN dotnet build -c release --no-restore

# test stage -- exposes optional entrypoint
# target entrypoint with: docker build --target test
FROM build AS test
WORKDIR /source/tests

COPY tests/*.csproj .
RUN dotnet restore tests.csproj

COPY tests/ .
RUN dotnet build --no-restore

ENTRYPOINT ["dotnet", "test", "--logger:trx", "--no-restore", "--no-build"]

FROM build AS publish
RUN dotnet publish -c release --no-build -o /app

# final stage/image
FROM mcr.microsoft.com/dotnet/runtime:6.0
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "complexapp.dll"]
```

someone's handy tool, `dotnet subset`, which simplified the workflow

```Dockerfile
# https://hub.docker.com/_/microsoft-dotnet
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS prepare-restore-files
ENV PATH="${PATH}:/root/.dotnet/tools"
RUN dotnet tool install --global --no-cache dotnet-subset --version 0.3.2
WORKDIR /source
COPY . .
RUN dotnet subset restore complexapp/complexapp.csproj --root-directory /source --output restore_subset/

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /source
COPY --from=prepare-restore-files /source/restore_subset .
RUN dotnet restore complexapp/complexapp.csproj

# copy and build app and libraries
COPY complexapp/ complexapp/
COPY libfoo/ libfoo/
COPY libbar/ libbar/
WORKDIR /source/complexapp
RUN dotnet build -c release --no-restore

...
```

[Sos](https://blog.nimbleways.com/docker-build-caching-for-dotnet-applications-done-right-with-dotnet-subset/)

## Sources

1. [Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
2. [Dockerfile docs](https://docs.docker.com/engine/reference/builder/)
3. [Compose docs](https://docs.docker.com/compose/compose-file/compose-file-v3/#volumes)
4. [Networking](https://docs.docker.com/compose/networking/)
5. [Docker build](https://docs.docker.com/engine/reference/commandline/compose_build/)
6. [Compose](https://docs.docker.com/engine/reference/commandline/compose_up/)
7. [Moving docker data](https://www.digitalocean.com/community/questions/how-to-move-the-default-var-lib-docker-to-another-directory-for-docker-on-linux)
8. [YT](https://www.youtube.com/watch?v=pTFZFxd4hOI)
