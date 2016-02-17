#!/usr/bin/env python
#coding: utf8
import sys
from util import * 
from weathericons import *

key = "e6aa0bba54460efe"
place = "Germany/Karlsruhe"
if(len(sys.argv)>1):
	place = sys.argv[1]

weathercondition = jsonwunderground(place, key, "conditions");
#Parse CONTENT from JSON
city = weathercondition["location"]["city"]
felttemp = weathercondition["current_observation"]["feelslike_c"]
icon = weathercondition["current_observation"]["icon"]
temperature = 	weathercondition["current_observation"]["temp_c"]
weather = weathercondition["current_observation"]["weather"]
wind_dir = weathercondition["current_observation"]["wind_dir"]
wind_degrees = weathercondition["current_observation"]["wind_degrees"]
wind_kph = weathercondition["current_observation"]["wind_kph"]


#Forecast
forecast  = jsonwunderground(place, key, "forecast");
nextdays = forecast["forecast"]["simpleforecast"]["forecastday"]

#OUTPUTTING to Terminal
prettyprint ("----------------------")
prettyprint ("Wetterbericht für")
prettyprint (city)
prettyprint ("")
prettyprint (weather + " bei %d°C" % temperature)
prettyprint ("Gefühlt wie %s°C" % felttemp)
printweather(icon)
prettyprint ("")
prettyprint ("Wind:")
prettyprint ("%s" % wind_dir +" %skm/h"%  wind_kph )
prettyprint ("")

#Print Forecast
prettyprint ("----------------------")
prettyprint ("Vorschau")
for (i, day) in enumerate(nextdays):
	if i>0:
		printforecast (day)
		print()
prettyprint ("")
prettyprint ("")



#print json_string
