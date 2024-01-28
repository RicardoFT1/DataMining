import Modelo
import pandas as pd

def imprimir_nombres_columnas():
    # descarga los datos de Kaggle
    kaggle_dataset = 'pablobravo73/real-estate-bogota'
    path = './data'
    Modelo.descargar_datos_kaggle(kaggle_dataset, path)
    df_inmuebles_bogota = pd.read_csv(path + '/inmuebles_bogota.csv')

    # Creamos el diccionario de los df
    dataframes = {
        'Espacio Público': Modelo.obtener_datos_api('https://www.datos.gov.co/resource/276j-m5rd.json'),
        'Inmuebles Bogotá': df_inmuebles_bogota,
        'Inmuebles Venta': Modelo.obtener_datos_api('https://www.datos.gov.co/resource/72gd-px77.json'),
        'Plan Estratégico': Modelo.obtener_datos_api('https://www.datos.gov.co/resource/gw5r-fvqd.json'),
        'Mercado Inmobiliario': Modelo.obtener_datos_api('https://datosabiertos.bogota.gov.co/api/3/action/datastore_search?resource_id=bc37b0f6-4463-4052-a0f4-ab3b4ff4ce4b&limit=5&q=title:jones')
    }

    for nombre, df in dataframes.items():
        print(f"Nombres de columnas para el dataset '{nombre}':")
        print(df.columns)

if __name__ == "__main__":
    imprimir_nombres_columnas()
