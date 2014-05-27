#!/usr/bin/env python2

"""
    Exercise from "Learn Python Through Public Data Hacking
    ---
    Task:
    We have just forgotten our briefcase on a bus and want to get it back.
    The bus might be on the road for hours so we can't rely on their Lost&Found
    box. They do offer realtime XML information on their bus lines though in-
    cluding latitude and longitude:
    http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22
    The task is to first find out or guess which exact bus we just traveled
    with and monitor it's movement to see when it passes us to retrieve the
    briefcase. For simplicities sake, the route is North-South only so we only
    really need latitude.
    ---
    Parse realtime XML data of a public transportation data, get vehicle IDs,
    their latitude and longitudes and compare their distance to our location.
    Monitor their movements and show their location on a map.
"""

import urllib
from xml.etree.ElementTree import parse
from subprocess import call
from time import sleep

doc = parse('rt22.xml')
daves_latitude = 41.98062
daves_longitude = -87.668452

def get_xml():
    u = urllib.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
    data = u.read()
    f = open("rt22.xml", "wb")
    f.write(data)
    f.close()

def get_buses():
    candidates = []
    for bus in doc.findall("bus"):
        lat = bus.findtext('lat')
        lon = bus.findtext('lon')
        if float(lat) > daves_latitude:
            direction = bus.findtext('d')
            if direction.startswith("North"):
                busid = bus.findtext('id')
                candidates.append(busid)
    return candidates

def distance(lat1, lat2):
    return 69*abs(lat1 - lat2)

def monitor_candidates():
    candidates = get_buses()
    #~ candidates = ['1783', '1903']
    u = urllib.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = bus.findtext('lat')
            lon = bus.findtext('lon')
            dis = distance(float(lat), daves_latitude)
            print busid, dis, 'miles'
            url = "https://maps.google.com/maps?q="+lat+",+"+lon
            call(["firefox","-new-tab", url])
    print '-'*10

def main():
    while True:
        monitor_candidates()
        sleep(45)

get_xml()
main()
