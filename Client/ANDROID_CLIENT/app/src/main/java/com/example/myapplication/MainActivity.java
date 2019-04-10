package com.example.myapplication;


import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.IOException;
import java.net.InetAddress;
import java.net.UnknownHostException;


public class MainActivity extends AppCompatActivity {

    private Button connectToServer;
    private EditText serverIP;
    private TextView statusVal;
    public Context context = this;

    private TextView moo;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        serverIP = (EditText) findViewById(R.id.serverInput);
        connectToServer = (Button) findViewById(R.id.connectButton);
        statusVal = (TextView) findViewById(R.id.status);
        moo = (TextView) findViewById(R.id.textView);

        connectToServer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AsyncTaskRunner runner = new AsyncTaskRunner();
                String sleepTime = serverIP.getText().toString();
                runner.execute(sleepTime);
            }
        });

    }

    private class AsyncTaskRunner extends AsyncTask<String, String, String> {

        private String resp;
        ProgressDialog progressDialog;

        @Override
        protected String doInBackground(String... params) {

            String host;
            int port = 12345;

            publishProgress("Connecting to Server"); // Calls onProgressUpdate()

            try {
                InetAddress serverAddress= InetAddress.getByName("192.168.0.10");
                ClientConnect con = new ClientConnect(serverAddress, 12345);
                con.send("receive_database");
                con.getFile("database.db", context);
                System.out.println("closing connection");

                return null;

            } catch (UnknownHostException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }

            return null;
        }

        @Override
        protected void onPreExecute() {
            progressDialog = ProgressDialog.show(MainActivity.this,
                    "Please Wait",
                    "Currently trying to connect. Please wait!");
        }


        @Override
        protected void onProgressUpdate(String... text) {
            //finalResult.setText(text[0]);
            // Things to be done while execution of long running operation is in
            // progress. For example updating ProgessDialog
        }

        @Override
        protected void onPostExecute(String result) {
            // execution of result of Long time consuming operation
            progressDialog.dismiss();
            moo.setText("At this point, we have successfully downloaded from the server.");
            Intent intent = new Intent(context, BuildMenu.class);
            startActivity(intent);

        }
    }
}