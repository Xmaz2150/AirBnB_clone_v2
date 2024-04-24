#!/usr/bin/python3
"""
simple Flask web app
"""

from flask import Flask, render_template, redirect, url_for
from models import storage
from werkzeug.exceptions import NotFound

app = Flask(__name__)

objs = storage.all('State')


@app.teardown_appcontext
def cleanup(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ returns page with list of states and cities """
    states = []
    for obj_id, obj in objs.items():
        states.append(obj)

    print(len(states))
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
