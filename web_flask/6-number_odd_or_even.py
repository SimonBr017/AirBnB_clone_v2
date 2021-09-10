#!/usr/bin/python3
"""script that starts a Flask web application
/: dysplay 'Hello HBNB!'
/hbnb: dysplay 'HBNB' """
from flask import Flask
from flask import render_template

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


@web_app.route('/number/<int:n>', strict_slashes=False)
def is_it_a_number(n):
    """display n only if is an int"""
    return '{} is a number'.format(n)


@web_app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display HTML page only if n is an int"""
    return render_template('5-number.html', number=n)


@web_app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """display HTML page only if n is an
    with variable body content"""
    if n % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    return render_template('6-number_odd_or_even.html',
                           number=n, odd_or_even=odd_or_even)


if __name__ == "__main__":
    web_app.run(host='0.0.0.0', port='5000')
