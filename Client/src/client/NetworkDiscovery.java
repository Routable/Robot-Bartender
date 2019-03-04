package client;


import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;

public class NetworkDiscovery {
	private int discoveryPort; 
	
	
	public NetworkDiscovery(int discoveryPort) {
		this.discoveryPort = discoveryPort;
		System.out.println("Searching Network for Server");
	}
	
	
  public String Listener() throws IOException {
	  
		 String serverAddress = null;
		 MulticastSocket mcSocket = null;
		 
	while(true) {
		 mcSocket = new MulticastSocket(discoveryPort);
		 System.out.println("Multicast Receiver running on:" + mcSocket.getLocalSocketAddress());
		 DatagramPacket packet = new DatagramPacket(new byte[1024], 1024);
		    
		 System.out.println("Waiting for a  multicast message...");
		 mcSocket.receive(packet);
		 String msg = new String(packet.getData(), packet.getOffset(), packet.getLength());
		 System.out.println("Message received from" + packet.getAddress());

		 if(validateServer(msg)) {
			 serverAddress = packet.getAddress().getHostAddress();

			 System.out.println("Server found at" + serverAddress);
			 mcSocket.close();
			 break;
		 } 
	}
	 return serverAddress;
  }
  
  
  // Simple validation to see if multicast request is genuine or not. 
  public boolean validateServer(String appPassword) {
	  if(appPassword.equals("application_password")) {
		  return true;
	  } else {
		  return false;
	  }
  }
  
}