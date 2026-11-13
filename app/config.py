"""Configuración de la aplicación y variables de entorno."""
import os
import hashlib

SECRET_KEY = "workshop-demo-secret"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///demo.db")

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()
