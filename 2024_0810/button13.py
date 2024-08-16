import signal
from gpiozero import Button, LED

press_count = 0


def user_press():
    led.on()
    global press_count
    press_count += 1
    print(f"Button pressed:{press_count} times.")


def user_released():
    led.off()
    print("Button released")


if __name__ == "__main__":
    button = Button(pin=18)
    led = LED(pin=25)
    button.when_pressed = user_press
    button.when_released = user_released
    signal.pause()
