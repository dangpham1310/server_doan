import paho.mqtt.client as mqtt
import time

MQTT_SERVER = "mqttserver.tk"
MQTT_PORT = 1883
MQTT_USERNAME = "innovation"
MQTT_PASSWORD = "Innovation_RgPQAZoA5N"

MQTT_TOPIC_SUB_SOIL = "/innovation/soilmonitoring/WSNs"
MQTT_TOPIC_SUB_WATER = "/innovation/watermonitoring/WSNs"
MQTT_TOPIC_SUB_AIR = "/innovation/airmonitoring/WSNs"

MQTT_TOPIC_PUB_SOIL = "/innovation/soilmonitoring/WSNs"
MQTT_TOPIC_PUB_WATER = "/innovation/watermonitoring/WSNs"
MQTT_TOPIC_PUB_AIR = "/innovation/airmonitoring/WSNs"

def mqtt_connected(client, userdata, flags, rc):
    print("Connected succesfully!!")
    client.subscribe(MQTT_TOPIC_SUB_SOIL)
    client.subscribe(MQTT_TOPIC_SUB_WATER)
    client.subscribe(MQTT_TOPIC_SUB_AIR)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")


def mqtt_recv_message(client, userdata, message):
    print("Received: ", message.payload.decode("utf-8"))


mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)

#Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
mqttClient.on_message = mqtt_recv_message

mqttClient.loop_start()
counter = 0

while True:
    print("Client is running...", counter)
    mqttClient.publish(MQTT_TOPIC_PUB_SOIL, counter, retain=True)
    mqttClient.publish(MQTT_TOPIC_PUB_WATER, counter + 1, retain=True)
    mqttClient.publish(MQTT_TOPIC_PUB_AIR, counter + 2, retain=True)
    
    counter = counter + 1
    time.sleep(2)