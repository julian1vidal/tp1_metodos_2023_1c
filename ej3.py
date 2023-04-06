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
c_vec = (np.array([0, 3, 1, 1, 0], dtype=float)).tolist()
b_vec = (np.array([1, 2, 1, 3, 1], dtype=float)).tolist()
a_vec = (np.array([0, 3, 4, 1, 2], dtype=float)).tolist()
d_vec = b_ini
d_vec.tolist()
x_vec = (np.zeros(5, dtype=float)).tolist()
# m_vec = np.zeros(5)

"""
# Esta funcion utiliza un vector extra para guardar los mi 
  (el vector a se convierte en vector nulo luego de la EG)

for i in range(0, SIZE-1):
    m_vec[i + 1] = a_vec[i + 1] / b_vec[i]
    a_vec[i + 1] -= b_vec[i] * m_vec[i + 1]
    b_vec[i + 1] -= c_vec[i] * m_vec[i + 1]
    # (basicamente Fj - (Fj-1 * mj)) (con j = i+1)
"""

# Triangulo A (sin modificar el vector indep. "d")
for i in range(0, SIZE-1):
    a_vec[i + 1] /= b_vec[i]  # En a_vec[i+1] guardo los mi+1 (ya que a termina siendo el vector nulo)
    b_vec[i + 1] -= c_vec[i] * a_vec[i + 1]  # Aca c_vec[i] se multiplica por el mi+1
    # (basicamente Fj - (Fj-1 * mj)) (con j = i+1)

# Modifico d con los mi guardados en el vector a
for i in range(0, SIZE-1):
    d_vec[i+1] -= d_vec[i] * a_vec[i+1]

# Resuelvo el sistema para el vector indep d
x_vec[SIZE-1] = d_vec[SIZE-1] / b_vec[SIZE-1]   # Resuelvo primer caso (bn * xn = dn)
for i in range(SIZE-2, -1, -1):                 # Resuelvo para el resto de la matriz
    termino_2 = c_vec[i] * x_vec[i + 1]
    x_vec[i] = (d_vec[i] - termino_2) / b_vec[i]


print(f"NUESTRA: {x_vec}")
print(f"esperada: {x_ini}")