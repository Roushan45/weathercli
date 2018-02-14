import json
import os
"""
main": {
        "temp": 302.621,
        "pressure": 953.77,
        "humidity": 41,
        "temp_min": 302.621,
        "temp_max": 302.621,
        "sea_level": 1028.21,
        "grnd_level": 953.77
    },
"""
f=open('/home/centos/weather-cli/weather/test.json')
data=json.load(f)
print("view : " + data['weather'][0]['description'])
print("Current Temp : "+str(data['main']['temp']))
print("Max Temp : "+str(data['main']['temp_max']))
print("Min Temp : "+str(data['main']['temp_min']))


