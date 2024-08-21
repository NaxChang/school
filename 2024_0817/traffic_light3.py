from gpiozero import LED, Button
from time import sleep

# 初始化LED灯和按钮
red_led = LED(pin=27)
green_led = LED(pin=23)
yellow_led = LED(pin=25)
button = Button(pin=18)  # 按钮连接到18号引脚

# 设置要执行的次数
num_cycles = 4
current_cycle = 0

def start_led_sequence():
    global current_cycle
    current_cycle = 0  # 重置计数器
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

        # 增加计数变量
        current_cycle += 1

def button_pressed():
    print("按钮被按下，开始LED灯循环...")
    start_led_sequence()

def button_released():
    print("按钮被释放")

# 设置按钮的事件处理程序
button.when_pressed = button_pressed
button.when_released = button_released

# 保持程序持续运行以处理按钮事件
while True:
    sleep(1)  # 保持脚本运行
