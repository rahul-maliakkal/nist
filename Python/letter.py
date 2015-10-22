# BEFORE DOING THIS RUN 'pip install overpy' in terminal
import overpy
api = overpy.Overpass()
print("Querying UF Campus with coordinates (-82.355444, 29.635203, 82.339565, 29.652099) ...")
# result = api.query("node(-82.355444, 29.635203, 82.339565, 29.652099)[highway=motorway];out;")

result = api.query("""way(29.627404, -82.372599, 29.652378, -82.339341)["highway"];
    (._;>;);
    out body;
    """)
print "Number of nodes: ", len(result.nodes)
print "Number of ways: ", len(result.ways)
for node in result.ways:
	print "Node id: ", node.id
	# print "Node lat/lon: ", node.lat, node.lon
	print "Node tags: ", node.tags
	print Node.name
