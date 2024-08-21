from gpiozero import LED
from time import sleep

# 模擬 LED 引腳 25,23
led_pins = [25, 23]

leds = []
for pin in led_pins:
    leds.append(LED(pin))

while True:
    for led in leds:
        led.on()
        sleep(1)
    for led in leds:
        led.off()
        sleep(1)
