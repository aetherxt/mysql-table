from flask import Flask, redirect, url_for, render_template, request, make_response
import json
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abcd@1234",
    database="school"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students")
schooldb = mycursor.fetchall()


searchresult = []
search = 'Marcus'
mycursor.execute("SELECT * FROM STUDENTS WHERE id LIKE CONCAT('%', %(search)s, '%') OR fname LIKE CONCAT('%', %(search)s, '%') OR lname LIKE CONCAT('%', %(search)s, '%')", {'search': search})
searchresult = mycursor.fetchall()

print(searchresult)