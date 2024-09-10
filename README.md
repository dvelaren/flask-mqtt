# Flask MQTT

This is a simple example of how to use Flask with MQTT. The application is a simple web page that allows you to publish messages to a MQTT broker.

## Installation

1. Clone the repository

2. Create a virtual environment and activate it
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the requirements

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with the following content

   ```env
   MQTT_BROKER_URL=<your_mqtt_broker_url>
   MQTT_BROKER_PORT=<your_mqtt_broker_port>
   MQTT_USERNAME=<your_mqtt_username>
   MQTT_PASSWORD=<your_mqtt_password>
   MQTT_TOPIC=<your_mqtt_topic>
   ```

5. Run the application
   ```bash
   python app.py
   ```
