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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
