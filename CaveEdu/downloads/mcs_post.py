import requests
import time

device_id = "Dr0KvUbv"
device_key = "GShrg05jR7tvH1Ij"
data_channel = "analog"

def send(send_data):
    r = requests.post("http://api.mediatek.com/mcs/v2/devices/"+ device_id + "/datapoints.csv", 
            headers = { "deviceKey": device_key},
            data = data_channel + ",," + str(send_data))

while True:
    for a in range(1023):
        print a
        send(a)
        time.sleep(0.5)
