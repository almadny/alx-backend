#!/usr/bin/env python3
""" A Simple Flask Route """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """ Defines page configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """ Determine the supported language """
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    if request.args.get('locale'):
        if request.args['locale'] in app.config['LANGUAGES']:
            return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Get a user from request object """
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
        if user_id in users.keys():
            return users[user_id]
    return None


@app.before_request
def before_request():
    """ find a user and sets it as a global on g.user """
    g.user = get_user()


@app.route('/')
def index():
    """ My index page route """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
