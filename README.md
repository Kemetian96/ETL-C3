# C3 Automático

Automatiza la descarga de reportes de C3, procesa la información con un flujo ETL y genera un Excel final consolidado.

## Qué hace

1. Inicia sesión en C3 con credenciales de entorno.
2. Descarga reportes de llamadas y encuestas en un rango de fechas automático (hoy - 5 días a hoy).
3. Extrae y transforma los archivos descargados.
4. Genera el archivo final `Llamadas_General_V3.xlsx`.

## Estructura actual

```text
.
├─ main.py
├─ config/
│  ├─ credentials.py
│  ├─ endpoints.py
│  └─ paths.py
├─ session/
│  └─ c3_session.py
├─ downloader/
│  └─ reports_downloader.py
├─ etl/
│  ├─ extract.py
│  ├─ transform.py
│  └─ load.py
└─ requirements.txt
```

## Requisitos

- Python 3.10+ (recomendado)
- Acceso de red a `https://cc.platanitos.c3.pe`
- Dependencias de `requirements.txt`

## Instalación

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuración de credenciales

Crea un archivo `.env` en la raíz del proyecto:

```env
C3_USERNAME=tu_usuario
C3_PASSWORD=tu_password
```

`config/credentials.py` carga estas variables con `python-dotenv` y detiene la ejecución si faltan.

## Configuración de rutas

En `config/paths.py` está definido `BASE_DIR` (actualmente una ruta de red compartida).  
Se usan estas rutas:

- `RAW_CALLS`: carpeta de llamadas descargadas
- `RAW_SURVEYS`: carpeta de encuestas descargadas
- `FINAL_DIR`: carpeta de salida final
- `FINAL_EXCEL`: Excel consolidado final

## Ejecución

```powershell
python main.py
```

## Flujo de ejecución

1. `main.py` llama a las parte y calcula la fecha.
2. `session/c3_session.py` autentica y devuelve una sesión HTTP.
3. `downloader/reports_downloader.py` descarga reportes RAW.
4. `etl/extract.py` lee los Excel descargados.
5. `etl/transform.py` normaliza y consolida datasets.
6. `etl/load.py` escribe el archivo final.

## Salida esperada

Archivo final:

- `Llamadas_General_V3.xlsx`

Archivos intermedios RAW (llamadas y encuestas) según las rutas definidas en `config/paths.py`.

## Errores comunes

- `Faltan credenciales C3...`
  - Verifica que `.env` exista y tenga `C3_USERNAME` y `C3_PASSWORD`.
- Warnings de pandas sobre `Hora` (`Could not infer format`)
  - No bloquean ejecución, pero conviene definir formato explícito para mejorar consistencia.
- Fallo de login
  - Revisa credenciales, conectividad y disponibilidad de C3.

## Notas de repositorio

- El proyecto incluye `.gitignore` para evitar subir:
  - credenciales (`.env`)
  - salidas generadas (`output/`, `*.xlsx`)
  - residuos de build/caché (`build/`, `dist/`, `__pycache__/`)
