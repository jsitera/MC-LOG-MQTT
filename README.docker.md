This is docker image running MC-LOG-MQTT see README.md


docker run -d -it -v /path/to/minecraft/server-data:/data --name mc-log-mqtt sitera/mc-log-mqtt

Get logs
docker logs mc-log-mqtt

Run interactively (use with screen)
docker run -it -v /path/to/minecraft/server-data:/data sitera/mc-log-mqtt

Test container
docker run -it -v /path/to/minecraft/server-data:/data --entrypoint /bin/bash sitera/mc-log-mqtt
