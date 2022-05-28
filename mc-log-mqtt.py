#!/usr/bin/env python3

# MQTT Minecraft server log parser
# reads Minecraft server logs and sends appropriate messages via MQTT

# requirements
# pip3 install paho-mqtt
# pip3 install sh
# pip3 install python-dotenv

import paho.mqtt.client as mqtt
from time import time, sleep
import signal
import sys
import re
import sh
import os
from dotenv import load_dotenv

# configuration
load_dotenv()  # take environment variables from .env.

base_topic = 'PI1'
mqtt_hostname = os.getenv('MQTT_HOSTNAME')
mqtt_port = int(os.getenv('MQTT_PORT'))
#mqtt_clientname = 'mc-log-mqtt'
input_filename = os.getenv('INPUT_FILENAME')



# Hook for cleanup after interrupt
def signal_handler(signal, frame):
    # cleanup
    print("mc-log-mqtt ending.")
    mqtt_client.disconnect()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
interrupted = False

print("This is Minecraft log parser sending MQTT messages for every")
print("line containing predefined message described by regexp")
print("MQTT hostname: ", mqtt_hostname, "MQTT port: ", mqtt_port)


def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True
        print("MQTT on_connect callback: connected ok")
    else:
        print("MQTT on_connect callback: Bad connection Returned code=",rc)
    
# MQTT connection initialization
mqtt_client = mqtt.Client()
mqtt_client.on_connect=on_connect  #bind call back function
mqtt_client.loop_start()
mqtt.Client.connected_flag=False
print("Connecting to MQTT broker ",mqtt_hostname)
mqtt_client.connect(mqtt_hostname,port=mqtt_port)
while not mqtt_client.connected_flag: #wait in loop
    print("Wait for MQTT callback")
    sleep(1)


print("LOG filename: ", input_filename)
# wait if the input_filename does't exists
while not os.path.exists(input_filename):
    print("Wait for LOG file to exist")
    sleep(1)
print("Entering the tail loop")

# main loop
for line in sh.tail("-0f", input_filename, _iter=True):

    tokens = re.findall(r'UUID: (.*), Channel: (.*), Power: (.*)', line)  # find relevant part
    if tokens:
        topic=tokens[0][0]
        subtopic=tokens[0][1]
        message=tokens[0][2]

        if topic and message:

            print("Sending MQTT message: ", topic, "/", subtopic, "> ",  message)
            print(base_topic+"/ESPblock/"+topic+"/"+subtopic, message)
            mqtt_client.publish(base_topic+"/ESPblock/"+topic+"/"+subtopic, message)
