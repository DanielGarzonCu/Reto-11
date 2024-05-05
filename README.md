# Reto-11
# Reto_10
# ¡PYTHON FC!

<details>
  <summary>¡ESCUDO!</summary>
  
  [![PYTHON-F-C-B.jpg](https://i.postimg.cc/1Xpw71f0/PYTHON-F-C-B.jpg)](https://postimg.cc/jnSDC96C)

</details>

# Primero
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```ruby
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
```

# Segundo
Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```ruby
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

```
# Tercero
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```ruby
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
```

# Cuarto
Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```ruby
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
```

# Quinto
Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```ruby
def sumar_fila(matriz, indice):

    # This function calculates the sum of a specific row in a given matrix
    # The matrix is represented as a list of lists, where each inner list is a row

    suma = 0
    for j in range(len(matriz[indice-1])):
        # The sum of the elements in the desired row is calculated
        # The row index is obtained from the user input
        suma += matriz[indice-1][j]
    return suma

if __name__ == '__main__':

    # This section of the code is executed when the script is run directly
    # It handles user input for the matrix dimensions and desired row to sum

    nfils = int(input("ingrese el numero de filas: "))
    ncols = int(input("ingrese el numero de columnas: "))
    matriz = []

    for i in range(nfils):
        filas = []
        for j in range(ncols):
            valor = float(input(f"ingrese el valor para [{i+1}],[{j+1}]: "))
            filas.append(valor)
        matriz.append(filas)

    for i in range(len(matriz)):
        print (matriz[i])

    indice = int(input("¿cual fila desea sumar?: "))
    resultado = sumar_fila(matriz, indice)
    print(f"la suma de la fila {indice} es: {resultado}")
```
