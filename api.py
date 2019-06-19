#!/usr/bin/env python

import urllib2
import json
import getpass

mac_address = raw_input("Enter your Mac Address: ")
api_key = getpass.getpass("Enter your API_Key: ")
url = 'https://api.macaddress.io/v1?apiKey=' + api_key
final_url = url + "&output=json" + "&search=" + mac_address

object = urllib2.urlopen(final_url)
data = json.load(object)
print("Company's Name for the MAC Address is {[vendorDetails][companyName]}".format(data))
