from flask import Flask, Blueprint, url_for, render_template

sobre_route = Blueprint('sobre_route', __name__)

@sobre_route.route("/")
def sobre():
    return render_template("sobre.html")