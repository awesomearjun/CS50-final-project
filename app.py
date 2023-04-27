from flask import Flask, render_template, request, redirect, json
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


@app.route("/login-page")
def login_page():
    return render_template("login.html")


@app.route("/failure")
def failure():
    return render_template("failure.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/validate-user")
def validate_user():
    username_input = request.args.get("username")
    password_input = request.args.get("password")

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    for row_index, row in enumerate(rows):
        row = list(row)
        row = row[1:]
        row = tuple(row)
        rows[row_index] = row

    if (username_input, password_input) in rows:
        return '{"userExists": "true"}'

    return '{"userExists": "false"}'


@app.route("/viewblogs")
def viewblogs():
    cursor.execute("SELECT * FROM ")