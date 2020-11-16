# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 19:08:58 2019

@author: marcus.bonifacio

1) Três séries, v,y e t seguem as seguintes regras:
v[i]=v[i−1]+0,01.(−9,81)
y[i]=y[i−1]+0,01v[i−1]
t[i]=t[i−1]+0,01
Começando com v[0] = 10 m/s, y[0] = 0 m e t[0] = 0 s, calcule os 250 primeiros valores das três séries.

Faça os gráficos com os valores encontrados de y em função de t e dos valores encontrados de v em função de t.

Observação: o cálculo destas três séries é uma simulação computacional para calcular a 
posição e velocidade de uma partícula lançada na vertical com velocidade inicial de 10 m/s. 
O método utilizado para realizar esta simulação é conhecido como método de Euler.
"""


    
import numpy as np
import matplotlib.pyplot as plt
    
n = 250 #define o numero de elementos
v = np.zeros((n)) #cria vetor com zeros
y = np.zeros((n))
t = np.zeros((n))
v[0] = 10 #define o primeiro elemento do vetor
y[0] = 0
t[0] = 0
for i in range(1, len(v)): #loop para preencher valores dos vetores
    v[i] = v[i - 1] + (0.01*(-9.81))
    y[i] = y[i - 1] + 0.01*v[i - 1]
    t[i] = t[i - 1] + 0.01

plt.figure() #plot do gráfico
plt.plot(t, y, color='orange')
plt.xlabel('tempo (s)')
plt.ylabel('distância (m)')
plt.title('y em função de t')
plt.show()

plt.figure() #plot do gráfico
plt.plot(t, v, color='red')
plt.xlabel('tempo (s)')
plt.ylabel('velocidade (m/s')
plt.title('v em função de t')
plt.show()