# FTB-Retro

(written up post for reddit)

Disclaimer: this is more of a archive post to have this index'd for others since i google'd around for 2 days not being able to find anything usage.

I wanted to play *good old* Feed The Beast Pyramid with couple friends and since curseforge, FTB and other stuff didn't work they way they should, i had to compile this guide for them

## Client fide

1. Download FTB retro SMP via curseforge

2. Download MultiMC, go to setting -> Accounts to login and Minecraft to set memory

3. launch MultiMC -> add Instance -> FTB Legacy -> scroll completely down -> click `Feed The Beast Retro SMP` -> ok (launch it and close it down)

4. select FTB SMP in MultiMC and click Minecraft Folder on the right panel

5. open CurseForge and select FTB Retro SMP -> burger(3 dots. menu -> click Open Folder

6. now you got both these folder next to each other

7. select everything in the CurseForge folder and copy it over to MultiMC folder

8. close everything, go to MultiMC and launch, once in minecraft connect to your server's IP

Note: for SSP, the steps are same except you install `Feed The Beast Retro SSP`

## Server

How to server? The server file on curseforge `Feed The Beast Retro SMP` works, just extract it and run it. Except you need Java 8 which isn't problem on Windows. However on linux, it might be a bit tricky and easiest workaround is just to use docker. Create the two files with the contents below, download and install docker. Run `docker-compose build` and then `docker-compose up -d` to start it, use `docker stop FTB-Retro-SMP` to stop the server.

Note: the MP map is missing gravel block, you'll have to give it to yourself and easiest way is to add nickname of one of the players into `ops.txt`, restart the server, give it via NEI, remove it and restart the server again. Also might wanna cheat in one block marble for building variety.

Dockerfile

```dockerfile
FROM openjdk:8u342-jdk-slim

WORKDIR /data

CMD ["bash"]
```

docker-compose.yml

```yaml
version: "3.9"

services:
  ftb-retro-smp:
    container_name: FTB-Retro-SMP
    build: .
    image: ftb-retro:latest
    volumes:
      - type: bind
        source: /path/to/dir/with/extracted/zip
        target: /data
    ports:
    - "25565:25565"
    restart: on-failure:3
    tty: true
    #net: "host" # if you need to connect from host machine
    command: >
      bash -c "echo "Feed\ The\ Beast\ Insanity!"
      && java -Xmx1G -Xms1G -jar craftbukkit.jar
      "
```
