import paho.mqtt.client as mqtt
import ssl
from datetime import datetime as dt
def on_connect(client, userdata, flags, reason_code, properties=None):
    client.subscribe(topic="/call_id")
def on_message(client, userdata, message, properties=None):
    print(
        f"{dt.now()} Received message {message.payload} on topic '{message.topic}' with QoS {message.qos}"
    )
def on_subscribe(client, userdata, mid, qos, properties=None):
    print(f"{dt.now()} Subscribed with QoS {qos}")


client = mqtt.Client(client_id="clientid", protocol=mqtt.MQTTv311, clean_session=True)
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.username_pw_set(username="username", password="password")
# client.tls_set(ca_certs="cacerts/isrgrootx1.pem")
client.connect(host="127.0.0.1", port=1883, keepalive=60)
client.loop_forever()