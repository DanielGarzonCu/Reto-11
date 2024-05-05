def suma_resta_matrices(matrices, operacion):
    """
    Esta funcion realiza la suma o resta de un numero n de matrices.
    Verificando si las matrices tienen las mismas dimensiones.
    """
    if len(matrices) == 0:
        return "No hay matrices para operar"
    
    filas = len(matrices[0])
    cols = len(matrices[0][0])

    # Check if all the matrices have the same dimensions
    for matriz in matrices:
        if len(matriz) != filas or len(matriz[0]) != cols:
            return "Las matrices no tienen las mismas dimensiones"

    matriz_resultante = []
    for i in range(filas):
        fila_actual = []
        for j in range(cols):
            if operacion == 1:  # Suma
                suma = sum(matriz[i][j] for matriz in matrices)
                fila_actual.append(suma)
            elif operacion == 2:  # Resta
                resta = matrices[0][i][j] - sum(matriz[i][j] for matriz in matrices[1:])
                fila_actual.append(resta)
        matriz_resultante.append(fila_actual)

    return matriz_resultante

if __name__ == "__main__":
    
    print("las matrices deben tener las mismas dimensiones")
    n_matrices = int(input("Ingrese el número de matrices que desea sumar o restar: "))
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

    operacion = int(input("Ingrese la operacion que desea realizar: 1. Suma 2. Resta: "))

    try:
        matriz_resultante = suma_resta_matrices(matrices, operacion)
        if matriz_resultante == "Las matrices no tienen las mismas dimensiones":
            raise ValueError("Las matrices no tienen las mismas dimensiones")
        print("Matriz resultante:")
        for fila in matriz_resultante:
            print(fila)
    except ValueError as e:
        print(e)
