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
