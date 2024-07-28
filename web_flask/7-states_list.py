#!/usr/bin/python3
"""
flask application that displays a list of states from the db
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """
    closes the current SQLAlchemy session.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    display states list
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
