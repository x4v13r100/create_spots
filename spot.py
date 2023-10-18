import geopandas as gpd
from shapely.geometry import Polygon, Point
import pandas as pd


#! Se necesita el poligono.csv
#! conseguir los datosde la tabla puntos lotes => lat,lng

# Carga el polígono desde el archivo CSV
polygon_csv = "./file/poligono.csv"
polygon_df = pd.read_csv(polygon_csv)

# Convierte las coordenadas del polígono en una lista de tuplas
polygon_coords = [(float(row['lat']), float(row['lng'])) for _, row in polygon_df.iterrows()]

# Crea un objeto Polygon a partir de las coordenadas del polígono
polygon = Polygon(polygon_coords)

distance_meters = 10.0
meters_to_degrees = 111320.0
# Distancia entre puntos (2 metros)
distance_between_points = distance_meters / meters_to_degrees  # Aproximadamente 2 metros en latitud/longitud

# Genera puntos ordenados dentro del polígono
points = []
x_min, y_min, x_max, y_max = polygon.bounds

x = x_min
line = 1
point_number = 1

while x <= x_max:
    y = y_min
    while y <= y_max:
        point = Point(x, y)
        
        if point.within(polygon):
            points.append((point, line, point_number))
            point_number += 1
            
        y += distance_between_points
    x += distance_between_points
    line += 1
    point_number = 1

# Extrae las coordenadas de los puntos en formato (latitud, longitud)
point_coords = [(point.x, point.y, line, point_number) for point, line, point_number in points]

# Crea un DataFrame de pandas para los puntos
points_df = pd.DataFrame(point_coords, columns=['lat', 'lng', 'linea', 'posicion'])

# Guarda el DataFrame en un archivo CSV
points_csv = "./results/puntos_generados.csv"
points_df.to_csv(points_csv, index=False)

print(f"Se han generado puntos ordenados con una separación de 2 metros dentro del polígono y se han guardado en '{points_csv}'.")
