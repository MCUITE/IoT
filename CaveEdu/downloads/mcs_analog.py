import serial
import requests
import time

device_id = "Dr0KvUbv"
device_key = "GShrg05jR7tvH1Ij"
data_channel = "analog"

def send(send_data):
    r = requests.post("http://api.mediatek.com/mcs/v2/devices/"+ device_id + "/datapoints.csv", 
            headers = { "deviceKey": device_key},
            data = data_channel + ",," + str(send_data))

s = serial.Serial("/dev/ttyS0", 9600)
while True:
    value = s.readline()
    print value
    send(value)
    time.sleep(0.5)

