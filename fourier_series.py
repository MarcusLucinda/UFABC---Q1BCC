# -*- coding: utf-8 -*-
"""
Marcus Bonifacio
11201921166

Esse Script é a tarefa 12 da aula de BCC

"""

print('1) Faça a aproximação de π usando a fórmula de Leibniz:'

'π≈4−43+45−47+49+...'
'Calcule (e mostre na tela) a aproximação de π considerando: '
'a) 50 termos '
'b) 500 termos '
'c) 1000 termos '
'd) 10000 termos')
print('\n')

   


import numpy as np #importa as bibliotecas que serão utilizadas no script
import matplotlib.pyplot as plt
import pandas as pd


n1 = 50 #define os valores dos termos
n2 = 500
n3 = 1000
n4 = 10000
pi1 = 0
pi2 = 0
pi3 = 0
pi4 = 0

for i in range(0, n1+1, 1): #define o loop utilizado na somatória
    pi1 = (pi1+((-1)**i)/(2*i+1)) #fórmula de leibniz para aproximação de π/4
    
    
for i in range(0, n2+1, 1):
    pi2 = (pi2+((-1)**i)/(2*i+1))
    
    
for i in range(0, n3+1, 1):
    pi3 = (pi3+((-1)**i)/(2*i+1))
    
for i in range(0, n4+1, 1):
    pi4 = (pi4+((-1)**i)/(2*i+1))


print('Valor real de π = ',np.pi)
#valores aproximados de π pela fórmula
print('a) π com N = 50',4*pi1)
print('b) π com N = 500',4*pi2)
print('c) π com N = 1000',4*pi3)
print('d) π com N = 10000',4*pi4)
print('\n')
print('\n')


print('2) Faça um gráfico com a taxa de inflação anual em função dos anos, de 1945 a 2018.')
print('\n')
inf1 = pd.read_csv('inflacaoMensal.csv') #carrega o dataframe com os dados de inflação
#dataframes inf2 e inf3 criados para completar os meses faltantes no dataframe de inflação
inf2c = ['Ano','Mês','Inflação']
meses = [7,8,9,10,11,12]
inf2 = pd.DataFrame(0, index=np.arange(0,6,1), columns = inf2c)
inf2['Ano'] = 2019
inf2['Mês'] = meses
inf3 = pd.DataFrame(0, index=np.arange(0,1,1), columns = inf2c)
inf3['Ano'] = 1944
inf3['Mês'] = 1
inflacao = inf3.append(inf1,ignore_index=True)
inflacao = inflacao.append(inf2, ignore_index=True) #junta os dataframes


ano = np.arange(1944,2020,1) #cria vetor com os anos
colunas = ['Ano', 'Inflação']

#criação de dataframe vazio para preencher com a inflação anual
infla = pd.DataFrame(0, index = np.arange(0,76,1), columns = colunas)
infla['Ano'] = ano
infla = infla.set_index('Ano')


k = 1
for w in range(1944, 2020, 1): #define os valores com os anos para serem varridos
    for e in range(1,13,1): #define os valores dos meses a serem varridos
        #loop que realiza a leitura das inflações mensais e calcula inflação anual
        m = (inflacao.loc[(np.logical_and((inflacao['Ano']) == w, (inflacao['Mês']) == e)),['Inflação']])
        k = k*(1 + (m['Inflação'].values[0])/100)
        
        if e == 12: #condição que determina o final do ano e reseta o calculo
            k = np.round(((k-1)*100),2)
            infla.loc[[w],['Inflação']] = k #amazena o valor da inflação anual no dataframe
            k = 1
            
#plot do gráfico de inflação anual
plt.figure()
plt.plot(np.arange(1944, 2020, 1), infla['Inflação'],)
plt.title('Inflação no Brasil')
plt.ylabel('Inflação (%)')
plt.xlabel('Ano')
plt.xlim(1944, 2019)
plt.show()
print('\n')
print('\n')



print('Calcular a aproximação de uma onda quadrada seguindo a seguinte expressão (a expressão abaixo é calculada utilizando uma teoria matemática conhecida como série de Fourier)'

'(t)≈4π∑i=1Nsin[(2i−1)t]2i−1')
print('n')
#o vetor t foi criado com 5000 valores pois mais que isso dava pau no meu pc
t = np.linspace(0,10,5000) #cria vetor com valores de t
z = t.tolist() #converte t para lista
v = (4/np.pi) #multiplicador da somatória


y=0
h = np.zeros(5000) #cria vetor para ser preenchido por x(t)
for x in z:
    for j in range(1,12,1): #define N
        y = y + ((np.sin(((2*j)-1)*x))/((2*j)-1)) #série de Fourier
        if j == 10:
            h[z.index(x)] = v*y #preenche o vetor com os valores de x(t)
        if j == 11:
            y = 0
       



y1=0
h1 = np.zeros(5000)
for x1 in z:
    for j1 in range(1,102,1):
        y1 = y1 + ((np.sin(((2*j1)-1)*x1))/((2*j1)-1))
        if j1 == 100:
            h1[z.index(x1)] = v*y1
        if j1 == 101:
            y1 = 0



y2=0
h2 = np.zeros(5000)
for x2 in z:
    for j2 in range(1,1002,1):
        y2 = y2 + ((np.sin(((2*j2)-1)*x2))/((2*j2)-1))
        if j2 == 1000:
            h2[z.index(x2)] = v*y2
        if j2 == 1001:
            y2 = 0



y3=0
h3 = np.zeros(5000)
for x3 in z:
    for j3 in range(1,10002,1):
        y3 = y3 + ((np.sin(((2*j3)-1)*x3))/((2*j3)-1))
        if j3 == 10000:
            h3[z.index(x3)] = v*y3
        if j3 == 10001:
            y3 = 0

#plota o gráfico com as séries
plt.figure()
plt.legend()
plt.plot(t, h, label='N = 10')
plt.plot(t, h1, color = 'red', label = 'N = 100')
plt.plot(t, h2, color = 'magenta', label = 'N = 1000')
plt.plot(t, h3, color = 'green', label = 'N = 10000')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Série de Fourier')
plt.legend()
plt.show()

"""
Fim do Script
"""

