'''
Gerar uma lista com duas matrizes (2,3,3)
de 0 a 8 e 9 a 17
'''
import numpy as np
#teste1
numeros = np.arange(18)
print(18)
lm = numeros.reshape(2,3,3)
print(lm)

#teste2
numeros = np.arange(24)
print(24)
lm2 = numeros.reshape(2,3,-1)
print(lm2)