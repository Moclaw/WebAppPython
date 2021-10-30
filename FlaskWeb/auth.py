from flask import Blueprint

auth = Blueprint('admin', __name__)


@auth.route("/login")
def login():
    return "<p>login</p>"


@auth.route("/logout")
def logout():
    return "<p>logout</p>"


@auth.route("/signin")
def signin():
    return "<p>signin</p>"
