from flask import Blueprint, render_template, url_for, redirect
from flask.views import View, MethodView


class IndexView(View):
    def __init__(self):
        self.welcome_text = "Hello!"

    def dispatch_request(self):
        return render_template("index.html")
