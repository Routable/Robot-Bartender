import java.io.IOException;
import java.net.InetAddress;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		try {
			NetworkDiscovery Discovery = new NetworkDiscovery(37020);
			InetAddress serverAddress = InetAddress.getByName(Discovery.Listener());
			ClientConnect con = new ClientConnect(serverAddress, 12345);
			Scanner input = new Scanner(System.in);

			con.send("receive_database");
			con.getFile("database");

			System.out.println("Connected to Server");
			
			String userInput = "";
			


			do {
				System.out.println("Enter test_off, or test_on:");
				userInput = input.nextLine();
				con.send(userInput);
				
				if (userInput.equals("quit")) break;

				} while (true);
	
		
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
