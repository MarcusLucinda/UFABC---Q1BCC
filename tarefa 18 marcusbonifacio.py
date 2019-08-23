# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:43:57 2019

@author: Marcus
"""
#importa bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import funcs as f1


print('1) Faça o gráfico de dispersão do tamanho do pé (FootLen) em função da altura da pessoa (Height). Calcule (e mostre na tela) a correlação e plote a reta de regressão entre esses dados.')
print()

experimento = pd.read_csv('BDSinfo.csv', delimiter = '\t') #carrega dataframe  com dados
pe = experimento['FootLen'] #cria vetor com dados da coluna
altura = experimento['Height']

m1, b1 = f1.regressao(altura, pe) #calcula a reta de regressão

plt.figure() #plota o gráfico de dispersão com a reta de regressão
plt.plot(altura , pe, marker='o', color='red', linestyle='')
plt.plot(altura, m1*altura+b1, linewidth = '3')
plt.title('Tamanho do pé em função da altura')
plt.xlabel('Altura')
plt.ylabel('Tamanho do pé')
plt.grid()
plt.show()

r1 = f1.corr(altura, pe) #calcula a correlação
print('Correlação =',np.round(r1,2))
print('\n')
print('\n')


print('2) Faça o gráfico de dispersão entre o crescimento do PIB e a inflação anual de 1961 a 2018. Calcule e mostre na tela a correlação entre as duas grandezas.')
print()

infla = pd.read_csv('inflaAnual.csv') #carrega dataframe  com dados
pibanual = pd.read_csv('pibAnual.csv') #cria vetor com dados da coluna
infla2 = infla.iloc[16:74]
pib = pibanual['Variação anual do PIB real (%)']
inflacao = infla2['Inflação'].reset_index(drop=True)

m3, b3 = f1.regressao(pib, inflacao) #calcula a reta de regressão

plt.figure() #plota o gráfico de dispersão com a reta de regressão
plt.plot(pib, inflacao, marker='o', color='magenta', linestyle='')
plt.plot(pib, m3*pib+b3, color = 'brown', linewidth = '3')
plt.title('Inflação em função do PIB')
plt.xlabel('PIB')
plt.ylabel('Inflação (%)')
plt.grid()
plt.show()

r3 = f1.corr(pib, inflacao) #calcula a correlação
print('Correlação =',np.round(r3,2))
print('\n')
print('\n')



print('3) Faça o gráfico de dispersão do número de medicamentos que a pessoa toma (Nmedication) em função da idade da pessoa (Age). Calcule (e mostre na tela) a correlação e plote a reta de regressão entre esses dados.')
print()
remedio = experimento['Nmedication'] #cria vetor com dados da coluna
idade = experimento['Age']

m2, b2 = f1.regressao(idade, remedio) #calcula a reta de regressão

plt.figure() #plota o gráfico de dispersão com a reta de regressão
plt.plot(idade , remedio, marker='o', color='green', linestyle='')
plt.plot(idade, m2*idade+b2, linewidth = '3', color = 'orange')
plt.title('Idade em função do nº de medicamentos')
plt.xlabel('Idade')
plt.ylabel('Nº de medicamentos')
plt.grid()
plt.show()

r2 = f1.corr(idade, remedio) #calcula a correlação
print('Correlação =',np.round(r2,2))


