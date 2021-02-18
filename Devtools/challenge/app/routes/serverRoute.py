from flask import Blueprint, redirect, request, render_template, url_for
import io

from app.controllers.server import serverController

bp = Blueprint('serverRoute', __name__)

@bp.route("/", methods=["GET"])
def home():
    return render_template("server/home.html")

@bp.route("/server", methods=["GET"])
def servers():
    servers = serverController()
    servers = servers.find_all()
    return render_template("server/servers.html", servers=servers)

@bp.route("/server/new", methods=["GET", "POST"])
def new_server():
    if request.method == "POST":
        server = serverController()
        server.insert_server(request.form)
    return "Server created"

@bp.route("/server/edit/<id>", methods=["GET", "POST"])
def update_server(id):
    if request.method == "POST":
        server = serverController()
        server.update_server(servers, request.form)
    return "server updated"

@bp.route("/server/delete/<id>", methods=["GET", "POST"])
def remove_server(id):
    if request.method == "POST":
        server = serverController()
        server.delete_server(id)
    return "Server deleted"