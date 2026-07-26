import paho.mqtt.client as mqtt #import the client1
import time


broker_address = "broker.hivemq.com" #use external broker

import paho.mqtt.client as mqtt

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="publisher"
)    #create new instance

client.connect(broker_address) #connect to broker



while True :
    client.publish("house/bulbs/bulb1","OFF")
    print("Publishing message to topic","house/bulbs/bulb1")
    time.sleep(1) # wait

client.loop_stop() #stop the loop
