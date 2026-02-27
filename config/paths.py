from pathlib import Path

BASE_DIR = Path(
    r"G:\Unidades compartidas\SAC - ADMIN\05.- Reportes\C3 - KPIs\C3-REPORTES"
)

RAW_CALLS = BASE_DIR / "imput"
RAW_SURVEYS = BASE_DIR / "imput/encuestas"
FINAL_DIR = BASE_DIR / "output"

FINAL_EXCEL = FINAL_DIR / "Llamadas_General_V3.xlsx"

RAW_CALLS.mkdir(parents=True, exist_ok=True)
RAW_SURVEYS.mkdir(parents=True, exist_ok=True)
FINAL_DIR.mkdir(parents=True, exist_ok=True)
