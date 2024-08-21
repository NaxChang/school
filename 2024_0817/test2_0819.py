import time

# 模擬 LED 引腳 25,23
led_pins = [25, 23]

while True:
    for pin in led_pins:
        print(f"LED {pin} ON")
        time.sleep(1)
        print(f"LED {pin} OFF")
        time.sleep(1)
