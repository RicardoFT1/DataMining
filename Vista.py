#Permite visualizar algunar relaciones de datos
#Solo para graficar los datos antes de la analitica, demostrando que no hay informacion que muestre un resultado optimo sin realizar una exploracion y analisis de los datos.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Controlador import (
    limpiar_transformar_espacio_publico,
    limpiar_transformar_inmuebles_bogota,
    limpiar_transformar_inmuebles_venta,
    limpiar_transformar_plan_estrategico,
    limpiar_transformar_mercado_inmobiliario
)
import Modelo

def visualizar_espacio_publico(df):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='tipo_de_espacio', y='numero_habitantes', data=df)
    plt.title('Espacio Público Verde por Habitante')
    plt.xlabel('Tipo de Espacio')
    plt.ylabel('Espacio en m² por Habitante')
    plt.xticks(rotation=90)
    plt.show()

def visualizar_inmuebles_bogota(df):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='Área', y='Valor', hue='Tipo', data=df)
    plt.title('Relación Área-Valor de Inmuebles en Bogotá')
    plt.xlabel('Área (m²)')
    plt.ylabel('Valor (COP)')
    plt.show()

def visualizar_inmuebles_venta(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(df['precio'], kde=True)
    plt.title('Distribución de Precios de Inmuebles Disponibles para la Venta')
    plt.xlabel('Precio')
    plt.ylabel('Frecuencia')
    plt.show()

def analizar_datos():
    df_espacio_publico = Modelo.obtener_datos_api(Modelo.url_espacio_publico)
    df_inmuebles_bogota = pd.read_csv('./data/inmuebles_bogota.csv')
    df_inmuebles_venta = Modelo.obtener_datos_api(Modelo.url_inmuebles_venta)
    df_plan_estrategico = Modelo.obtener_datos_api(Modelo.url_plan_estrategico)
    df_mercado_inmobiliario = Modelo.obtener_datos_api(Modelo.url_mercado_inmobiliario)
    
    df_espacio_publico_limpio = limpiar_transformar_espacio_publico(df_espacio_publico)
    df_inmuebles_bogota_limpio = limpiar_transformar_inmuebles_bogota(df_inmuebles_bogota)
    df_inmuebles_venta_limpio = limpiar_transformar_inmuebles_venta(df_inmuebles_venta)
    df_plan_estrategico_limpio = limpiar_transformar_plan_estrategico(df_plan_estrategico)
    df_mercado_inmobiliario_limpio = limpiar_transformar_mercado_inmobiliario(df_mercado_inmobiliario)
    
    visualizar_espacio_publico(df_espacio_publico_limpio)
    visualizar_inmuebles_bogota(df_inmuebles_bogota_limpio)
    visualizar_inmuebles_venta(df_inmuebles_venta_limpio)

if __name__ == "__main__":
    analizar_datos()