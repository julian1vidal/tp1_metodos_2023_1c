import numpy as np
EPS = 1.0e-4
import ej3
import math


def armar_sistema_laplaciano(vector_solucion):
    n = len(vector_solucion)
    a = np.ones(n)
    b = np.ones(n) * -2
    c = np.ones(n)
    a[0] = 0
    c[-1] = 0

    result = ej3.resolver_tridiagonal(a, b, c, vector_solucion)
    
    return result

def armar_lista_a(largo):
  res = []
  condicion = math.floor(largo/2) + 1
  for i in range(largo):
    if (i==condicion):
      #se genera error numerico al dividir por numeros pequenios
      # o multiplicar por numeros grandes (asi q tamo bien)
      res.append(4/largo)
    else:
      res.append(0)

  return(res)

def armar_lista_b(largo):
  res = []
  elemento = 4 / (largo ** 2)
  for i in range(largo):
    res.append(elemento)
  
  return res


def armar_lista_c(largo):
  res = []
  fijo = 12 / (largo ** 2)
  for i in range(largo):
    elemento = (-1 + (2 * i / (largo - 1))) * fijo
    res.append(elemento)

  return res


#a = armar_lista_a(101)
#resultadoa = armar_sistema_laplaciano(a)
#b = armar_lista_b(101)
#resultadob = armar_sistema_laplaciano(b)
#c = armar_lista_c(101)
#resultadoc = armar_sistema_laplaciano(c)
#plt.plot(resultadoa)
#plt.plot(resultadob)
#plt.plot(resultadoc)
