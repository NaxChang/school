from gpiozero import Button

button = Button(pin=18)
while True:
    if button.is_pressed:
        print("目前被按壓")
    else:
        print("目前是放開的")
