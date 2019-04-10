package com.example.myapplication;

import android.content.Context;

//import com.example.myapplication.database.SqliteDatabase;

import java.net.*;
import java.nio.ByteBuffer;
import java.io.*;
import java.util.Scanner;

public class ClientConnect {

    private Socket socket = null;
    private FileOutputStream fos = null;
    private DataInputStream din = null;
    private PrintStream pout = null;
    private Scanner scan = null;

    public ClientConnect(InetAddress address, int port) throws IOException
    {
        System.out.println("Initializing Client");
        socket = new Socket(address, port);
        scan = new Scanner(System.in);
        din = new DataInputStream(socket.getInputStream());
        pout = new PrintStream(socket.getOutputStream());
    }

    public void send(String msg) throws IOException
    {
        pout.print(msg);
        pout.flush();
    }

    public String recv() throws IOException
    {
        byte[] bytes = new byte[1024];
        din.read(bytes);
        String reply = new String(bytes, "UTF-8");
        System.out.println("Inside recv(): ");
        return reply;
    }

    public void closeConnections() throws IOException
    {
        // Clean up when a connection is ended
        socket.close();
        din.close();
        pout.close();
        scan.close();
    }

    public void chat() throws IOException
    {
        String response = "s";

        System.out.println("Initiating Chat Sequence");
        while(!response.equals("QUIT")){
            System.out.print("Client: ");
            String message = scan.nextLine();
            send(message);
            if(message.equals("QUIT"))
                break;
            response = recv();
            System.out.println("Server: " + response);
        }
        closeConnections();
    }

    // Request a specific file from the server
    public void getFile(String filename, Context context)
    {

        System.out.println("Requested File: " + filename);

        String filePath = context.getFilesDir().getPath().toString() + "/database.db";

        System.out.println(filePath);


        try {

            File file = new File(filePath);
            // Create new file if it does not exist
            // Then request the file from server

            fos = new FileOutputStream(file);
            // variable we use to verify the file was sent
            // properly over the network.
            byte[] size_buff = new byte[4];

            // Determining expected file size.
            din.read(size_buff);
            int size = ByteBuffer.wrap(size_buff).asIntBuffer().get();
            System.out.format("Expecting %d bytes\n", size);
            pout.write(size_buff);


            // Get content in bytes and write to a file
            byte[] buffer = new byte[size];
            //int test = ByteBuffer.wrap(buffer).asIntBuffer().get();



            for(int counter = 0; (counter = din.read(buffer, 0, buffer.length)) > 0;){
                fos.write(buffer, 0, counter);
            }

            System.out.println(fos);
            fos.flush();
            fos.close();

            //File dbFile = mContext.getDatabasePath(DB_NAME);

        } catch (IOException e) {
            e.printStackTrace();
        }


    }
}