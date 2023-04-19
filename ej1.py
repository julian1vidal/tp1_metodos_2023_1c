import numpy as np
from numpy.random import rand
EPS = 1.0e-4

def eliminacion_sin_pivoteo(matriz, B):
    x = [0.0] * len(matriz)
    matriz = extender_matriz(matriz, B)
    rango = range(1, len(matriz))
    for n in rango:
        modif = eliminar_sobrantes_columna(matriz, matriz[n-1], n-1)
        if modif == -1:
            print("No se puede realizar la EG sin pivoteo (division por 0)")
            return x
        matriz = modif

    vector_B = []
    for fila in matriz:
        vector_B.append(fila.pop(-1))

    size = len(matriz)
    if matriz[size-1][size-1] == 0:  # Ultima fila
        print("El sistema no tiene solucion unica (matriz singular)")
        return x

    result = resolver_ecuaciones(matriz, vector_B)
    return result

def eliminar_sobrantes_columna(matriz, fila_pivot, posicion_aii):
    es_singular = False
    posible_error = False
    elemento_divisor = fila_pivot[posicion_aii]
    if elemento_divisor == 0:
        return -1

    for n in range(posicion_aii + 1, len(matriz)):
        fila_a_modificar = matriz[n]
        elemento_modificador = fila_a_modificar[posicion_aii] / elemento_divisor
        if elemento_divisor < EPS:
            posible_error = True

        for j in range(posicion_aii, len(fila_a_modificar)):
            fila_a_modificar[j] = fila_a_modificar[j] - (elemento_modificador * fila_pivot[j])

        matriz[n] = fila_a_modificar

    if posible_error:
        print("Posible acarreo de error triangulando la matriz")
    return matriz

def extender_matriz(matriz, extension):
    for n in range(len(matriz)):
        matriz[n].append(extension[n])
    return matriz

def resolver_ecuaciones(matriz, vector_B):
    posible_error = False
    x=[n for n in range(len(matriz))]
    for i in range(len(matriz) - 1, -1, -1):
        suma = 0
        for j in range(i + 1, len(matriz[i])):
            suma = suma + x[j] * matriz[i][j]
        x[i] = (vector_B[i] - suma) / matriz[i][i]
        if matriz[i][i] < EPS:
            posible_error = True

    if posible_error:
        print("Posible acarreo de error resolviendo el sistema")

    return x
