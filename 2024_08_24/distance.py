from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=23, trigger=24)

while True:
    distance = sensor.distance
    print(f"距離在最近的物件: {distance}m")
    sleep(1)
