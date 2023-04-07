import numpy as np

arr = np.array([[1, 0, 0, 0, 0], [3, 2, 3, 0, 0], [0, 4, 1, 1, 0], [0, 0, 1, 3, 1], [0, 0, 0, 2, 1]], dtype=float)
x_ini = np.array([1, 1, -1, 0, 5], dtype=float)
b_ini = np.matmul(arr, x_ini)

# print(np.linalg.solve(arr, b_ini))
# print(np.matmul(arr, x_ini))

"""
A = [b1   c1   0      ...    0]
    [a2   b2   c2     ...    0]
    [...  ...  ...    ...    0]
    [...  ...  ...      c(n-1)]
    [0    ...  ...    an   bn ] 

(a1 y cn) = 0
Ax = vec_d
"""

SIZE = b_ini.size
c_vec = ((np.array([0, 3, 1, 1, 0], dtype=float)).tolist())
b_vec = ((np.array([1, 2, 1, 3, 1], dtype=float)).tolist())
a_vec = ((np.array([0, 3, 4, 1, 2], dtype=float)).tolist())
d_vec = (b_ini.tolist())
x_vec = ((np.zeros(5, dtype=float)).tolist())


def resolver_tridiagonal(a_vec, b_vec, c_vec, d_vec):
    triangular(a_vec, b_vec, c_vec)
    modificar_indep(a_vec, d_vec)  # a_vec = mi
    resolver(b_vec, c_vec, d_vec)


def triangular(a_vec, b_vec, c_vec):  # Triangulo A (sin modificar el vector indep.)
    for i in range(0, SIZE - 1):
        a_vec[i + 1] /= b_vec[i]  # En a_vec[i+1] guardo los mi+1 (ya que a termina siendo el vector nulo)
        b_vec[i + 1] -= c_vec[i] * a_vec[i + 1]


def modificar_indep(a_vec, d_vec):  # Modifico d con los mi guardados en el vector a
    for i in range(0, SIZE - 1):
        d_vec[i + 1] -= d_vec[i] * a_vec[i + 1]


def resolver(b_vec, c_vec, d_vec):
    x_vec[SIZE - 1] = d_vec[SIZE - 1] / b_vec[SIZE - 1]  # Resuelvo primer caso (bn * xn = dn)
    for i in range(SIZE - 2, -1, -1):  # Resuelvo para el resto de la matriz
        termino_2 = c_vec[i] * x_vec[i + 1]
        x_vec[i] = (d_vec[i] - termino_2) / b_vec[i]


resolver_tridiagonal(a_vec, b_vec, c_vec, d_vec)
print(f"NUESTRA: {x_vec}")
print(f"esperada: {x_ini}")
