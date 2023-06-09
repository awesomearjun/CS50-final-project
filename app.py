from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect("blogs.db", check_same_thread=False)
cursor = connection.cursor()


@app.route("/")
def index():
    return redirect("/register-page")


@app.route("/register-page")
def register_page():
    return render_template("register.html")


@app.route("/username-exists")
def username_exists():
    username = request.args.get("username")

    cursor.execute("SELECT (username) FROM users")

    if (f"{username}",) in cursor.fetchall():
        return {"usernameExists": True}
    else:
        return {"usernameExists": False}


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(force=True)

    print(data["username"], data["password"])

    if not data["username"] or not data["password"]:
        return

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (data["username"], data["password"]))
    connection.commit()

    return jsonify(status=200)


@ app.route("/login-page")
def login_page():
    return render_template("login.html")


@ app.route("/validate-user")
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


@app.route("/createblogs")
def create_blog():
    return render_template("createblogs.html")


@ app.route("/viewblogs")
def view_blogs():
    cursor.execute("SELECT * FROM blogs ORDER BY id DESC")
    rows = cursor.fetchall()
    data = list()

    for row in rows:
        print(row)
        data_dict = dict()
        cursor.execute(
            "SELECT username FROM users WHERE id=(SELECT posterID FROM blogs WHERE posterID=?)", (str(row[1]),))
        data_dict["user"] = str(cursor.fetchall())
        data_dict["user"] = data_dict["user"].replace("[", "").replace("]", "").replace(
            "'", "").replace(",", "").replace("(", "").replace(")", "")
        print(data_dict["user"])
        data_dict["title"] = row[2]
        data_dict["description"] = row[3]
        data_dict["content"] = row[4]
        data.append(data_dict)

    return render_template("viewblogs.html", data=data)


@app.route("/createblog", methods=["POST"])
def createblog():
    data = request.get_json(force=True)

    print(data["username"], data["password"], data["title"],
          data["description"], data["content"])

    if not data["title"] or not data["description"] or not data["content"] or not data["username"] or not data["password"]:
        return

    cursor.execute("INSERT INTO blogs (posterId, title, description, content) VALUES ((SELECT id FROM users WHERE username=? AND password=?), ?, ?, ?)",
                   (data["username"], data["password"], data["title"], data["description"], data["content"]))
    connection.commit()

    return jsonify(status=200)
