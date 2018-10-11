#!/usr/bin/env python

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

gw_url = noc_url + gw
dataset = json.loads(requests.get(gw_url).text)

lastcontact = int(dataset["time"])

if "uplink" in dataset:
    data_up = dataset["uplink"]
else:
    data_up= 0

if "downlink" in dataset:
    data_down = dataset["downlink"]
else:
    data_down = 0

lastcontact_date = datetime.datetime.fromtimestamp(lastcontact/1000000000)
now = datetime.datetime.now()
lastseen = now - lastcontact_date

if item == "up":
    print(data_up)
elif item == "down":
    print(data_down)
else:
    print int(lastseen.total_seconds())
