def multiplicacion_matrices(matrices):
    """
    Esta función multiplica múltiples matrices.
    Validando las condiciones de multiplicación de matrices, (el numero de columnas de la matriz debe ser igual al numero de filas de la siguiente)
    en otras palabras el numero de elementos de cada arreglo de la primera matriz debe ser igual numero de arreglos de la matriz con la que se este multiplicando.
    """
    # Verificar si es posible multiplicar las matrices
    for i in range(len(matrices) - 1):
        if len(matrices[i][0]) != len(matrices[i + 1]):
            return "Las matrices no cumplen las condiciones"

    # Realizar la multiplicación de las matrices
    resultante = matrices[0]
    for i in range(1, len(matrices)):
        resultante = producto_matrices(resultante, matrices[i])

    return resultante


def producto_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    cols_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    cols_matriz2 = len(matriz2[0])

    if cols_matriz1 != filas_matriz2:
        raise ValueError("Las matrices no cumplen las condiciones")

    resultado = [[0] * cols_matriz2 for _ in range(filas_matriz1)]

    for i in range(filas_matriz1):
        for j in range(cols_matriz2):
            for k in range(cols_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado


if __name__ == "__main__":
    n_matrices = int(input("Ingrese el número de matrices que desea multiplicar: "))
    matrices = []
    
    # Recorremos las matrices 
    for i in range(n_matrices):
        filas = int(input(f"Ingrese el número de filas de la matriz {i+1}: "))
        cols = int(input(f"Ingrese el número de columnas de la matriz {i+1}: "))

        matriz = []
        # Recorremos las filas de la matriz
        for j in range(filas):
            fila = []
            for k in range(cols):
                valor = int(input(f"Ingrese el valor para [{j+1}], [{k+1}] de la matriz {i+1}: "))
                fila.append(valor)
            matriz.append(fila)

        matrices.append(matriz)

    try:
        matriz_resultante = multiplicacion_matrices(matrices)
        if matriz_resultante == "Las matrices no cumplen las condiciones":
            raise ValueError("Las matrices no cumplen las condiciones")
        print("Matriz resultante:")
        for fila in matriz_resultante:
            print(fila)
    except ValueError as e:
        print(e)
