from flask import Flask
from flask import request
from flask import jsonify

from markupsafe import escape

import os
import requests


app = Flask(__name__)


HOST = os.environ.get("FLASK_API_HOST", "0.0.0.0")
PORT = os.environ.get("FLASK_API_PORT", "5000")
FLASK_API_VERSION = str(os.environ.get("FLASK_API_VERSION", "/api/v1"))


@app.route("/", methods=["GET"])
def index():
    body = "<h1>This is the API home page. Try some endpoints:</h1>"
    body+="<ul>"
    body+=f"<li><a href='{FLASK_API_VERSION}/posts'>{FLASK_API_VERSION}/posts</li>"
    body+=f"<li><a href='{FLASK_API_VERSION}/comments'>{FLASK_API_VERSION}/comments</li>"
    body+=f"<li><a href='{FLASK_API_VERSION}/albums'>{FLASK_API_VERSION}/albums</li>"
    body+=f"<li><a href='{FLASK_API_VERSION}/photos'>{FLASK_API_VERSION}/photos</li>"
    body+=f"<li><a href='{FLASK_API_VERSION}/todos'>{FLASK_API_VERSION}/todos</li>"
    body+=f"<li><a href='{FLASK_API_VERSION}/users'>{FLASK_API_VERSION}/users</li>"
    body+="</ul>"
    return body


@app.route(os.path.join(FLASK_API_VERSION, "posts"), methods=["GET"])
def posts():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/posts").json())


@app.route(os.path.join(FLASK_API_VERSION, "comments"), methods=["GET"])
def comments():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/comments").json())


@app.route(os.path.join(FLASK_API_VERSION, "albums"), methods=["GET"])
def albums():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/albums").json())



@app.route(os.path.join(FLASK_API_VERSION, "photos"), methods=["GET"])
def photos():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/photos").json())



@app.route(os.path.join(FLASK_API_VERSION, "todos"), methods=["GET"])
def todos():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/todos").json())



@app.route(os.path.join(FLASK_API_VERSION, "users"), methods=["GET"])
def users():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/users").json())


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
