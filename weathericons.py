#!/usr/bin/env python
# coding: utf8
from util import * 

def printforecast(day):
	prettyprint(day["date"]["weekday_short"]+", %d.%d" % (day["date"]["day"], day["date"]["month"]))
	condition = day["conditions"]	
	prettyprint(condition)
	prettyprint("bei %s°C bis %s°C" % (day["low"]["celsius"],day["high"]["celsius"]))	
	return

def printweather( icon ):
	if icon in weathericon:
		for line in (weathericon[icon]):
			prettyprint (line)
	else:
		icon = "questionmark"
		for line in (weathericon[icon]):
			prettyprint (line)
	return

def printwind (icon):
	if icon in windicon:
		for line in (windicon[icon]):
			prettyprint (line)
	else:
		icon = "Variable"
		for line in (windicon[icon]):
			prettyprint (line)	
	return

questionmark = [
		"    .-.      ",
		"     __)     ",
		"    (        ",
		"     `-’     ",
		"      •      "]
sunny = [
		"    \\   /    ",
		"     .-.     ",
		"  ― (   ) ―  ",
		"     `-’     ",
		"    /   \\    "]
partlycloudy = [
		"   \\  /      ",
		" _ /\"\".-.    ",
		"   \\_(   ).  ",
		"   /(___(__) ",
		"             "]
cloudy = [
		"             ",
		"     .--.    ",
		"  .-(    ).  ",
		" (___.__)__) ",
		"             "]
lightshowers = [
		" _`/  .-.    ",
		"  ,\_(   ).  ",
		"    (___(__) ",
		"     ‘ ‘ ‘ ‘ ",
		"    ‘ ‘ ‘ ‘  "]
heavyshowers = [
		" _`/``.-.    ",
		"  ,\_(   ).  ",
		"   /(___(__) ",
		"   ‚‘‚‘‚‘‚‘  ",
		"   ‚’‚’‚’‚’  "]
lightsnowshowers = [
		" _`/\"\".-.    ",
		"  ,\\_(   ).  ",
		"   /(___(__) ",
		"     *  *  * ",
		"    *  *  *  "]
heavysnowshowers =  [
		" _`/\"\".-.    ",
		"  ,\\_(   ).  ",
		"   /(___(__) ",
		"    * * * *  ",
		"   * * * *   "]
lightsleetshowers = [
		" _`/\"\".-.    ",
		"  ,\\_(   ).  ",
		"   /(___(__) ",
		"     ‘ * ‘ * ",
		"    * ‘ * ‘  "]
thunderyshowers = [
		" _`/\"\".-.    ",
		"  ,\\_(   ).  ",
		"   /(___(__) ",
		"    ⚡‘ ‘⚡‘ ‘ ",
		"    ‘ ‘ ‘ ‘  "]
lightrain = [
		"     .-.     ",
		"    (   ).   ",
		"   (___(__)  ",
		"    ‘ ‘ ‘ ‘  ",
		"   ‘ ‘ ‘ ‘   "]
heavyrain = [
		"     .-.     ",
		"    (   ).   ",
		"   (___(__)  ",
		"  ‚‘‚‘‚‘‚‘   ",
		"  ‚’‚’‚’‚’   "]

lightsnow = [
		"     .-.     ",
		"    (   ).   ",
		"   (___(__)  ",
		"    *  *  *  ",
		"   *  *  *   "]
heavysnow = [
		"     .-.     ",
		"    (   ).   ",
		"   (___(__)  ",
		"   * * * *   ",
		"  * * * *    "]
lightsleet = [
		"     .-.     ",
		"    (   ).   ",
		"   (___(__)  ",
		"    ‘ * ‘ *  ",
		"   * ‘ * ‘   "]
fog= [
		"             ",
		" _ - _ - _ - ",
		"  _ - _ - _  ",
		" _ - _ - _ - ",
		"             "]

weathericon = {
	"chanceflurries": 		questionmark,
	"chancerain": 			questionmark,
	"chancesleet": 			questionmark,
	"chancesnow": 			questionmark,
	"chancetstorms": 		questionmark,

	"sunny" : 				sunny,
	"clear" : 				sunny,
	
	"mostlysunny" : 		partlycloudy,
	"partlycloudy" : 		partlycloudy,
	
	"cloudy" : 				cloudy,
	"flurries" : 			cloudy,
	"verycloudy" : 			cloudy,
	"mostlycloudy" : 		cloudy,
	"partlysunny" :			cloudy,

	"lightshowers" : 		lightshowers,

	"heavyshowers" : 		heavyshowers,

	"lightsnowshowers" : 	lightsnowshowers,

	"heavysnowshowers" : 	heavysnowshowers,

	"lightsleetshowers" : 	lightsleetshowers,

	"thunderyshowers" : 	thunderyshowers,

	"lightrain" : 			lightrain,

	"heavyrain" : 			heavyrain,
	"rain" : 				heavyrain,

	"lightsnow" : 			lightsnow,

	"heavysnow" : 			heavysnow,
	"snow" : 				heavysnow,

	"lightsleet" : 			lightsleet,
	"sleet" : 				lightsleet,

	"fog" : fog
}

N =  [
		" / \ ",
		"  |  ",
		"  |  "]
NE =  [
		"  _  ",
		"  /| ",
		" /   "]
E =  [
		"     ",
		"---->",
		"     "]
SE =  [
		" \   ",
		"  \  ",
		"  _\|"]
S =  [
		"  |  ",
		"  |  ",
		" \ / "]
SW =  [
		"   / ",
		"  /  ",
		"|/_  "]
W =  [
		"     ",
		"<----",
		"     "]
NW =  [
		"  _  ",
		" |\  ",
		"   \ "]
VAR =  [
		" .-. ",
		"( x )",
		" '*' "]

windicon = {
	0 : N,
	1 : NE,
	2 : E,
	3 : SE,
	4 : S,
	5 : SW,
	6 : W,
	7 : NW,
	8 : N,
	"Variable" : VAR
}

