# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:54:48 2019

@author: Marcus Bonifacio

Esse script é a tarefa 8 da aula de Bases Computacionais
"""

print('1) Mostrar a classificação do IMC para as seguintes pessoas:') #enunciado
print('Pessoa a: m = 52Kg e h = 1,58m')
print('Pessoa b: m = 83Kg e h = 1,75m')
print('Pessoa c: m = 70Kg e h = 1,79m')
print('\n')

import numpy as np #importa a biblioteca numpy para o script
import matplotlib.pyplot as plt


#Pessoa a
IMCa1 = 52/(1.58**2) #cálculo para o imc da pessoa a 
IMCa = np.round(IMCa1, 1) #arrendondamento do valor do imc para uma casa decimal
if IMCa < 17: #linhas que comparam o valor do imc e definem a categoria que a pessoa se enquadra
    print('Pessoa a : IMC =',IMCa,'; Muito abaixo do peso') 
else:
    if IMCa >= 17 and IMCa < 18.5:
        print('Pessoa a : IMC =',IMCa,'; Abaixo do peso')
    else:
        if IMCa >= 18.5 and IMCa < 25:
            print('Pessoa a : IMC =',IMCa,'; Peso normal')
        else:
            if IMCa >= 25 and IMCa < 30:
                print('Pessoa a : IMC =',IMCa,'; Acima do peso')
            else:
                if IMCa >= 30 and IMCa < 35:
                    print('Pessoa a : IMC =',IMCa,'; Obesidade Grau I')
                else:
                    if IMCa >= 35 and IMCa < 40:
                        print('Pessoa a : IMC =',IMCa,'; Obesidade Grau II')
                    else:
                        print('Pessoa a : IMC =',IMCa,'; Obesidade Grau III')
                        

                    
#Pessoa b
IMCb1 = 83/(1.75**2) #cálculo para o imc da pessoa b 
IMCb = np.round(IMCb1, 1) #arrendondamento do valor do imc para uma casa decimal
if IMCb < 17: #linhas que comparam o valor do imc e definem a categoria que a pessoa se enquadra
    print('Pessoa b : IMC =',IMCb,'; Muito abaixo do peso') 
else:
    if IMCb >= 17 and IMCb < 18.5:
        print('Pessoa b : IMC =',IMCb,'; Abaixo do peso')
    else:
        if IMCb >= 18.5 and IMCb < 25:
            print('Pessoa b : IMC =',IMCb,'; Peso normal')
        else:
            if IMCb >= 25 and IMCb < 30:
                print('Pessoa b : IMC =',IMCb,'; Acima do peso')
            else:
                if IMCb >= 30 and IMCb < 35:
                    print('Pessoa b : IMC =',IMCb,'; Obesidade Grau I')
                else:
                    if IMCb >= 35 and IMCb < 40:
                        print('Pessoa b : IMC =',IMCb,'; Obesidade Grau II')
                    else:
                        print('Pessoa b : IMC =',IMCb,'; Obesidade Grau III')           
                    
                    
                    
#Pessoa c
IMCc1 = 70/(1.79**2) #cálculo para o imc da pessoa c
IMCc = np.round(IMCc1, 1) #arrendondamento do valor do imc para uma casa decimal
if IMCc < 17: #linhas que comparam o valor do imc e definem a categoria que a pessoa se enquadra
    print('Pessoa c : IMC =',IMCc,'; Muito abaixo do peso') 
else:
    if IMCc >= 17 and IMCc < 18.5:
        print('Pessoa c : IMC =',IMCb,'; Abaixo do peso')
    else:
        if IMCc >= 18.5 and IMCc < 25:
            print('Pessoa c : IMC =',IMCc,'; Peso normal')
        else:
            if IMCc >= 25 and IMCc < 30:
                print('Pessoa c : IMC =',IMCc,'; Acima do peso')
            else:
                if IMCc >= 30 and IMCc < 35:
                    print('Pessoa c : IMC =',IMCc,'; Obesidade Grau I')
                else:
                    if IMCc >= 35 and IMCc < 40:
                        print('Pessoa c : IMC =',IMCc,'; Obesidade Grau II')
                    else:
                        print('Pessoa c : IMC =',IMCc,'; Obesidade Grau III')
                    
print('\n')
print('\n')

print('2) A acidez A(x) de uma solução de hidróxido de magnésio em ácido clorídrico, sob certas condições experimentais, é dada pela equação:'

'A(x)=x³+3x²−54'
' na qual x é a concentração de íons hidrônio.'

' Pede-se:'

' 1) Gere o gráfico de A(x) em função de x para 0 ⩽x⩽8.'

' 2) Determine a concentração x do íon de hidrônio que resulta em solução saturada (i.e., com acidez nula). Acrescente uma instrução que gere um ponto vermelho no gráfico correspondente à saturação nula da solução.')
print('\n')

x1 = np.arange(0, 8.1, 0.1) #cria um vetor com os valores da concentração de hidrônio


Ax = (x1**3) + (3*(x1**2)) - 54 #definicão da acidez da solução em função da concentração


plt.figure()
plt.plot(x1, Ax, color = 'red', marker = 's', markevery = np.arange(len(x1))[Ax==0]) #configurações visuais do gráfico
plt.title('Acidez da solução de Mg(OH)\u2082 em HCl') #título do gráfico
plt.xlabel('Concentração de H\u2083O') #rótulo do eixo x
plt.ylabel('Acidez') #rótulo do eixo y
plt.show()

print('Concentração de H\u2083O quando a acidez é 0 =',x1[Ax==0])

print('\n')
print('\n')

print('3) Faça o gráfico de:'
' f(x)=|x−2|+|2x+1|−x−6'
' Faça o gráfico com x variando de -10 a 10.'

' Mostre no Console o menor valor de x tal que f(x)>0 e x>0.')
    
x2 = np.arange(-10, 10.1, 0.1) #cria vetor com os valores de x

y2 = (np.abs(x2-2)) + (np.abs((2*x2)+1)) - x2 - 6 #função para o vetor com valores de f(x)

plt.figure() #gráfico da função
plt.plot(x2, y2, color='green')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de f(x)=|x−2|+|2x+1|−x−6')
plt.show()

z2 = np.logical_and(x2 > 0, y2 >= 0) #condição para criação do vetor onde f(x) e x > 0

xm2 = x2[z2] #cria o vetor com os elementos em que f(x) e x > 0

xmin = np.min(xm2) #valor mínimo do vetor acima
print('Valor mínimo de x para f(x) e x > 0 =',np.round(xmin,1))

print('\n')
print('\n')

print('3) Faça o gráfico da seguinte função:'

' f(x)=x²–sin(0.784x²)–2'
' Mostre no Console as raízes da função (i.e. os valores de x para os quais f(x)=0).')

x3 = np.round(np.arange(-5, 5.1, 0.001),3) #cria um vetor com valores de x


y3 = (x3**2)-(np.sin(0.784*(x3**2)))-2 #define os valores de f(x)

plt.figure() #gráfico da função
plt.plot(x3, y3, color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de f(x)=x²–sin(0.784x²)–2')
plt.show()

print('Raízes da função: x =',x3[np.logical_and(y3 > -0.002, y3 < 0.002)]) #busca os valores de x quando f(x) = 0
#como não há valor exato 0 no vetor, busca-se o valor mais próximo

"""
Fim do Script
"""












