#!/usr/bin/python3.5
#import urllib.request
import urllib.request as req
import json
import codecs
import re
import sys

#print (sys.getdefaultencoding())
URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
DEVICE_WITHOUT_LOCATION_SENSOR = "&sensor=false"
ADDRESS_LINE = "Landsberger Str. 2 80339 München"
#enc_parameter = req.pathname2url(ADDRESS_LINE)

def readJsonFromWeb(URL):
    data = req.urlopen(URL).read()
    return data

def readHtmlFile(filename):
    file_stream = codecs.open(filename, "r", "utf-8")
    lines = file_stream.read()
    file_stream.close()
    return lines

def readAddress():
    with codecs.open("addresses.txt", "r", "utf-8") as f:
      #content = f.readlines()
      content = f.read().splitlines() 
      return content
		
def writeFile(filename, content):
    file_stream = codecs.open(filename, "a", "utf-8")
    file_stream.write(content)
    file_stream.close()

def checkJsonOk(json_obj):
    json_status = json_obj['status']
    if json_status=="OK":
       status=True
    else:
       status=False
    
    print("status:" + str(status))

def init():
    print()
    print("Lat-Long from address generator V.1.0" )
    print()

def main(address_line):
   enc_parameter = req.pathname2url(address_line)
   url_full = URL + enc_parameter + DEVICE_WITHOUT_LOCATION_SENSOR
   #print ("address line:" + ADDRESS_LINE)
   print ("address line:" + address_line)
   print (url_full)
   html = readJsonFromWeb(url_full)
   json_obj = json.loads(html.decode())
   #writeFile("testfile.txt", str(html.decode()))

   #html = readHtmlFile("address.json")
   #json_obj  = json.loads(html)

   lat = json_obj['results'][0]["geometry"]["location"]["lat"]
   lng = json_obj['results'][0]["geometry"]["location"]["lng"]

   print()
   print("lat: " + str(lat))
   print("lng: " + str(lng))
   
   lineToWrite = address_line + ";" + str(lat) + ";" + str(lng) + "\r\n"
   writeFile("addressesOut.txt", lineToWrite)
   
init()

arr_addresses = readAddress()
for address in arr_addresses:
   print (address)
   main(address)
  #print (arr_addresses)
