
import paho.mqtt.client as mqtt #import the client1
import time
############

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################

broker_address = "broker.hivemq.com" #use external broker

print("creating new instance")
import paho.mqtt.client as mqtt

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="subscriber"
)

client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop

print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")

client.loop_forever()# wait
#client.loop_stop() #stop the loop
 