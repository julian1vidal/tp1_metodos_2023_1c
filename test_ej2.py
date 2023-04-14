import pytest
import numpy as np
import ej2


# Defino lista de tamaños de matriz a probar
tamaños = [3, 5, 10, 100]

# Repetir las pruebas n veces
num_repeticiones = 100


def test_eg_con_pivoteo():      # Testeo pivoteando y sin pivotear
    for tam in tamaños:
        for i in range(num_repeticiones):
            sin_pivoteo(tam)
            con_pivoteo(tam)

def sin_pivoteo(tam):
    # Generar matriz A de rango completo de tamaño tam
    A = generar_mat_rango_completo(tam)

    x_ini = np.random.rand(tam)
    d = np.dot(A, x_ini)

    x_vec = paso_a_lista_y_ejecuto(A, d)  # Devuelve un numpy array para testear con np.allclose
    assert np.allclose(x_vec, x_ini)

def con_pivoteo(tam):
    A = generar_mat_rango_completo(tam)
    np.fill_diagonal(A, 0)      # pongo 0s en la diag. para obligar a pivotear

    x_ini = np.random.rand(tam)
    d = np.dot(A, x_ini)

    x_vec = paso_a_lista_y_ejecuto(A, d)
    assert np.allclose(x_vec, x_ini)


# Genero matriz de rango completo para que haya solucion unica.
def generar_mat_rango_completo(n):
    A = np.random.rand(n, n)
    while np.linalg.matrix_rank(A) < n:
        A = np.random.rand(n, n)
    return A


# Convierto vectores a lista, ejecuto nuestra funcion
# y convierto a np.array para testear
def paso_a_lista_y_ejecuto(A, d):
    A = A.tolist()
    d = d.tolist()
    x_vec = ej2.eliminacion_con_pivoteo(A, d)
    return np.array(x_vec)