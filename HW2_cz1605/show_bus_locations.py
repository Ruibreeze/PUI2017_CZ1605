
# coding: utf-8

# In[ ]:

from __future__ import print_function
import numpy as np
import pylab as pl
import os
import json
import sys
import urllib as url

resource = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = url.urlopen(resource)
data = response.read().decode("utf-8")
data = json.loads(data)

activity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
number = len(activity)
Number = str(number)
print('Bus Line :' + sys.argv[2])
print('Number of Active Buses :' + Number)

for i in range(number):
    latitude = activity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = activity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus {} is at latitude {} and longitude {}".format(i, latitude, longitude))