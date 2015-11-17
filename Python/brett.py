import overpy
import csv
import pandas as pd
from math import radians, cos, sin, asin, sqrt

from osmapi import OsmApi

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    rKm = 6371 # Radius of earth in kilometers. Use 3956 for miles
    rM = 3956
    return c * rM

s = "-77.25\t38.78\t-76.75\t39.0\t2015-03-01T00:00:00\t2015-03-31T23:59:59"

# Split by tabs
x = s.split("\t")

# Assign to variables
minLat = x[0]
minLon = x[1]
maxLat = x[2]
maxLon = x[3]
startStamp = x[4]
endStamp = x[5]
month = startStamp.split("-")[1]
coordinateString = minLon + ", "+minLat+", "+maxLon+", "+maxLat
print coordinateString
print "sampleCoordinateString = 38.735808,-77.654564,39.285358,-77.02262"



# Test print
print "minLat = ", minLat
print "minLon = ", minLon
print "maxLat = ", maxLat
print "maxLon = ", maxLon
print "month = ", month

csvfile = open("./test.csv",'wb')
csvwriter = csv.writer(csvfile, delimiter=",")

print("Querying with coords: (" + coordinateString + ") ...")
api = overpy.Overpass()
result = api.query("""way(""" + coordinateString + """)["highway"];
    (._;>;);
    out body;
    """)
print "Number of nodes: ", len(result.nodes)
print "Number of ways: ", len(result.ways)
s = []
w = {}


csvwriter.writerow(["index","road_length","highway","crossing","service","traffic_signals","tertiary","residential","motorway_junction","month"])
index = 0

for way in result.ways:
    print("Name: " + way.tags.get("name", "n/a").encode("UTF8"))

    # csv += ""+way.tags.get("name", "n/a").encode("UTF8")+","
    way_name = way.tags.get("name", "n/a").encode("UTF8")


    # Contain the different kinds of higways on our way
    num_crossing = 0
    num_service = 0
    num_traffic_signals = 0
    num_tertiary = 0
    num_residential = 0
    num_motorway_junction = 0
    num_motorway = 0

    highwayDict = {};

    way_highway = way.tags.get("highway", "n/a")
    if way_highway != "n/a":
        highwayDict[way_highway] = 1
        if way_highway == "crossing":
            num_crossing = 1
        elif way_highway == "service":
            num_service = 1
        elif way_highway == "traffic_signals":
            num_traffic_signals = 1
        elif way_highway == "tertiary":
            num_tertiary = 1
        elif way_highway == "residential":
            num_residential = 1
        elif way_highway == "motorway_junction":
            num_motorway_junction += 1
        elif way_highway == "motorway":
            num_motorway = 1

    print("  Highway: " + way_highway)
    print("  Nodes:")
    max_lat = -9999
    min_lat = 9999
    max_lon = -9999
    min_lon = 9999

    for node in way.nodes:

        if node.lat < min_lat:
            min_lat = node.lat
        if node.lat > max_lat:
            max_lat = node.lat
        if node.lon < min_lon:
            min_lon = node.lon
        if node.lon > max_lon:
            max_lon = node.lon
        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
        print(node.tags)
        node_highway = node.tags.get("highway", "n/a")
        if node_highway is not "n/a":
            if len(highwayDict) != 0:
                if node_highway in highwayDict.keys():
                    highwayDict[node_highway] += 1
                    if node_highway == "crossing":
                        num_crossing += 1
                    elif node_highway == "service":
                        print("SERVICE!!")

                        num_service += 1
                        print(num_service)
                    elif node_highway == "traffic_signals":
                        num_traffic_signals += 1
                    elif node_highway == "tertiary":
                        num_tertiary += 1
                    elif node_highway == "residential":
                        num_residential += 1
                    elif node_highway == "motorway_junction":
                        num_motorway_junction += 1
                    elif node_highway == "motorway":
                        num_motorway += 1
                else:
                    highwayDict[node_highway] = 1
                    if node_highway == "crossing":
                        num_crossing = 1
                    elif node_highway == "service":
                        num_service = 1
                        print("Found first service")
                    elif node_highway == "traffic_signals":
                        num_traffic_signals = 1
                    elif node_highway == "tertiary":
                        num_tertiary = 1
                    elif node_highway == "residential":
                        num_residential = 1
                    elif node_highway == "motorway_junction":
                        num_motorway_junction += 1
                    elif node_highway == "motorway":
                        num_motorway = 1

    way.distance = haversine(min_lat, min_lon, max_lat, max_lon)

    csvwriter.writerow([index, way.distance, num_crossing, num_service, num_traffic_signals, num_tertiary, num_residential, num_motorway_junction, num_motorway, month])
    index += 1
    print("{} and {}".format("ROAD LENGTH: ", way.distance))



