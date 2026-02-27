from datetime import date
from config.endpoints import CALLS_EXPORT, SURVEY_EXPORT
from config.paths import RAW_CALLS, RAW_SURVEYS

def _date_params(fecha_inicio: date, fecha_fin: date) -> dict:
    return {
        "date_init": f"{fecha_inicio} 00:00",
        "date_end": f"{fecha_fin} 23:59"
    }

def download_all_reports(session, fecha_inicio, fecha_fin):
    download_calls(session, fecha_inicio, fecha_fin)
    download_surveys(session, fecha_inicio, fecha_fin)

def download_calls(session, fecha_inicio, fecha_fin):

    # Entrantes
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
    r = session.get(CALLS_EXPORT, params=params_in)
    (RAW_CALLS / "Reporte_de_llamadas.xlsx").write_bytes(r.content)

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

    r = session.get(CALLS_EXPORT, params=params_out)
    (RAW_CALLS / "Reporte_de_llamadas_salientes.xlsx").write_bytes(r.content)

def download_surveys(session, fecha_inicio, fecha_fin):
    surveys = {
        "platanitos": 75,
        "tiendas": 71,
        "resikla": 73,
        "chile": 74
    }

    for name, survey_id in surveys.items():
        params = {
            **_date_params(fecha_inicio, fecha_fin),
            "survey_id": survey_id,
            "status": "ALL",
            "agent": 0,
            "agents": 0
        }

        r = session.get(SURVEY_EXPORT, params=params)
        (RAW_SURVEYS / f"reporte_encuesta_{name}.xlsx").write_bytes(r.content)
