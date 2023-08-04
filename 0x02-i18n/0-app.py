#!/usr/bin/env python3
""" A Simple Flask Route """
from flask import Flask, render_template
from app import routes

app = Flask(__name__)


@app.route
def index('/'):
    """ My index page route """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
