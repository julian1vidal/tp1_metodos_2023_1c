import numpy as np

MAX_NUM = 10
SIZE = 5

# Testeo con matrices tridiagonales aleatorias (enteros del 0 al 9 incl.) y de tamano 5x5.
c_ini = np.random.randint(MAX_NUM, size=SIZE)
c_ini[SIZE-1] = 0       # cn = 0
b_ini = np.random.randint(MAX_NUM, size=SIZE)
a_ini = np.random.randint(MAX_NUM, size=SIZE)
a_ini[0] = 0            # a1 = 0

# Paso los vectores a matriz para formar a A
diag_sup = np.diagflat(c_ini[:SIZE-1], 1)   # no cuento a cn
diag_principal = np.diag(b_ini)
diag_inf = np.diagflat(a_ini[1:], -1)       # no cuento a a1
A_mat = diag_sup + diag_principal + diag_inf

# Calculo el termino independiente con un x aleatorio (con el que luego comparo)
x_ini = np.random.randint(MAX_NUM, size=SIZE)
d_ini = np.matmul(A_mat, x_ini)

"""
A = [b1   c1   0      ...    0]
    [a2   b2   c2     ...    0]
    [...  ...  ...    ...    0]
    [...  ...  ...      c(n-1)]
    [0    ...  ...    an   bn ] 

(a1 y cn) = 0
Ax = vec_d
"""

c_vec = c_ini.tolist()
b_vec = b_ini.tolist()
a_vec = a_ini.tolist()
d_vec = d_ini.tolist()
x_vec = ((np.zeros(SIZE, dtype=float)).tolist())


def resolver_tridiagonal(a_vec, b_vec, c_vec, d_vec):
    triangular(a_vec, b_vec, c_vec)
    modificar_indep(a_vec, d_vec)  # a_vec = mi
    resolver(b_vec, c_vec, d_vec)



def triangular(a_vec, b_vec, c_vec):  # Triangulo A (sin modificar el vector indep.)
    for i in range(0, SIZE - 1):
        try:
            a_vec[i + 1] /= b_vec[i]  # En a_vec[i+1] guardo los mi+1 (ya que a termina siendo el vector nulo)
        except ZeroDivisionError:
            print("Error: division por cero")
            raise SystemExit
        b_vec[i + 1] -= c_vec[i] * a_vec[i + 1]


def modificar_indep(a_vec, d_vec):  # Modifico d con los mi guardados en el vector a
    for i in range(0, SIZE - 1):
        d_vec[i + 1] -= d_vec[i] * a_vec[i + 1]


def resolver(b_vec, c_vec, d_vec):
    try:
        x_vec[SIZE - 1] = d_vec[SIZE - 1] / b_vec[SIZE - 1]  # Resuelvo primer caso (bn * xn = dn)
    except ZeroDivisionError:
        print("Error: division por cero")
        raise SystemExit

    for i in range(SIZE - 2, -1, -1):  # Resuelvo para el resto de la matriz
        termino_2 = c_vec[i] * x_vec[i + 1]
        try:
            x_vec[i] = (d_vec[i] - termino_2) / b_vec[i]
        except ZeroDivisionError:
            print("Error: division por cero")
            raise SystemExit

resolver_tridiagonal(a_vec, b_vec, c_vec, d_vec)
for i in range(SIZE):
    x_vec[i] = round(x_vec[i])
print(f"NUESTRA: {x_vec}")
print(f"esperada: {x_ini}")