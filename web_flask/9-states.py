#!/usr/bin/python3
"""
simple Flask web app
"""

from flask import Flask, render_template, redirect, url_for
from models import storage
from models.state import State
from werkzeug.exceptions import NotFound

app = Flask(__name__)

objs = storage.all(State)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_1.html'), 404


app.register_error_handler(404, page_not_found)


@app.teardown_appcontext
def cleanup(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ returns page with list of states """
    states = []
    for obj_id, obj in objs.items():
        states.append(obj)

    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ returns page with list of states """
    states = []
    try:
        states.append(objs['State.{}'.format(id)])
    except KeyError:
        raise NotFound()

    return render_template('9-states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
