from gpiozero import LED, Button
from signal import pause
import threading
import time

led1 = LED(25)
led2 = LED(23)
button = Button(18)

blinking = False  # 用于跟踪闪烁状态的变量


def blink_leds():
    while blinking:  # 只要 blinking 为 True 就持续闪烁
        led1.on()
        led2.on()
        time.sleep(0.5)
        led1.off()
        led2.off()
        time.sleep(0.5)


def toggle_blinking():
    global blinking
    if not blinking:  # 如果目前不闪烁，开始闪烁
        blinking = True
        threading.Thread(target=blink_leds).start()  # 开启一个线程运行 blink_leds
    else:  # 如果目前正在闪烁，停止闪烁
        blinking = False
        led1.off()  # 按下按钮时立即关闭LED
        led2.off()


button.when_pressed = toggle_blinking  # 按下按钮切换闪烁状态

pause()
