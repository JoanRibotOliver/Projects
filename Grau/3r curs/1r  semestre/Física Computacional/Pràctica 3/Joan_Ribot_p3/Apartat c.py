"""
Created on Wed Oct 26 11:15:13 2022

@author: joanribot
"""

# =============================================================================
# =============================================================================
# PRÀCTICA 3, APARTAT C)
# =============================================================================
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import time

# Demanam per quines CI es vol resoldre:  
I = input("Quines condicions inicials s'apliquen: les de l'apartat a) o les del b)?")

# El comptador de temps que tarda el programa en córrer s'inicia...
inici = time.time()

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


# Paràmetres del mètode Theta.
J = 41

x = np.zeros(J)
dx = 1/(J-1) # Pas de posició segons el paràmetre J.

theta = 0.75
nu = 0.2
#mu = 1/4
#nu = mu / dx
mu = nu * dx

# Varis comptadors del programa.
i = 0
k = 0
l = 0

t0 = 0 # Definim el temps inicial.
tf = 0.5 # I el temps final.
dt = nu * dx**2 # El pas de temps ve definit pel nombre de punts amb els que es separa l'espai (uniformement).

# Arrays buides per resoldre Thomas... s'ompliran a mesura que el programa fa càlculs.
a = np.zeros(J)
c = np.zeros(J)
b = np.zeros(J)
d = np.zeros(J)
u = np.zeros(J)
u0 = np.zeros(J)

# Llistes pel nombre d'iteracions als quals es volen estudiar els resultats del programa.
Elist1 = []
Elist2 = []
    
# Nombre de termes de la sumatòria de la solució analítica.
n = 1000
 
# Llistes per resoldre la solució analítica.
u_a1 = np.zeros(J)
u_a2 = np.zeros(J)

# =============================================================================
# Perfil a
# =============================================================================
if I == "a" or I == "a)" or I == "A":
    
    # Bucle per aplicar les C.I. a):
    for i in range(J):
        x[i] = i * dx
             
        if x[i] <= 0.5:
            u0[i] = 2 * x[i]
        
        elif x[i] >= 0.5 and u0[i] <= 1:
            u0[i] = 2 - 2 * x[i]

        a[i] = -theta*nu
        b[i] = (1+2*theta*nu)
        c[i] = -theta*nu
        # Vectors constants en totes les iteracions
        
    # Bucle pel temps...
    while t0 <= tf:
        
        # Dins l'interval de temps calculam Thomas i l'analítica a cada iteració, les restam i sabem E.
        
        # Algorisme de Thomas:
        for i in range(1,J-1,1):
        
            d[i] = (1 + (1-theta)*nu*-2)*u0[i] + (1-theta)*nu*u0[i+1] + (1-theta)*nu*u0[i-1]
        
        u = thomas(a, b, c, d)
        
        u0 = u # Calculam u1 i repetim els càlculs per conéixer d1, llavors u2 i successivament.

        # A partir d'aquest nou t0 hem de començar a calcular l'analítica...
        if t0 >= 0.1:

            for l in range(0,J,1):
                
                p = 0
                g = l * dx
                
                for m in range(1,n+1,1):
                    
                    p += 4 * (2*np.sin(m*np.pi/2)-np.sin(m*np.pi))* np.sin(m*np.pi*g) * np.exp(- m**2 * (np.pi)**2 * t0) / (m*np.pi)**2
                
                u_a1[l] = p

            # Calculam ñ'error a partir de la diferència entre soluions.
            E1 = abs(u-u_a1)
            Elist1.append(max(E1))
            
            print(max(Elist1))

        t0 += dt # Sumam el contador per fer el bucle.
        
# =============================================================================
# Perfil b
# =============================================================================
elif I == "b" or I == "b)" or I == "B":

    # Bucle per aplicar les C.I. b):
    for i in range(J):
        x[i] = i * dx
    
        if 0.25 <= x[i] <= 0.75:
            u0[i] = 1
        
        else:
            u0[i] = 0

        a[i] = -theta*nu
        b[i] = (1+2*theta*nu)
        c[i] = -theta*nu
        # Vectors constants en totes les iteracions
    
    # Bucle pel temps...
    while t0 <= tf:
        
        # Dins l'interval de temps calculam Thomas i l'analítica a cada iteració, les restam i sabem E.
        
        # Thomas:
        for i in range(1,J-1,1):
        
            d[i] = (1 + (1-theta)*nu*-2)*u0[i] + (1-theta)*nu*u0[i+1] + (1-theta)*nu*u0[i-1]
        
        u = thomas(a, b, c, d)
        
        u0 = u # Calculam u1 i repetim els càlculs per conéixer d1, llavors u2 i successivament.
        
        # Calculam l'analítica a partir de t0 > 0.1:
        if t0 >= 0.1:

            for l in range(0,J,1):
                
                q = 0
                g = l * dx
                
                for m in range(1,n+1,1):
                    
                    q += 4*(np.sin(m*np.pi/4)*np.sin(m*np.pi/2))*np.sin(m*g*np.pi)*np.exp(- m**2 * (np.pi)**2 * t0)/(m*np.pi)
            
                u_a2[l] = q
            
            # Calculam ñ'error a partir de la diferència entre soluions.
            E2 = abs(u-u_a2)
            Elist2.append(max(E2))
        
            print(max(Elist2))
        
        t0 += dt # Sumam el contador per fer el bucle.


print("Theta:",theta,", Nu",nu,", Mu",mu)
        
final = time.time()
print("El programa ha tardat "+str(final-inici)+" segons")
print("El programa ha tardat "+str((final-inici)/60)+" minuts")
print("El programa ha tardat "+str((final-inici)/3600)+" hores")

