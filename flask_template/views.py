from flask import Flask, render_template, Blueprint, redirect, url_for


my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/zeb')
def zeb():
    return render_template("zeb.html")

@my_view.route('/about')
def about():
    return render_template("about.html")

@my_view.route('/aboutme')
def about_redirect():
    return redirect(url_for("my_view.about"))

@my_view.route('/Zeb')
def zeb_redirect():
    return redirect(url_for("zeb.html"))
    