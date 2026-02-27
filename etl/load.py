import pandas as pd
from config.paths import FINAL_DIR, FINAL_EXCEL

SHEETS = [
    "Llamadas_Consolidado",
    "Encuestas_Consolidado",
    "Encuesta_Tiendas",
    "Encueta_Resikla",
    "Encuestas_Platanitos",
    "Encuestas_Chile",
    "SOPORTE ATC (2)",
    "PLATANITOS (2)",
    "SOPORTE ATC",
    "RESIKLA",
    "PLATANITOS CHILE",
    "PLATANITOS"
]


def create_excel_structure():
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(FINAL_EXCEL, engine="openpyxl") as writer:
        for sheet in SHEETS:
            pd.DataFrame().to_excel(writer, sheet_name=sheet, index=False)


def write_final_excel(dfs: dict):
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(FINAL_EXCEL, engine="openpyxl", mode="w") as writer:
        for sheet in SHEETS:
            dfs.get(sheet, pd.DataFrame()).to_excel(
                writer, sheet_name=sheet, index=False
            )
