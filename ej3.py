import numpy as np
EPS = 1.0e-4


# En este caso le paso la matriz ya triangulada con la funcion triangular.
def resolver_ya_triangulada(a_vec, b_vec, c_vec, d_vec):    # a_vec son los multiplicadores
    modificar_indep(a_vec, d_vec)
    return resolver(b_vec, c_vec, d_vec)


def triangular(a_vec, b_vec, c_vec):  # Triangulo A (sin modificar el vector indep.)
    posible_error = False
    size = len(b_vec)
    for i in range(0, size - 1):
        try:
            a_vec[i + 1] /= b_vec[i]  # En a_vec[i+1] guardo los mi+1 (ya que a termina siendo el vector nulo)
        except ZeroDivisionError:
            print("Error: division por cero")
            raise SystemExit
        if b_vec[i] < EPS:
            posible_error = True
        b_vec[i + 1] -= c_vec[i] * a_vec[i + 1]
    if posible_error:
        print("Posible acarreo de error triangulando la matriz")
        
        
def modificar_indep(a_vec, d_vec):  # Modifico d con los mi guardados en el vector a
    size = len(a_vec)
    for i in range(0, size - 1):
        d_vec[i + 1] -= d_vec[i] * a_vec[i + 1]


def resolver_tridiagonal(a_vec, b_vec, c_vec, d_vec):   # Triangula en todos los casos
    triangular_con_indep(a_vec, b_vec, c_vec, d_vec)
    return resolver(b_vec, c_vec, d_vec)


def triangular_con_indep(a_vec, b_vec, c_vec, d_vec):  # Triangulo A (modificando el vector indep.)
    posible_error = False
    size = len(b_vec)
    for i in range(0, size - 1):
        try:
            a_vec[i + 1] /= b_vec[i]  # En a_vec[i+1] guardo los mi+1 (ya que a termina siendo el vector nulo)
        except ZeroDivisionError:
            print("Error: division por cero")
            raise SystemExit
        if b_vec[i] < EPS:
            posible_error = True
        b_vec[i + 1] -= c_vec[i] * a_vec[i + 1]
        d_vec[i + 1] -= d_vec[i] * a_vec[i + 1]     # a_vec = mi
    if posible_error:
        print("Posible acarreo de error triangulando la matriz")


def resolver(b_vec, c_vec, d_vec):  # Devuelve el vector solucion
    posible_error = False
    size = len(b_vec)
    x_vec = [0] * size      # Creo vector sol.
    try:
        x_vec[size - 1] = d_vec[size - 1] / b_vec[size - 1]  # Resuelvo primer caso (bn * xn = dn)
    except ZeroDivisionError:
        print("Error: division por cero")
        raise SystemExit
    if b_vec[size - 1] < EPS:
        posible_error = True

    for i in range(size - 2, -1, -1):  # Resuelvo para el resto de la matriz
        termino_2 = c_vec[i] * x_vec[i + 1]
        try:
            x_vec[i] = (d_vec[i] - termino_2) / b_vec[i]
        except ZeroDivisionError:
            print("Error: division por cero")
            raise SystemExit
        if b_vec[i] < EPS:
            posible_error = True

    if posible_error:
        print("Posible acarreo de error resolviendo el sistema")

    return x_vec
