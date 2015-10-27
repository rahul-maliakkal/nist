# BEFORE DOING THIS RUN 'pip install overpy' in terminal
import overpy
import csv
from math import radians, cos, sin, asin, sqrt


from osmapi import OsmApi

def searchForName(values, searchFor):
    # print MyApi.Map(38.735808,-77.654564,39.285358,-77.02262)
    # realized from http://andrew.hedges.name/experiments/haversine/
    for k in values:
        if searchFor in v:
            return k
    return None

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


with open('nvirginiaroads.csv','wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    api = overpy.Overpass()

    coords = "38.735808,-77.654564,39.285358,-77.02262"
    print("Querying with coords: (" + coords + ") ...")
    # result = api.query("node(-82.355444, 29.635203, 82.339565, 29.652099)[highway=motorway];out;")

    result = api.query("""way(""" + coords + """)["highway"];
        (._;>;);
        out body;
        """)
    print "Number of nodes: ", len(result.nodes)
    print "Number of ways: ", len(result.ways)
    s = []
    w = {}
    csvwriter.writerow(["road_name","road_length","crossing","service","traffic_signals","tertiary","residential","motorway_junction","motorway","min_lat","min_lon","max_lat","max_lon"])
    for way in result.ways:
        print("Name: " + way.tags.get("name", "n/a").encode("UTF8"))

        # csv += ""+way.tags.get("name", "n/a").encode("UTF8")+","
        way_name = way.tags.get("name", "n/a").encode("UTF8")


        highwayDict = {};
        way_highway = way.tags.get("highway", "n/a")
        if way_highway != "n/a":
            highwayDict[way_highway] = 1

        print("  Highway: " + way_highway)
        print("  Nodes:")
        max_lat = -9999
        min_lat = 9999
        max_lon = -9999
        min_lon = 9999

        for node in way.nodes:
            num_crossing = 0
            num_service = 0
            num_traffic_signals = 0
            num_tertiary = 0
            num_residential = 0
            num_motorway_junction = 0
            num_motorway = 0

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
                        if node_highway == "crossing":
                            num_crossing += 1
                        elif node_highway == "service":
                            num_service += 1
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
                        if node_highway == "crossing":
                            num_crossing += 1
                        elif node_highway == "service":
                            num_service += 1
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



        way.distance = haversine(min_lat, min_lon, max_lat, max_lon)
        # csv += ""+way.distance+","+highwayDict+","+min_lat+","+min_lon+","+max_lat+","+max_lon+"\n"
        csvwriter.writerow([way_name, way.distance, num_crossing, num_service, num_traffic_signals, num_tertiary, num_residential, num_motorway_junction, num_motorway, min_lat, min_lon, max_lat, max_lon])
        print("{} and {}".format("ROAD LENGTH: ", way.distance))




    # s = sorted(s)
    # for street in s:
    #   print street




