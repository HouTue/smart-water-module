import paho.mqtt.client as mqtt
import time
import ssl
import random
import json

# MQTT configuration
MQTT_BROKER = "ur own broker"
MQTT_PORT = 8883
MQTT_USERNAME = "ur own user"
MQTT_PASSWORD = "ur own pws"
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
    """
    Nhận lệnh từ Node-RED: ON / OFF
    """
    global pump_on
    command = msg.payload.decode().strip()
    if command == "ON":
        pump_on = True
        print("Nhận lệnh: Bơm NƯỚC BẬT (pump_on = True)")
    elif command == "OFF":
        pump_on = False
        print("Nhận lệnh: Bơm NƯỚC TẮT (pump_on = False)")
    else:
        print(f"⚠ Lệnh không hợp lệ: {command}")

client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(TOPIC_PUMP)
client.loop_start()

# Initial water level
water_level = 50  # mực nước ban đầu

while True:
    if pump_on:
        # Bơm bật => nước tăng
        water_level += random.randint(3, 7)
        print("Bơm đang hoạt động ➜ Nước tăng")
    else:
        # Bơm tắt => nước giảm tự nhiên
        water_level -= random.randint(1, 4)
        print("🐾 Thú cưng đang uống ➜ Nước giảm")

    # Giới hạn mức nước từ 0 đến 100
    water_level = max(0, min(100, water_level))

    # Publish water level
    payload = json.dumps({"level": water_level})
    client.publish(TOPIC_LEVEL, payload)

    # Hiển thị log rõ ràng
    print(f"Mực nước hiện tại: {water_level}% | Trạng thái bơm: {'ON' if pump_on else 'OFF'}")

    # Delay 3 giây
    time.sleep(3)
