import numpy as np
import ej3
import math

def generar_sistema_de_difusion(alfa, u, iteraciones):
    res = [u]
    c_vec = armar_diagonales(alfa, len(u))
    c_vec[-1] = 0
    a_vec = armar_diagonales(alfa, len(u))
    a_vec[0] = 0
    b_vec = armar_central(alfa, len(u))
    ej3.triangular(a_vec, b_vec, c_vec)
    
    for i in range(iteraciones):
        u = ej3.resolver_ya_triangulada(a_vec, b_vec, c_vec, u)
        res.append(u)
    return res

def armar_diagonales(alfa, n):
    unos = np.ones(n)
    res = unos * (-alfa)
    return res

def armar_central(alfa, n):
    diag = np.ones(n) * (-2)
    res = (diag * (-alfa)) + np.ones(n)
    return res


def armar_u_consigna(n, r):
    res = []
    cota_menor = math.floor(n/2) - r
    cota_mayor = math.floor(n/2) + r
    for i in range(n):
      if (cota_menor < i & i < cota_mayor):
        res.append(1)
      else:
        res.append(0)
    return res
