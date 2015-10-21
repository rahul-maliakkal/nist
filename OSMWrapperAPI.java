/**
 * (c) Jens Kübler
 * This software is public domain
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 * 
 */

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.net.Authenticator;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

// import org.osm.lights.diff.OSMNode;
// import org.osm.lights.upload.BasicAuthenticator;
import org.w3c.dom.Document;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

/**
 * 
 */
public class OSMWrapperAPI {

	private static final String OVERPASS_API = "http://www.overpass-api.de/api/interpreter";
	private static final String OPENSTREETMAP_API_06 = "http://www.openstreetmap.org/api/0.6/";

	public static OSMNode getNode(String nodeId) throws IOException, ParserConfigurationException, SAXException {
		String string = "http://www.openstreetmap.org/api/0.6/node/" + nodeId;
		URL osm = new URL(string);
		HttpURLConnection connection = (HttpURLConnection) osm.openConnection();

		DocumentBuilderFactory dbfac = DocumentBuilderFactory.newInstance();
		DocumentBuilder docBuilder = dbfac.newDocumentBuilder();
		Document document = docBuilder.parse(connection.getInputStream());
		List<OSMNode> nodes = getNodes(document);
		if (!nodes.isEmpty()) {
			return nodes.iterator().next();
		}
		return null;
	}

	/**
	 * 
	 * @param lon the longitude
	 * @param lat the latitude
	 * @param vicinityRange bounding box in this range
	 * @return the xml document containing the queries nodes
	 * @throws IOException
	 * @throws SAXException
	 * @throws ParserConfigurationException
	 */
	@SuppressWarnings("nls")
	private static Document getXML(double lon, double lat, double vicinityRange) throws IOException, SAXException,
			ParserConfigurationException {

		DecimalFormat format = new DecimalFormat("##0.0000000", DecimalFormatSymbols.getInstance(Locale.ENGLISH)); //$NON-NLS-1$
		String left = format.format(lat - vicinityRange);
		String bottom = format.format(lon - vicinityRange);
		String right = format.format(lat + vicinityRange);
		String top = format.format(lon + vicinityRange);

		String string = OPENSTREETMAP_API_06 + "map?bbox=" + left + "," + bottom + "," + right + ","
				+ top;
		URL osm = new URL(string);
		HttpURLConnection connection = (HttpURLConnection) osm.openConnection();

		DocumentBuilderFactory dbfac = DocumentBuilderFactory.newInstance();
		DocumentBuilder docBuilder = dbfac.newDocumentBuilder();
		return docBuilder.parse(connection.getInputStream());
	}

	private static Document betXML(double bleft, double bbottom, double bright, double btop) throws IOException, SAXException,
		ParserConfigurationException {

	DecimalFormat format = new DecimalFormat("##0.0000000", DecimalFormatSymbols.getInstance(Locale.ENGLISH)); //$NON-NLS-1$
	String left = format.format(bleft);
	String bottom = format.format(bbottom);
	String right = format.format(bright);
	String top = format.format(btop);


	String string = OPENSTREETMAP_API_06 + "map?bbox=" + left + "," + bottom + "," + right + "," + top;
	System.out.println("STRING: "+string);
	URL osm = new URL(string);
	HttpURLConnection connection = (HttpURLConnection) osm.openConnection();

	DocumentBuilderFactory dbfac = DocumentBuilderFactory.newInstance();
	DocumentBuilder docBuilder = dbfac.newDocumentBuilder();
	return docBuilder.parse(connection.getInputStream());
	}

	public static Document getXMLFile(String location) throws ParserConfigurationException, SAXException, IOException {
		DocumentBuilderFactory dbfac = DocumentBuilderFactory.newInstance();
		DocumentBuilder docBuilder = dbfac.newDocumentBuilder();
		return docBuilder.parse(location);
	}


	/**
	 * 
	 * @param xmlDocument 
	 * @return a list of openseamap nodes extracted from xml
	 */
	@SuppressWarnings("nls")
	public static List<OSMNode> getNodes(Document xmlDocument) {
		List<OSMNode> osmNodes = new ArrayList<OSMNode>();

		// Document xml = getXML(8.32, 49.001);
		Node osmRoot = xmlDocument.getFirstChild();

		System.out.println("FirstChild = "+osmRoot.toString());

		NodeList osmXMLNodes = osmRoot.getChildNodes();

		System.out.println("Childnodes = "+osmXMLNodes.toString());

		for (int i = 1; i < osmXMLNodes.getLength(); i++) {
			// System.out.println("i is "+i);
			Node item = osmXMLNodes.item(i);
			if (item.getNodeName().equals("node")) {
				NamedNodeMap attributes = item.getAttributes();
				NodeList tagXMLNodes = item.getChildNodes();
				Map<String, String> tags = new HashMap<String, String>();
				for (int j = 1; j < tagXMLNodes.getLength(); j++) {
					// System.out.println("J is "+j);
					Node tagItem = tagXMLNodes.item(j);
					NamedNodeMap tagAttributes = tagItem.getAttributes();
					if (tagAttributes != null) {
						tags.put(tagAttributes.getNamedItem("k").getNodeValue(), tagAttributes.getNamedItem("v")
								.getNodeValue());
					}
				}

				Node namedItemID = attributes.getNamedItem("id");
				Node namedItemLat = attributes.getNamedItem("lat");
				Node namedItemLon = attributes.getNamedItem("lon");
				Node namedItemVersion = attributes.getNamedItem("version");
				
				// System.out.println("ID/Lat/Long/Version = "+namedItemID+" / "+namedItemLat+" / "+namedItemLon+" / "+namedItemVersion);

				String id = namedItemID.getNodeValue();
				String latitude = namedItemLat.getNodeValue();
				String longitude = namedItemLon.getNodeValue();
				String version = "0";
				if (namedItemVersion != null) {
					version = namedItemVersion.getNodeValue();
				}

				osmNodes.add(new OSMNode(id, latitude, longitude, version, tags));
			}

		}
		return osmNodes;
	}

	public static List<OSMNode> getOSMNodesInVicinity(double lat, double lon, double vicinityRange) throws IOException,
			SAXException, ParserConfigurationException {
		return OSMWrapperAPI.getNodes(getXML(lon, lat, vicinityRange));
	}

	public static List<OSMNode> betOSMNodesInVicinity(double left, double bottom, double right, double top) throws IOException,
			SAXException, ParserConfigurationException {
		return OSMWrapperAPI.getNodes(betXML(left, bottom, right, top));
	}

	/**
	 * 
	 * @param query the overpass query
	 * @return the nodes in the formulated query
	 * @throws IOException
	 * @throws ParserConfigurationException
	 * @throws SAXException
	 */
	public static Document getNodesViaOverpass(String query) throws IOException, ParserConfigurationException, SAXException {
		String hostname = OVERPASS_API;
		String queryString = readFileAsString(query);

		URL osm = new URL(hostname);
		HttpURLConnection connection = (HttpURLConnection) osm.openConnection();
		connection.setDoInput(true);
		connection.setDoOutput(true);
		connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

		DataOutputStream printout = new DataOutputStream(connection.getOutputStream());
		printout.writeBytes("data=" + URLEncoder.encode(queryString, "utf-8"));
		printout.flush();
		printout.close();

		DocumentBuilderFactory dbfac = DocumentBuilderFactory.newInstance();
		DocumentBuilder docBuilder = dbfac.newDocumentBuilder();
		return docBuilder.parse(connection.getInputStream());
	}

	/**
	 * 
	 * @param filePath
	 * @return
	 * @throws java.io.IOException
	 */
	private static String readFileAsString(String filePath) throws java.io.IOException {
		StringBuffer fileData = new StringBuffer(1000);
		BufferedReader reader = new BufferedReader(new FileReader(filePath));
		char[] buf = new char[1024];
		int numRead = 0;
		while ((numRead = reader.read(buf)) != -1) {
			String readData = String.valueOf(buf, 0, numRead);
			fileData.append(readData);
			buf = new char[1024];
		}
		reader.close();
		return fileData.toString();
	}

	/**
	 * main method that simply reads some nodes
	 * 
	 * @param args
	 * @throws IOException
	 * @throws SAXException
	 * @throws ParserConfigurationException
	 */
	public static void main(String[] args) throws IOException, SAXException, ParserConfigurationException {
		Authenticator.setDefault(new BasicAuthenticator("youruser", "yourpassword"));
		// List<OSMNode> osmNodesInVicinity = getOSMNodesInVicinity(49, 8.3, 0.105);

		// LEFT, BOTTOM, RIGHT, TOP
		// List<OSMNode> osmNodesInVicinity = betOSMNodesInVicinity(82.20, 29.37, 82.17, 29.41);

		List<OSMNode> osmNodesInVicinity = betOSMNodesInVicinity(82.3200, 29.60, 82.3300, 29.70);
		// $$c(W 82°20'00"--W 82°17'00"/N 29°41'00"--N 29°37'00")
		
		for (OSMNode osmNode : osmNodesInVicinity) {
			System.out.println(osmNode.getId() + "\t:" + osmNode.getLat() + "\t:" + osmNode.getLon()+"\t: "+osmNode.getTags().toString());
		}
	}
	
}

