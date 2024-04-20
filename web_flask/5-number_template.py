#!/usr/bin/python3
"""
simple Flask web app
"""

from flask import Flask, render_template, redirect, url_for
from werkzeug.exceptions import NotFound

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


app.register_error_handler(404, page_not_found)


@app.route('/', strict_slashes=False)
def index():
    """ returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """ returns C <text> """
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
def python():
    """ returns default text if main route has invalid n """
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """  returns Python <text> """
    if not text:
        return redirect(url_for('python'))
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """ returns <n> is number """
    try:
        n = int(n)
        return '{} is a number'.format(n)
    except ValueError:
        raise NotFound()


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """ returns page with <n> if is number """
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except ValueError:
        raise NotFound()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
