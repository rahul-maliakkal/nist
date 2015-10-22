# BEFORE DOING THIS RUN 'pip install overpy' in terminal
import overpy
api = overpy.Overpass()
print("Querying UF Campus with coordinates (-82.355444, 29.635203, 82.339565, 29.652099) ...")
# result = api.query("node(-82.355444, 29.635203, 82.339565, 29.652099)[highway=motorway];out;")

result = api.query("node(11.54,48.14,11.543,48.145);out;")
print "Number of nodes: ", len(result.nodes)
print "Number of ways: ", len(result.ways)
for node in result.nodes:
	print "Node id: ", node.id
	print "Node lat/lon: ", node.lat, node.lon
	print "Node tags: ", node.tags
