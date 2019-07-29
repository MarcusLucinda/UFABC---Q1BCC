# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np

n1 = 50
n2 = 500
n2 = 1000
n3 = 10000
pi1 = 0
pi2 = 0
pi3 = 0

for i in range(0, n1+1, 1):
    pi1 = (pi1+((-1)**i)/(2*i+1))
    
    
for i in range(0, n2+1, 1):
    pi2 = (pi2+((-1)**i)/(2*i+1))
    
    
for i in range(0, n3+1, 1):
    pi3 = (pi3+((-1)**i)/(2*i+1))

print(np.pi)
print(4*pi1)
print(4*pi2)
print(4*pi3)



na = 10
nb = 100
nc = 1000
nd = 10000
x = 0
for j in range(1, na+1, 1):
    for t in range(0, 11, 1):
        x = x + ((np.sin((2*j-1)*t))/(2*j-1))
        print(j,t,x)






































