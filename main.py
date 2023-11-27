import paho.mqtt.client as mqtt
import json

import influx_handler

HUM = 'relative_humidity_2'
TEM = 'temperature_1'

username = 'moja-testowa-aplikacja@ttn'
password = 'NNSXS.M62D5R3KQ2SFBWHZEAWGJ3KALR3YEEVTSSPDKTQ.WLSAKB2A6TVNRFHWDWGDDVOO7CTNBR2ROXCLBU7V64TLG5KP6BSQ'
app_id = ''
access_key = ''
topic = f'v3/{username}/devices/252716249383/up'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)
    print(f"Subscribed to topic: {topic}")


def on_message(client, userdata, msg):
    #    print(msg.topic+" "+str(msg.payload))
    payload = json.loads(msg.payload)
    data = payload['uplink_message']['decoded_payload']
    influx_handler.write_measurement(measurement='pomiary',
                                     device_id=payload['end_device_ids']['device_id'],
                                     temp=data[TEM],
                                     hum=data[HUM])


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)

if __name__ == "__main__":
    client.connect("eu1.cloud.thethings.network", 1883, 60)
    client.loop_forever()
