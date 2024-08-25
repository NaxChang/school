from gpiozero import Button, LED
from time import sleep
from signal import pause

button = Button(pin=18)
led = LED(pin=17)

led_on = False


def button_pressed():
    global led_on
    if led_on:
        print("目前是按壓的,熄燈")
        led.off()
        led_on = False
    else:
        print("目前是按壓的,亮燈")
        led.on()
        led_on = True


def button_released():
    sleep(0.1)
    pass


button.when_pressed = button_pressed
button.when_released = button_released

pause()
