import flask
from flask import request, json, jsonify
import requests

app = flask.Flask(_name_)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def index():
    data = requests.get('https://randomuser.me/api')
    return data.json()

if _name_ == "_main_"
    app.run(host="0.0.0.0", debug=True, port="5000")