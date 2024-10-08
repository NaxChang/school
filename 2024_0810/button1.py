import signal
from gpiozero import Button, LED


def user_release():
    print("使用者按下放開")
    led.toggle()  # 按一次會進行關或開


if __name__ == "__main__":  # button 全域
    button = Button(pin=18)
    # print(button.pin)
    button.when_released = user_release
    led = LED(pin=25)
    signal.pause()

"""
儲存資料 1.attribute 2.property
功能 method 一定要有括號
button.method()
"""
