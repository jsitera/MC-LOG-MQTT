#!/usr/bin/env python3

# MQTT Minecraft server log parser
# reads Minecraft server logs and sends appropriate messages via MQTT

# requirements
# pip3 install paho-mqtt
# pip3 install sh

import paho.mqtt.client as mqtt
from time import time, sleep
import signal
import sys
import re
import config    # my local config file
import sh

# configuration
base_topic = 'MC1'
mqtt_hostname = config.mqtt_hostname
mqtt_clientname = 'mc-log-mqtt'
input_filename = config.input_filename



# Hook for cleanup after interrupt
def signal_handler(signal, frame):
    # cleanup
    print("mc-log-mqtt ending.")
    mqtt_client.disconnect()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
interrupted = False

print("This is Minecraft log parser sending MQTT messages for every")
print("line containing /tell mqtt topic message")
    
# MQTT connection initialization
mqtt_client = mqtt.Client()

try:
  mqtt_client.connect(mqtt_hostname,port=80)
except:
  print("MQTT connection error.")
  sys.exit(1)
else:
  print("MQTT connection established.")


print("LOG filename: ", input_filename)

mqtt_client.loop_start()
sleep(1)

# main loop
for line in sh.tail("-0f", input_filename, _iter=True):
   
    command = re.search('/tell mqtt .*', line)  # find relevant part
    if command:
        (tell, sep, args) = command.group().partition(" ")
        (mqtt, sep, args) = args.partition(" ")
        
        (topic, sep, message) = args.partition(" ")

        if topic and message:

            print("Sending MQTT message: ", topic, "> ",  message)
            mqtt_client.publish(base_topic+"/"+topic, message)
