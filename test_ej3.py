import pytest
import numpy as np
import ej3

"""
A = [b1   c1   0      ...    0]
    [a2   b2   c2     ...    0]
    [...  ...  ...    ...    0]
    [...  ...  ...      c(n-1)]
    [0    ...  ...    an   bn ] 

(a1 y cn) = 0
Ax = vec_d
"""


def test_identidad_3x3():
    # Genero vectores
    size = 3
    a = np.zeros(size)
    b = np.ones(size)
    c = np.zeros(size)
    x_esperado = np.random.randint(10, size=size)
    d = generar_vec_indep(a, b, c, x_esperado)

    x_vec = paso_a_lista_y_ejecuto(a, b, c, d)
    assert np.allclose(x_vec, x_esperado)


def test_identidad_10x10():
    # Genero vectores
    size = 10
    a = np.zeros(size)
    b = np.ones(size)
    c = np.zeros(size)
    x_esperado = np.random.randint(10, size=size)     # Enteros del 1 al 9 incl.
    d = generar_vec_indep(a, b, c, x_esperado)

    x_vec = paso_a_lista_y_ejecuto(a, b, c, d)
    assert np.allclose(x_vec, x_esperado)





# Convierto vectores a lista, ejecuto nuestra funcion
# y convierto a np.array para testear
def paso_a_lista_y_ejecuto(a, b, c, d):
    convertir_a_lista(a, b, c, d)
    x_vec = ej3.resolver_tridiagonal(a, b, c, d)
    return np.array(x_vec)


# Junto los vectores a, b y c en una matriz y multiplico por x
# Devuelve el vector independiente d.
def generar_vec_indep(a_ini, b_ini, c_ini, x_ini):
    size = c_ini.size
    diag_sup = np.diagflat(c_ini[:size - 1], 1)  # no cuento a cn
    diag_principal = np.diag(b_ini)
    diag_inf = np.diagflat(a_ini[1:], -1)  # no cuento a a1
    A_mat = diag_sup + diag_principal + diag_inf
    d_ini = np.matmul(A_mat, x_ini)
    return d_ini


# Convierto vectores de numpy a listas.
def convertir_a_lista(a, b, c, d):
    a = a.tolist()
    b = b.tolist()
    c = c.tolist()
    d = d.tolist()
