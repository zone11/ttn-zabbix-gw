#!/usr/bin/env python

# simple script to grab TTN gateway informations from the TTN NOC
# 1. argument is the gateway ID eg. "eui-b827ebxxxxxxxxxx"
# 2. argument is the type of data you like: up, down or last connect if empty
#
# Christian Egger, 2018.09.09

import sys, requests, json, datetime

#Actual URL to the TTN NOC API
noc_url = "http://noc.thethingsnetwork.org:8085/api/v2/gateways/"

if len(sys.argv) > 1:
        gw = sys.argv[1] 
        if len(sys.argv) > 2:
                item = sys.argv[2]
        else:
                item = ""
else:
        sys.exit()

# Grab data from NOC
gw_url = noc_url + gw
dataset = json.loads(requests.get(gw_url).text)

lastcontact = int(dataset["time"])
data_up = dataset["uplink"]
data_down = dataset["downlink"]

# Calculate seconds the gateway hast checked in for the last time
lastcontact_date = datetime.datetime.fromtimestamp(lastcontact/1000000000)
now = datetime.datetime.now()
lastseen = now - lastcontact_date

# Depending on the second argument, print data
if item == "up":
        print(data_up)
elif item == "down":
        print(data_down)
else:
        print int(lastseen.total_seconds())