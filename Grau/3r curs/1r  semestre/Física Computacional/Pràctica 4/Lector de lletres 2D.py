"""
Created on Mon Nov  7 09:55:22 2022

@author: joanribot
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from mpl_toolkits.mplot3d import get_test_data
from matplotlib import cm,ticker

from pylab import *
from sympy import *
from sympy.abc import x, y

# Funció que resol pel mètode Thomas:
def thomas(a,b,c,d):
# a diag inferior   (n-1)
# b diag principal  (n)
# c diag superior   (n-1)
# d part de la dreta de Ax = d (n)
    a = a * -1
    c = c * -1
    n = len(b)
    x = np.zeros(n)
    e = np.zeros(n)
    f = np.zeros(n)
    #x = [0] * n # Es pot definir de les dues maneres i de les dues funciona...
    
    e[0] = c[0] / b[0]
    f[0] = d[0] / b[0]
    
    for j in range(n):
        e[j] = c[j] / (b[j] - a[j]*e[j-1])
        f[j] = (d[j] + a[j] * f[j-1]) / (b[j] - a[j]*e[j-1])

    x[n-1] = f[n-1]
    
    for j in range(n-2,-1,-1):
        x[j]=f[j]+e[j]*x[j+1]
    return x


#Codi python per llegir les lletres de la pràctica 4
def llegeixCI():
    
#Nom del fitxer de dades
    file_name="J_200x320.dat"
    
#Lectura del fitxer linia a linia
    with open(file_name) as f:
        content=f.read().splitlines()
        
#Definim una matriu de 200 files (=y) i 320 columnes (=x) per guardar les dades de la condicio inicial
    un=np.zeros((200,320))
    
#Guardam les dades a una matriu. Notar que: i=files=y, j=columnes=x
    for i in range(0,200):
        j=0
        for x in content[i]:
            un[i,j]=x
            j=j+1
    return un

#plt.imshow(llegeixCI())

# Representar també en 3D

"""
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,T,cmap='coolwarm',rstride=True,cstride=True)
ax.set_title("x")
show()

ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,phi,cmap='viridis',rstride=True,cstride=True)
show()
"""


# Funció que resol pel mètode Thomas:
def thomas(a,b,c,d):
# a diag inferior   (n-1)
# b diag principal  (n)
# c diag superior   (n-1)
# d part de la dreta de Ax = d (n)
    a = a * -1
    c = c * -1
    n = len(b)
    x = np.zeros(n)
    e = np.zeros(n)
    f = np.zeros(n)
    #x = [0] * n # Es pot definir de les dues maneres i de les dues funciona...
    
    e[0] = c[0] / b[0]
    f[0] = d[0] / b[0]
    
    for j in range(n):
        e[j] = c[j] / (b[j] - a[j]*e[j-1])
        f[j] = (d[j] + a[j] * f[j-1]) / (b[j] - a[j]*e[j-1])

    x[n-1] = f[n-1]
    
    for j in range(n-2,-1,-1):
        x[j]=f[j]+e[j]*x[j+1]
    return x

# =============================================================================
# Peaceman - Rachford
# =============================================================================

# Discretització de la regió:
X = 320
Y = 200

d = 5
Jx = d
Jy = d

dx = X / Jx
dy = Y / Jy


# Condicions de contorn:




sigma = 1
dt = 1 # ?

nux = sigma * dt / dx**2 # 0.75
nuy = sigma * dt / dy**2 # 0.75


# Matriu U(i,j)

# Matriu U+1/2(i,j)


# =============================================================================
# On u ha de ser sa llista de files de sa lletra
# =============================================================================

def Un(x,y):
    
    while t0 <= tf:
        
        # Algorisme de Thomas:
        for i in range(1,J-1,1):
        
            d[i] = (1 + (1-theta)*nu*-2)*u0[i] + (1-theta)*nu*u0[i+1] + (1-theta)*nu*u0[i-1]
        
        u = thomas(a, b, c, d)
        
        u0 = u # Calculam u1 i repetim els càlculs per conéixer d1, llavors u2 i successivament.
       
    t0 += dt # Sumam el contador de temps
    t0 = round(t0,10) # Perque tot funcionàs he hagut d'arrodonir... tenia problemes amb el darrer decimal que guarda python (10**-16).
        
    
    return x,y

def Unp1(x,y):
    
    return x,y




