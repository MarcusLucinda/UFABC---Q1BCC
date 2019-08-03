# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:28:09 2019

@author: marcus.bonifacio

Esse script e tarefa 14 da aula de bcc

1) Para este item você deverá usar o arquivo com todos os resultados do campeonato Brasileiro de futebol de 2018 (tabelaBrasileirao2018.csv encontrado na pasta aula7/dados) (dados obtidos desta e desta página da Wikipedia).

Escolha um time e faça o histograma da distribuição do público nos jogos em que este time foi o mandante.

Calcule qual foi o público médio nos jogos em que o time escolhido foi o mandante.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv('tabelaBrasileirao2018.csv')



tabela[tabela['Mandante']=='Palmeiras']['Público'].plot.hist(19)




mediapalmeiras = tabela[tabela['Mandante']=='Palmeiras']['Público'].mean()
print('Média de público do Palmeiras =', np.round(mediapalmeiras, 2),'pessoas')

