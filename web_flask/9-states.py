#!/usr/bin/python3
"""cities by states"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """close"""
    storage.close()


@app.route('/states', strict_slashes=False)
def showStates():
    """show states"""
    states = storage.all(State)
    return render_template("9-states.html", states=states,
                           justStates=1)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """show state id"""
    states = storage.all(State)
    cities = storage.all(City)
    flag = 0
    state = None
    for value in states.values():
        if value.id == id:
            flag = 1
            state = value
    return render_template("9-states.html", states=states,
                           cities=cities, flag=flag,
                           state=state, justStates=0)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
