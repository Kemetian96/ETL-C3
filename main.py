from datetime import date, timedelta
from etl.extract import extract_all
from etl.transform import transform_all
from etl.load import create_excel_structure, write_final_excel
from session.c3_session import create_c3_session
from downloader.reports_downloader import download_all_reports



def main():
    # Rango de fechas (automático)
    fecha_inicio = date.today() - timedelta(days=5) 
    fecha_fin = date.today()
    # Secion C3 y descarga
    session = create_c3_session()
    download_all_reports(session, fecha_inicio, fecha_fin)
    # Crea el excel
    create_excel_structure()
    # Extrae la data
    raw_data = extract_all()
    # Transforma la data
    final_data = transform_all(raw_data)
    # Caraga la data
    write_final_excel(final_data)


if __name__ == "__main__":
    main()
