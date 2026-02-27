import pandas as pd
from config.paths import RAW_CALLS, RAW_SURVEYS


def extract_platanitos() -> pd.DataFrame:
    return pd.read_excel(
        RAW_CALLS / "Reporte_de_llamadas.xlsx",
        sheet_name="PLATANITOS"
    )

def extract_platanitos_chile() -> pd.DataFrame:
    return pd.read_excel(
        RAW_CALLS / "Reporte_de_llamadas.xlsx",
        sheet_name="PLATANITOS CHILE"
    )
def extract_platanitos_resikla() -> pd.DataFrame:
    return pd.read_excel(
        RAW_CALLS / "Reporte_de_llamadas.xlsx",
        sheet_name="RESIKLA"
    )
def extract_platanitos_soporte_atc() -> pd.DataFrame:
    return pd.read_excel(
        RAW_CALLS / "Reporte_de_llamadas.xlsx",
        sheet_name="SOPORTE ATC"
    )

def extract_salientes_platanitos() -> pd.DataFrame:
    return pd.read_excel(
        RAW_CALLS / "Reporte_de_llamadas_salientes.xlsx",
        sheet_name="PLATANITOS"
    )
def extract_salientes_soporte_atc() -> pd.DataFrame:
    return pd.read_excel(
        RAW_CALLS / "Reporte_de_llamadas_salientes.xlsx",
        sheet_name="SOPORTE ATC"
    )

def extrac_encuesta_chile() -> pd.DataFrame:
    return pd.read_excel(
        RAW_SURVEYS / "reporte_encuesta_chile.xlsx",
        sheet_name="Worksheet"
    )
def extrac_encuesta_platanitos() -> pd.DataFrame:
    return pd.read_excel(
        RAW_SURVEYS / "reporte_encuesta_platanitos.xlsx",
        sheet_name="Worksheet"
    )
def extrac_encuesta_resikla() -> pd.DataFrame:
    return pd.read_excel(
        RAW_SURVEYS / "reporte_encuesta_resikla.xlsx",
        sheet_name="Worksheet"
    )
def extrac_encuesta_tiendas() -> pd.DataFrame:
    return pd.read_excel(
        RAW_SURVEYS / "reporte_encuesta_tiendas.xlsx",
        sheet_name="Worksheet"
    )


def extract_all() -> dict:
    """
    Extrae todos los archivos RAW y los devuelve como DataFrames
    """
    return {
        "llamadas_entrantes_platanitos": extract_platanitos(),
        "llamadas_entrantes_chile": extract_platanitos_chile(),   
        "llamadas_entrantes_resikla": extract_platanitos_resikla(),          
        "llamadas_entrantes_soporte_atc": extract_platanitos_soporte_atc(),          
        "llamadas_salientes_platanitos": extract_salientes_platanitos(),
        "llamadas_salientes_soporte_atc": extract_salientes_soporte_atc(),
        "reporte_encuesta_chile": extrac_encuesta_chile(),
        "reporte_encuesta_platanitos": extrac_encuesta_platanitos(),
        "reporte_encuesta_resikla": extrac_encuesta_resikla(),
        "reporte_encuesta_tiendas": extrac_encuesta_tiendas()
    }
