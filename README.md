# metodos_tps
# metodos_tps

Instrucciones de uso:

FUNCIONES:

ej1.py:
- eliminacion_sin_pivoteo(matriz, B): toma una matriz y un vector independiente y devuelve el vector solucion del sistema.

ej2.py:
- eliminacion_con_pivoteo(A, b): toma una matriz y un vector independiente y devuelve el vector solucion del sistema, pero realizando pivoteo parcial.

ej3.py:
- resolver_ya_triangulada(a_vec, b_vec, c_vec, d_vec): 
resuelve el sistema lineal para matrices tridiagonales con la matriz ya triangulada. Devuelve el vector resultante
Se espera que la matriz se triangule antes con la funcion triangular(a_vec, b_vec, c_vec).

- resolver_tridiagonal(a_vec, b_vec, c_vec, d_vec):
Resuelve la eliminacion gaussiana y el sistema lineal equivalente para matrices tridiagonales. Devuelve el vector resultante

ej5.py:
- armar_sistema_laplaciano(d_vec): resuelve el sistema lineal Ax = d con A siendo la matriz laplaciana. Devuelve el vector solucion.

ej6.py: 
- generar_sistema_de_difusion(alfa, u_vec, iteraciones): genera un sistema de difusion de forma iterativa en el que modifica el vector u. Devuelve un vector de vectores u que representa la difusion de ese vector.

Aclaraciones: 
- las matrices son listas de listas y los vectores son listas.
- alfa e iteraciones son enteros.


TESTS:
Para correr todos los tests, escribir en consola "pytest" y esperar al resultado.
Para correr un test especifico, escribir "pytest {nombre_del_test}".
