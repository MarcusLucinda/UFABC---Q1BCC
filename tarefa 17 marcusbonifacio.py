# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:24:15 2019

@author: marcus.bonifacio
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import funcs as f1

tabela = pd.read_csv('tabelaBrasileirao2018.csv')
x = tabela['Público']
y = tabela['Renda (R$)']

r = f1.corr(x, y)
print('Coeficiente de correlação =',r)