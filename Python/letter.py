# BEFORE DOING THIS RUN 'pip install overpy' in terminal
import overpy
import math
from osmapi import OsmApi

def searchForName(values, searchFor):
    for k in values:
            if searchFor in v:
                return k
    return None

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
for way in result.ways:
    print("Name: " + way.tags.get("name", "n/a"))
    print("  Highway: " + way.tags.get("highway", "n/a"))
    print("  Nodes:")
    for node in way.nodes:
        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
        print(node.tags)

s = sorted(s)
for street in s:
	print street


MyApi = OsmApi(api="api06.dev.openstreetmap.org")

# print MyApi.Map(38.735808,-77.654564,39.285358,-77.02262)
# realized from http://andrew.hedges.name/experiments/haversine/
def latLonDist(lat1, lon1, lat2, lon2):
	R = 6378.1 #Radius of the Earth
	dlat = lat2 - lat1
	dlon = lon2 - lon1
	a = math.pow((math.sin(dlat/2)), 2) + math.cos(lat1) * math.cos(lat2) * math.pow(math.sin((dlon/2)), 2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

