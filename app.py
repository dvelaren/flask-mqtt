import os
import json
from flask import Flask, render_template, request, url_for, jsonify
from flask_mqtt import Mqtt
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MQTT_BROKER_URL"] = os.getenv("MQTT_BROKER_URL") or "mqtt.dis.eafit.edu.co"
app.config["MQTT_BROKER_PORT"] = os.getenv("MQTT_BROKER_PORT") or 1883
app.config["MQTT_USERNAME"] = os.getenv("MQTT_USERNAME")
app.config["MQTT_PASSWORD"] = os.getenv("MQTT_PASSWORD")
topic = os.getenv("MQTT_TOPIC") or "/devices/esp32"

mqtt_client = Mqtt(app)

led_red = 0


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        mqtt_client.subscribe(topic)  # subscribe topic
    else:
        print("Bad connection. Code:", rc)


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    global led_red
    data = dict(topic=message.topic, payload=json.loads(message.payload.decode()))
    led_red = data["payload"].get("led_red")
    print("Received message on topic: {topic} with payload: {payload}".format(**data))


@app.route("/")
def home():
    return render_template("index.html")


@app.post("/")
def send_data():
    data = request.get_json()
    publish_result = mqtt_client.publish(topic, json.dumps(data))
    print("Published to topic: " + topic + " | Message: " + json.dumps(data))
    publish_result2 = mqtt_client.publish(
        f"{topic}/{list(data.keys())[0]}", float(list(data.values())[0])
    )
    print(
        "Published to topic: "
        + f"{topic}/{list(data.keys())[0]}"
        + f" | Message: {float(list(data.values())[0])}"
    )
    return jsonify({"code": publish_result[0]})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
