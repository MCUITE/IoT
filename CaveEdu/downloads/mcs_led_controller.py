import requests
import time
import mraa as m

led = m.Gpio(44)
led.dir(m.DIR_OUT)


device_id = "Dr0KvUbv"
device_key = "GShrg05jR7tvH1Ij"
data_channel = "led_controller"
url = "http://api.mediatek.com/mcs/v2/devices/" + device_id 
url += "/datachannels/" + data_channel + "/datapoints.csv"
while True:
    r = requests.get(url, headers = {"deviceKey" : device_key})
    data = r.content.split(',')[-1]
    if data == "1":
        print "ON"
        led.write(0)
    else:
        print "OFF"
        led.write(1)
    time.sleep(0.4)

