import numpy as np
EPS = 1.0e-4


# En este caso le paso la matriz ya triangulada con la funcion triangular.
def resolver_ya_triangulada(a_vec, b_vec, c_vec, d_vec):    # a_vec son los multiplicadores
    modificar_indep(a_vec, d_vec)
    return resolver(b_vec, c_vec, d_vec)


def triangular(a_vec, b_vec, c_vec):  # Triangulo A (sin modificar el vector indep.)
    es_singular = False
    posible_error = False
    size = len(b_vec)
    x = [0.0] * size

    for i in range(0, size - 1):
        if b_vec[i] == 0:
            print("Error: division por cero")
            return x

        a_vec[i + 1] /= b_vec[i]  # En a_vec[i+1] guardo los mi+1 (ya que a termina siendo el vector nulo)
        if b_vec[i] < EPS:
            posible_error = True
        b_vec[i + 1] -= c_vec[i] * a_vec[i + 1]

    if b_vec[size-1] == 0:
        print("Matriz singular sin solucion unica")     # Devuelvo array de 0s
        return x

    if posible_error:
        print("Posible acarreo de error triangulando la matriz")
        
        
def modificar_indep(a_vec, d_vec):  # Modifico d con los mi guardados en el vector a
    size = len(a_vec)
    for i in range(0, size - 1):
        d_vec[i + 1] -= d_vec[i] * a_vec[i + 1]


def resolver_tridiagonal(a_vec, b_vec, c_vec, d_vec):   # Triangula en todos los casos
    x = [0.0] * len(b_vec)
    if triangular_con_indep(a_vec, b_vec, c_vec, d_vec) == -1:  # Devuelvo vector de 0s si no se puede realizar
        return x
    return resolver(b_vec, c_vec, d_vec)


def triangular_con_indep(a_vec, b_vec, c_vec, d_vec):  # Triangulo A (modificando el vector indep.)
    posible_error = False
    size = len(b_vec)

    for i in range(0, size - 1):
        if b_vec[i] == 0:
            print("Error: division por cero")
            return -1

        a_vec[i + 1] /= b_vec[i]  # En a_vec[i+1] guardo los mi+1 (ya que a termina siendo el vector nulo)
        if b_vec[i] < EPS:
            posible_error = True
        b_vec[i + 1] -= c_vec[i] * a_vec[i + 1]
        d_vec[i + 1] -= d_vec[i] * a_vec[i + 1]     # a_vec = mi

    if b_vec[size-1] == 0:
        print("Matriz singular sin solucion unica")
        return -1

    if posible_error:
        print("Posible acarreo de error triangulando la matriz")


def resolver(b_vec, c_vec, d_vec):  # Devuelve el vector solucion
    posible_error = False
    size = len(b_vec)
    x_vec = [0] * size      # Creo vector sol.
    if b_vec[size - 1] == 0:
        print("Error: division por cero")
        return -1
    x_vec[size - 1] = d_vec[size - 1] / b_vec[size - 1]  # Resuelvo primer caso (bn * xn = dn)

    if b_vec[size - 1] < EPS:
        posible_error = True

    for i in range(size - 2, -1, -1):  # Resuelvo para el resto de la matriz
        termino_2 = c_vec[i] * x_vec[i + 1]
        if b_vec[i] == 0:
            print("Error: division por cero")
            return -1

        x_vec[i] = (d_vec[i] - termino_2) / b_vec[i]

        if b_vec[i] < EPS:
            posible_error = True

    if posible_error:
        print("Posible acarreo de error resolviendo el sistema")

    return x_vec
