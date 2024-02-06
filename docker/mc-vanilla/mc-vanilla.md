# Vanilla/basic modded

everything was configured according to  [this](https://docker-minecraft-server.readthedocs.io/en/latest/) website

## Usage

start server with

```bash
docker compose up -d
```

and connect to rcon/server console with:

```bash
docker exec -i <container-name> rcon-cli --password <password from server.properties>
```

## configs

- EULA: "TRUE": accepts EULA, *mandatory*
- MEMORY: "4G": sets max RAM limit
- ENABLE_ROLLING_LOGS: true: curbs amount of logs
- ENABLE_WHITELIST: true: enables whitelist, need to manually add people, look above, if you want auto mounting from file
- DIFFICULTY: "hard": default difficulty
- MAX_WORLD_SIZE: 25000: max world size, curbs needed space
- TYPE: "FABRIC": enables fabric based server for plugins and more config
- VERSION: "1.20.4": minecraft version
- OVERRIDE_SERVER_PROPERTIES: false: disables override on every containers startup, i.e. allows manual config of `server.properties`
