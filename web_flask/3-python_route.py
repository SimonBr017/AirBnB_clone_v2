#!/usr/bin/python3
"""script that starts a Flask web application
/: dysplay 'Hello HBNB!'
/hbnb: dysplay 'HBNB' """
from flask import Flask

web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def index():
    """display 'Hello HBNB!' """
    return "Hello HBNB!"


@web_app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Dysplay 'HBNB'"""
    return "HBNB"


@web_app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """display 'C' folowed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@web_app.route('/python', strict_slashes=False)
@web_app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """ display 'Python' followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    web_app.run(host='0.0.0.0', port='5000')
