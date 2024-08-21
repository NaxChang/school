from gpiozero import LED
from time import sleep

red_led = LED(pin=18)
green_led = LED(pin=23)
yellow_led = LED(pin=25)

while True:
    green_led.on()  # 确保这些行都正确缩排
    sleep(2)
    green_led.off()

    yellow_led.on()  # 同样确保这些行缩排一致
    sleep(1)
    yellow_led.off()

    red_led.on()  # 最后确保这些行的缩排也正确
    sleep(2)
    red_led.off()
