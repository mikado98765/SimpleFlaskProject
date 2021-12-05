from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>FUCK YOU DAVE</p>"

def index():
    return "<p>Hello from index</p>"