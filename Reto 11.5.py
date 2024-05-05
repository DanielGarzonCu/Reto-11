def sumar_fila(matriz, indice):
    suma = 0
    for j in range(len(matriz[indice])):
        suma += matriz[indice][j]
    return suma

if __name__ == '__main__':
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
        print(matriz[i])

    indice = int(input("¿cual fila desea sumar?: "))
    resultado = sumar_fila(matriz, indice)
    print(f"la suma de la fila {indice} es: {resultado}")