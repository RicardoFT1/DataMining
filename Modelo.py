import pandas as pd
import urllib.request
import json
import logging
import kaggle
import os

# Url como variables
url_mercado_inmobiliario = 'https://datosabiertos.bogota.gov.co/api/3/action/datastore_search?resource_id=bc37b0f6-4463-4052-a0f4-ab3b4ff4ce4b&limit=5&q=title:jones'
url_plan_estrategico = 'https://www.datos.gov.co/resource/gw5r-fvqd.json'
url_espacio_publico = 'https://www.datos.gov.co/resource/276j-m5rd.json'
url_inmuebles_venta = 'https://www.datos.gov.co/resource/72gd-px77.json'
kaggle_dataset = 'pablobravo73/real-estate-bogota'
url_georeferencia_localidad = 'https://bogota-laburbano.opendatasoft.com/api/explore/v2.1/catalog/datasets/georeferencia-puntual-por-localidad/records?limit=20'

def obtener_datos_api(url):
    df = pd.DataFrame()
    try:
        fileobj = urllib.request.urlopen(url)
        data = fileobj.read()
        data_str = data.decode('utf-8')
        data_json = json.loads(data_str)
        
        # Extraccion y cargue df
        new_records = pd.DataFrame(data_json)
        df = pd.concat([df, new_records], ignore_index=True)

    except Exception as e:
        logging.error("Error al obtener datos de la API", exc_info=True)

    return df

def descargar_datos_kaggle(path):
    try:
        os.environ['KAGGLE_CONFIG_DIR'] = "C:\\Users\\RTOFA2\\.kaggle\\"
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(kaggle_dataset, path=path, unzip=True)
    except Exception as e:
        logging.error("Error al descargar datos de Kaggle", exc_info=True)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    df_mercado_inmobiliario = obtener_datos_api(url_mercado_inmobiliario)
    print(df_mercado_inmobiliario)
    
    df_plan_estrategico = obtener_datos_api(url_plan_estrategico)
    print(df_plan_estrategico)
    
    df_espacio_publico = obtener_datos_api(url_espacio_publico)
    print(df_espacio_publico)
    
    df_inmuebles_venta = obtener_datos_api(url_inmuebles_venta)
    print(df_inmuebles_venta)

    df_georeferencia_localidad = obtener_datos_api(url_georeferencia_localidad)
    print(df_georeferencia_localidad)
    
    # Descargando DataSet de Kaggle
    descargar_datos_kaggle('./data')
    df_kaggle = pd.read_csv('./data/inmuebles_bogota.csv')
    print(df_kaggle)