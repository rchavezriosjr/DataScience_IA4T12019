"""Ejercicio 11"""

import pandas as pd

datos_est = pd.read_csv('ejemplo_estudiantes.csv', delimiter = ';', decimal = ",", 
                        header = 0, index_col = 0)
datos_est
def cantidadvalores(datos_est):
    tam_filas, tam_columnas = datos_est.shape
    cantidad = 0
    for indice_fila in range(tam_filas):
        for indice_columna in range(tam_columnas):
            if ((datos_est.iloc[indice_fila, indice_columna])%3) == 0:
                cantidad = cantidad +1
                
    return cantidad
                
        
cantidadvalores(datos_est)