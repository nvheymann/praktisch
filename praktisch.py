import math
import sqlite3
import time
import paho.mqtt.client as mqtt


# Mqtt zum subscrieben und Publischen
class p_mqtt:
    # Initialisiren der Werte von dir
    def __init__(self):
        self.topic = ""
        self.broker = "nicovonheymann.local"
        self.port = 1883

    # Subscriber eines topics
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

    # publischer eines Topics
    def pub(self, payload="test"):
        publisher = mqtt.Client()
        publisher.connect(self.broker, self.port)
        publisher.loop_start()

        while True:
            publisher.publish(topic=self.topic, payload=payload)
            time.sleep(1)


# Datenbank
class sqlite:
    def __init__(self, dbname):
        self.dbname = dbname
        self.datenbank = dbname + ".db"
        self.conn = sqlite3.connect(self.datenbank)
        self.c = self.conn.cursor()

    # Erstellen von Tabellen
    def table(self, tabelle1=None, tabelle2=None, tabelle3=None, tabelle4=None, tabelle5=None, sql=None):

        # Ein lesen eines Sqlite Scriptes
        if sql is not None:
            datei = sql
            datei = open(datei).read()
            sql_datei = datei.split(";")
            for command in sql_datei:
                self.c.execute(command)
                self.conn.commit()

        # Weitere Tabelle hinzufügen wenn erwünscht
        elif tabelle1 is not None:
            self.c.execute(tabelle1)
            self.conn.commit()

        # Weitere Tabelle hinzufügen wenn erwünscht
        elif tabelle2 is not None:
            self.c.execute(tabelle2)
            self.conn.commit()

        # Weitere Tabelle hinzufügen wenn erwünscht
        elif tabelle3 is not None:
            self.c.execute(tabelle3)
            self.conn.commit()

        # Weitere Tabelle hinzufügen wenn erwünscht
        elif tabelle4 is not None:
            self.c.execute(tabelle4)
            self.conn.commit()

        # Weitere Tabelle hinzufügen wenn erwünscht
        elif tabelle5 is not None:
            self.c.execute(tabelle5)
            self.conn.commit()

        else:
            print("Datenbank erstellt keine Tabellen eingefügt!!!")

    # Auswertung
    def select(self, abfrage):
        auswertung = self.c.execute(abfrage)
        inhalt = auswertung.fetchall()
        return inhalt
