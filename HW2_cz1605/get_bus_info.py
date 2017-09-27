
# coding: utf-8

# In[5]:




# In[ ]:

from __future__ import print_function
import csv
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
filename = sys.argv[3]
f = open(filename,'wb')
writer = csv.writer(f)
writer.writerow(["Latitude","Longitude","Stop Name","Stop Status"])
for i in range(number):
    try :
        stopname = activity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']  
        stopstatus = activity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except KeyError:
        stopname = "N/A"
        stopstatus = "N/A"
    latitude = activity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = activity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
     
    writer.writerow([latitude,longitude,stopname,stopstatus])
f.close()

r = open(filename,'rb')
reader = csv.reader(r)
for row in reader:
    print (row)
r.close()


# In[ ]:



