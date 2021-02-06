This is docker image running MC-LOG-MQTT see README.md

Running the image needs setting environment variables. It can be done
by docker-compose or using .env (dotenv).

docker run -d -it -v /path/to/minecraft/server-data:/data --name mc-log-mqtt --env-file=.env sitera/mc-log-mqtt

Get logs
docker logs mc-log-mqtt

Run interactively (use with screen)
docker run -it --env-file=.env -v /path/to/minecraft/server-data:/data sitera/mc-log-mqtt

Test container
docker run -it --env-file=.env -v /path/to/minecraft/server-data:/data --entrypoint /bin/bash sitera/mc-log-mqtt
