def sumar_columna(matriz):

    # Esta función calcula la suma de una columna específica en una matriz dada
    # La matriz se representa como una lista de listas, donde cada lista interna es una fila

    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            # Se calcula la suma de los elementos en la columna deseada
            # El índice de la columna se obtiene a partir de la entrada del usuario
            suma += matriz[j][indice-1]  
        print(f"la suma de la columna {indice} es: {suma}")

if __name__ == '__main__':

    # Esta sección del código se ejecuta cuando el script se ejecuta directamente
    # Maneja la entrada del usuario para las dimensiones de la matriz y la columna deseada para sumar

    nfils = int(input("ingrese el numero de filas: "))
    ncols = int(input("ingrese el numero de columnas: "))
    matriz = []
    indice = int(input("¿cual columna desea sumar?: "))

    for i in range(nfils):
        filas = []
        for j in range(ncols):
            valor = float(input(f"ingrese el valor para [{i+1}],[{j+1}]: "))
            filas.append(valor)
        matriz.append(filas)

    for i in range(len(matriz)):
        print (matriz[i])

    sumar_columna(matriz)