import signal
from gpiozero import Button, LED


def user_release():
    print("press the button and then release it")


if __name__ == "__main__":
    button = Button(pin=18)
    button.when_released = user_release
    led = LED(pin=25)
    signal.pause()
