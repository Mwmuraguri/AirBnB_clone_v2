#!/usr/bin/python3
"""Flask framework that starts a Flask web application"""
from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """returns hello hbhb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """returns the text given"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def display(text):
    """displays “Python ”, followed by the value of the text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num_display(n):
    """displays “n is a number” only"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_html(n):
    """display HTML is "n" is a number only"""
    return render_template('5-number.html', name=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
