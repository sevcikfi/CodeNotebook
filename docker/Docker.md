# Docker 

*le container hellscape*

## Building image

`docker build -t myApp /path/to/dockerfile`
- \-t for "name tag"

`docker images` to list images
`docker image rm <full:name or id>` to rm image

## Composing image

`docker-compose up` for running docker-compose on current dir
`docker-compose down` to shutodwn the containers

## Running it

`docker ps` to list containers (`-a` for all)

`docker run myApp-iamge`
- \-d for detached mode
- \-e for env vars
- \-i for interactive (keep STDIN)
- \-l for label metdata
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

`docker exec -it <name>` for getting insinde



## Dockerfile

`FROM "image:version"`

`RUN "command -params`

### ADD vs COPY

`ADD /local/file /inside/path`

`COPY /local/file /inside/path`

### ARG vs ENV

`ENV ENV-STUFF=XYZ`
`ARG BUILD-ARG`

### ENTRYPOINT vs CMD

`ENTRYPOINT`

`CMD ["execute", "params", "paramsX"]`

Note: **command** from compose.yml overrides *CMD*

## docker-compose.yml

`build: .` where dockerfile

```yaml
services:
  somename:
    build:
      context: ./app
      dockerfile: Dockerfile
      args:
        some_variable_name: a_value
```

`ports: - host:container` for exposing ports