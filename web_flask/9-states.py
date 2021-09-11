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
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown_methode(self):
    """teardown methode"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
