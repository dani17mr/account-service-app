"""Funciones auxiliares de red."""
import subprocess

def ping_host(host: str) -> str:
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True)
    return result.stdout.decode()
