from gpiozero import LED
from time import sleep

red_led = LED(pin=18)
green_led = LED(pin=23)
yellow_led = LED(pin=25)

current_cycle = 0
num_cycle = 5

while current_cycle < num_cycle:
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

    current_cycle += 1
    print(f"目前做了{current_cycle}次循環")
