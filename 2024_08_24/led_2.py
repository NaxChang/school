from gpiozero import Button, LED
from signal import pause
from time import sleep

# 初始化按鈕和LED
button = Button(pin=18)
led = LED(pin=17)

# 状态变量，初始为 False（表示 LED 关闭）
led_on = False


def button_pressed():
    global led_on  # 使用全局变量
    if led_on:
        print("目前是按壓的，熄燈")
        led.off()
        led_on = False
    else:
        print("目前是按壓的，點亮")
        led.on()
        led_on = True

    sleep(0.1)  # 短暂的休眠，减少 CPU 占用


def button_released():
    sleep(0.1)  # 短暂的休眠，减少 CPU 占用
    # 在这个示例中，按钮释放时不需要做任何事
    pass


# 将按钮按下事件绑定到 button_pressed 函数
button.when_pressed = button_pressed
button.when_released = button_released

# 维持程序运行，等待按鈕事件
pause()
