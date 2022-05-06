#!/usr/bin/env python

import yaml
import os.path

if os.path.exists('config.yml'):  
	with open("config.yml", "r") as ymlfile:
		cfg = yaml.load(ymlfile)
		
	#if cfg["message"]:
	if cfg and "message" in cfg:
		print("Hello: " + cfg["message"])
	else: 
		print("Hello: message not found")
		
else: 
	print("Hello: config file not found")

