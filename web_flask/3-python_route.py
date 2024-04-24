#!/usr/bin/python3
"""
simple Flask web app
"""

from flask import Flask
app = Flask(__name__)


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
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    if not text:
        return redirect(url_for('python'))
    return 'Python {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
