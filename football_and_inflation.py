# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:37:53 2019

@author: Marcus

Este script é a tarefa 10 de BCC
"""

import numpy as np #importa a biblioteca numpy
import matplotlib.pyplot as plt #importa a biblioteca pyplot
import pandas as pd #importa a biblioteca pandas

print('1) Sobre o campeonato brasileiro de 2018:')
print('Calcule (e mostre o resultado na tela) a porcentagem de jogos que o time da casa (mandante) ganhou o jogo.')
print('Calcule (e mostre o resultado na tela) a porcentagem de jogos que o time da casa (mandante) não perdeu o jogo.')
print('\n')
tabela = pd.read_csv('tabelaBrasileirao2018.csv') #carreca o arquivo csv
vmandante = tabela[tabela['Placar do Mandante'] > tabela['Placar do Visitante']] #cria dataframe com vitórias dos mandantes
vmandante2 = tabela[tabela['Placar do Mandante'] >= tabela['Placar do Visitante']]


vm = (len(vmandante)/len(tabela))*100 #cálculo da porcentagem em que o mandante venceu
print('Porcentagem de vitórias dos mandantes =', np.round(vm,1), '%')
evm = (len(vmandante2)/len(tabela))*100 #cálculo da porcentagem em que o mandante não perdeu
print('Porcentagem de jogos que os mandantes não perderam',np.round(evm,1),'%')
print('\n')
print('\n')

print('2) Em relação à inflação brasileira:.')

print('Faça um gráfico da taxa de inflação mensal em função do tempo.')
print('Mostre em que mês e ano e qual foi a maior taxa de inflação mensal medida neste período (fevereiro de 1944 a junho de 2019)')

inflacao = pd.read_csv('inflacaoMensal.csv')
inflacao['anomes']  = inflacao['Mês'].map(str) + '/' + inflacao['Ano'].map(str) #cria coluna com mês e ano


plt.figure() #gráfico da inflação no período
plt.plot(inflacao['anomes'], inflacao['Inflação'], linewidth=0.8) 
plt.ylabel('Inflação Mensal')
plt.yticks(range(0,100,10))
plt.xlabel('Período')
plt.xticks(inflacao['anomes'][::36],inflacao['Ano'][::36], rotation='vertical')
plt.show()

pico = np.max(inflacao['Inflação']) #cálculo da máxima da inflação

print('Maior inflação registrada em:', inflacao['anomes'].values[inflacao['Inflação'] == pico])
print('\n')
print('\n')

print('3) De acordo com o histórico do Netflix')
print('Mostre quais são os 10 programas mais vistos.')
print('Em qual mês do ano foi assistido mais programas?')
print('\n')

netflix = pd.read_csv('netflix.csv')

netflix['Categoria'] = 'Filme'  
netflix['Categoria'][netflix['Title'].str.contains(": Temporada|: Stranger|: Parte")] = 'Série'  
netflix['Programa'] = netflix['Title']  
netflix[['Programa','Episódio']] = netflix[netflix['Categoria']=='Série']['Title'].str.split(pat = ': Temporada|: Stranger Things|: Parte', expand = True, n = 1)   
netflix.loc[netflix['Categoria']=='Filme', 'Programa'] = netflix.loc[netflix['Categoria']=='Filme', 'Title']  
netflix = netflix.drop(columns = 'Title')

netflix['Date'] = pd.to_datetime(netflix['Date'], format = '%d/%m/%Y') #organiza as datas no dataframe
programas = netflix['Programa'].value_counts() #cria uma série com a quantidade que cada programa é assistido
print('Os 10 programas mais assistidos são:')
print(programas.head(10)) #exibe os 10 programas mais assistidos
print('\n')

netflix['Ano'] = netflix['Date'].dt.year #cria uma coluna com os anos
netflix['Mês'] = netflix['Date'].dt.month #cria uma coluna com os meses
mes = netflix[netflix['Ano'] == 2019] #variável com os meses de 2019
cmes = mes['Mês'].value_counts()  #calcula a quantidade de programas exibidos nos meses de 2019
print('O mês com mais programas assistidos em 2019 foi o mês',cmes.index[0],'com',cmes[cmes.index[0]],'programas')


"""
Fim do Script
"""
