import time # 首先控制秒數,需要import time

# 模擬 LED 引腳
led_pins = [25, 23]  # 剛才有說LED放在引腳的25,還有23
 
while True: #緊接著,不定迴圈
    for pin in led_pins:  # 接著我用for迴圈去迭代
        print(f"LED {pin} ON") # 讓它印出顯示on的狀態
        time.sleep(1)  # 模擬 LED 亮起 1秒之後
        print(f"LED {pin} OFF") # 讓它印出顯示off的狀態
        time.sleep(1)  # 模擬 LED 熄滅後等待 1 秒