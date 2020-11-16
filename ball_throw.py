# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:15:46 2019

@author: marcus.bonifacio

Esse script tem por finalidade calcular a altura de uma bola após lançamento

"""

import numpy as np #importa biblioteca numpy
import matplotlib.pyplot as plt #importa biblioteca pyplot


t = np.arange(0, 5.1 ,0.1) #cria módulo com o tempo, de 0 a 5 segundos com intevalo de 0,1 s


h = -(t**2) + (4*t) #formula para calcular a altura da bola em função do tempo

print('Uma bola é lançada ao ar')
plt.figure() #Inicia o plot do gráfico
plt.plot(t, h, #definição dos eixos dos gráficos
         color = 'green') #defien a cor do gráfico
plt.title('Grafico da altura alcançada pela bola em função do tempo') #título do gráfico
plt.xlabel('Tempo (s)') #nome do eixo x
plt.ylabel('Altura (m)') #nome do eixo y
plt.show() #finaliza o plot do gráfico

m = np.max(h) #comando para retornar o valor máximo do módulo h
print('Altura máxima alcançada =',m,'m') 
