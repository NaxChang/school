import signal
from gpiozero import Button, LED
from datetime import datetime


def user_release():
    print("User presses and releases")
    led.toggle()  # 按一次會進行關或開
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(now_str)
    if led.is_lit:
        print("light on")
    else:
        print("light off")


if __name__ == "__main__":  # button 全域
    button = Button(pin=18)
    # print(button.pin)
    button.when_released = user_release
    led = LED(pin=25)
    signal.pause()
