from flask import Blueprint, redirect, request, render_template, url_for
import io

from app.controllers.alert import alertController

bp = Blueprint('alertRoute', __name__)


@bp.route("/alert", methods=["GET"])
def alerts():
    alert = alertController()
    alert = alert.find_all(alert)
    return render_template("server/alerts.html", alert=alert)

@bp.route("/alert/new", methods=["GET", "POST"])
def new_alert():
    if request.method == "POST":
        alert = alertController()
        alert.insert_alert(request.form)
    return "Alert created"

@bp.route("/alert/edit/<alert>", methods=["GET", "POST"])
def update_alert(alert):
    if request.method == "POST":
        alert = alertController()
        alert.update_alert(alerts, request.form)
    return "Alert updated"

@bp.route("/alert/delete/<alert>", methods=["GET", "POST"])
def remove_alert(alert):
    if request.method == "POST":
        alert = alertController()
        alert.delete_alert(alert)
    return "Alert deleted"