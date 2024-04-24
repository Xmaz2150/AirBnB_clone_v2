#!/usr/bin/python3
"""
simple Flask web app
"""

from flask import Flask, render_template, redirect, url_for
from models import storage
from models.state import State
from models.amenity import Amenity
from werkzeug.exceptions import NotFound

app = Flask(__name__)

stateObjs = storage.all(State)
amenityObjs = storage.all(Amenity)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_1.html'), 404


app.register_error_handler(404, page_not_found)


@app.teardown_appcontext
def cleanup(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ returns page with list of states and amenities"""
    states = []
    amenities = []
    for obj_id, obj in stateObjs.items():
        states.append(obj)

    for obj_id, obj in amenityObjs.items():
        amenities.append(obj)

    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
