package client;

import java.io.*;  
import java.net.*; 
import java.lang.*;

public class Client {
	
	public String host;
	public int port;
	
	
	public Client(String host, int port) {
		this.host = host;
		this.port = port;
	}
	
	
	public void connect() {

	    try{    
	    	System.out.println("Trying to connect to " + host + " on port " + port);
	        Socket socket = new Socket(host, port);  

	        DataOutputStream out = new DataOutputStream(socket.getOutputStream());  
	        DataInputStream in = new DataInputStream(socket.getInputStream());


	        out.writeUTF("Rum and Coke");
	        out.flush();
	        String str = in.readUTF();//in.readLine();

	        System.out.println("Server: " + str);


	        out.close();  
	        in.close();
	        socket.close();
	        }

	    catch(Exception e){
	        e.printStackTrace();}   

	}
}