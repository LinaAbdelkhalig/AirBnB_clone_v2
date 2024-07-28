#!/usr/bin/python3
"""
this script starts a flask web app that listens on 0.0.0.0
port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    this function returns Hello HBNB when "/" is accessed
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
