import pandas as pd
import random
from datetime import datetime

puntos_df = pd.read_csv('./puntos_generados.csv')

finca_id = 367
lote_id = 1

fecha = datetime.now().strftime('%Y-%m-%d')

nuevo_df = pd.DataFrame({
    'nombre_spot': ['Spot1', 'Spot2'],  # Cambia estos nombres si lo deseas
    'lat': puntos_df['lat'],
    'lng': puntos_df['lng'],
    'lote_id': lote_id,
    'linea': random.randint(1, 10),
    'posicion': random.randint(1, 10),
    'tipo_poligono_id': random.randint(1, 10),
    'distancia': random.randint(1, 100),
    'distancia_2': random.randint(1, 100),
    'spot_id': random.randint(1, 1000),
    'nombre_planta': ['Planta1', 'Planta2'],  # Cambia estos nombres si lo deseas
    'fecha_siembra': fecha,
    'tipo_variedad_id': 5,
    'tipo_riego_id': 1
    'finca_id': finca_id
})

nuevo_df.to_csv('./spots.csv', index=False)

print("Se han generado spots y se han guardado en 'spots.csv'")