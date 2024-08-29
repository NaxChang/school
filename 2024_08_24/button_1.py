from gpiozero import Button
from signal import pause

button = Button(pin=18)


def button_pressed():
    print("目前是按壓的")


def button_released():
    print("目前是放開的")


button.when_pressed = button_pressed
button.when_released = button_released

pause()
