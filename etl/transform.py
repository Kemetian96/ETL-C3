import pandas as pd


def transform_platanitos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    errors="coerce",
    dayfirst=True
).dt.date

    df["Hora"] = pd.to_datetime(df["Hora"], errors="coerce").dt.time
    df["Linkedid"] = df["Linkedid"].astype(str)

    df = df.drop(columns=[
        "VIP", "Averia", "Marcador manual",
        "Marcador automático", "Form. Almacenado",
        "Casilla de observaciones"
    ], errors="ignore")

    df["Agente"] = df.apply(
        lambda x: None if x["Estado"] == "Abandonada" else x["Agente"],
        axis=1
    )

    df = df.rename(columns={
        "Tipo_Consulta_Perú": "Tipo_consulta"
    })

    return df[[
        "Fecha", "Hora", "Campaña", "Agente", "Extension",
        "Nº Cliente", "Nombre cliente", "Total llamada",
        "Timbrado llamada", "Hablado llamada", "Linkedid",
        "Tipo llamada", "Estado", "Nombre audio", "Tipo_consulta"
    ]]

def transform_platanitos_chile(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "Tipo_Consulta_Chile" not in df.columns:
        df["Tipo_Consulta_Chile"] = None

    df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    errors="coerce",
    dayfirst=True
).dt.date

    df["Hora"] = pd.to_datetime(df["Hora"], errors="coerce").dt.time
    df["Linkedid"] = df["Linkedid"].astype(str)
    df = df.drop(columns=[
        "VIP", "Averia", "Marcador manual",
        "Marcador automático", "Form. Almacenado"
    ], errors="ignore")

    df["Agente"] = df.apply(
        lambda x: "" if x["Estado"] == "Abandonada" else x["Agente"],
        axis=1
    )

    df = df.rename(columns={
        "Tipo_Consulta_Chile": "Tipo_Consulta"
    })

    return df[[
        "Fecha", "Hora", "Campaña", "Agente", "Extension",
        "Nº Cliente", "Nombre cliente", "Total llamada",
        "Timbrado llamada", "Hablado llamada", "Linkedid",
        "Tipo llamada", "Estado", "Nombre audio", "Tipo_Consulta"
    ]]



def transform_resikla(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    columnas_opcionales = [
        "Casilla de observaciones",
        "Tipo_consulta",
        "Tipo_Consulta_Resikla"
    ]

    for col in columnas_opcionales:
        if col not in df.columns:
            df[col] = None


    df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce", dayfirst=True).dt.date
    df["Hora"] = pd.to_datetime(df["Hora"], errors="coerce").dt.time
    df["Linkedid"] = df["Linkedid"].astype(str)
    df = df.drop(
        columns=[
            "VIP","Averia","Marcador manual","Marcador automático",
            "Form. Almacenado","Casilla de observaciones",
        ],
        errors="ignore"
    )

    df["Agente"] = df.apply(
        lambda x: "" if x["Estado"] == "Abandonada" else x["Agente"],
        axis=1
    )

    df["Tipo_consulta"] = (
        df["Tipo_Consulta_Resikla"].fillna("") +
        df["Tipo_consulta"].fillna("")
    )

    df = df.drop(
        columns=["Tipo_Consulta_Resikla"],
        errors="ignore"
    )

    return df[[
        "Fecha","Hora","Campaña","Agente","Extension","Nº Cliente",
        "Nombre cliente","Total llamada","Timbrado llamada",
        "Hablado llamada","Linkedid","Tipo llamada","Estado",
        "Nombre audio","Tipo_consulta",
    ]]


def transform_soporte_atc(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    errors="coerce",
    dayfirst=True
).dt.date

    df["Hora"] = pd.to_datetime(df["Hora"], errors="coerce").dt.time
    df["Linkedid"] = df["Linkedid"].astype(str)
    df = df.drop(columns=[
        "VIP","Averia","Marcador manual","Marcador automático",
        "Form. Almacenado","Contacto","Contacto n2",
        "Casilla de observaciones"
    ], errors="ignore")

    df = df.rename(columns={
        "Tematicos": "Tipo_consulta"
    })

    df["Agente"] = df.apply(
        lambda x: "" if x["Estado"] == "Abandonada" else x["Agente"],
        axis=1
    )

    return df[[
        "Fecha","Hora","Campaña","Agente","Extension","Nº Cliente",
        "Nombre cliente","Total llamada","Timbrado llamada",
        "Hablado llamada","Linkedid","Tipo llamada","Estado",
        "Nombre audio","Tipo_consulta"
    ]]


def transform_platanitos_salientes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    errors="coerce",
    dayfirst=True
).dt.date

    df["Hora"] = pd.to_datetime(df["Hora"], errors="coerce").dt.time
    df["Linkedid"] = df["Linkedid"].astype(str)
    df = df.drop(columns=[
        "VIP",
        "Averia",
        "Marcador manual",
        "Marcador automático",
        "Form. Almacenado"
    ], errors="ignore")

    df["Agente"] = df.apply(
        lambda x: "" if x["Estado"] == "Abandonada" else x["Agente"],
        axis=1
    )

    df = df.rename(columns={
        "Tipo_Consulta_Perú": "Tipo_consulta"
    })
    if "Casilla de observaciones" not in df.columns:
        df["Casilla de observaciones"] = None

    return df[[
        "Fecha",
        "Hora",
        "Campaña",
        "Agente",
        "Extension",
        "Nº Cliente",
        "Nombre cliente",
        "Total llamada",
        "Timbrado llamada",
        "Hablado llamada",
        "Linkedid",
        "Tipo llamada",
        "Estado",
        "Nombre audio",
        "Casilla de observaciones",
        "Tipo_consulta"
    ]]


def transform_soporte_atc_salientes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    errors="coerce",
    dayfirst=True
).dt.date

    df["Hora"] = pd.to_datetime(df["Hora"], errors="coerce").dt.time
    df["Linkedid"] = df["Linkedid"].astype(str)
    df = df.drop(columns=[
        "VIP",
        "Averia",
        "Marcador manual",
        "Marcador automático",
        "Form. Almacenado",
        "Contacto",
        "Contacto n2",
        "Casilla de observaciones"
    ], errors="ignore")

    df["Agente"] = df.apply(
        lambda x: "" if x["Estado"] == "Abandonada" else x["Agente"],
        axis=1
    )

    df = df.rename(columns={
        "Tematicos": "Tipo_consulta"
    })

    return df[[
        "Fecha",
        "Hora",
        "Campaña",
        "Agente",
        "Extension",
        "Nº Cliente",
        "Nombre cliente",
        "Total llamada",
        "Timbrado llamada",
        "Hablado llamada",
        "Linkedid",
        "Tipo llamada",
        "Estado",
        "Nombre audio",
        "Tipo_consulta"
    ]]


# Para el caso de consolidado que es la union de varias tablas 



def transform_llamadas_consolidado(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    df = pd.concat(dfs, ignore_index=True)

    def format_time(t):
        if pd.isna(t):
            return None

        if isinstance(t, str):
            return t if t.startswith("0.") else f"0.{t}"

        return f"0.{t.hour:02d}:{t.minute:02d}:{t.second:02d}"

    df["Hora_Duracion_1"] = df["Hora"].apply(format_time)
    df["Hora_Duracion_2"] = df["Total llamada"].apply(format_time)
    df["Hora_Duracion_3"] = df["Timbrado llamada"].apply(format_time)
    df["Hora_Duracion_4"] = df["Hablado llamada"].apply(format_time)
    df["Linkedid"] = df["Linkedid"].astype(str)
    df = df.drop(columns=["Hora"])
    df = df.rename(columns={"Hora_Duracion_1": "Hora"})

    df = df.drop(columns=["Total llamada"])
    df = df.rename(columns={"Hora_Duracion_2": "Total llamada"})

    df = df.drop(columns=["Timbrado llamada"])
    df = df.rename(columns={"Hora_Duracion_3": "Timbrado llamada"})

    df = df.drop(columns=["Hablado llamada"])
    df = df.rename(columns={"Hora_Duracion_4": "Hablado llamada"})

    if "Tipo_Consulta" in df.columns:
        df = df.drop(columns=["Tipo_Consulta"])

    return df[[
        "Fecha",
        "Hora",
        "Campaña",
        "Agente",
        "Extension",
        "Nº Cliente",
        "Nombre cliente",
        "Total llamada",
        "Timbrado llamada",
        "Hablado llamada",
        "Linkedid",
        "Casilla de observaciones",
        "Tipo llamada",
        "Estado",
        "Nombre audio",
        "Tipo_consulta"
    ]]
 

def transform_encuesta_chile(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    errors="coerce",
    dayfirst=True
)


    df = df.drop(columns=["Marcador"], errors="ignore")

    df = df.rename(columns={
        "¿Cómo calificas la atención recibida?": "Encuesta-V2",
        "¿Qué tan probable es que recomiendes Platanitos Chile a tus amigos y familiares?": "Encuesta-NPS"
    })

    df["Campaña"] = df["Campaña"].astype(str)
    df["Agente"] = df["Agente"].astype(str)
    df["Extensión"] = pd.to_numeric(df["Extensión"], errors="coerce").astype("Int64")
    df["Linkedid"] = df["Linkedid"].astype(str)
    df["Número"] = df["Número"].astype(str)
    df["Estado"] = df["Estado"].astype(str)
    df["Encuesta-V2"] = df["Encuesta-V2"].astype(str)
    df["Encuesta-NPS"] = df["Encuesta-NPS"].astype(str)    
    return df[[
        "Fecha",
        "Campaña",
        "Agente",
        "Extensión",
        "Linkedid",
        "Número",
        "Estado",
        "Encuesta-V2",
        "Encuesta-NPS"
    ]]

def transform_encuesta_platanitos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    errors="coerce",
    dayfirst=True
)


    df = df.rename(columns={
        "¿Cómo calificarias la atención recibida?": "Encuesta-V2",
        "¿Qué tan probable es que recomiendes Platanito Perú a tus amigos y familiares?": "Encuesta-NPS"
    })

    df = df.drop(columns=["Marcador"], errors="ignore")

    df["Campaña"] = df["Campaña"].astype(str)
    df["Agente"] = df["Agente"].astype(str)
    df["Extensión"] = pd.to_numeric(df["Extensión"], errors="coerce").astype("Int64")
    df["Linkedid"] = df["Linkedid"].astype(str)
    df["Número"] = df["Número"].astype(str)
    df["Estado"] = df["Estado"].astype(str)
    df["Encuesta-V2"] = df["Encuesta-V2"].astype(str)
    df["Encuesta-NPS"] = df["Encuesta-NPS"].astype(str)    
    return df[[
        "Fecha",
        "Campaña",
        "Agente",
        "Extensión",
        "Linkedid",
        "Número",
        "Estado",
        "Encuesta-V2",
        "Encuesta-NPS"
    ]]

def transform_encuesta_resikla(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    errors="coerce",
    dayfirst=True
)


    df = df.rename(columns={
        "¿Cómo calificarías la atención recibida?": "Encuesta-V2",
        "¿Que tan probable es que recomiendes recikla a tus amigos y familiares?": "Encuesta-NPS"
    })

    df = df.drop(columns=["Marcador"], errors="ignore")

    df["Campaña"] = df["Campaña"].astype(str)
    df["Agente"] = df["Agente"].astype(str)
    df["Extensión"] = pd.to_numeric(df["Extensión"], errors="coerce").astype("Int64")
    df["Linkedid"] = df["Linkedid"].astype(str)
    df["Número"] = df["Número"].astype(str)
    df["Estado"] = df["Estado"].astype(str)
    df["Encuesta-V2"] = df["Encuesta-V2"].astype(str)
    df["Encuesta-NPS"] = df["Encuesta-NPS"].astype(str)    
    return df[[
        "Fecha",
        "Campaña",
        "Agente",
        "Extensión",
        "Linkedid",
        "Número",
        "Estado",
        "Encuesta-V2",
        "Encuesta-NPS"
    ]]


def transform_encuesta_tiendas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    errors="coerce",
    dayfirst=True
)


    df = df.drop(columns=["Marcador"], errors="ignore")

    df["Encuesta-NPS"] = None

    df["Campaña"] = df["Campaña"].astype(str)
    df["Agente"] = df["Agente"].astype(str)
    df["Extensión"] = pd.to_numeric(df["Extensión"], errors="coerce").astype("Int64")
    df["Linkedid"] = df["Linkedid"].astype(str)
    df["Número"] = df["Número"].astype(str)
    df["Estado"] = df["Estado"].astype(str)
    df["Encuesta-V2"] = df["Encuesta-V2"].astype(str)
    df["Encuesta-NPS"] = df["Encuesta-NPS"].astype(str)    
    return df[[
        "Fecha",
        "Campaña",
        "Agente",
        "Extensión",
        "Linkedid",
        "Número",
        "Estado",
        "Encuesta-V2"
    ]]

def transform_encuestas_consolidado(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    df = pd.concat(dfs, ignore_index=True)
    df["Linkedid"] = df["Linkedid"].astype(str)  
    return df[[
        "Fecha",
        "Campaña",
        "Agente",
        "Extensión",
        "Linkedid",
        "Número",
        "Estado",
        "Encuesta-V2",
        "Encuesta-NPS"
    ]]

def agregar_columnas_encuesta(
    df_llamadas: pd.DataFrame,
    df_encuestas: pd.DataFrame
) -> pd.DataFrame:

    df = df_llamadas.merge(
        df_encuestas[[
            "Linkedid",
            "Estado",
            "Encuesta-V2",
            "Encuesta-NPS"
        ]],
        on="Linkedid",
        how="left"
    )

    df["Estado Encuesta"] = df["Estado_y"].fillna("Sin Encuesta")
    df["Resultado Encuesta"] = df["Encuesta-V2"].fillna("Sin Encuesta")
    df["Resultado NPS"] = df["Encuesta-NPS"].fillna("Sin Encuesta")

    df = df.drop(columns=[
        "Estado_y",
        "Encuesta-V2",
        "Encuesta-NPS"
    ])

    df = df.rename(columns={
        "Estado_x": "Estado"
    })

    return df


def transform_all(raw: dict) -> dict:
    result = {}
    # ================= ENCUESTAS =================
    result["Encuestas_Platanitos"] = transform_encuesta_platanitos(raw["reporte_encuesta_platanitos"])
    result["Encuestas_Chile"] = transform_encuesta_chile(raw["reporte_encuesta_chile"])
    result["Encueta_Resikla"] = transform_encuesta_resikla(raw["reporte_encuesta_resikla"])
    result["Encuesta_Tiendas"] = transform_encuesta_tiendas(raw["reporte_encuesta_tiendas"])

    result["Encuestas_Consolidado"] = transform_encuestas_consolidado([
        result["Encuestas_Platanitos"],
        result["Encuestas_Chile"],
        result["Encueta_Resikla"],
        result["Encuesta_Tiendas"]
    ])
    # ================= LLAMADAS =================
    result["PLATANITOS"] = transform_platanitos(raw["llamadas_entrantes_platanitos"])
    result["PLATANITOS CHILE"] = transform_platanitos_chile(raw["llamadas_entrantes_chile"])
    result["RESIKLA"] = transform_resikla(raw["llamadas_entrantes_resikla"])
    result["SOPORTE ATC"] = transform_soporte_atc(raw["llamadas_entrantes_soporte_atc"])
    result["PLATANITOS (2)"] = transform_platanitos_salientes(raw["llamadas_salientes_platanitos"])
    result["SOPORTE ATC (2)"] = transform_soporte_atc_salientes(raw["llamadas_salientes_soporte_atc"])

    result["Llamadas_Consolidado"] = transform_llamadas_consolidado([
        result["PLATANITOS"],
        result["PLATANITOS CHILE"],
        result["RESIKLA"],
        result["SOPORTE ATC"],
        result["PLATANITOS (2)"],
        result["SOPORTE ATC (2)"]
    ])
    result["Llamadas_Consolidado"] = agregar_columnas_encuesta(
        result["Llamadas_Consolidado"],
        result["Encuestas_Consolidado"]
    )



    return result
