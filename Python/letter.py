# BEFORE DOING THIS RUN 'pip install overpy' in terminal
import overpy

def searchForName(values, searchFor):
    for k in values:
            if searchFor in v:
                return k
    return None

api = overpy.Overpass()
print("Querying UF Campus with coordinates (29.627404, -82.372599, 29.652378, -82.339341) ...")
# result = api.query("node(-82.355444, 29.635203, 82.339565, 29.652099)[highway=motorway];out;")

result = api.query("""way(29.627404, -82.372599, 29.652378, -82.339341)["highway"];
    (._;>;);
    out body;
    """)
print "Number of nodes: ", len(result.nodes)
print "Number of ways: ", len(result.ways)
s = []
for node in result.ways:
	# print "Node id: ", node.id
	# print "Node lat/lon: ", node.lat, node.lon
	# print "Node tags: ", node.tags
	if "name" in node.tags:
		name = node.tags.get("name")
		if name not in s:
			s.append(node.tags.get("name"));

s = sorted(s)
for street in s:
	print street

