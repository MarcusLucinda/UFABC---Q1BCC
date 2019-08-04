# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:14:03 2019

@author: Marcus Bonifácio

Esse script é a tarefa 14 da aula de BCC
"""

#importa as bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''
print('1) Para este item você deverá usar o arquivo com dados de força e torque medidos no chão enquanto uma pessoa tenta ficar em pé o mais parada possível durante um minuto')
print('Faça o gráfico do torque na direção y (My [Nm]) em função do tempo (Time [s]).')
print('Mostre na tela a média e o desvio-padrão do torque na direção y.')
print()
'''
balance = pd.read_csv('balance.csv') #carrega a tabela com os dados
mynm = balance['My[Nm]'].values #organiza os valores da coluna em um vetor
tempo = balance['Time[s]'].values

plt.figure() #plot do gráfico
plt.plot(tempo, mynm, color='green')
plt.title('Torque em função do tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('My (Nm)')
plt.show()

mtorque = np.mean(mynm) #calcula média do vetor
dtorque = mynm.std() #calcula desvio padrão do vetor
print('Média de torque =',mtorque,'Nm')
print('Desvio padrão =',dtorque,'Nm')
print('\n')
print('\n')





'''
print('2) Para este item você deverá usar o arquivo com a taxa de inflação mensal (IGP-DI) no Brasil de fevereiro de 1944 a junho de 2019 (dados disponibilizados por Ipeadata).')
print('Calcule a mediana da inflação mensal nos meses de março.')
print('Calcule a média da inflação mensal nos meses de março.')
print('Calcule o desvio-padrão da inflação mensal nos meses de março.')
print('Faça o histograma da inflação mensal nos meses de março.')
print()
'''

inflacao = pd.read_csv('inflacaoMensal.csv') #carrega a tabela com os dados
q = (inflacao.loc[((inflacao['Mês']) == 3),['Inflação']]) #busca os valores de acordo com a condição
março = q['Inflação'].values #organiza os valores da coluna em um vetor

medianainfla = np.round(np.median(março),2) #calcula mediana do vetor
mediainfla = np.round(np.mean(março),2) #calcula média do vetor
dinfla = np.round(março.std(),2) #calcula desvio padrão do vetor
print('Mediana da inflação nos meses de março entre 1944 e 2019 =', medianainfla,'%')
print('Média da inflação nos meses de março entre 1944 e 2019 =', mediainfla,'%')
print('Desvio padrão da inflação nos meses de março entre 1944 e 2019 =', dinfla,'%')
print()
plt.figure() #plot do gráfico
plt.hist(março,75, color='red')
plt.xticks(np.arange(-5, 86, 5))
plt.title('Inflação nos meses de março de 1944 a 2019')
plt.xlabel('Taxa de Inflação(%)')
plt.ylabel('Frequência')
plt.show()
print('\n')
print('\n')



'''
print('3) Para este item você deverá usar o arquivo com a taxa de inflação mensal (IGP-DI) no Brasil de fevereiro de 1944 a junho de 2019 (dados disponibilizados por Ipeadata).')
print('Calcule a mediana da inflação mensal nos meses de março a partir de 1995.')
print('Calcule a média da inflação mensal nos meses de março a partir de 1995.')
print('Calcule o desvio-padrão da inflação mensal nos meses de março a partir de 1995.')
print('Faça o histograma da inflação mensal nos meses de março a partir de 1995.')
print('Coloque um comentário no seu script comentando a razão da diferença entre a média e a mediana ser alta no segundo item e baixa no terceiro item.')
print()
'''
w = (inflacao.loc[(np.logical_and((inflacao['Ano']) >= 1995, (inflacao['Mês']) == 3)),['Inflação']]) #busca os valores de acordo com a condição
março95 = w['Inflação'].values #organiza os valores da coluna em um vetor

medianainfla95 = np.round(np.median(março95),2) #calcula mediana do vetor
mediainfla95 = np.round(np.mean(março95),2) #calcula média do vetor
dinfla95 = np.round(março95.std(),2) #calcula desvio padrão do vetor

print('Mediana da inflação nos meses de março entre 1995 e 2019 =', medianainfla95,'%')
print('Média da inflação nos meses de março entre 1995 e 2019 =', mediainfla95,'%')
print('Desvio padrão da inflação nos meses de março entre 1995 e 2019 =', dinfla95,'%')
print()
plt.figure() #plot do gráfico
plt.hist(março95,25, color='blue')
plt.xticks(np.arange(-1, 4, 1))
plt.title('Inflação nos meses de março de 1995 a 2019')
plt.xlabel('Taxa de Inflação(%)')
plt.ylabel('Frequência')
plt.show()

print('Em 1994 houve o início do plano real, que ajudou a controlar a hiperinflação '
      'vivida no país, portanto os índices de inflação a partir de 95 são menores')
print('\n')
print('\n')



'''
print('4) Use o comando np.random.rand(N) para gerar N números aleatórios entre 0 e 1.')
print('Faça o histograma e calcule (e mostre na tela) a média dos valores gerados.')
print('Faça isso para a) N = 100, N = 1000, c) N = 10000, d) N = 100000')
print()
'''

for N in np.array([100, 1000, 10000, 100000]): #cria um loop com os valores de N
    b = np.random.rand(N) #cria vetor com números aleatórios
    print('N =',N)
    print('Média =',np.mean(b)) #média de N no loop
    print()
    plt.figure() #plot do gráfico pra N no loop
    plt.hist(b, 200)
    plt.title('Histograma para N = {}'.format(N))
    plt.xlabel('Valor aleatório')
    plt.ylabel('Frequência')
    plt.show()


'''
Fim do Script
'''

