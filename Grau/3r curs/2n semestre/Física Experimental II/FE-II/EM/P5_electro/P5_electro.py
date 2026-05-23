# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# El primer índex indica 2 massis i 1 laminar ???
# El segon índex indica el cas... transcriure MIGUEL


# Importam les llistes amb les dades:

I_1_1 = np.load('I_1_1.npy')
B_1_1 = np.load('B_1_1.npy')
 
I_1_2 = np.load('I_1_2.npy')
B_1_2 = np.load('B_1_2.npy')
 
I_1_3 = np.load('I_1_3.npy')
B_1_3 = np.load('B_1_3.npy')
 
I_1_5 = np.load('I_1_5.npy')
B_1_5 = np.load('B_1_5.npy')
 
I_1_6 = np.load('I_1_6.npy')
B_1_6 = np.load('B_1_6.npy')
 
I_2_1 = np.load('I_2_1.npy')
B_2_1 = np.load('B_2_1.npy')
 
I_2_2 = np.load('I_2_2.npy')
B_2_2 = np.load('B_2_2.npy')
 
I_2_3 = np.load('I_2_3.npy')
B_2_3 = np.load('B_2_3.npy')
 
I_2_4 = np.load('I_2_4.npy')
B_2_4 = np.load('B_2_4.npy') 
 
I_2_5 = np.load('I_2_5.npy')
B_2_5 = np.load('B_2_5.npy')
 
I_2_6 = np.load('I_2_6.npy')
B_2_6 = np.load('B_2_6.npy')
 

N_espiras = 500
L_massis = 0.232
L_laminat = 0.244

n_massis = (N_espiras / L_massis)
n_laminat = (N_espiras / L_laminat)

# Convertim I en H: H = N/L * I
    
H_1_1 = n_laminat * I_1_1
H_1_2 = n_laminat * I_1_2
H_1_3 = n_laminat * I_1_3
H_1_5 = n_laminat * I_1_5
H_1_6 = n_laminat * I_1_6

H_2_1 = n_massis * I_2_1
H_2_2 = n_massis * I_2_2
H_2_3 = n_massis * I_2_3
H_2_4 = n_massis * I_2_4
H_2_5 = n_massis * I_2_5
H_2_6 = n_massis * I_2_6



# =============================================================================
# Representació
# =============================================================================

plt.title("B vs H")
plt.xlabel("H (A/m)")
plt.ylabel("B (T)")
plt.scatter(H_1_1,B_1_1,s=0.1,c='g')

plt.grid(color='b', linestyle='dotted', linewidth=1)

plt.show()


# =============================================================================
# Càlcul de l'àrea - Energia dissipada
# =============================================================================


n1 = np.argmax(B_1_1) # Valor màxim...
n2 = np.argmax(B_2_1)


I_1 = np.trapz(H_1_1[:n1],B_1_1[:n1])
I0_1 = np.trapz(H_1_1[n1:],B_1_1[n1:])
I0_1 = np.absolute(I0_1)



I_2 = np.trapz(H_2_1[:n2],B_2_1[:n2])
I0_2 = np.trapz(H_2_1[n2:],B_2_1[n2:])
I0_2 = np.absolute(I0_2)

# =============================================================================
# NO ESTÀ BÉ !!! REVISAR QUE NO FACI EL PROMIG... SEPARAR EN 2 PARTS: B < 0 I B > 0 ???
# =============================================================================


print(I_1-I0_1,"J d'energia dissipada")
print(I_2-I0_2,"J d'energia dissipada")


