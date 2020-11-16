# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:07:15 2019

@author: marcus.bonifacio
"""

import numpy as np



print('1) Faça um script para estimar o valor de π utilizando o método de Monte Carlo.')

N = 10000000 #define quantidade de pontos
x = np.random.rand(N) #gera números aleatórios de 0 a 1 
y = np.random.rand(N)
deltax = (0.5-x)**2 #calcula a diferença das coordenadas do ponto para o centro do círculo
deltay = (0.5-y)**2
d = np.sqrt(deltax + deltay) #calcula a distancia do ponto para o centro do círculo

circ = d[d <= 0.5] #seleciona os pontos dentro do círculo

razao = len(circ)/N #razão dos pontos dentro do círculo e todos os pontos
pi = 4*razao #aproxima pi
print('Valor aproximado de PI pelo método Monte Carlo =',pi)
