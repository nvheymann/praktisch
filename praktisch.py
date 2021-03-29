import math
import sqlite3
import time
import paho.mqtt.client as mqtt


# Mqtt zum subscrieben und Publischen
class p_mqtt:

    def __init__(self):
        self.topic = ""
        self.broker = "nicovonheymann.local"
        self.port = 1883

    def sub(self):
        def my_connect_method(self, client, userdata, flags, rc):
            print(" Connected . Subscribing to topic ", self.topic)
            client.subscribe(self.topic)

        def my_message_method(client, userdata, msg):
            print(" Message received :", msg.topic, msg.payload)

        client = mqtt.Client()
        client.on_connect = my_connect_method
        client.on_message = my_message_method
        client.connect(self.broker, self.port, keepalive=60)
        client.loop_forever()

    def pub(self, payload="test"):
        publisher = mqtt.Client()
        publisher.connect(self.broker, self.port)
        publisher.loop_start()

        while True:
            publisher.publish(topic=self.topic, payload=payload)
            time.sleep(1)


class sqlite():
    def __init__(self,dbname):
        self.dbname=dbname
        self.datenbank=dbname+".db"
        self.conn = sqlite3.connect(self.datenbank)
        self.c = self.conn.cursor()

    def table(self,sql):
        self.c.execute(str(sql))
        self.conn.commit()



