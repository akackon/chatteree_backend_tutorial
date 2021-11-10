from flask import Blueprint
from flask.helpers import url_for
from flask.templating import render_template

views = Blueprint("views", __name__)


@views.route("/")
def index():
    # to redirect to the signin page first
    return "<p>Index page</p>"


@views.route("chat")
def chat():
    return "Chat"
