import paho.mqtt.client as mqtt
import time
import json
import random
import requests
class MQTTHelper:

    MQTT_SERVER = "mqttserver.tk"
    MQTT_PORT = 1883
    MQTT_USERNAME = "innovation"
    MQTT_PASSWORD = "Innovation_RgPQAZoA5N"

    MQTT_TOPIC_SUB_SOIL = "/innovation/soilmonitoring/WSNs"
    MQTT_TOPIC_SUB_WATER = "/innovation/watermonitoring/WSNs"
    MQTT_TOPIC_SUB_AIR = "/innovation/airmonitoring/WSNs"
    recvCallBack = None

    def mqtt_connected(self, client, userdata, flags, rc):
        print("Connected succesfully!!")
        client.subscribe(self.MQTT_TOPIC_SUB_SOIL)
        client.subscribe(self.MQTT_TOPIC_SUB_WATER)
        client.subscribe(self.MQTT_TOPIC_SUB_AIR)
        
    def mqtt_subscribed(self, client, userdata, mid, granted_qos):
        print("Subscribed to Topic!!!")


    def mqtt_recv_message(self, client, userdata, message):
        #print("Received: ", message.payload.decode("utf-8"))
        self.recvCallBack(message.payload.decode("utf-8"))

    def __init__(self):

        self.mqttClient = mqtt.Client()
        self.mqttClient.username_pw_set(self.MQTT_USERNAME, self.MQTT_PASSWORD)
        self.mqttClient.connect(self.MQTT_SERVER, int(self.MQTT_PORT), 60)

        # Register mqtt events
        self.mqttClient.on_connect = self.mqtt_connected
        self.mqttClient.on_subscribe = self.mqtt_subscribed
        self.mqttClient.on_message = self.mqtt_recv_message

        self.mqttClient.loop_start()

    def setRecvCallBack(self, func):
        self.recvCallBack = func


def mqtt_callback(msg):
    # print("\n\nMain.py  ---", msg)
    # print("\n\n")
    # print(json.loads(msg)["station_id"])
    # print(json.loads(msg)["station_name"])
    # print(len(json.loads(msg)["sensors"]))
    for i in range(len(json.loads(msg)["sensors"])):
        print(json.loads(msg)["station_id"])
        print(json.loads(msg)["station_name"])
        print(json.loads(msg)["sensors"][i]["sensor_id"])
        print(json.loads(msg)["sensors"][i]["sensor_value"])

        requests.post("http://10.128.70.89:5000/sensor", data={'station_id':json.loads(msg)["station_id"],'station_name':json.loads(msg)["station_name"],'sensor_id':json.loads(msg)["sensors"][i]["sensor_id"],'sensor_value':json.loads(msg)["sensors"][i]["sensor_value"]})
        print("\n")
    # print(json.loads(msg)["station_name"])

mqttObject = MQTTHelper()

while True:
    mqttObject.setRecvCallBack(mqtt_callback)