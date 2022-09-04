[![Build and publish docker image](https://github.com/jsitera/MC-LOG-MQTT/actions/workflows/build-and-publish.yml/badge.svg)](https://github.com/jsitera/MC-LOG-MQTT/actions/workflows/build-and-publish.yml)

# MC-LOG-MQTT
This component reads a Minecraft server log and sends MQTT messages. It is a part of Minecraft IoT project, a gateway between the Minecraft server and anything via MQTT standard.
# description
Allows to send MQTT messages from unmodified Minecraft server. 
Acts as a Minecraft log parser and sends a MQTT message for every line containging predefined structure. There is a regexp describing the line structure and finding the topic and message in the log line.
# How to use it
You can use a command say or tell in your command block or in fuctions.
# How to setup it
The configuration is based on https://github.com/theskumar/python-dotenv Use environment variables or .env file. See https://github.com/jsitera/MC-LOG-MQTT/blob/master/README.docker.md
Start the parser as a deamon. It can be stopped using CTRL-C.
# Contributing
- install minecraft server with scripts using docker-compose (via https://github.com/jsitera/ansible-minecraft-server minecraft-docker-compose role)
- clone this repository git clone https://github.com/jsitera/MC-LOG-MQTT.git
- create appropriate .env file
- test your changes by running container and the script inside the container - see README.docker.md
- commit your changes (clonning the repository and submitting merge request can be needed)
# Build and publish docker image automation
There is available docker image on hub.docker.io called sitera/mc-log-mqtt.

On each commit to this repository the build and publish action is automatically invoked.
