# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:09:04 2019

@author: marcus.bonifacio
Esse script é a tarefa 15 da aula de bcc
"""

print('Faça uma função que receba um número a, um número b e um número x. Esta função deve retornar True se x estiver entre a e b e False caso contrário. Além disso a função deve mostrar uma mensagem dizendo se x está no intervalo entre a e b ou não.')
print('\n')

def estaNoIntervalo(a, b, x):
    '''
    Retorna True se x está entre a e b e False se não
    
    Parâmetros
    a, b, x: float
    Números que serão verificados
    '''
    
    verifica = x > a and x < b
    if verifica:
        resposta = True
    else:
        resposta = False
    return resposta
        

x1 = estaNoIntervalo(-2.5, 6.3, 9.1)
print('a) x = 9,1; a = -2,5; b = 6,3',x1)

    
x2 = estaNoIntervalo(-10, 7, 2.2)
print('a) x = 2.2; a = -10; b = 7,',x2)
    
x3 = estaNoIntervalo(67.2, 87.2, 8.1)
print('a) x = 8,1; a = 67,2; b = 87,2',x3)