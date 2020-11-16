# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:10:55 2019

@author: Marcus
"""

#importa bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


print('1) Faça uma função que receba um vetor t,um valor A, um valor b e um valor c e retorne um outro vetor x.')


def formula(A, b, c, t):
    '''
    Cria um vetor x de acordo com a função
    
    Parâmetros:
    A: float
    
    b:float
    
    c:float
    
    t:array
        vetor com as variáveis da função
    '''
    x = []
    for i in t:
        xm = (A*(np.sqrt(1+(b*(i**2)))))+c
        x.append(xm)
    plt.figure()
    plt.plot(t, x)
    plt.title('A = %s; b = %s; c = %s'%(A,b,c))
    plt.xlabel('t')
    plt.ylabel('x')
    plt.show()

#valores das variáveis que serão usadas
t1 = np.linspace(0,10,1000) #cria vetor com número de t
formula(2,0.5,0,t1) #chama a função com as variáveis

t2 = np.arange(0,15.1,0.2)
formula(10,0.2,1,t2)

t3 = np.linspace(-0.5,0.5,500)
formula(-3,-1.5,-10,t3)

print('\n')
print('\n')


print('2) Faça uma função que ao ser executada sorteia um número entre 0 e 1. Se esse número for menor do que 0,5 apareça na tela a mensagem Cara. Se esse número for maior do que 0,5 apareça a mensagem Coroa'
' Teste a função chamando 10 vezes a função que você fez.')
    
def cara_ou_coroa():
    '''
    Define cara ou coroa de acordo com número aleatório
    '''
    z = np.random.rand(1)
    if z[0] <= 0.5:
        moeda = 'Cara'
    else:
        moeda = 'Coroa'
    print(moeda)
    
#chamar a função em loop
for _ in range(10):
    cara_ou_coroa()

print('\n')
print('\n')


print('3) Faça uma função que retorne a moda (ver aula 7) de uma coluna de um DataFrame do Pandas. As entradas devem ser o DataFrame do Pandas e o nome da coluna. Além de retornar a moda, a função deve mostrar na tela qual é a moda encontrada')
print()

tabela = pd.read_csv('tabelaBrasileirao2018.csv') #carrega a tabela com os dados do campeonato

def estadio():
    '''
    Busca e imprime o estádio onde houveram mais jogos
    '''
    print('Estádio mais utilizado:',tabela['Estádio'].value_counts().index[0])

estadio()
print('\n')
print('\n')

print('Dados valores x1, y1, x2, y2, sendo esses valores das coordenadas (x1,y1) e (x2,y2) de dois pontos.'

' Fazer uma função que encontre a inclinação da reta m e o ponto b em que a reta cruza o eixo y da reta y=mx+b que passa pelos dois pontos. Além disso deve ser feito o gráfico da reta encontrada com N pontos, além de mostrar os dois pontos dados como entrada, indicados com marcadores quadrados.'

' Essa função deve retornar m e b e receber como parâmetros x1, y1, x2, y2 e N.')

def reta(x1, y1, x2, y2, N):
    '''
    Calcula inclinação m da reta e ponto b em que a reta cruza o eixo y de mx+b
    
    Parâmetros
    x1: float
        coordenada do eixo x do primero ponto
    y1: float
         coordenada do eixo y do primero ponto
    x2: float
         coordenada do eixo x do segundo ponto
    y2: float
         coordenada do eixo y do segundo ponto
    N: int
        número de pontos na reta
    '''
    m = (y2-y1)/(x2-x1)
    b = (y1 - (m*x1))
    y = []
    x = np.linspace(-50,50,N)
    for xa in x:
        ya = (m*xa)+b
        y.append(ya)
    plt.figure()
    plt.plot(x, y, color='red')
    plt.plot([x1,x2],[y1,y2], marker='s', linestyle='none')
    plt.text(x1,y1,'(%s, %s)'%(x1,y1))
    plt.text(x2,y2,'(%s, %s)'%(x2,y2))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('m = %s, b = %s'%(np.round(m,2),np.round(b,2)))
    plt.show()
    
    
#variáveis que serão utilizadas na função
reta(19,2,10,-10,1000)

reta(-2,8,20,43,2000)

reta(7,13,1,2,500)























