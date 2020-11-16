# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:59:52 2019

@author: Marcus

Script da Tarefa 4 de Bases Computacionais

"""


"""
1) Calculo do volume de uma esfera com raio R
"""

import numpy as np #importar biblioteca de equações
print('1) Calculo do volume de uma esfera com raio R')
print()
R1 = 0.32 #raio da esfera
VR1 = (4* np.pi * (R1**3))/3 #fórmula de cálculo de volume
print('R1 =',R1,'m') #exibir raio no console
print('VR1 =',round (VR1, 3),'m³') #exibir volume no console
print()

R2 = 1 
VR2 = (4* np.pi * (R2**3))/3 
print('R2 =',R2,'m')
print('VR2 =',round (VR2, 3),'m³')
print()

R3 = 1.9
VR3 = (4* np.pi * (R3**3))/3 
print('R3 =',R3,'m')
print('VR3 =',round (VR3, 3),'m³')
print()
print()
print()

"""
2) Temperatura em Fahrenheit dada a temperatura em Celcius na variável T
"""
print('2) Temperatura em Fahrenheit dada a temperatura em Celcius')
print()
T1 = -10 #Temperatura em Celcius
F1 = T1 * (9/5) + 32 #Fórmula de convesão para F
print('T1 =',T1,'°C') #Exibir T em celcius no console
print('F1 =', F1, '°F') #Exibir temp. convertida
print()

T2 = 30
F2 = T2 * (9/5) + 32
print('T2 =',T2,'°C')
print('F2 =', F2, '°F')
print()

T3 = 5
F3 = T3 * (9/5) + 32
print('T3 =',T3,'°C')
print('F3 =', F3, '°F')
print()
print()
print()


"""
3) Lado c de um triângulo com a b e θ conhecidos 
"""

print('3)Definição do lado c de um triângulo com os lados a e b e o ângulo θ conhecidos')
print()
print('Triangulo 1')
a1 = 1 #Lado a do triangulo
b1 = 2 #Lado b do triangulo
θ1 = 30 #angulo dos lados a e b triangulo
rad1 = np.deg2rad(θ1) #conversão do angulo para radianos
c1 = np.sqrt(a1**2 + b1**2 - (a1 * b1 * 2 * np.cos(rad1))) #aplicação da lei dos cossenos
print('a =',a1)
print('b =',b1)
print('θ=',θ1,'°')
print('c =',round (c1, 3))
print()

print('Triangulo 2')
a2 = 3
b2 = 1
θ2 = 45
rad2 = np.deg2rad(θ2)
c2 = np.sqrt(a2**2 + b2**2 - (a2 * b2 * 2 * np.cos(rad2)))
print('a =',a2)
print('b =',b2)
print('θ=',θ2,'°')
print('c =',round (c2, 3))
print()

print('Triangulo 3')
a3 = 10
b3 = 11
θ3 = 15
rad3 = np.deg2rad(θ3)
c3 = np.sqrt(a3**2 + b3**2 - (a3 * b3 * 2 * np.cos(rad3)))
print('a =',a3)
print('b =',b3)
print('θ=',θ3,'°')
print('c =',round (c3, 3))
print()
print()
print()


"""3) Sequencia de Fibonacci"""

print('3) Identificação do n-ésimo número na sequência de Fibonacci')
print()
n1 = 30 # número na sequencia
f1 = np.floor(((((1 + np.sqrt(5)) / 2)**n1) - (((1 - np.sqrt(5)) / 2)**n1)) / np.sqrt(5)) #cálculo para valor da sequencia
print('n =',n1)
print('F =',f1)
print()

n2 = 31
f2 = np.floor(((((1 + np.sqrt(5)) / 2)**n2) - (((1 - np.sqrt(5)) / 2)**n2)) / np.sqrt(5)) 
print('n =',n2)
print('F =',f2)
print()

n3 = 32
f3 = np.floor(((((1 + np.sqrt(5)) / 2)**n3) - (((1 - np.sqrt(5)) / 2)**n3)) / np.sqrt(5)) 
print('n =',n3)
print('F =',f3)
print()

"""
Fim do Script
"""























