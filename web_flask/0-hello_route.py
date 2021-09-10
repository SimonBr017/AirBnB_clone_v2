#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def index():
    """display 'Hello HBNB!' """
    return "Hello HBNB!"


if __name__ == "__main__":
    web_app.run(host='0.0.0.0', port='5000')
