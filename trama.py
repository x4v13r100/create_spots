import pandas as pd
import random
from datetime import datetime

#! Trasforma los datos de spot.py
#
puntos_df = pd.read_csv('./results/puntos_generados.csv')

finca_id = 367
lote_id = 1

fecha = datetime.now().strftime('%Y-%m-%d')

def generar_sufijo():
    return str(random.randint(1000, 9999))

def nombre_planta(posicion):
    return 'AGPL47L' + str(posicion)

nuevo_df = pd.DataFrame({
    'nombre_spot': ['AGPL47L' + generar_sufijo() for _ in range(len(puntos_df))],
    'lat': puntos_df['lat'],
    'lng': puntos_df['lng'],
    'lote_id': lote_id,
    'linea': puntos_df['linea'],
    'posicion': puntos_df['posicion'],
    'tipo_poligono_id': [1] * len(puntos_df),
    'distancia': [10] * len(puntos_df),
    'distancia_2': "",
    'spot_id': list(range(1, len(puntos_df) + 1)),
    'nombre_planta': puntos_df['posicion'].apply(nombre_planta),
    'fecha_siembra': [fecha] * len(puntos_df),
    'tipo_variedad_id': [5] * len(puntos_df),
    'tipo_riego_id': [1] * len(puntos_df),
    'finca_id': [finca_id] * len(puntos_df) 
})

nuevo_df.to_csv('./results/subir_spots.csv', index=False, sep=';')

print("Se han generado spots y se han guardado en 'spots.csv'")