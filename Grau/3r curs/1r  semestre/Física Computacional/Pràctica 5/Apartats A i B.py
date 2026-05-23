#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:24:01 2022

@author: joanribot
"""

# =============================================================================
# =============================================================================
# # PRÀCTICA 5, CONDICIONS INICIALS A I B
# =============================================================================
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Apartat A
# =============================================================================
    
# Funció gaussiana
def gauss(amp, dev, pos, x):
    return amp * np.exp(-((x-pos)**2)/(2*dev**2))

x0 = 0
xf = 500 # cm
t0 = 0
tf = 90 # s

J = (xf - x0)

amp1 = 2
dev1 = 20
pos1 = 50

amp2 = -2
dev2 = 10
pos2 = 30

amp3 = 1
dev3 = 4
pos3 = 58

x = 0
o1 = []
o2 = []
o3 = []
ona = np.zeros(int(J))

xlist = np.zeros(int(J))
dx = 1/(J-1)



while x <= xf:
    
    a = gauss(amp1, dev1, pos1, x)
    b = gauss(amp2, dev2, pos2, x)
    c = gauss(amp3, dev3, pos3, x)
         
    o1.append(a)
    o2.append(b)
    o3.append(c)
    
    x = x + 1

for i in range(0,J-1,1):
    xlist[i] = i * dx
    
    d = o1[i] + o2[i] + o3[i]
    ona[i] = d
    

#plt.plot(o1,"r.",label="Ona 1")
#plt.plot(o2,"b.",label="Ona 2")
#plt.plot(o3,"y.",label="Ona 3")

plt.plot(ona,label="Ona incial A")
plt.legend()

# =============================================================================
# Apartat B)
# =============================================================================

x0 = 0
xf = 500 # cm

x = [0] * int(J)
dx = 1
u0 = np.zeros(J)

for i in range(J):
    x[i] = i * dx
    
    if x[i] < 20:
        u0[i] = 0
        
    elif 20 <= x[i] <= 30:
        u0[i] = 2
        
    elif 30 <= x[i] <= 35:
        u0[i] = 1
        
    elif 35 <= x[i] <= 40:
        u0[i] = -1
        
    elif x[i] >= 40:
        u0[i] = 0
        
plt.plot(u0,label="Ona inicial B")
plt.legend()



