if __name__ == '__main__':
    # Ingrese el número de filas y columnas
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    # Crear una matriz vacía
    matriz = []

    # Ingrese valores para cada posición de la matriz
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor para [{i+1}], [{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)

    # Crear matriz transpuesta
    matriz_transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

    # Mostrar la matriz original y la matriz transpuesta
    print("Matriz original:")
    for fila in matriz:
        print(fila)
    print("Matriz transpuesta:")
    for fila in matriz_transpuesta:
        print(fila)