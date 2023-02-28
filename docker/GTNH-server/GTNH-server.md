# Gregtech New Horizons

> *the torture and suffering is real*

Decide whether to use the container only as java runtime or somehow think out way to utilize it properly?

~~I mean, you *could* only map the `World` folder from outside.~~ Done

Maybe make just the barebones version (or at least startable via command outside) to allow addition of other mods + initial access to the console (may)

**TODO:** change the apt-get into one command
EDIT: done (remove in next cleaning)

## Basic setup

1. Download the server zip from here: <http://downloads.gtnewhorizons.com/ServerPacks/>

    ```bash
    wget http://downloads.gtnewhorizons.com/ServerPacks/GT_New_Horizons_server_version_SERVER.zip
    ```

2. Unzip it with `unzip server.zip -d destination`
3. Agree to Minecraft EULA

    ```bash
    cd your_minecraft_server_folder
    echo "eula=true" > eula.txt
    ```

4. Launch server to test functionality, add yourself to `whitelist` and maybe `ops`

    ```bash
    bash startserver.sh
    whitelist add your_nick
    op your_nick
    ```

### Install mod for backups and chunkloading

Download the latest from here:

- FTB-Utilities is located here: <https://github.com/GTNewHorizons/FTB-Utilities/releases>
- FTB-Library is located here: <https://github.com/GTNewHorizons/FTB-Library/releases>

```bash
cd server_directory/mods
wget https://github.com/GTNewHorizons/FTB-Utilities/releases/download/1.0.18.7-GTNH/FTBUtilities-1.7.10-1.0.18.7-GTNH.jar
wget https://github.com/GTNewHorizons/FTB-Library/releases/download/1.0.18.5-GTNH/FTBLib-1.7.10-1.0.18.5-GTNH.jar
```

Change the config here, you usually want to change

```json
"backups_to_keep": 10, #number of backups
"backup_timer": 1.0, #hours
"max_claims": 1000,
"max_loaded_chunks": 50,
"max_claims": 100, 
```

## Docker image

Change `source: path/to/somewhere` to where you `World/` will be on the disk. Now build the image, find the name of the image, run the image.

```bash
docker-compose build 
docker image list
docker run -it imageName-or-ID
```

Start the server for the first time using `bash startserver.sh`, wait for it load and add yourself to whitelist with `whitelist add your_nick`, you may want to add yourself to ops via `ops your_nick`. Now you can stop the server and 1) change the configs or server.properties as like and 2) download FTB-Utils and/or other stuff as described above i.e. `cd` mods folder and `wget` it. Once you're done, you can exit the container and start the way you always will from this folder via:

```bash
docker-compose up
```

Or alternatively from anywhere in the system with the following. Note that you'll need to know id or name of the container.

```bash
docker start <name-or-ID>
```

## Sos

[wiki guide](https://gtnh.miraheze.org/wiki/Server_Setup)
