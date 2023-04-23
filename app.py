from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    return render_template("success.html")