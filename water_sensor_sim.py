import paho.mqtt.client as mqtt
import time
import ssl
import random
import json

# MQTT configuration
MQTT_BROKER = "77cc33d43e4b436a9e5614150a6050bb.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USERNAME = "test-user"
MQTT_PASSWORD = "Danggtuee@265"
TOPIC_LEVEL = "water/level"
TOPIC_PUMP = "water/pump"

# MQTT client setup
client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.tls_insecure_set(True)

# Pump state
pump_on = False

def on_message(client, userdata, msg):
    global pump_on
    command = msg.payload.decode()
    if command == "ON":
        print("Bơm nước được bật!")
        pump_on = True
    elif command == "OFF":
        print("Bơm nước được tắt!")
        pump_on = False

client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(TOPIC_PUMP)
client.loop_start()

# Simulate water level
water_level = 100
while True:
    if pump_on:
        water_level += random.randint(5, 10)  # tăng nước khi bơm bật
    else:
        water_level -= random.randint(2, 5)  # giảm dần khi bơm tắt
    
    water_level = max(0, min(100, water_level))
    
    payload = json.dumps({"level": water_level})
    client.publish(TOPIC_LEVEL, payload)
    print(f"📡 Mực nước hiện tại: {water_level}%")
    
    time.sleep(3)
