from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def logIn():
    return "<p>Login</p>"


@auth.route('/logout')
def logOut():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def signUp():
    return "<p>sign up</p>"
