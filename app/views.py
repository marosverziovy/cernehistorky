from flask import render_template
from app import app
import yaml

with open("cards.yaml", "r") as file:
    f = yaml.load(file)

version = 'v0.0.1'

@app.context_processor
def inject_version():
    return dict(version=version)

# errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

# pages
@app.route('/')
@app.route('/index')
@app.route('/cards')
def index():
    return render_template("listcards.html",
                           f=f)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/rules')
def rules():
    return render_template("rules.html")

@app.route('/cards/<name>')
def playcards(name):
    return render_template("playcard.html",
                           f=f,
                           page=name)