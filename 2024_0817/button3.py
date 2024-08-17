import signal
from gpiozero import Button, LED
from datetime import datetime
import paho.mqtt.publish as publish


def user_release():
    print("User presses and releases")
    led.toggle()  # 按一次會進行關或開
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(now_str)
    if led.is_lit:
        message = f"""{{
            "status": true,
            "date": {now_str},
            "topic": "501教室/學員nameless",
        }}"""

        # message = "燈是開的"
        print(message)
        publish.single(
            topic="501教室/學員nameless", payload=message, hostname="127.0.0.1", qos=2
        )
    else:
        message = f"""{{
            "status": false,
            "date": {now_str},
            "topic": "501教室/學員nameless",
        }}"""
        print(message)
        publish.single(
            topic="501教室/學員nameless", payload=message, hostname="127.0.0.1", qos=2
        )


if __name__ == "__main__":  # button 全域
    button = Button(pin=18)
    # print(button.pin)
    button.when_released = user_release
    led = LED(pin=25)
    signal.pause()
