from flask import Blueprint, render_template, request, redirect, url_for, flash


stats = Blueprint("stats", __name__)


@stats.route("/stats")
def stats(): 

    return render_template("stats.html")