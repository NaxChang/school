from gpiozero import LED
from time import sleep

red_led = LED(pin=18)
green_led = LED(pin=23)
yellow_led = LED(pin=25)


while True:
    green_led.on()
    print("The green light is ON")
    sleep(2)
    green_led.off()

    yellow_led.on()
    print("The yellow light is ON")
    sleep(1)
    yellow_led.off()

    red_led.on()
    print("The red light is ON")
    sleep(2)
    red_led.off()
