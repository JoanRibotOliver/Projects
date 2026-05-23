#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:15:40 2022

@author: joanribot
"""

# =============================================================================
# =============================================================================
# # Joan Ribot Oliver, PRÀCTICA 1, APARTAT C), Entrega 16/11/2022
# =============================================================================
# =============================================================================

import matplotlib.pyplot as plt

# El problema és resoldre l'equació diferencial de l'oscil·lador de Van der Pol.

# Sistema de funcions de 1r ordre a integrar:
    
# Funció acceleració, derivada de la velocitat respecte el temps. L'acceleració depèn de la velocitat i de la posició.
def v(t,x,v,m=4):
    return m*(1-x**2)*v-x
# És important el nombre de m, que és el coeficient d'esmorteïment de l'oscil·lador.

# Funció velocitat, derivada de la posició respecte el temps.
def x(t,x,v):
    return v


# Inicialment es crea una funció que resolgui les fórmules de RK d'ordre 4 i 5:
# Ordre, t0, x0, v0, funcions, h, paràmetre (posició ò velocitat)
def RK45(o,t0,x0,v0,f,g,h,n):
    
    # Fórmules de RK fins ordre 5:
    f0=f(t0,x0,v0)
    g0=g(t0,x0,v0)
    f1=f(t0+h/4,x0+h/4*f0,v0+h/4*g0)
    g1=g(t0+h/4,x0+h/4*f0,v0+h/4*g0)
    f2=f(t0+3*h/8,x0+3*h/32*f0+9*h/32*f1,v0+3*h/32*f0+9*h/32*g1)
    g2=g(t0+3*h/8,x0+3*h/32*f0+9*h/32*f1,v0+3*h/32*f0+9*h/32*g1)
    f3=f(t0+12*h/13,x0+1932*h/2197*f0-7200*h/2197*f1+7296*h/2197*f2,v0+1932*h/2197*g0-7200*h/2197*g1+7296*h/2197*g2)
    g3=g(t0+12*h/13,x0+1932*h/2197*f0-7200*h/2197*f1+7296*h/2197*f2,v0+1932*h/2197*g0-7200*h/2197*g1+7296*h/2197*g2)
    f4=f(t0+h,x0+439*h/216*f0-8*h*f1+3680*h/513*f2-845*h/4104*f3,v0+439*h/216*g0-8*h*g1+3680*h/513*g2-845*h/4104*g3)
    g4=g(t0+h,x0+439*h/216*f0-8*h*f1+3680*h/513*f2-845*h/4104*f3,v0+439*h/216*g0-8*h*g1+3680*h/513*g2-845*h/4104*g3)
    f5=f(t0+h/2,x0-8*h/27*f0+2*h*f1-3544*h/2565*f2+1859*h/4104*f3-11*h/40*f4,v0-8*h/27*g0+2*h*g1-3544*h/2565*g2+1859*h/4104*g3-11*h/40*g4)
    g5=g(t0+h/2,x0-8*h/27*f0+2*h*f1-3544*h/2565*f2+1859*h/4104*f3-11*h/40*f4,v0-8*h/27*g0+2*h*g1-3544*h/2565*g2+1859*h/4104*g3-11*h/40*g4)
    
    # Solucions a les fórmules d'ordre 4 i 5 de les variables dependents:
    xo4 = x0+(h*(((25*f0)/216)+((1408*f2)/2565)+((2197*f3)/4104)-((f4)/5)))
    vo4 = v0+(h*(((25*g0)/216)+((1408*g2)/2565)+((2197*g3)/4104)-((g4)/5)))
    xo5 = x0+(h*(((16*f0)/135)+((6656*f2)/12825)+((28561*f3)/56430)-((9*f4)/50)+((2*f5)/55)))
    vo5 = v0+(h*(((16*g0)/135)+((6656*g2)/12825)+((28561*g3)/56430)-((9*g4)/50)+((2*g5)/55)))
    
    # Si l'ordre és 4 i volem la posició:
    if o == 4 and n==1 :
        return xo4
    # Si l'ordre és 4 i volem la velocitat:
    elif o==4 and n==2 :
        return vo4
    # Si l'ordre és 5 i volem la posició:
    if o == 5 and n==1 :
        return xo5
    # Si l'ordre és 5 i volem la velocitat:
    elif o==5 and n==2 :
        return vo5
    
# Funció que resol 2 EDO's de qr ordre, que a més són dependents:
# Ordre, funcions, t0, tf, x0, v0, h, toleràncies, flag (Fehlberg)
def RKFo2(o,f,g,t0,tf,x0,v0,h,tolx,tolv,flag):
    
    # Llistes per més tard representar gràficament els resultats
    tlist = []
    xlist = []
    vlist = []
    hlist = [] 
   
    # Si el Fehlberg està desactivat:
    if flag == False:
       
       # Bucle per iterar dins l'interval de temps
       while t0 < tf:
           
            # Afegim les condicions inicials a la llista:
            tlist.append(t0)
            xlist.append(x0)
            vlist.append(v0)
            
            # Calculam els nous valors de velocitat i posició:
            x = RK45(o,t0,x0,v0,f,g,h,1)
            v = RK45(o,t0,x0,v0,f,g,h,2)
                        
            # S'avança dins el bucle
            t = t0 + h
            
            # I es redefineixen els nous valors de velocitat i posició:
            t0 = t
            x0 = x
            v0 = v
   
    # En el cas de que el Fehlberg estigui activat:
    elif flag == True:
        
        # Bucle per iterar dins l'interval de temps
        while t0 < tf:
            
            # Es calculen les noves variables de posició i velocitat cridant a la funció RK:
            xo4 = RK45(o,t0,x0,v0,f,g,h,1)
            vo4 = RK45(o,t0,x0,v0,f,g,h,2)
            xo5 = RK45(o+1,t0,x0,v0,f,g,h,1)
            vo5 = RK45(o+1,t0,x0,v0,f,g,h,2)
            
            # Es calcula el seu error fent la diferència entre les aproximacions per l'ordre 4 i 5:
            errorx = abs(xo5-xo4)
            errorv = abs(vo5-vo4)
            
            # Es calcula el nou pas d'integració per a cada variable dependent (posició i velocitat):
            hnx = 0.9*h*(((tolx)/(errorx))**(1/4))
            hnv = 0.9*h*(((tolv)/(errorv))**(1/4))
            
            # I s'escull el menor:
            hn = min(hnx,hnv)
            
            # Si el nou pas és menor a l'anterior:
            if hn < h:
                h = hn
                
            # En qualsevol altre cas (nou pas major a l'anterior), es repeteix tot el procés:
            else:
                # Es calculen les variables de posició i velocitat de nou, cridant RK:
                xo4 = RK45(o,t0,x0,v0,f,g,h,1)
                vo4 = RK45(o,t0,x0,v0,f,g,h,2)
                xo5 = RK45(o+1,t0,x0,v0,f,g,h,1)
                vo5 = RK45(o+1,t0,x0,v0,f,g,h,2)
                
                # S'afegeixen aquests a les corresponents llistes, juntament amb el temps:
                tlist.append(t0)
                xlist.append(x0)
                vlist.append(v0)
                
                # Es calculen els seu errors fent la diferència entre les aproximacions per l'ordre 4 i 5:
                errorx = abs(xo5-xo4)
                errorv = abs(vo5-vo4)
                
                # Es redefineixen els nous valors de posició i velocitat:
                x0 = xo5
                v0 = vo5
                
                # S'avança dins el bucle:
                t0 = t0 + h
                
                # I s'afegeix a la llista de passes d'integració el valor pel que s'ha realitzat aquest procés:
                h = hn
                hlist.append(h)
                
    # Finalment es representen les dades obtingudes:
    plt.plot(xlist,vlist,"ro-"), plt.xlabel("x (m)"), plt.ylabel("v (m/s)"), plt.grid()
    plt.show()            
    
    plt.plot(tlist,xlist,"mo-"), plt.xlabel("t (s)"), plt.ylabel("x (m)"), plt.grid()
    plt.show()
    
    plt.plot(tlist,vlist,"co-"), plt.xlabel("t (s)"), plt.ylabel("v (m/s)"), plt.grid()
    plt.show()
    
    # En el cas de que el Fehlberg estigui activat també es representa el canvi del pas en funció del temps:
    if flag == True:
        plt.plot(tlist,hlist,"b-"), plt.xlabel("t (s)"), plt.ylabel("Pas d'integració (h)"), plt.grid()
        plt.show()             
                
    return "Finalitzat!" 
    

# Cridam a la funció que resol 2 EDO's de 1r ordre amb les CI que marca l'enunciat:
# Ordre, funcions, t0, tf, x0, v0, h, errors, flag (Fehlberg)
print(RKFo2(o = 4,f = x,g = v,t0 = 0,tf = 21,x0 = 2,v0 = 0,h = 0.01,tolx = 10**-3,tolv = 10**-5,flag = 1))






