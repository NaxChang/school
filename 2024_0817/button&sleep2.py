from gpiozero import LED, Button
from signal import pause
import time

led1 = LED(25)
led2 = LED(23)
button = Button(18)


def blink_leds():
    for _ in range(100):  # 设置循环次数为5次
        led1.on()
        led2.on()
        time.sleep(0.5)  # 两个LED同时亮起0.5秒
        led1.off()
        led2.off()
        time.sleep(0.5)  # 两个LED同时熄灭0.5秒


button.when_pressed = blink_leds

pause()
