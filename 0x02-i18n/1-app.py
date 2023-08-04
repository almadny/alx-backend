#!/usr/bin/env python
""" A Simple Flask Route """
from flask import Flask, render_template
from flask_babel import Babel
from app import routes

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Defines page configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route
def index('/'):
    """ My index page route """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
