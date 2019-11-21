"""Ejercicio 12  """
import pandas as pd
datos_est = pd.read_csv('C:\ejemplo_estudiantes.csv', delimiter = ';', decimal = ",", 
                        header = 0, index_col = 0)
datos_est
def cantidadvalores(datos_est, a,b):
    suma = 0
    cov1 = datos_est.iloc[:, a]
    cov2 = datos_est.iloc[:, b]
        
    covarianza = df.cov()[cov1.name][cov2.name]
    columnas = (cov1.name +" y " +cov2.name)
    correlacion = cov1.corr(cov2)
    
    dic= { "Columnas analizadas: ":columnas, "Covarianza: ":covarianza, "Correlación: ": correlacion }
    
    return dic

cantidadvalores(datos_est,0,1)