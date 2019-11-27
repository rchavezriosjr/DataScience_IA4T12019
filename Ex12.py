import pandas
info = pandas.read_csv('ejemplo_estudiantes.csv', delimiter = ';', decimal = ",", header = 0, index_col = 0)
def main(info, a, b):
    suma = 0
    cov1 = info.iloc[:, a]
    cov2 = info.iloc[:, b]
    covarianza = info.cov()[cov1.name][cov2.name]
    columnas = (cov1.name +" y " +cov2.name)
    correlacion = cov1.corr(cov2)
    
    dic= { "Columnas analizadas: ":columnas, "Covarianza: ":covarianza, "Correlación: ": correlacion }
    
    return dic

if __name__== "__main__":
    main(info,0,1)