#!/usr/bin/python3
"""
this script start a flask web app that listens on port 0.0.0.0
port 5000
"""

from flask import Flask

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
    return str(n) + " is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
