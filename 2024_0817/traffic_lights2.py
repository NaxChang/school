from gpiozero import LED
from time import sleep

# 初始化LED燈 240821
red_led = LED(pin=18)
green_led = LED(pin=23)
yellow_led = LED(pin=25)

# 設定要執行的次數
num_cycles = 4
current_cycle = 0

while current_cycle < num_cycles:
    green_led.on()
    sleep(2)
    green_led.off()

    yellow_led.on()
    sleep(1)
    yellow_led.off()

    red_led.on()
    sleep(2)
    red_led.off()
    
    # 增加計數變量
    current_cycle += 1
