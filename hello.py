from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>HI DAVE</p>"

# @app.route("/<bruv>")
# def index(bruv):
#     return f"<p>Hello from index {bruv}</p>"

@app.route("/add/<num1>/<num2>")
def add(num1, num2):
    return str(int(num1)+int(num2))

@app.route("/subtract/<num1>/<num2>")
def subtract(num1, num2):
    return str(int(num1)-int(num2))