from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect("blogs.db", check_same_thread=False)
cursor = connection.cursor()


@app.route("/")
def index():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    print(username, password)

    if not username or not password:
        return
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    connection.commit()

    return render_template("success.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
     
    return render_template("success.html")