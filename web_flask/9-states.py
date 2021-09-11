#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask.templating import render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states_list():
    """list all states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>')
def show_state(id):
    """show all the cities for a given id states"""
    states = storage.all(State)
    k = 'State.{}'.format(id)
    if k in states:
        state = states[k]
    else:
        state = None
    return render_template('9-states.html', state=state, k=k)


@app.teardown_appcontext
def teardown_methode(self):
    """teardown methode"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
