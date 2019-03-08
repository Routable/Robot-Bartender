import java.io.IOException;
import java.net.InetAddress;

public class Main {
	public static void main(String[] args) {
		try {
			NetworkDiscovery Discovery = new NetworkDiscovery(37020);
			InetAddress serverAddress = InetAddress.getByName(Discovery.Listener());
			ClientConnect con = new ClientConnect(serverAddress, 12345);
			//con.send("receive_database");
			//con.getFile("database");
			con.send("QUIT");
			System.out.println("Client Disconnected");
		
			
		
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
