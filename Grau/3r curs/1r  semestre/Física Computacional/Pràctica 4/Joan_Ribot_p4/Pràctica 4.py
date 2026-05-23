"""
Created on Mon Nov  7 09:55:22 2022

@author: joanribot
"""

# =============================================================================
# PRÀCTICA 4
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import time


# Funció que resol pel mètode Thomas:
def thomas(theta,nu,I,d):
    
    # Arrays per la solució numèrica i pels paràmetres no constants de l'algorisme.
    U = np.zeros(I+1)
    e = np.zeros(I)
    f = np.zeros(I) 

    # Càlcul dels paràmetres constants de l'algorisme de Thomas.
    a = theta*nu
    b = 1+2*theta*nu
    c = theta*nu

    # Càlcul dels paràmetres no constants "cap endavant":
    for j in range(1,I):
     
        e[j] = c / ( b - a * e[j-1] )
     
        f[j] = ( d[j] + a * f[j-1] ) / ( b - a * e[j-1] )

    # Càlcul del valor de U per J-1
    U[I-1] = f[I-1]
 
    # Càlcul dels valors de la U numèrica, tenint en compte que anam "cap enrere" i ja coneixem el valor J-1:
    for j in range(I-2,0,-1):
     
        U[j] = f[j] + e[j] * U[j+1]
 
    return U # Retorna el següent valor de U com a resultat.


# Peaceman i Rachford
def PR(nu,R,S,CI):
    
    d_r = np.zeros(R)
    d_s = np.zeros(S)
 
    # Es calculen els vectors d a fora de l'algorisme de Thomas.
    # Primer calcul columna per columna.
    for r in range(1,R):
     
        # Càlcul del vector d no constant per cada columna:
        for s in range(1,S):
         
            d_s[s] = 1/2 * nu * U[r+1,s] + (1-nu) * U[r,s] + 1/2 * nu * U[r-1,s]
     
        # Us de l'algorisme de Thomas per les columnes. La notació de slice : significa que el càlcul és fa per totes les columnes.
        U[r,:] = thomas(theta,nu,S,d_s)
     
    # Segon calcul fila per fila.
    for s in range(1,S):
 
        # Càlcul del vector d no constant per cada fila:
        for r in range(1,R):
         
            d_r[r] = 1/2 * nu * U[r,s+1] + (1-nu) * U[r,s] + 1/2 * nu * U[r,s-1]

        # Us de l'algorisme de Thomas per les files.         
        U[:,s] = thomas(theta,nu,R,d_r)

    return U # Retorna el següent valor de U una vegada aplicat el mètode de Peaceman i Rachford.


# Codi python per llegir les lletres de la pràctica 4:
def llegeixCI():
    
    # Nom del fitxer de dades
    file_name="J_200x320.dat"
    
    # Lectura del fitxer linia a linia
    with open(file_name) as f:
        content=f.read().splitlines() 
    
    # Definim una matriu de 200 files (=y) i 320 columnes (=x) per guardar les dades de la condicio inicial
    un = np.zeros((200,320))
    
    # Guardam les dades a una matriu. Notar que: i=files=y, j=columnes=x
    for i in range(0,200):
         j=0
         for x in content[i]:
             un[i,j]=x
             j=j+1
    return un[::-1,:]


# Paràmetres per realitzar els càlculs:
nu = 0.75
theta = 0.5
R = 199
S = 319
U = llegeixCI()
T = [time.time()]
i = 0

# =============================================================================
# Delta t?
# =============================================================================

# R i S son 1 valor menor a la malla degut a que tenim condicions de contorn ja imposades.
# T és el paràmetre per veure quan temps tarda.
# i és el paràmetre iteratiu.
# theta val 0.5 ja que el mètode PR és una extensió del mètode C-N, que és per theta 0.5


# Representació de la lletra:
while True:

    if i in [0,10,100,500,1000,1500]:

        # Definim una malla per representar:
        x=np.arange(0,320,1)
        y=np.arange(0,200,1)        


        # Representació en 3D ja que és molt visual:
        X,Y = np.meshgrid(x,y)
        
        fig = plt.figure(figsize=(8,6))
        
        ax = fig.add_subplot(111, projection='3d')
        ax.set_title('Difusió')
        
        ax.set_xlabel('Eix x')
        ax.set_ylabel('Eix y')
        ax.set_zlabel('U')
        ax.set_zlim(0, 1)
        ax.view_init(55, -120)
        
        ploti = ax.plot_surface(X,Y,U,rstride=2, cstride=2,cmap=cm.inferno,linewidth=0, antialiased=False,alpha=0.95)
        fig.colorbar(ploti, shrink=0.75, aspect=20)
        plt.savefig('3d_iter{}_ν{}.svg'.format(i,nu))
        #plt.legend(['Iteració número {}'.format(i)])
        plt.show()


        # Representació en 2D:
        plt.figure(figsize=(6,4))
        plt.contourf(range(U.shape[1]),range(U.shape[0]),U,cmap=cm.inferno, antialiased=False)
        plt.xlabel('Eix x')
        plt.ylabel('Eix y')
        #plt.legend(['Iteració número {}'.format(i)])
        plt.title("Difusió")
        plt.colorbar()
        plt.savefig('ctr_iter{}_ν{}.svg'.format(i,nu))
        plt.show()
 
 
        # Representació d'una línia d'interés - Apartat G (opcional):
        plt.figure(figsize=(6,4))
        plt.xlabel("Eix x")
        plt.ylabel("U")
        plt.title('Representació de la fila s=165. Iteració {}'.format(i))
        plt.grid(True)
        plt.ylim(bottom=0,top=1)
        plt.plot(x,U[90,:],'r.-')
        plt.savefig('lin_iter{}_ν{}.svg'.format(i,nu))
        plt.show()


        print('Han passat:',T[-1]-T[0],'segons per arribar a la iteració {}'.format(i))

    if i > 1500:
        break
 
    U = PR(nu,R,S,U) # Calcula el següent valor de U usant el mètode de Peaceman i Rachford.
    
    T.append(time.time())
    
    i += 1 # Mira el temps tardat i afegeix un valor a la iteració.

print("Nu val",nu)


