from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(pin=18)
led = LED(pin=16)

pir.when_motion = led.on
pir.when_no_motion = led.off

pause()
