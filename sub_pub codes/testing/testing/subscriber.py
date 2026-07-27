
import paho.mqtt.client as mqtt #import the client1
############
def on_connect(client, userdata, flags, reason_code, properties):
    print("connected!")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("ssp/sensors")
    print("Subscribing to topic","ssp/sensors")

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)

########################################

broker_address = "broker.hivemq.com" #use external broker

print("creating new instance")
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id="subscriber")

client.on_message=on_message #attach function to callback
client.on_connect=on_connect

print("connecting to broker")
client.connect(broker_address, 1883, 60)#connect to broker


client.loop_forever()# wait
#client.loop_stop() #stop the loop
 

