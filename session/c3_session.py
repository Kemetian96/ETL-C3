import requests
from config.credentials import C3_USERNAME, C3_PASSWORD, validate_credentials
from config.endpoints import LOGIN_PAGE, LOGIN_POST

def create_c3_session() -> requests.Session:
    validate_credentials()
    session = requests.Session()

    login_page = session.get(LOGIN_PAGE)
    token = None

    for field in login_page.text.split("name=\"_token\""):
        if "value=\"" in field:
            token = field.split("value=\"")[1].split("\"")[0]
            break

    if not token:
        raise RuntimeError("No se pudo obtener token CSRF")

    payload = {
        "_token": token,
        "username": C3_USERNAME,
        "password": C3_PASSWORD
    }

    response = session.post(LOGIN_POST, data=payload)

    if response.status_code != 200:
        raise RuntimeError("Login fallido")

    return session
