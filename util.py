import urllib.request
import json

def prettyprint(text):
	if(len(text)>24):
		if " " in text:
			parts = text.split(' ', 1)
			prettyprint(parts[0])
			prettyprint(parts[1])
		else:
			prettyprint(text[:24])
			prettyprint(text[24:])
			
	else:
		spaces = " " * int((24-len(text))/2) 
		print (spaces+text)
	return


def jsonwunderground(place, key, feature):
	url = "http://api.wunderground.com/api/" + key + "/geolookup/"+feature+"/lang:DL/q/" + place + ".json"
	response = urllib.request.urlopen(url)
	json_string = response.read().decode()
	json_encoded = json.loads(json_string)
	return json_encoded

