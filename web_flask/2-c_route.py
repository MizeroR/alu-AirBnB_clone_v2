#!/usr/bin/python3
"""Flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """prints Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns "HBNB" """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def echo(text):
    """Returns the string "C" followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000'
