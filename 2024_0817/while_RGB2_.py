from gpiozero import RGBLED, Button
from time import sleep

# 初始化RGB LED和按钮
led = RGBLED(red=6, green=26, blue=16)
button = Button(18)

# LED控制状态标志
led_active = False


def toggle_led():
    global led_active
    led_active = not led_active


# 设定按钮的按下事件
button.when_pressed = toggle_led

while True:
    if led_active:
        # R
        led.color = (1, 0, 0)
        sleep(1.5)

        led.color = (0, 0, 0)
        sleep(0.5)

        # G
        led.color = (0, 1, 0)
        sleep(1.5)

        led.color = (0, 0, 0)
        sleep(0.5)

        # B
        led.color = (0, 0, 1)
        sleep(1.5)

        led.color = (0, 0, 0)
        sleep(0.5)
    else:
        # 关闭LED
        led.color = (0, 0, 0)
        sleep(0.1)  # 调整循环速度以减少CPU使用
