import numpy as np

def armar_sistema_laplaciano(vector_solucion):
    diag_tr = armar_diagonal_triangulada(len(vector_solucion))
    v_modif = modificar_vector_solucion(vector_solucion)
    matriz = armar_matriz_triangulada(diag_tr)
    print(matriz)
    #resolver(matriz, v_modif)

def armar_diagonal_triangulada(n):
    a_s = -2
    a_i = 1
    res = []
    for j in range(n):
        res.append(a_s / a_i)
        a_s -= 1
        a_i += 1

    return res
def modificar_vector_solucion(vector_solu):
    #decido hacerlo por copia, creo el vector_modif, y le asigno de primer elemento el primero de la solu
    vector_modif = [vector_solu[0]]

    for j in range(1, len(vector_solu)):
        #para no dividir 1 sobre algo que tiende a 0, saco a_s y a_i en funcion de n
        #, que son [a_s=-2-n] y [a_i = n + 1], pero aca estoy usando j =n, entonces
        #debe ser j-1, ya que necesito tomar los de la fila anterior
        factor_multiplicador = (j) / (-2-(j-1))
        vector_modif.append (vector_solu[j] - vector_modif[j-1] * factor_multiplicador)

    return vector_modif

def armar_matriz_triangulada(diagonal_triangulada):
    matriz_d = np.diagflat(diagonal_triangulada)

    diagonal_unos = np.ones((1, len(diagonal_triangulada) - 1))
    matriz_unos = np.diagflat(diagonal_unos, 1)

    result = matriz_d + matriz_unos
    return result

def resolver():
    pass

vector_solu = [4, 6 ,2 ,3 ,6 ,7]
armar_sistema_laplaciano(vector_solu)
