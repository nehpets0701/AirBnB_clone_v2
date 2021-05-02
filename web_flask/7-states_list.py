#!/usr/bin/python3
"""flask storage"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """closes"""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def html_display():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
