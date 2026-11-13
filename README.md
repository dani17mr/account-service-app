# Demo del taller de seguridad

**Repositorio de ejercicios del taller. Los ejemplos son intencionalmente inseguros y no deben desplegarse.**

Ejemplos en Python para el taller de seguridad de software CITIS 2026. El mapa de ejercicios está en la sección 7 del [diseño del taller](2026-11-09-security-workshop-design.md).

## Preparación

Se requiere Python 3.9 o posterior y Git. Crea y activa un entorno virtual e instala las dependencias:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
```

Puedes iniciar localmente los ejemplos Flask con `flask --app app.routes run` (el ejemplo `/ping` ejecuta una utilidad del sistema). El código es intencionalmente inseguro: nunca lo expongas a una red ni lo despliegues. Las dependencias antiguas sirven para el ejercicio con `pip-audit`; los hallazgos pueden cambiar cuando se actualizan las bases de avisos. Usa la salida preparada por el instructor si la herramienta o la conexión a internet no están disponibles.

## Flujo de trabajo

1. Crea un fork del repositorio público `security-workshop-demo` del instructor en GitHub.
2. Clona tu fork: `git clone https://github.com/<tu-usuario>/security-workshop-demo`
3. Entra al directorio y crea una rama: `git checkout -b fix/<tu-nombre>`
4. Sigue los ejercicios del taller y confirma tus cambios con commits.
5. Sube la rama y abre un PR hacia la rama `main` del instructor durante el Bloque 6.

Quienes no tengan cuenta de GitHub pueden trabajar en pareja, como se indica en el diseño del taller.

## Mapa de ejercicios

| Archivo | Tema del taller | Problema intencional |
|---|---|---|
| `app/auth.py` | Bloques 2 y 5 | Privilegios excesivos en la base de datos; registro de credenciales |
| `app/routes.py` | Bloque 3 | Interpolación SQL; ruta de archivo sin restringir |
| `app/utils.py` | Bloque 3 | Comando con `shell=True` construido con datos de entrada |
| `app/config.py` | Bloque 4 | Secreto fijo, valor alternativo inseguro y hashing MD5 |
| `.gitignore` | Bloque 4 | No ignora `.env` |
| `requirements.txt` | Bloque 6 | Dependencias antiguas para `pip-audit` |

`.env.example` solo contiene valores de ejemplo. En el ejercicio de secretos, revisa las reglas de exclusión del repositorio.

## Adding a comment for a PR test