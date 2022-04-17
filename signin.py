import mysql.connector
from flask import request, url_for, redirect

def submitsignup(dbname, tablename):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abcd@1234",
        database=dbname
    )
    mycursor = mydb.cursor()

    # request user data from db
    requestcmd = f"SELECT * FROM {tablename}"
    mycursor.execute(requestcmd)
    
