import paho.mqtt.client as mqtt #import the client1
import time
import json


broker_address = "localhost"#use external broker

import paho.mqtt.client as mqtt

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="publisher"
)    #create new instance

client.connect(broker_address) #connect to broker
#client.publish("ssp/sensors", json_data)

while True:
    # اقرأ السنسور
    #temperature = sensor.read_temperature()
    #humidity = sensor.read_humidity()

#-------------------just for simulation-------------#
    sensor_data = {
    "temperature": 25,
    "humidity": 60,
    "motion": True
}
#-------------------just for simulation-------------#

    client.publish("ssp/sensors",json.dumps(sensor_data))
    time.sleep(1)



