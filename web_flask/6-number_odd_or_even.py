#!/usr/bin/python3
"""flask"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pythontext(text="is cool"):
    """python text"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def isnum(n):
    """is number?"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def htmlnum(n):
    """html num"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def evenodd(n):
    """even/odd"""
    if (n % 2) == 0:
        result = "{} is even".format(n)
    else:
        result = "{} is odd".format(n)
    return render_template('6-number_odd_or_even.html', result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
