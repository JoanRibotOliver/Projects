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



# Aproximació de la solució
def Sol(mètode):

    # Paràmetres del problema:
    a = 5
    nu = 0.75
    
    Dx = 2
    Dt = Dx * nu / a
    
    # Posició i temps inicial:
    x0 = 0
    t0 = 0
    
    # Posició i temps final:
    xf = 500
    tf = 90
    
    # Separació
    Jx = int(xf/Dx+1)
    Jt = int(tf/Dt+1)
    
    
    # Condició inicial apartat A:
    if mètode == 'CIA':
        
        CI = 'A'
        
        U = C0(Jt,Jx,xf,CI)
        U_a1 = AN(U,Jt,Jx,nu,CI)
        legend = ['Solució analítica']
        
        plt_2d(xf,Jx,Jt,U,Dx,nu,tf,legend)
        
        
    # Condició inicial apartat B:
    elif mètode == 'CIB':
        
        CI = 'B'
        
        U = C0(Jt,Jx,xf,CI)
        U_a1 = AN(U,Jt,Jx,nu,CI)
        legend = ['Solució analítica']
        
        plt_2d(xf,Jx,Jt,U,Dx,nu,tf,legend)
    
    
    # Solució pel mètode Upwind amb la condicó inicial de l'apartat A:
    elif mètode == 'UW1A':
        
        CI = 'A'
        
        U = C0(Jt,Jx,xf,CI)
        U_uw1 = UW(U,Jt,Jx,nu)
        legend = ['Solució numèrica per Upwind']
        plt_2d(xf,Jx,Jt,U_uw1,Dx,nu,tf,legend)
        
            
    # Comparació per a diferents passos de temps amb condició inicial A:
    elif mètode == 'UW2A':
        
        CI = 'A'
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            
            Dx = 2
            nu = 0.75
            Dt = Dx*nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:],'b')
            
            U01 = C0(Jt,Jx,xf,CI)
            U1 = UW(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:],'r')
            
            Dx = 10
            nu = 0.75
            Dt = Dx*nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = UW(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:],'y')
            
            Dx = 0.1
            nu = 0.75
            Dt = Dx*nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U03 = C0(Jt,Jx,xf,CI)
            U3 = UW(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:],'g')
            
            plt.legend((['Analítica','Δx = 2 cm','Δx = 10 cm','Δx = 0.1 cm']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Upwind, ν = 0.75, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
        
        
    # Comparació per a diferents valors de nu (relació del pas del temps respecte el pas d'espai) amb la condició inicial A:
    elif mètode == 'UW3A':
    
        CI = 'A'
        Dx = 2
                    
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            nu = 0.75
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.5
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI)
            U1 = UW(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.9
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = UW(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:])
            
            nu = 1
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U03 = C0(Jt,Jx,xf,CI)
            U3 = UW(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:])
            
            plt.legend((['Analítica','ν = 0.5','ν = 0.9','ν = 1']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Upwind, Δx = 2 cm, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
    
            
    # Solució pel mètode Upwind amb la condicó inicial de l'apartat B:
    elif mètode == 'UW1B':
        
        CI = 'B'
        
        U = C0(Jt,Jx,xf,CI)
        U_uw1 = UW(U,Jt,Jx,nu)
        legend = ['Solució numèrica per Upwind']
        
        plt_2d(xf,Jx,Jt, U_uw1, Dx, nu,tf,legend)
        
    
    # Comparació per a diferents passos de temps amb condició inicial B:
    elif mètode == 'UW2B':
        
        CI = 'B'
        nu = 0.75
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))

            Dx = 2
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:],'b')
            
            U01 = C0(Jt,Jx,xf,CI)
            U1 = UW(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:],'r')
            
            Dx = 10
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = UW(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:],'y')
            
            Dx = 0.1
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U03 = C0(Jt,Jx,xf,CI)
            U3 = UW(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:],'g')
            
            plt.legend((['Analítica','Δx = 2 cm','Δx = 10 cm','Δx = 0.1 cm']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Upwind, ν = 0.75, t = {} segons".fomrat(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
    
        
    # Comparació per a diferents valors de nu (relació del pas del temps respecte el pas d'espai) amb la condició inicial B:
    elif mètode == 'UW3B':
    
        CI = 'B'
        Dx = 2
                    
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            nu = 0.75
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.5
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI)
            U1 = UW(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.9
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = UW(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:])
            
            nu = 1
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U03 = C0(Jt,Jx,xf,CI)
            U3 = UW(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:])
            
            plt.legend((['Analítica','ν = 0.5','ν = 0.9','ν = 1']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Upwind, Δx = 2 cm, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
  

    # Solució pel mètode Lax-Wendroff amb la condicó inicial de l'apartat A:
    elif mètode == 'LW1A':
        
        CI = 'A'
        Dx = 2
        nu = 0.75
        Dt = Dx * nu/a
        Jx = int(xf/Dx+1)
        Jt = int(tf/Dt+1)
        
        U = C0(Jt,Jx,xf,CI)
        U_lw1 = LW(U,Jt,Jx,nu)
        legend = ['Solució numèrica per Lax-Wendroff']
        plt_2d(xf,Jx,Jt,U_lw1,Dx,nu,tf,legend)
    

    # Comparació per a diferents passos de temps amb condició inicial A:
    elif mètode == 'LW2A':
        
        CI = 'A'
        nu = 0.75
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            
            Dx = 2
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:],'b')
            
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI)
            U1 = LW(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:],'r')
            
            Dx = 10 
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = LW(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:],'y')
            
            Dx = 0.1
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U03 = C0(Jt,Jx,xf,CI)
            U3 = LW(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:],'g')
            
            plt.legend((['Analítica','Δx = 2 cm','Δx = 10 cm','Δx = 0.1 cm']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Lax-Wendroff, ν = 0.75, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
  
    
    # Comparació per a diferents valors de nu (relació del pas del temps respecte el pas d'espai) amb la condició inicial A:
    elif mètode == 'LW3A':
        
        CI = 'A'
        Dx = 2
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.5
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI)
            U1 = LW(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.9
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = LW(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:])
            
            nu = 1
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U03 = C0(Jt,Jx,xf,CI)
            U3 = LW(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:])
            
            plt.legend((['Analítica','ν = 0.5','ν = 0.9','ν = 1']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Lax-Wendroff, Δx = 2 cm, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
            
            
    # Solució pel mètode Lax-Wendroff amb la condicó inicial de l'apartat B:   
    elif mètode == 'LW1B':
        
        CI = 'B'
        Dx = 2
        nu = 0.75
        Dt = Dx * nu/a
        Jx = int(xf/Dx+1)
        Jt = int(tf/Dt+1)
        
        U = C0(Jt,Jx,xf,CI)
        U_lw1 = LW(U,Jt,Jx,nu) # Càlcul 
        legend = ['Solució numèrica per Lax-Wendroff']

        plt_2d(xf,Jx,Jt,U_lw1,Dx,nu,tf,legend)


    # Comparació per a diferents passos de temps amb condició inicial B:
    elif mètode == 'LW2B':
        
        CI = 'B'
        nu = 0.75
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            
            Dx = 2
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:],'b')
            
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI)
            U1 = LW(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:],'r')
            
            Dx = 10 
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = LW(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:],'y')
            
            Dx = 0.1
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U03 = C0(Jt,Jx,xf,CI)
            U3 = LW(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:],'g')
            
            plt.legend((['Analítica','Δx = 2 cm','Δx = 10 cm','Δx = 0.1 cm']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Lax-Wendroff, ν = 0.75, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()


    # Comparació per a diferents valors de nu (relació del pas del temps respecte el pas d'espai) amb la condició inicial B:
    elif mètode == 'LW3B':
        
        CI = 'B'
        Dx = 2
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.5
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI)
            U1 = LW(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.9
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = LW(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:])
            
            nu = 1
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U03 = C0(Jt,Jx,xf,CI)
            U3 = LW(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:])
            
            plt.legend((['Analítica','ν = 0.5','ν = 0.9','ν = 1']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Lax-Wendroff, Δx = 2 cm, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()


    # Solució pel mètode Leap-Frog amb la condicó inicial de l'apartat A:
    elif mètode == 'LF1A':
        
        CI = 'A'
        Dx = 2
        nu = 0.75
        Dt = Dx * nu/a
        Jx = int(xf/Dx+1)
        Jt = int(tf/Dt+1)
        
        U = C0(Jt,Jx,xf,CI)
        U_lf1 = LF(U,Jt,Jx,nu)
        legend = ['Solució numèrica per Leap-Frog']
        plt_2d(xf,Jx,Jt,U_lf1,Dx,nu,tf,legend)
    
    
    # Comparació per a diferents passos de temps amb condició inicial A:
    elif mètode == 'LF2A':
        
        CI = 'A'
        nu = 0.75
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            
            Dx = 0.2
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:],'b')
            
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI)
            U1 = LF(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:],'r')
            
            Dx = 10
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = LF(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:],'y')

            Dx = 0.1
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U03 = C0(Jt,Jx,xf,CI)
            U3 = LF(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:],'g')
            
            plt.legend((['Analítica','Δx = 2 cm','Δx = 10 cm','Δx = 0.1 cm']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Leap-Frog, ν = 0.75, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
            
            
    # Comparació per a diferents valors de nu (relació del pas del temps respecte el pas d'espai) amb la condició inicial A:
    elif mètode == 'LF3A':
        
        CI = 'A'
        Dx = 0.2
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.5
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI)
            U1 = LF(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.9
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = LF(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:])
            
            nu = 1
            Dt = Dx * nu/a 
            Jx = int(xf/Dx+1) 
            Jt = int(tf/Dt+1) 
            U03 = C0(Jt,Jx,xf,CI) 
            U3 = LF(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:])
            
            plt.legend((['Analítica','ν = 0.5','ν = 0.9','ν = 1']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Leap-Frog, Δx = 2 cm, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()


    # Solució pel mètode Leap-Frog amb la condicó inicial de l'apartat B:
    elif mètode == 'LF1B':
        
        CI = 'B'
        Dx = 2
        nu = 0.75
        Dt = Dx * nu/a
        Jx = int(xf/Dx+1)
        Jt = int(tf/Dt+1)
        
        U = C0(Jt,Jx,xf,CI)
        U_lf1 = LF(U,Jt,Jx,nu)
        legend = ['Solució numèrica per Leap-Frog']
        plt_2d(xf,Jx,Jt,U_lf1,Dx,nu,tf,legend)
    
    
    # Comparació per a diferents passos de temps amb condició inicial B:
    elif mètode == 'LF2B':
        
        CI = 'B'
        nu = 0.75
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            
            Dx = 0.2
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:],'b')
            
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI)
            U1 = LF(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:],'r')
            
            Dx = 10
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = LF(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:],'y')

            Dx = 0.1
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U03 = C0(Jt,Jx,xf,CI)
            U3 = LF(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:],'g')
            
            plt.legend((['Analítica','Δx = 2 cm','Δx = 10 cm','Δx = 0.1 cm']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Leap-Frog, ν = 0.75, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
            
            
    # Comparació per a diferents valors de nu (relació del pas del temps respecte el pas d'espai) amb la condició inicial B:
    elif mètode == 'LF3B':
        
        CI = 'B'
        Dx = 0.2
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U00 = C0(Jt,Jx,xf,CI)
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.5
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI)
            U1 = LF(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:])
            
            nu = 0.9
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI)
            U2 = LF(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:])
            
            nu = 1
            Dt = Dx * nu/a 
            Jx = int(xf/Dx+1) 
            Jt = int(tf/Dt+1) 
            U03 = C0(Jt,Jx,xf,CI) 
            U3 = LF(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:])
            
            plt.legend((['Analítica','ν = 0.5','ν = 0.9','ν = 1']))
            plt.ylabel('u (x,t)')
            plt.xlabel('x (cm)')
            plt.title("Leap-Frog, Δx = 2 cm, t = {} segons".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
            
    
    # Comparació dels diferents mètodes per a la condició inicial A:
    elif mètode == 'TA':
        
        CI = 'A'
        Dx = 2
        nu = 0.75
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1) 
            Jt = int(tf/Dt+1) 
            U00 = C0(Jt,Jx,xf,CI) 
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:],'b')
            
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI) 
            U1 = UW(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:],'r')
            
            Dt = Dx * nu/a 
            Jx = int(xf/Dx+1) 
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI) 
            U2 = LW(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:],'y')
            
            Dt = Dx * nu/a 
            Jx = int(xf/Dx+1) 
            Jt = int(tf/Dt+1) 
            U03 = C0(Jt,Jx,xf,CI) 
            U3 = LF(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:],'g')
            
            plt.legend((['Analítica','Upwind','Lax-Wendroff','Leap-Frog']))
            plt.ylabel('u (x,t) (cm/s)')
            plt.xlabel('x (cm)')
            plt.title("Solució als {} segons, ν = 0.75, Δx = 2cm".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
   
    
    # Comparació dels diferents mètodes per a la condició inicial B:
    elif mètode == 'TB':
        
        CI = 'B'
        Dx = 2
        nu = 0.75
        
        for t0 in [0,30,60]:
            
            plt.figure(figsize=(6,6))
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1) 
            Jt = int(tf/Dt+1) 
            U00 = C0(Jt,Jx,xf,CI) 
            U0 = AN(U00,Jt,Jx,nu,CI)
            plt.plot(np.linspace(0,xf,Jx),U0[int(round(t0*(Jt)/tf)),:],'b')
            
            Dt = Dx * nu/a
            Jx = int(xf/Dx+1)
            Jt = int(tf/Dt+1)
            U01 = C0(Jt,Jx,xf,CI) 
            U1 = UW(U01,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U1[int(round(t0*(Jt)/tf)),:],'r')
            
            Dt = Dx * nu/a 
            Jx = int(xf/Dx+1) 
            Jt = int(tf/Dt+1)
            U02 = C0(Jt,Jx,xf,CI) 
            U2 = LW(U02,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U2[int(round(t0*(Jt)/tf)),:],'y')
            
            Dt = Dx * nu/a 
            Jx = int(xf/Dx+1) 
            Jt = int(tf/Dt+1) 
            U03 = C0(Jt,Jx,xf,CI) 
            U3 = LF(U03,Jt,Jx,nu)
            plt.plot(np.linspace(0,xf,Jx),U3[int(round(t0*(Jt)/tf)),:],'g')
            
            plt.legend((['Analítica','Upwind','Lax-Wendroff','Leap-Frog']))
            plt.ylabel('u (x,t) (cm/s)')
            plt.xlabel('x (cm)')
            #plt.title("Solució als {} segons, ν = 0.75, Δx = 2cm".format(t0))
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()
    
    
    # Apartat F (nova condició de contorn, condició inicial B i resolució per Leap-Frog):
    elif mètode == 'FB':
        
        CI = 'B'
        Dx = 2 
        nu = 0.75 
        Dt = Dx * nu/a
        Jx = int(xf/Dx+1) 
        Jt = int(tf/Dt+1)
        U = C0(Jt,Jx,xf,CI)
        Ix = Jx-1
        print(Jt)
        
        # Per a cada passa de temps
        for n in np.arange(0,Jt-1,1):
            
            # Es calcula la posició a cada punt mitjançant Leap-Frog excepte els extrems
            for j in np.arange(1,Ix,1): 
                
                # El primer punt ve donat per la condició inicial:
                if n < 25 * (301/90) or n > 40 * (301/90):
                    
                    U[n,0] = 0 
                
                else:
                    
                    U[n,0] = 2 * np.exp(-(1/3)*((n*(90/301))-32)**6)
                
                # I la resta es calcula pel mètode de Leap-Frog:
                U[n+1,j] = U[n-1,j] - nu * (U[n,j+1] - U[n,j-1])
            
        # Aplicam la condició de derivada nula: U_j = U_j-1   
        U[n,Ix] = U[n,Ix-1]
        legend = ["Leap-Frog amb u (0,t)"]
        
        for t0 in [0,30,60,90]:
            
            plt.figure(figsize=(5,3))
            plt.plot(np.linspace(0,xf,Jx),U[int(round(t0*(Jt-1)/tf)),:],'b')
            plt.xlabel('x (cm)')
            plt.ylabel('u (x,t)')
            plt.title("Solució als {} segons, ν = 0.75, Δx = 2cm".format(t0))
            plt.legend(legend)
            plt.ylim(bottom=-1.1,top=3)
            plt.xlim(left=0,right=500)
            plt.show()

 
    


# Condició inicial apartat A
def A(x):
    return 2 * np.exp(-0.5*((x-50)/20)**2) - 2 * np.exp(-0.5*((x-30)/10)**2) + 1 * np.exp(-0.5*((x-58)/4)**2)


# Condició inicial apartat B
def B(x):
    if 20 <= x <= 30:
        return 2
    elif 30 <= x <= 35:
        return 1
    elif 35 <= x <= 40:
        return -1
    else:
        return 0
    return np.vectorize(B)


# Comptador per crear les condicions inicials
k = 0


# Elecció de la condició inicial A o B:
def C0(Jt,Jx,xf,i,k=0):
    
    x = np.linspace(0,xf,Jx) # Malla de x0 a xf separada Jx
    U = np.zeros((Jt,Jx)) # Matriu amb els valors de les condicions inicial i la de contorn
    
    if i == 'A':
        
        for j in np.arange(1,Jx,1):
            
            U[0,j] = A(x[j-k]) # Condició inicial per apartat A
            
    elif i == 'B':
        
        for j in np.arange(1,Jx,1):
            
            U[0,j] = B(x[j-k]) # Condició inicial per apartat B
            
    return U


# Solució analítica: avenç "intacte" de les condicions inicials. Servirà per comparar la solució per diferents mètodes
def AN(U,Jt,Jx,nu,CI):
    
    x = np.linspace(0,500,Jx)
    t = np.linspace(0,90,Jt)
    
    # Per a cada pas de temps
    for n in np.arange(0,Jt-1,1):
        
        # Es calcula la posició de cada punt
        for j in np.arange(1,Jx-1,1):
            
            # La condició inicial B es deslaça segons la solució general
            if CI == 'B':
                U[n+1,j] = B(x[j]-5*t[n])
            
            # La condició inicial A es deslaça segons la solució general
            else:
                U[n+1,j] = A(x[j]-5*t[n])
                
    return U


# Esquema Upwind
def UW(U,Jt,Jx,nu):
    
    # Per a cada pas de temps
    for n in np.arange(0,Jt-1,1):
    
        # Es calcula la posició a cada punt mitjançant Upwind
        for j in np.arange(1,Jx-1,1):
            
            U[n+1,j] = (1-nu) * U[n,j] + nu * U[n,j-1]
            
    return U


# Esquema de Lax-Wendroff
def LW(U,Jt,Jx,nu):
    
    # Redefinim l'extrem de posició final
    Ix = Jx-1
    
    # Per a cada pas de temps
    for n in np.arange(0,Jt-1,1):

        # Es calcula la posició a cada punt mitjançant Lax-Wendroff
        for j in np.arange(1,Ix,1):
            
            U[n+1,j] = 0.5 * nu * (1+nu) * U[n,j-1] + (1-nu**2) * U[n,j] - 0.5 * nu * (1-nu) * U[n,j+1]
            
        # I aplicam la condició de derivada nula: U_j = U_j-1
        U[n,Ix] = U[n,Ix-1]
        
    return U


# Esquema Leap-Frog
def LF(U,Jt,Jx,nu):
    
    # Redefinim l'extrem de posició final
    Ix = Jx-1
    
    # Per a cada pas de temps
    for n in np.arange(0,Jt-1,1):
        
        # Es calcula la posició a cada punt mitjançant Leap-Frog excepte els extrems
        for j in np.arange(1,Ix,1): 
            
            # El primer punt es calcula pel mètode de Lax-Wendroff:
            if n == 0:
                
                U[n+1,j] = 0.5 * nu * (1+nu) * U[n,j-1] + (1-nu**2) * U[n,j] - 0.5 * nu * (1-nu) * U[n,j+1]
                
            # I la resta es calcula pel mètode de Leap-Frog:
            else:
                U[n+1,j] = U[n-1,j] - nu * (U[n,j+1]-U[n,j-1])
         
        # I tornam a aplicar la condició de derivada nula: U_j = U_j-1        
        U[n,Ix] = U[n,Ix-1]
        
    return U


# Representació en 2D
def plt_2d(xf,Jx,Jt,U,Dx,nu,tf,legend):
    
    for t0 in [0,30,45,60,90]:
        
        plt.figure(figsize=(5,3))
        plt.plot(np.linspace(0,xf,Jx),U[int(round(t0*(Jt-1)/tf)),:],'b')
        plt.ylabel('u (x,t)')
        plt.xlabel('x (cm)')
        plt.title("Solució als {} segons.".format(t0))
        plt.xlim(left=0,right=500)
        plt.ylim(bottom=-1.1,top=3)
        plt.legend(legend)
        plt.show()



Sol('FB')









