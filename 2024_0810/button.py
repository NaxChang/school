# 2024

from gpiozero import Button

button = Button(pin=18)

while True:
    if button.is_pressed:
        print("The button was pressed!")
    else:
        print("The button was not pressed!")