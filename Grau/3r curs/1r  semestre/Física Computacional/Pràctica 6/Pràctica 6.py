"""
Created on Wed Dec 21 11:46:03 2022

@author: joanribot
"""

# =============================================================================
# PRÀCTICA 6
# =============================================================================


import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# Representació dels camps sobre el domini
# =============================================================================

def phi(x,y):
    return 5370 - 143 * np.arctan(((np.pi * (y - 3.6*10**6 + 15*10**4))/(2*10**6))) - 160 / ( ((x - 3*10**6 + 5*10**4)/(4*10**5))**2 + ((y - 3*10**6 + 15*10**4)/(5*10**5))**2 + 1 )


def T(x,y):
    return 245 - 14.3 * np.arctan(((np.pi * (y - 3.6*10**6 - 15*10**4))/(2*10**6))) - 18 / ( ((x - 3*10**6 - 5*10**4)/(4*10**5))**2 + ((y - 3*10**6 - 15*10**4)/(5*10**5))**2 + 1 )


xm = 0
ym = 0
XM = 9000000 # 9000 km -> m
YM = 7200000 # 7200 km -> m
d = 90000 # 90 km -> m

dx = d
dy = d

xarray = np.arange(xm,XM,dx)
yarray = np.arange(ym,YM,dy)

X,Y = np.meshgrid(xarray,yarray)


R = 287.04 # J / kg K
p = 5 * 10**4 # Pa
p0 = 10**5 # Pa
Cp = 1005 # J / kg K
f0 = 10**-4 # 1/s


h = (R/p) * (p/p0)**(R/Cp)
sigma = 2.5 * 10**-6 # m^2 / s^2 Pa^2


# Càlcul de la matriu F_Q:
def F_Q():
    return - 2 * ( h / sigma ) * div(Q())


# Funció divergència d'una funció f:
def div(f):
    return partial_x(f[0]) + partial_y(f[1])


# Funció vector Q:
def Q():
    return np.array(( (partial_x(partial_y(phi(X,Y))) * partial_x(T(X,Y)) - partial_x(partial_x(phi(X,Y))) * partial_y(T(X,Y))) / f0, (partial_y(partial_y(phi(X,Y))) * partial_x(T(X,Y)) - partial_x(partial_y(phi(X,Y))) * partial_y(T(X,Y))) / f0 ))


# Derivada d'una funció respecte x emprant 3 punts:
def partial_x(f):

    rows = len(f[0,:])
    cols = len(f[:,0])
 
    # Matriu on es ficaran els valors de la derivada parcial respecte x:
    dxf = np.zeros((cols,rows)) 
 
    # En els extrems no podem emprar 3 punts, llavors n'empram 2:
    dxf[:,0] = (f[:,1] - f[:,0]) / d
    dxf[:,-1] = (f[:,-1] - f[:,-2]) / d
 
    # Només es fa el calcul per les files. Cada una correspon a una y
    # Pels punts interiors empram 3 punts:
    for y in range(1,rows-1):
        
        dxf[:,y] = (f[:,y+1] - f[:,y-1]) / (2*d)
     
    return dxf


# Derivada d'una funció respecte x emprant 3 punts:
def partial_y(f):

    rows = len(f[0,:])
    cols = len(f[:,0])
 
    # Matriu on es ficaran els valors de la derivada parcial respecte y:
    dyf = np.zeros((cols,rows))
 
    # En els extrems no podem emprar 3 punts, llavors n'empram 2:    
    dyf[0,:] = (f[1,:] - f[0,:]) / d
    dyf[-1,:] = (f[-1,:] - f[-2,:]) / d
 
    # Només es fa el calcul per les fcolumnes. Cada una correspon a una x
    # Pels punts interiors empram 3 punts:
    for x in range(1,cols-1):
        
        dyf[x,:] = (f[x+1,:] - f[x-1,:]) / (2*d)
    
    return dyf



## càlcul de β_opt ##
def Sol(apartat):
    
    # Representació dels apartats A, B i C:
    if apartat == 'ABC':

        xm = 0
        ym = 0
        XM = 9000000 # 9000 km -> m
        YM = 7200000 # 7200 km -> m
        d = 90000 # 90 km -> m

        dx = d
        dy = d

        xarray = np.arange(xm,XM,dx)
        yarray = np.arange(ym,YM,dy)

        X,Y = np.meshgrid(xarray,yarray)

        
        # Representació del camp Φ en 3D:
        fig = plt.figure(figsize=(12,9)) 
        ax = plt.axes(projection='3d') 
        ax.set_xlabel('x (m)') 
        ax.set_ylabel('y (m)') 
        ax.set_zlabel('Φ(x,y)') 
        ax.grid(True)
        plot1 = ax.plot_surface(X,Y,phi(X,Y),cmap='viridis',rstride=1, cstride=1,linewidth=0, antialiased=True,alpha=0.9) 
        plt.title("Representació de Φ(x,y)")
        fig.colorbar(plot1, shrink=0.75, aspect=20)
        plt.show()
   
        # Representació del camp Φ en 2D:
        fig = plt.figure(figsize=(10,8))
        plt.contourf(X,Y,phi(X,Y),cmap='viridis',levels=15)
        plt.colorbar()
        plt.ylabel('y (m)')
        plt.xlabel('x (m)')
        plt.title("Representació de Φ(x,y)")
        
        # Representació del camp T en 3D:
        fig = plt.figure(figsize=(12,9)) 
        ax = plt.axes(projection='3d') 
        ax.set_xlabel('x (m)')  
        ax.set_ylabel('y (m)') 
        ax.set_zlabel('T(x,y)')  
        ax.grid(True)
        plot2 = ax.plot_surface(X,Y,T(X,Y),cmap='inferno',rstride=1, cstride=1,linewidth=0, antialiased=True,alpha=0.9) 
        plt.title("Representació de T(x,y)")
        fig.colorbar(plot2, shrink=0.75, aspect=20)
        plt.show()
        
        # Representació del camp T en 2D:
        fig = plt.figure(figsize=(10,8))
        plt.contourf(X,Y,T(X,Y),cmap='inferno',levels=15) 
        plt.colorbar() 
        plt.ylabel('y (m)') 
        plt.xlabel('x (m)')
        plt.title("Representació de T(x,y)")
        
        
        # Representació de la funció F_Q en 3D:
        fig = plt.figure(figsize=(12,9)) 
        ax = plt.axes(projection='3d') 
        ax.set_xlabel('x (m)') 
        ax.set_ylabel('y (m)') 
        ax.set_zlabel('F_Q(x,y)') 
        ax.grid(True)
        plot3 = ax.plot_surface(Y,X,F_Q(),cmap='coolwarm',rstride=1, cstride=1,linewidth=1, antialiased=True,alpha=0.9) 
        plt.title("Representació de F_Q(x,y) (Forçament)")
        fig.colorbar(plot3, shrink=0.75, aspect=20) 
        plt.show()
        
        # Representació de la funció F_Q en 2D:     
        fig = plt.figure(figsize=(12,9)) 
        plt.contourf(X,Y,F_Q(),cmap='coolwarm',levels=8) 
        plt.colorbar() 
        plt.ylabel('y (m)') 
        plt.xlabel('x (m)')
        plt.title("Representació de F_Q(x,y) (Forçament)")


    # Solució per a B òptima:
    elif apartat == 'D':
        
        # Paràmetres del problema:
        xm = 0
        ym = 0
        XM = 9000000 # 9000 km -> m
        YM = 7200000 # 7200 km -> m
        d = 90000 # 90 km -> m
        
        m = XM/d
        n = YM/d
        
        lamb = np.sqrt( (2 * (f0)**2) / (sigma * (p-p0)**2) )

        # Paràmentres de l'apartat D:        
        Z = ( np.cos(np.pi/m) + np.cos(np.pi/n) ) * (2 / (4 + (lamb*d)**2) )
        c = 2/Z**2 - 1
        Bopt = 1 + c - np.sqrt(c**2 - 1)
        
        x = np.arange(0, XM, d) 
        y = np.arange(0, YM, d)
        m = len(x) 
        n = len(y)
        w = np.zeros((m,n)) 
        
        # Redefinim la funció FQ:
        FQ = F_Q() 
        
        # Comptador
        k = 0
        
        # Bucle per resoldre pel mètode SOR i Gauss-Seidel
        while True:
            
            k += 1
            w0 = np.copy(w)
            
            # Per a cada punt de l'eix x:
            for i in range(1,99):
                
                # Es calcula cada punt de l'eix y:
                for j in range(1,79):
                    
                    w[i,j] = w0[i,j] + (Bopt / (4 + lamb**4 * d**2)) * ( w0[i+1,j] + w[i-1,j] + w0[i,j+1] + w[i,j-1] - (4 + lamb**4 * d**2) * w0[i,j] - d**2 * FQ[j,i] )

            # Determinam la precissió que es demana en l'enunciat:
            if np.max(abs(w) - abs(w0)) < 0.001:
                break
        
        print("Han fet falta {} iteracions per resoldre SOR i Gauss-Seidel amb la β òptima ( Bopt = ".format(k),Bopt,") i una precisió de 10^-3.")
        
        x2 = np.arange(xm, XM, d) 
        y2 = np.arange(ym, YM, d)
        
        xx , yy = np.meshgrid(y2,x2)
        
        # Representació de la solució en 2D:
        fig = plt.figure(figsize=(10,8))
        plt.contourf(yy,xx,w,cmap='coolwarm',levels=8)
        plt.colorbar()
        plt.xlabel('x (m)')
        plt.ylabel('y (m)') 
        
        # Representació de la solució en 3D:    
        fig = plt.figure(figsize=(10,8)) 
        ax = plt.axes(projection='3d') 
        ax.set_xlabel('y (m)') 
        ax.set_ylabel('x (m)') 
        ax.set_zlabel('ω') 
        ax.grid(True) 
        X,Y = np.meshgrid(range(w.shape[1]),range(w.shape[0]))
        plot3 = ax.plot_surface(xx,yy,w,cmap='coolwarm',rstride=1, cstride=1,linewidth=1, antialiased=True,alpha=0.9)
        fig.colorbar(plot3, shrink=0.75, aspect=20) 
        plt.show()
       
    
    # Solució per a B = 1:
    elif apartat == 'E':
        
        # Paràmetres del problema:
        xm = 0
        ym = 0
        XM = 9000000 # 9000 km -> m
        YM = 7200000 # 7200 km -> m
        d = 90000 # 90 km -> m
        
        m = XM/d
        n = YM/d
        
        lamb = np.sqrt( (2 * (f0)**2) / (sigma * (p-p0)**2) )

        x = np.arange(0, XM, d) 
        y = np.arange(0, YM, d)
        m = len(x) 
        n = len(y)
        w = np.zeros((m,n))
        
        # Redefinim la funció FQ:
        FQ = F_Q() 
        
        # Comptador
        k = 0
        
        # Bucle per resoldre pel mètode SOR i Gauss-Seidel:
        while True:
            
            k += 1
            w0 = np.copy(w)
            
            # Per a cada punt de l'eix x:
            for i in range(1,99):
                
                # Es calcula cada punt de l'eix y:
                for j in range(1,79):
                    
                    w[i,j] = w0[i,j] + (1 / (4 + lamb**4 * d**2)) * ( w0[i+1,j] + w[i-1,j] + w0[i,j+1] + w[i,j-1] - (4 + lamb**4 * d**2) * w0[i,j] - d**2 * FQ[j,i] )

            if np.max(abs(w)-abs(w0)) < 0.001:
                break
            
        print("Han fet falta {} iteracions per resoldre SOR i Gauss-Seidel amb la β = 1 i una precisió de 10^-3.".format(k))  
        
        x2 = np.arange(xm, XM, d) 
        y2 = np.arange(ym, YM, d)
        xx , yy = np.meshgrid(y2,x2)
        
        # Representació de la solució en 2D:
        fig = plt.figure(figsize=(10,8)) 
        plt.contourf(yy,xx,w,cmap='coolwarm',levels=8) 
        plt.colorbar() 
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        
        # Representació de la solució en 3D:          
        fig = plt.figure(figsize=(10,8)) 
        ax = plt.axes(projection='3d') 
        ax.set_ylabel('x (m)')
        ax.set_xlabel('y (m)')
        ax.set_zlabel('ω')
        ax.grid(True) 
        X,Y = np.meshgrid(range(w.shape[1]),range(w.shape[0]))
        plot3 = ax.plot_surface(xx,yy,w,cmap='coolwarm',rstride=1, cstride=1,linewidth=1, antialiased=True,alpha=0.9) 
        fig.colorbar(plot3, shrink=0.75, aspect=20) 
        plt.show()


    # Solució per a B = 1 sense Gauss-Seidel:
    elif apartat == 'F':
        
        # Paràmetres del problema:
        xm = 0
        ym = 0
        XM = 9000000 # 9000 km -> m
        YM = 7200000 # 7200 km -> m
        d = 90000 # 90 km -> m
        
        m = XM/d
        n = YM/d
        
        lamb = np.sqrt( (2 * (f0)**2) / (sigma * (p-p0)**2) )

        x = np.arange(0, XM, d) 
        y = np.arange(0, YM, d)
        m = len(x) 
        n = len(y)
        w = np.zeros((m,n))
        
        # Redefinim la funció FQ:
        FQ = F_Q() 
        
        # Comptador
        k = 0
        
        # Bucle per resoldre pel mètode SOR:
        while True:
            
            k += 1
            w0 = np.copy(w)
            
            # Per a cada punt de l'eix x:
            for i in range(1,99):
                
                # Es calcula cada punt de l'eix y:
                for j in range(1,79):
                    
                    w[i,j] = w0[i,j] + ( 1 / (4 + lamb**4 * d**2)) * (w0[i+1,j] + w0[i-1,j] + w0[i,j+1] + w0[i,j-1] - ( 4 + lamb**4 * d**2) * w0[i,j] - d**2 * FQ[j,i] )

            if np.max(abs(w)-abs(w0)) < 0.001:
                break
            
        print("Han fet falta {} iteracions per resoldre SOR sense Gauss-Seidel amb la β = 1 i una precisió de 10^-3.".format(k))  
        
        x2 = np.arange(xm, XM, d) 
        y2 = np.arange(ym, YM, d)
        xx , yy = np.meshgrid(y2,x2)
        
        # Representació de la solució en 2D:
        fig = plt.figure(figsize=(10,8)) 
        plt.contourf(yy,xx,w,cmap='coolwarm',levels=8) 
        plt.colorbar() 
        plt.xlabel('x (m)')
        plt.ylabel('y (m)') 
        
        # Representació de la solució en 3D:
        fig = plt.figure(figsize=(10,8)) 
        ax = plt.axes(projection='3d') 
        ax.set_ylabel('x (m)') 
        ax.set_xlabel('y (m)') 
        ax.set_zlabel('ω') 
        ax.grid(True) 
        X,Y = np.meshgrid(range(w.shape[1]),range(w.shape[0]))
        plot3 = ax.plot_surface(xx,yy,w,cmap='coolwarm',rstride=1, cstride=1,linewidth=1, antialiased=True,alpha=0.9)
        fig.colorbar(plot3, shrink=0.75, aspect=20) 
        plt.show()



Sol('F')


