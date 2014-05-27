#!/usr/bin/env python2

"""
    Exercise #2 from "Learn Python Through Public Data Hacking
    ---
    Task:
    Find the five most post-apocalyptic pothole-filled 10-block sections of road
    in Chicago. For added complexity, identify the worst road based on historical
    data involving actual number of patched potholes.
    Use the City of Chicago Data Portal (data.cityofchicago.org)
"""


import csv

def potholes_nolib():
    # Dictionary used to tabulate results
    potholes_by_zip = {}

    f = open('potholes.csv', 'r')
    for row in csv.DictReader(f):
        status = row['STATUS']
        zipcode = row['ZIP']
        if status == 'Open':
            if zipcode not in potholes_by_zip:
                potholes_by_zip[zipcode] = 1
            else:
                potholes_by_zip[zipcode] += 1

    # Print a table showing the number of open potholes by zipcode
    print('Number of open potholes by zipcode')
    for zc in sorted(potholes_by_zip):
        print('%8s %d' % (zc, potholes_by_zip[zc]))

# OR:

def potholes_itertools():
    from itertools import groupby
    f = open('potholes.csv', 'r')
    potholes = list(csv.DictReader(f))
    groups = groupby(potholes, key=lambda r: r['ZIP'])
    for zipcode, group in groups:
        for r in group:
            pass
        

def potholes_collections():
    from collections import Counter

    f = open('potholes.csv', 'r')
    potholes = list(csv.DictReader(f))
    addresses = [hole['ZIP'] for hole in potholes if hole['STATUS'] == "Open"]
    tabulate = Counter(addresses)
    print tabulate.most_common(10)


