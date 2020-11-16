# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:24:15 2019

@author: marcus.bonifacio
"""
#importa bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import funcs as f1


tabela = pd.read_csv('tabelaBrasileirao2018.csv') #importa arquivo com os dados
x = tabela['Público'] #cria vetor com os valores da coluna especificada
y = tabela['Renda (R$)']

r = f1.corr(x, y) #chama a função de correlação e insere as variáveis
print('Coeficiente de correlação =',r)
