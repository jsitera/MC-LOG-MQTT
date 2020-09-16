# MC-LOG-MQTT
MQTT sender feeded via minecraft server log
# description
Allows to send MQTT messages from unmodified Minecraft server. 
This Minecraft log parser sends MQTT messages for every line containging /tell mqtt topic message.
# How to use it
Just use following command in your command block:
`/tell mqtt topic message`
# How to setup it
Create config.py file and start the parser as a deamon. It can be stopped using CTRL-C.
