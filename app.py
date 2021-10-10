from flask import Flask, redirect, url_for, render_template, request, make_response
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abcd@1234",
    database="school"
)
mycursor = mydb.cursor()


stdid = []
fname = []
lname = []
birth = []
sex = []
updated = []
searchlist = []
listname = ["id", "firstname", "lastname", "birthdate", "sex", "last updated"]

@app.route("/")
@app.route("/home")
def home():
    global searchlist
    mycursor.execute("SELECT * FROM students")
    schooldb = mycursor.fetchall()  
    stdid.clear()
    fname.clear()
    lname.clear()
    birth.clear()
    sex.clear()
    updated.clear()
    if searchlist == []:
        for value in schooldb:
            stdid.append(value[0])
            fname.append(value[1])
            lname.append(value[2])
            birth.append(value[3])
            sex.append(value[4])
            updated.append(value[5])
    else:
        for tuple in searchlist:
            stdid.append(tuple[0])
            fname.append(tuple[1])
            lname.append(tuple[2])
            birth.append(tuple[3])
            sex.append(tuple[4])
            updated.append(tuple[5])
        searchlist.clear()
    return render_template("main.html", id=stdid, fname=fname, lname=lname, birth=birth, sex=sex, updated=updated, listname=listname)

@app.route("/create")
def create():
    return render_template("create.html", success=request.args.get('success'))

@app.route("/search", methods=["POST"])
def search():
    global searchlist
    search = request.form["search"]
    mycursor.execute('SELECT * FROM students WHERE %s IN (stdid, fname, lname, birthdate, sex)', (search,))
    searchresult = mycursor.fetchall()
    print(searchresult)
    for i in range(len(searchresult)):
        searchlist.append(searchresult[i])
    return redirect(url_for("home"))

@app.route("/submit", methods=["POST"])
def reset():
    success = False
    fname = request.form["firstname"]
    lname = request.form["lastname"]
    birth = request.form["birth"]
    sex = request.form["sex"]
    print(fname, lname, birth, sex)
    return redirect(url_for("home", success=success))

@app.route("/reset")
def resetdata():
    global searchlist
    stdid.clear()
    fname.clear()
    lname.clear()
    birth.clear()
    sex.clear()
    updated.clear()
    searchlist.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)