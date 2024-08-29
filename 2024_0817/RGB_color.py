from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=6, green=26, blue=16)
# R
led.color = (
    1,
    0,
    0,
)
sleep(1.5)

led.color = (
    0,
    0,
    0,
)
sleep(0.5)

# G
led.color = (
    0,
    1,
    0,
)
sleep(1.5)

led.color = (
    0,
    0,
    0,
)
sleep(0.5)

# B
led.color = (
    0,
    0,
    1,
)
sleep(1.5)

led.color = (
    0,
    0,
    0,
)
sleep(0.5)
