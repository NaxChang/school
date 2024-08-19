from gpiozero import LED
from time import sleep

# 定义 LED 引脚
led_pins = [25, 23, 4, 17]
leds = []

# 初始化 LED 对象并添加到列表中
for i in led_pins:
    leds.append(LED(i))

n = 10  # 循环次数

# 循环控制 LED 的开关
while n > 0:
    for i in range(4):
        print(f"LED {i} is ON")
        leds[i].on()
        sleep(0.5)
        print(f"LED {i} is OFF")
        leds[i].off()
        sleep(0.5)
    n -= 1
