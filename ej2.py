from numpy import linalg

################# Ejercicios

# Aplica el método de la eliminación Gausseana sobre los parámetros:
# A: Matriz cuadrada de nxn
# b: Vector columna de nx1 con términos independientes
# Retorna el vector solución x de nx1
def eliminacion_con_pivoteo(A, b):

    # Tamaño de la matriz y vector solución x
    n = len(A)
    x = [0.0] * n

    # Iteramos la matriz por filas hasta la anteúltima fila. 
    for k in range(n-1):

        # Chequeo de pivoteo: 
        #   Si el elemento en la diagonal de la final actual es igual a cero 
        #   (menor a una constante muy pequeña) => 
        #       Intercambiamos la fila actual por la de mayor pivote entre las siguientes.
        if abs(A[k][k]) < 1.0e-12:

            for i in range(k+1, n):
                if abs(A[i][k]) > abs(A[k][k]):
                    # Intercambiamos filas en A.
                    fila_A_i = A[i]
                    A[i] = A[k]
                    A[k] = fila_A_i

                    # Intercambiamos valores en b.
                    valor_b_i = b[i]
                    b[i] = b[k]
                    b[k] = valor_b_i
                    break

        # Eliminación Guasseana:
        #   La aplicamos en la fila actual luego del chequeo de pivoteo.
        for i in range(k+1,n):
            if abs(A[i][k]) < 1.0e-12 : continue

            factor = A[k][k]/A[i][k]
            for j in range(k,n):
                A[i][j] = A[k][j] - A[i][j]*factor
        #   También acarreamos las operaciones en el vector b.
            b[i] = b[k] - b[i]*factor

    # Backwards substitution:
    #   Definimos el último elemento del vector x en base a la ecuación (A_nn . x_n = b_n)
    #   Resolvemos el sistema desde abajo hacia arriba.

    x[n-1] = b[n-1] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        acum = 0
    
        for j in range(i+1, n):
            acum += A[i][j] * x[j]
            
        x[i] = (b[i] - acum) / A[i][i]

    return x


################# Ejecución

# ejemplos internet
a = [[0, 6, -1, 2, 2],
           [0, 3, 4, 1, 7],
           [5, 1, 0, 3, -1],
           [3, 1, 3, 0, 2],
           [4, 4, 1, -2, 1]]
#the b matrix constant terms of the equations 
b = [5, 7, 2, 3, 4]


print("Solución Numpy:")
print(linalg.solve(a, b))

x = eliminacion_con_pivoteo(a,b)
print("La solución del sistema es:")
# Forzamos precisión de 8 decimales
print(list(map(lambda elem:  round(elem, 8),x)))