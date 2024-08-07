#!/usr/bin/python3
"""
this script start a flask web app that listens on port 0.0.0.0
port 5000
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    this function returns the following string when the route /
    is accessed
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """
    this function returns "HBNB" when routed to /hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    this function displays "C" followed by the value of <text>
    when routed to /c/<text>
    """
    return "C " + text.replace("_", " ")


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    this function displays "Python " followed by the value of <text>
    when routed to /python/<text>
    """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    this function displays n is a number
    only if n is an int when routed to
    /number/n
    """
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    this function display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_oddeven(n):
    """
    this function displays a different html page if n is int
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
