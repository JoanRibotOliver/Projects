"""
Created on Wed Nov 30 13:24:01 2022

@author: joanribot
"""

# =============================================================================
# =============================================================================
# # PRÀCTICA 5
# =============================================================================
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# A
def gauss(amp, dev, pos, x):
    return amp * np.exp(-((x-pos)**2)/(2*dev**2))

x0 = 0
xf = 500 # cm

Dx = 2
J = (xf - x0) / Dx
xlist = np.zeros(int(J))

t0 = 0
tf = 90

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
#ona = []
ona = np.zeros(int(J))


while x <= xf:
    
    a = gauss(amp1, dev1, pos1, x)
    b = gauss(amp2, dev2, pos2, x)
    c = gauss(amp3, dev3, pos3, x)
         
    o1.append(a)
    o2.append(b)
    o3.append(c)
    
    x += Dx

for i in range(0,int(J),1):
    
    xlist[i] = i * Dx
    
    s = o1[i] + o2[i] + o3[i]
    
    ona[i] = s
   
plt.plot(xlist,ona,label="A")
plt.legend()

# B
x = np.zeros(int(J))
u0 = np.zeros(int(J))

for i in range(int(J)):
    x[i] = i * Dx
    
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
        
#plt.plot(xlist,u0,label="B")
#plt.legend()


# =============================================================================
# Apartat C)
# =============================================================================

a = 5 # cm / s
nu = 0.75

Dt = nu * Dx / a

k = 0 # Contador

tlist = [30,60,90] # Pel temps que volem representar



# =============================================================================
# REPRESENTAR ANALÍTICA VS NUMERICA --- FALTA POSAR-LA
# =============================================================================




# =============================================================================
# UPWIND ---- FUNCIONA
# =============================================================================

#print(u0,ona) # Són les dues condicions incials...

u = np.zeros(int(J))
w = np.zeros(int(J))

def Upwind():
    
    t0 = 0
    k = 0

    while t0 < tf:
    
        for j in range(1,int(J),1):
        
            u[0] = 0
            w[0] = 0
        
            u[j] = nu * ona[j-1] + (1-nu) * ona[j]
            w[j] = nu * u0[j-1] + (1-nu) * u0[j]
    
        k += 1
        t0 = k * Dt
    
        ona[:] = u[:]
        u0[:] = w[:]


        if t0 in tlist:
            plt.plot(xlist,ona,label=int(t0))
            #plt.plot(xlist,u0,label=int(t0))
            plt.legend()
            plt.title("Upwind")
            plt.loc='best'
    plt.show()

#Upwind()




# =============================================================================
# LAX - WENDROFF --- FUNCIONA
# =============================================================================


f = np.zeros(int(J))
g = np.zeros(int(J))

#REDEFINIR U0 I ONA... SINOS AGAFA EL VALOR DE UPWIND...

def LW():
    
    t0 = 0
    k = 0
    
    while t0 < tf:
    
        for j in range(1,int(J),1):
            
            if j == int(J-1):
                f[j] = f[j-1]
                g[j] = g[j-1]
        
            else:
                f[j] = 0.5 * nu * (1+nu) * ona[j-1] - 0.5 * nu * (1-nu) * ona[j+1] + (1-nu**2) * ona[j]
                g[j] = 0.5 * nu * (1+nu) * u0[j-1] - 0.5 * nu * (1-nu) * u0[j+1] + (1-nu**2) * u0[j]
            
        ona[:] = f[:]
        u0[:] = g[:]
     
        k += 1
        t0 = k * Dt
     
        # print(t0,k)

        if t0 in tlist:
            plt.plot(xlist,ona,label=int(t0))
            #plt.plot(xlist,u0,label=int(t0))
            plt.legend()
            plt.title("Lax - Wendroff")
            plt.loc='best'
    plt.show()
        
#LW()



""" Esquema de Lax-wendroff """
def lax_wendroff(U,J_t,J_x,ν):
    
    I_x = J_x-1
    
    for n in np.arange(0,J_t-1,1): # Es fa el càlcul per cada un dels punts de la malla temporal
    
        for j in np.arange(1,I_x,1):
            
            U[n+1,j] = 0.5*ν*(1+ν)*U[n,j-1] + (1-ν**2)*U[n,j] - 0.5*ν*(1-ν)*U[n,j+1] # Per cada punt de la malla temporal s'aplica Lax Wendroff.
        
        U[n,I_x] = U[n,I_x-1] # "Emprau condicions de contorn a x=500cm amb derivada nula U_j = U_j-1
        
    return U













"""
# =============================================================================
# LEAP - FROG --- NO FUNCIONA
# =============================================================================

while t0 < tf:
    
    for j in range(1,J,1):
        
        if j == J-1:
            u[j] = u[j-1]
        
        else:
            u[j] = ona[j] - nu * (ona[j-1] + ona[j+1])
            
        # Condició incial LW
 
    ona[:] = u[:]
     
    k += 1
     
    t0 = k * Dt
     
    #print(t0,k)
 
    if t0 in tlist:    
        plt.plot(xlist,ona,label=int(t0))
        plt.plot(xlist,u0,label=int(t0))
        plt.legend()
"""






""" Esquema upwind """
def upwind(U,J_t,J_x,ν):
 for n in np.arange(0,J_t-1,1): # Es fa el càlcul per cada un dels punts de la malla temporal
  for j in np.arange(1,J_x-1,1): U[n+1,j] = (1-ν)*U[n,j]+ν*U[n,j-1] # Per cada punt de la malla temporal s'aplica Upwind.
 return U





""" Esquema leap-frog """
def leap_frog(U,J_t,J_x,ν):
 I_x = J_x-1
 for n in np.arange(0,J_t-1,1): # Es fa el càlcul per cada un dels punts de la malla temporal
  for j in np.arange(1,I_x,1): 
   if n==0: U[n+1,j] = 0.5*ν*(1+ν)*U[n,j-1] + (1-ν**2)*U[n,j] - 0.5*ν*(1-ν)*U[n,j+1] # Inici per Lax_wndroff
   else: U[n+1,j] = U[n-1,j] - ν*(U[n,j+1]-U[n,j-1]) # Llavors Leap-Frog
  U[n,I_x] = U[n,I_x-1] # "Emprau condicions de contorn a x=500cm amb derivada nula U_j = U_j-1
 return U
