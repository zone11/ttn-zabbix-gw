# ttn-zabbix-gw
A external script for ZABBIX to monitor your TTN Gateway metrics.  
This includes: Times since seen, packets up, packets, down

Requirements:
- ZABBIX 4.x, 5x
- Python 2.7 with these modules: requests, json, datetime
- Script installed in ExternalScripts location of your ZABBIX installation. (/usr/lib/zabbix/externalscripts)

Installation:
- Import the ZABBIX template (select the correct version)
- Add your gateway with the gateway-id (check you TTN console) as "Host Name" - Set the "Visible Name" to whatever you like
- Assign the "TTN Gateway" Template previously imported

The script is now triggered every 30 seconds and grabs data from the TTN NOC.  
There are also 3 triggers predefined to inform about gateways being offline.