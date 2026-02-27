from datetime import date
from pathlib import Path

import requests
from config.endpoints import CALLS_EXPORT, SURVEY_EXPORT
from config.paths import RAW_CALLS, RAW_SURVEYS

REQUEST_TIMEOUT = 60


def _date_params(fecha_inicio: date, fecha_fin: date) -> dict:
    # Normaliza el rango para endpoints que esperan fecha y hora explícitas.
    return {
        "date_init": f"{fecha_inicio} 00:00",
        "date_end": f"{fecha_fin} 23:59"
    }


def _validate_excel_response(response: requests.Response, report_name: str) -> None:
    # Evita persistir respuestas inválidas (por ejemplo HTML de error/login) como .xlsx.
    content_type = (response.headers.get("Content-Type") or "").lower()
    content = response.content

    if not content:
        raise RuntimeError(f"Descarga vacia para '{report_name}'")

    # Un archivo .xlsx es un contenedor ZIP y normalmente inicia con bytes "PK".
    if not content.startswith(b"PK"):
        preview = content[:200].decode("utf-8", errors="ignore")
        raise RuntimeError(
            f"Contenido invalido para '{report_name}'. "
            f"Content-Type: '{content_type}'. Vista previa: '{preview}'"
        )


def _download_excel(
    session: requests.Session,
    url: str,
    params: dict,
    output_path: Path,
    report_name: str,
) -> None:
    # Descarga segura con timeout, validación HTTP y verificación de formato antes de escribir.
    try:
        response = session.get(url, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Error HTTP descargando '{report_name}': {exc}") from exc

    _validate_excel_response(response, report_name)
    output_path.write_bytes(response.content)

def download_all_reports(session, fecha_inicio, fecha_fin):
    # Orquesta la descarga de todas las fuentes RAW.
    download_calls(session, fecha_inicio, fecha_fin)
    download_surveys(session, fecha_inicio, fecha_fin)

def download_calls(session, fecha_inicio, fecha_fin):

    # Descarga reporte de llamadas entrantes.
    params_in = {
        "date_init": f"{fecha_inicio} 00:00",
        "date_end": f"{fecha_fin} 23:59",
        "agent": "",
        "campaign": "",
        "linkedid": "",
        "number": "",
        "disposition": "",
        "typeExport": "incoming",
        "vip_only": "false",
        "with": "FORM"
    }
    _download_excel(
        session,
        CALLS_EXPORT,
        params_in,
        RAW_CALLS / "Reporte_de_llamadas.xlsx",
        "Reporte_de_llamadas.xlsx",
    )

    # Descarga reporte de llamadas salientes.
    params_out = {
        "date_init": f"{fecha_inicio} 00:00",
        "date_end": f"{fecha_fin} 23:59",
        "agent": "",
        "campaign": "",
        "linkedid": "",
        "number": "",
        "disposition": "",
        "typeExport": "outgoing",
        "with": "FORM",
        "manual_dialer_id": 0,
        "dialer_id": 0
    }

    _download_excel(
        session,
        CALLS_EXPORT,
        params_out,
        RAW_CALLS / "Reporte_de_llamadas_salientes.xlsx",
        "Reporte_de_llamadas_salientes.xlsx",
    )

def download_surveys(session, fecha_inicio, fecha_fin):
    # Mapa nombre de encuesta -> survey_id de C3.
    surveys = {
        "platanitos": 75,
        "tiendas": 71,
        "resikla": 73,
        "chile": 74
    }

    for name, survey_id in surveys.items():
        # Parámetros de exportación de encuesta por rango de fechas.
        params = {
            **_date_params(fecha_inicio, fecha_fin),
            "survey_id": survey_id,
            "status": "ALL",
            "agent": 0,
            "agents": 0
        }

        _download_excel(
            session,
            SURVEY_EXPORT,
            params,
            RAW_SURVEYS / f"reporte_encuesta_{name}.xlsx",
            f"reporte_encuesta_{name}.xlsx",
        )
