import mraa as m
import time

led = m.Gpio(44)
led.dir(m.DIR_OUT)

while True:
    led.write(1)
    time.sleep(0.1)
    led.write(0)
    time.sleep(0.1)


