from gpiozero import Button, LED
from time import sleep
import random

led = LED(pin=17)
player_1 = Button(pin=18)
player_2 = Button(pin=25)

time = random.uniform(4, 9)
sleep(time)
led.on()

while True:
    if player_1.is_pressed:
        print("老師獲勝")
        break
    if player_2.is_pressed:
        print("學生獲勝")
        break
led.off()
