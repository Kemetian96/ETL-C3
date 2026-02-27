import re

import requests
from config.credentials import C3_USERNAME, C3_PASSWORD, validate_credentials
from config.endpoints import LOGIN_PAGE, LOGIN_POST

REQUEST_TIMEOUT = 30


def _extract_csrf_token(html: str) -> str | None:
    # Common case: <input ... name="_token" ... value="...">
    match = re.search(r'name=["\']_token["\'][^>]*value=["\']([^"\']+)["\']', html)
    if match:
        return match.group(1)

    # Fallback for different attribute order: <input ... value="..." ... name="_token" ...>
    match = re.search(r'value=["\']([^"\']+)["\'][^>]*name=["\']_token["\']', html)
    if match:
        return match.group(1)

    return None


def _looks_like_login_page(response: requests.Response) -> bool:
    url = response.url.lower()
    text = response.text.lower()

    if "/user/login" in url or "/user/signin" in url:
        return True

    login_markers = ('name="username"', 'name="password"', 'name="_token"')
    return all(marker in text for marker in login_markers)


def create_c3_session() -> requests.Session:
    validate_credentials()
    session = requests.Session()

    try:
        login_page = session.get(LOGIN_PAGE, timeout=REQUEST_TIMEOUT)
        login_page.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"No se pudo abrir la página de login: {exc}") from exc

    token = _extract_csrf_token(login_page.text)

    if not token:
        raise RuntimeError("No se pudo obtener token CSRF")

    payload = {
        "_token": token,
        "username": C3_USERNAME,
        "password": C3_PASSWORD
    }

    try:
        response = session.post(
            LOGIN_POST,
            data=payload,
            timeout=REQUEST_TIMEOUT,
            allow_redirects=True,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Error HTTP durante el login: {exc}") from exc

    if _looks_like_login_page(response):
        raise RuntimeError("Login fallido: el servidor devolvió nuevamente la pantalla de login")

    if not session.cookies:
        raise RuntimeError("Login fallido: no se generaron cookies de sesión")

    return session
