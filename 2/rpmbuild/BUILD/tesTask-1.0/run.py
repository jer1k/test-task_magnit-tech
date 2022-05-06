#!/usr/bin/env python

import json
import os.path

if os.path.exists("/etc/tesTask/config.json"):  
	with open("/etc/tesTask/config.json") as json_data_file:
		data = json.load(json_data_file)
		
	if data and "message" in data:
		print("Hello: " + data["message"])
	else: 
		print("Hello: message not found")
		
else: 
	print("Hello: config file not found")

