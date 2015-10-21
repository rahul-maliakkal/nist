
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

public class OSMNode {
	
	private String id;
	
	private String lat;
	
	private String lon;
	
	private final Map<String, String> tags;

	private String version;

	public OSMNode(String tid, String tlat, String tlon, String tversion, Map<String, String> ttags)
	{
		this.id = tid;
		this.lat = tlat;
		this.lon = tlon;
		this.tags = ttags;
		this.version = tversion;
	}


	public String getId()
	{
		return id;
	}

	public String getLon()
	{
		return lon;
	}

	public String getLat()
	{
		return lat;
	}

	public String getTags()
	{
		return tags.toString();
	}

}