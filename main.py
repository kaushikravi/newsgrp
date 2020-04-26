from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Basic Test for MSDS 498"
