import mysql.connector
from flask import request, url_for, redirect, flash
from datetime import date

def submitsignup(dbname, tablename):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abcd@1234",
        database=dbname
    )
    mycursor = mydb.cursor()
    today = date.today()
    
    # get required values
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    joindate = today.strftime("%Y-%m-%d")
    
    # submit to db
    submitcmd = f"INSERT INTO {tablename} (username, email, password, joindate) VALUES (%s, %s, %s, %s)"
    values = (username, email, password, joindate)
    try:
        mycursor.execute(submitcmd, values)
        mydb.commit()
        # logging
        flash(f"{username} has been registered!")
        print("1 record inserted, ID:", mycursor.lastrowid)
    except:
        # error message
        flash(f"{username} is already taken.")
        print("lmao look at this dude imagine")
