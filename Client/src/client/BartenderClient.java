package client;

import java.io.IOException;

public class BartenderClient {
	
	public static void main(String[] args) throws IOException {  
		
		NetworkDiscovery Discovery = new NetworkDiscovery(37020);
		Client client = new Client(Discovery.Listener(), 12345);
		client.connect();
	}
}
