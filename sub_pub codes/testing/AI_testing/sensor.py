import time
import random
import json
import paho.mqtt.client as mqtt

# 1. Configuration (Using HiveMQ's free public broker)
BROKER = "test.mosquitto.org"
PORT = 1883
# CHANGE THIS TOPIC NAME TO SOMETHING UNIQUE SO OTHERS DON'T INTERFERE
TOPIC = "digitaltwin/ssp/sensor1" 

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

print("Connecting to broker...")
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        # Simulate sensor data
        temperature = round(random.uniform(20.0, 35.0), 2)
        payload = {"temperature": temperature, "status": "running"}
        
        # Publish to the broker
        client.publish(TOPIC, json.dumps(payload))
        print(f"Sent data to twin: {payload}")
        
        time.sleep(2)  # Send data every 2 seconds
except KeyboardInterrupt:
    print("Stopping simulator...")
    client.loop_stop()
    client.disconnect()
