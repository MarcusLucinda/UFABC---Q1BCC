# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 22:54:21 2019

@author: Marcus

Esse Script foi feito para a tarefa 6 da aula de BCC
"""

import numpy as np #importa a biblioteca numpy
import matplotlib.pyplot as plt #importa a bibliotewca pyplot

print()
print('1) Gráfico da tensão elétrica de um circuito em função do tempo') 
print()

t = np.arange(0, 10.001, 0.05) #cria o veor com as variáveis de tempo, de 0 a 10 segundos no passo de 0,05

v = (np.e**(-(0.5*t)))*(np.cos(2*np.pi*0.8*t)) #calculo para obter a tensão.



plt.figure() #inicia a construção do gráfico
plt.plot(t, v, 
         color = 'red') #define os eixos do gráfico e a cor da linha
plt.title('Tensão do circuito em função do tempo') #título do gráfico
plt.xlabel('Tempo (s)') #título do eixo x
plt.ylabel('Tensão (v)') #título do eixo y
plt.show() #fnaliza a construção do gráfico

print()
print()
print()
print()

print('2) Gráfico da equivalência da temperatura em Fahrenheits em função da temperatura em Celsius')
print()


c = np.linspace(-20, 100, 1000) #define os valores das temperaturas em Celcius, 1000 valores entre -20 e 100

f = ((9/5)*c)+32 #converte a temperatura para Fahrenheit


plt.figure() #inicia a construção do gráfico
plt.plot(c, f,) #define os eixos do gráfico
plt.xlabel('Celcius (°C)') #título do eixo x
plt.ylabel('Fahrenheits (°F)')  #título do eixo y
plt.title('Temepratura em Fahrenheits em função de Celcius') #título do gráfico
plt.show() #fnaliza a construção do gráfico

print()
print()
print()
print()

print('3) Função de crescimento populacional')
print()

a = np.arange(1994, 2020.1, 1) #cria o vetor com os anos, de 1994 a 2020

p = (800000*np.e)**((a-1994)/40) #calculo para o numero de habitantes


plt.figure()  #inicia a construção do gráfico
plt.plot(a, p, #define os eixos do gráfico
         color='green', #define a cor da linha
         marker='.') #define o marcador dos pontos no gráfico
plt.xlabel('Ano') #título do eixo x
plt.ylabel('Habitantes') #título do eixo y
plt.title('Número de habitantes da cidade') #título do gráfico
plt.show() #fnaliza a construção do gráfico

print()

m = np.max(p) #retorna o valor máximo de p
print('Previsão de população em 2020 =',np.around(m),'habitantes') #exibe o valor máximo de p

"""Fim do script"""











