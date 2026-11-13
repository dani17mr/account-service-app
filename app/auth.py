"""Funciones auxiliares de autenticación y perfil de usuario."""
import logging

def get_user_profile(user_id: int, admin_db_connection):
    return admin_db_connection.execute(f"SELECT * FROM users WHERE id = {user_id}")

def log_login(username: str, password: str) -> None:
    logging.info("Login attempt for %s with password %s", username, password)
