import paho.mqtt.client as mqtt
import redis
from dotenv import load_dotenv
import os

load_dotenv()

redis_conn = redis.Redis(
    host=os.environ['REDIS_HOST'],
    port=6379,
    password="password",
)


# print(redis_conn.ping())
# 會傳出redis的實體,實體內有屬性,屬性有兩種attribute,propertty
# 在Linux內密碼不讓別人看到,要設定環境變數


def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode("utf8")
    redis_conn.rpush(topic, message)
    print(f"top={topic},message:{message}")


if __name__ == "__main__":
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect(os.environ['MQTT_SERVER'])
    client.subscribe("501教室/學員nameless", qos=2)
    client.loop_forever()
