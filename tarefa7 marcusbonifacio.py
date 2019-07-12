# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 19:15:53 2019

@author: Marcus Bonifácio
11201921166

Esse script é a Tarefa 7 da aula de BCC
"""

print('Defina de os números 1, 24, 10, 5 são par ou ímpar') #Enunciado

print('\n') #pular linha

import numpy as np #importa biblioteca numpy

x = np.array([1, 24, 10, 5]) #cria um vetor x com as váriaveis que serão identificaas como par ou ímpar


if (x[0]%2 == 0): #condição se o resto da divisão do primeiro elemento de x por 2 é zero
    print(x[0], 'é um número par') #texto de for par
else:
    print(x[0], 'é um número ímpar') #texto se for ímpar
    
if (x[1]%2 == 0): #condição se o resto da divisão do segundo elemento de x por 2 é zero
    print(x[1], 'é um número par') #texto de for par
else:
    print(x[1], 'é um número ímpar') #texto se for ímpar
    
if (x[2]%2 == 0): #condição se o resto da divisão do terceiro elemento de x por 2 é zero
    print(x[2], 'é um número par') #texto de for par
else:
    print(x[2], 'é um número ímpar') #texto se for ímpar
    
if (x[3]%2 == 0): #condição se o resto da divisão do quarto elemento de x por 2 é zero
    print(x[3], 'é um número par') #texto de for par
else:
    print(x[3], 'é um número ímpar') #texto se for ímpar
    
"""

Fim do script

"""