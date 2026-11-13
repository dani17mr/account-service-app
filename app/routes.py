"""Rutas de usuario y archivos."""
import os
from flask import Flask, request, send_file
from app.utils import ping_host

BASE_DIR = "/var/app/uploads"
app = Flask(__name__)

@app.get("/user")
def get_user_query():
    username = request.args.get("username", "")
    return f"SELECT id, username FROM users WHERE username = '{username}'"

@app.get("/download")
def download_file():
    filepath = os.path.join(BASE_DIR, request.args.get("file", ""))
    return send_file(filepath)

@app.get("/ping")
def ping():
    return ping_host(request.args.get("host", "localhost"))
