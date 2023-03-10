import os
import functools
from distutils.util import strtobool

import flask
from auth.authentication import is_authenticated

def login_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated(flask.session):
            return flask.redirect(
                flask.url_for("login.candid_login", next=flask.request.path)
            )
        return f(*args, **kwargs)

    return decorated_function

