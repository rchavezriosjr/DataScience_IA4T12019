import pandas
def main():
    info = pandas.read_csv('ejemplo_estudiantes.csv', delimiter = ';', decimal = ",", header = 0, index_col = 0)
    rows_size, column_size = info.shape
    cont = 0
    for i in range(rows_size):
        for j in range(column_size):
            if ((info.iloc[i, j])%3) == 0:
                cont = cont +1 
    return cont

if __name__== "__main__":
    main()