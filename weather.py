#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests

WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_weather(weather_url):
	resp = requests.get(weather_url)

	if resp.status_code != requests.codes.ok:
		print "Error: Open Weather Map API returned error %d" % resp.status_code
		exit (-1)
		
	data = resp.json()
	print "%s: %d%sF, %dmph" % \
		(data['name'], data['main']['temp'], u'\N{DEGREE SIGN}',
		 data['wind']['speed'])


def main():
	location = os.environ.get('LOCATION_ZIP')
	if location is None:
		print "Error: Not able to fetch location from env."
		exit (-1)

	api_key = os.environ.get('KAPI_OPEN_WEATHER')
	if api_key is None:
		print "Error: Not able to fetch Open Weather Map API Key from env."
		exit (-1)

	params = "?zip=%s&units=imperial&APPID=%s" % (location, api_key)
	fetch_weather(WEATHER_BASE_URL + params)


if __name__ == "__main__":
    main()
