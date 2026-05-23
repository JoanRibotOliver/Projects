#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:24:01 2022

@author: joanribot
"""


# =============================================================================
# =============================================================================
# # Joan Ribot Oliver, PRÀCTICA 1, APARTAT B), Entrega 16/11/2022
# =============================================================================
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt


def f(x,y): # Funció que volem integrar, donada per l'enunciat.
    return (-1/(x**2)) - 4*(x-6)*np.exp(-2*((x-6)**2))


def sol_analitica(x): # Solució analítica a la funció f, calculada amb les condicions inicials de l'enunciat.
    return 1/x + np.exp(-2*((x-6)**2)) - np.exp(-50)

# Funció de python que resol EDo's de 1r ordre:
    # Ordre, funció, posició inicial, posició final, condició inicial, pas inicial, error tolerable i flag per activar o desactivar el mètode de Fehlberg.
def RKFo1(o,f,x0,xf,y0,h,tol,flag):
    
    # Llistes que ens serviran per representar les solucions.
    xlist = []
    ylist = []
    hlist = []
    errorlist = []
    
    # Bucle per iterar dins l'interval.
    while x0 <= xf:
        
        # Afegim els primers termes: les condicions inicials.
        xlist.append(x0)
        ylist.append(y0)
        
        # Si aplicam l'algorisme de Fehlberg.
        if flag == True:
            
            # Funcions del mètode RK fins ordre 5.
            f0 = f(x0,y0)
            f1 = f((x0 + h/4),(y0 + h/4 * f0))
            f2 = f((x0 + 3*h/8),(y0 + 3*h*f0/32 + 9*h*f1/32))
            f3 = f((x0 + 12*h/13),(y0 + 1932*h*f0/2197 - 7200*h*f1/2197 + 7296*h*f2/2197))
            f4 = f((x0 + h),(y0 + 439*h*f0/216 + -8*h*f1 + 3680*h*f2/513 - 845*h*f3/4104))
            f5 = f((x0 + h/2),(y0 -8*h*f0/27 + 2*h*f1 - 3554*h*f2/2565 + 1859*h*f3/4104 + -11*h*f4/40))
            
            # Nou pas d'iteració calculat com es menciona en l'informe.
            hnou = (0.9*h*(tol/(h*abs(1/360*f0-128/4275*f2-2197/75240*f3+f4/50+2*f5/55)))**(1/4))
            
            # Mentre el nou pas d'integració sigui major al  del pas anterior:
            if hnou >= h:
                h = hnou
            
            # Mentre el nou pas d'integració sigui menor al del pas anterior:
            while hnou <= h:
                h = hnou
                
                # Tornam a definir les funcions de RK perque es realitzin de nou els càlculs amb el pas adaptat correctament.
                f0 = f(x0,y0)
                f1 = f((x0 + h/4),(y0 + h/4 * f0))
                f2 = f((x0 + 3*h/8),(y0 + 3*h*f0/32 + 9*h*f1/32))
                f3 = f((x0 + 12*h/13),(y0 + 1932*h*f0/2197 - 7200*h*f1/2197 + 7296*h*f2/2197))
                f4 = f((x0 + h),(y0 + 439*h*f0/216 + -8*h*f1 + 3680*h*f2/513 - 845*h*f3/4104))
                f5 = f((x0 + h/2),(y0 -8*h*f0/27 + 2*h*f1 - 3554*h*f2/2565 + 1859*h*f3/4104 + -11*h*f4/40))
                
                # Calculam de nou el pròxim pas.
                hnou = (0.9*h*(tol/(h*abs(1/360*f0-128/4275*f2-2197/75240*f3+f4/50+2*f5/55)))**(1/4))
                
            
        # Definim les funcions del mètode RK per aproximar les solucions sense l'algorisme de Fehlberg.
        f0 = f(x0,y0)
        f1 = f((x0 + h/4),(y0 + h/4 * f0))
        f2 = f((x0 + 3*h/8),(y0 + 3*h*f0/32 + 9*h*f1/32))
        f3 = f((x0 + 12*h/13),(y0 + 1932*h*f0/2197 - 7200*h*f1/2197 + 7296*h*f2/2197))
        f4 = f((x0 + h),(y0 + 439*h*f0/216 + -8*h*f1 + 3680*h*f2/513 - 845*h*f3/4104))
        f5 = f((x0 + h/2),(y0 -8*h*f0/27 + 2*h*f1 - 3554*h*f2/2565 + 1859*h*f3/4104 + -11*h*f4/40))
        
        # Si l'ordre desitjat és 4:
        if o == 4:
            
            y0 = y0 + h*(25*f0/216 + 1408*f2/2565 + 2197*f3/4104 - 1*f4/5)
            
        # Si l'ordre desitjat és 5:
        elif o == 5:
            
            y0 = y0 + h*(16*f0/135 + 6656*f2/12825 + 28561*f3/56430 - 9*f4/50 + 2*f5/55)
        
        # En el cas de que l'ordre no sigui ni 4 ni 5:
        else:
            return "L'ordre seleccionat és diferent de 4 ò 5"
        
        # Avançam dins el bucle: calculam l'error i afegim tant el pas com l'error a les seves corresponents llistes
        x0 = x0 + h
        hlist.append(h)
        err = h * abs(1/360*f0-128/4275*f2-2197/75240*f3+f4/50+2*f5/55)
        errorlist.append(err)
        
    # Representam tot el que ens interessa:
    plt.plot(xlist,ylist,"ro",label="RKF, h inicial = 0.1"), plt.xlabel("Eix x"), plt.ylabel("Eix y")
    plt.plot(np.linspace(1,10,100),sol_analitica(np.linspace(1,10,100)),"g-",label="Solució analítica"), plt.grid(), plt.legend()
    plt.show()
    
    plt.plot(xlist,hlist,"bo-"), plt.xlabel("Eix x"), plt.ylabel("Pas d'integració (h)"), plt.grid()
    plt.show()
    
    plt.plot(xlist,errorlist,"co-"), plt.xlabel("Eix x"), plt.ylabel("Error"), plt.grid(), plt.show()

    
    return "Finalitzat!"
    
# Imprimim la funció creada amb les condicions inicials de l'enunciat.
print(RKFo1(o = 4,f = f,x0 = 1,xf = 10,y0 = 1,h = 10**-1,tol = 10**-6,flag = True))



