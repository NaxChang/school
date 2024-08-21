from gpiozero import LED, Button
from time import sleep

# 模擬 LED 引腳 25,23
led_pins = [25, 23]
button = Button(pin=18)

running = True


def stop_loop():
    global running
    running = False


button.when_released = stop_loop


leds = []
for pin in led_pins:
    leds.append(LED(pin))


while running:
    for led in leds:
        led.on()
        sleep(1)
    for led in leds:
        led.off()
        sleep(1)
