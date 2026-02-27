import os
from dotenv import load_dotenv

load_dotenv()

C3_USERNAME = os.getenv("C3_USERNAME")
C3_PASSWORD = os.getenv("C3_PASSWORD")


def validate_credentials() -> None:
    if not C3_USERNAME or not C3_PASSWORD:
        raise RuntimeError(
            "Faltan credenciales C3. Define C3_USERNAME y C3_PASSWORD en variables de entorno o .env."
        )
