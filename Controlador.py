import pandas as pd
import Modelo
import logging
import numpy as np
import unidecode

def limpiar_transformar_espacio_publico(df):
    df.rename(columns={'espacio_en_m2': 'codigo_upz', 'numero_habitantes': 'espacio_en_m2'}, inplace=True)
    df['tipo_de_espacio'] = df['tipo_de_espacio'].astype(str)
    df['codigo_upz'] = df['codigo_upz'].astype(str)
    df['espacio_en_m2'] = pd.to_numeric(df['espacio_en_m2'], errors='coerce').fillna(0).astype(int)
    df['poblacion'] = pd.to_numeric(df['poblacion'], errors='coerce').fillna(0).astype(int)
    return df

def limpiar_transformar_inmuebles_bogota(df):
    df['Tipo'] = df['Tipo'].astype(str)
    df['Descripcion'] = df['Descripcion'].astype(str)
    df['Barrio'] = df['Barrio'].astype(str)
    df['UPZ'] = df['UPZ'].astype(str)
    df['UPZ'] = df['UPZ'].apply(unidecode.unidecode)  # Normalizar para quitar acentos
    df['Habitaciones'] = pd.to_numeric(df['Habitaciones'], errors='coerce').fillna(0).astype(int)
    df['Baños'] = pd.to_numeric(df['Baños'], errors='coerce').fillna(0).astype(int)
    df['Área'] = pd.to_numeric(df['Área'], errors='coerce').fillna(0).astype(int)
    df['Valor'] = df['Valor'].replace({'\$': '', '\.': ''}, regex=True)
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce').fillna(0).astype(int)
    return df

def limpiar_transformar_inmuebles_venta(df):
    #pendiente analisis
    return df

def limpiar_transformar_plan_estrategico(df):
    # Pendiente analisis
    return df

def limpiar_transformar_mercado_inmobiliario(df):
    # Pendiente analisis
    return df

def limpiar_transformar_georeferencia_localidad(df):
    if 'results' in df.columns:
        # Lista para almacenar los datos de georeferencia
        localidades_data = []

        # Extraer y añadir los datos a la lista localidades_data
        for resultado in df['results']:
            if isinstance(resultado, dict):
                localidad = {
                    'localidad': unidecode.unidecode(resultado.get('localidad', '')),
                    'longitud': resultado.get('longitud', 0),
                    'latitud': resultado.get('latitud', 0)
                }
                localidades_data.append(localidad)

        # DataFrame a partir de la lista de diccionarios
        df_localidades = pd.DataFrame(localidades_data)
        return df_localidades
    else:
        return df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    try:
        df_espacio_publico = Modelo.obtener_datos_api(Modelo.url_espacio_publico)
        df_inmuebles_bogota = pd.read_csv('./data/inmuebles_bogota.csv')  # Debe existir el archivo en la ruta
        df_inmuebles_venta = Modelo.obtener_datos_api(Modelo.url_inmuebles_venta)
        df_plan_estrategico = Modelo.obtener_datos_api(Modelo.url_plan_estrategico)
        df_mercado_inmobiliario = Modelo.obtener_datos_api(Modelo.url_mercado_inmobiliario)
        df_georeferencia_localidad = Modelo.obtener_datos_api(Modelo.url_georeferencia_localidad)

        df_espacio_publico_limpio = limpiar_transformar_espacio_publico(df_espacio_publico)
        df_inmuebles_bogota_limpio = limpiar_transformar_inmuebles_bogota(df_inmuebles_bogota)
        df_inmuebles_venta_limpio = limpiar_transformar_inmuebles_venta(df_inmuebles_venta)
        df_plan_estrategico_limpio = limpiar_transformar_plan_estrategico(df_plan_estrategico)
        df_mercado_inmobiliario_limpio = limpiar_transformar_mercado_inmobiliario(df_mercado_inmobiliario)
        df_georeferencia_localidad_limpio = limpiar_transformar_georeferencia_localidad(df_georeferencia_localidad)

        print(df_inmuebles_bogota_limpio['Valor'].unique())
        print(df_inmuebles_bogota_limpio['Valor'].describe())
        print("Datos originales de espacio_en_m2:")
        print(df_inmuebles_bogota['Valor'].head())

    except Exception as e:
        logging.error("Error en la carga y limpieza de datos", exc_info=True)