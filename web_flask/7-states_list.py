#!/usr/bin/python3
"""
simple Flask web app
"""

from flask import Flask, render_template, redirect, url_for
from models import storage
from models.state import State
from werkzeug.exceptions import NotFound

app = Flask(__name__)

objs = storage.all()


@app.teardown_appcontext
def cleanup(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ returns page with list of states """
    states = []
    for obj_id, obj in objs.items():
        if obj_id.split('.')[0] == 'State':
            states.append(obj)

    print(len(states))
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
