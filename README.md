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
