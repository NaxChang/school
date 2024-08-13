# 2024

from gpiozero import Button

button = Button(pin=18)
while True:
    if button.is_pressed:
        print("按鈕被案了")
    else:
        print("按鈕沒被案了")
