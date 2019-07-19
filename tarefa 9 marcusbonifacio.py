# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:32:10 2019

@author: marcus.bonifacio

Esse script é a tarefa 9 da aula de BCC
"""

import numpy as np #importa biblioteca numpy
import matplotlib.pyplot as plt #importa biblioteca matplot
import pandas as pd #importa biblioteca pandas

analfa = pd.read_csv('analfabetismo.csv') #carrega tabela no script

plt.figure() #plot do gráfico de analfabetismo em são paulo
plt.plot(analfa['Ano'], analfa['São Paulo'], color = 'green')
plt.title('Número de analfabetos no estado de São Paulo')
plt.ylabel('% da população')
plt.xlabel('Ano')
plt.show()
