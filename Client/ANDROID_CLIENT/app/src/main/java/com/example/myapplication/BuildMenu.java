package com.example.myapplication;

import android.app.Activity;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteException;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;

import static android.database.sqlite.SQLiteDatabase.CREATE_IF_NECESSARY;
import static android.provider.Telephony.Mms.Part.FILENAME;

public class BuildMenu extends Activity {

    private TextView moo;
    Context context;
    String json_string;
    SQLiteDatabase myDatabase;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_build_menu);
        moo = (TextView) findViewById(R.id.textView3);

        File buildFile = getFileStreamPath("database.db");

        String file = buildFile.toString();

        System.out.println("About to test SQL");

        SQLiteDatabase db = SQLiteDatabase.openOrCreateDatabase(file, null);
        db.close();
        System.out.println(db);

        ArrayList<ContactModel> contacts = new ArrayList<ContactModel>();

        try {
            db = SQLiteDatabase.openDatabase(file, null,
                    SQLiteDatabase.OPEN_READONLY);

            System.out.println("MOO DB");

            Cursor cursor = db.rawQuery("SELECT * FROM RECIPES", null);

            System.out.println("Cursor has " + cursor.getCount() + " inputs");

            ContactModel contactModel;
            if (cursor.getCount() > 0) {
                for (int i = 0; i < cursor.getCount(); i++) {
                    cursor.moveToNext();
                    contactModel = new ContactModel();
                    contactModel.setID(cursor.getString(0));
                    contactModel.setFirstName(cursor.getString(1));
                    //contactModel.setLastName(cursor.getString(2));
                    contacts.add(contactModel);
                }
            }
            cursor.close();
            db.close();

            System.out.println("THE TEST WAS SUCCESSFUL!");
        } catch (SQLiteException e) {
            // database doesn't exist yet.
        }




/*
        StringBuilder stringBuilder = new StringBuilder();

        //Retrieves information from file
        try{
            FileInputStream in = openFileInput("database.db");
            InputStreamReader inputStreamReader = new InputStreamReader(in);
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                stringBuilder.append(line + "\n");
            }
            inputStreamReader.close();
            bufferedReader.close();
            System.out.println(stringBuilder);
        } catch (IOException e){
            Toast.makeText(getApplicationContext(),
                    "Problems: " + e.getMessage(), Toast.LENGTH_LONG).show();
        };
*/
    }
}
