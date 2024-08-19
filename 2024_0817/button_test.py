import signal
import time
from gpiozero import Button, LED

press_start = 0
press_count = 0


def user_press():
    global press_start, press_count
    press_start = time.time()
    press_count += 1
    led.on()
    print(f"Button pressed: {press_count} times.")


def user_released():
    global press_start
    led.off()
    press_duration = time.time() - press_start
    if press_duration > 2:  # 按住超過2秒
        print("Button long pressed")
    else:
        print("Button released")


if __name__ == "__main__":
    button = Button(pin=18)
    led = LED(pin=25)
    button.when_pressed = user_press
    button.when_released = user_released
    signal.pause()
