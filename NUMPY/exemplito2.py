import numpy as np

#slicing

lista = np.arange(15)
print(lista)

pedaco = lista[5:9]
print(pedaco)

pedaco[0] = 69
print(pedaco)
print(lista)

pedaco2 = lista[-5:]
print(pedaco2)

#data types

frutas = np.array(('banana','maça','morango','laranja'))
print(frutas)
print(frutas.dtype)

numeros = np.array([1,2,3,4],dtype ='i8')
print(numeros)
print(numeros.dtype)