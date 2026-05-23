#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:45:40 2022

@author: joanribot
"""

import numpy as np
import pandas as pd
from Multiplotter import PlotterScatter, Multiplotter

δy = 10e-3
δx = 10e-3

datos1 = pd.read_csv("golf15mm.txt",sep=";")
datos2 = pd.read_csv("gomablava30mm.txt",sep=";")
datos3 = pd.read_csv("tennis2520mm.txt",sep=";")
datos4 = pd.read_csv("tennis2550mm.txt",sep=";")
datos5 = pd.read_csv("tennis7520mm.txt",sep=";")
datos6 = pd.read_csv("golf8mm.txt",sep=";")
datos7 = pd.read_csv("superbotadora10mm.txt",sep=";")
datos8 = pd.read_csv("tt2mm.txt",sep=";")
datos9 = pd.read_csv("tt10mm.txt",sep=";")

datos_x1 = datos1["Deformacion no"].values
datos_y1 = datos1["Fuerza estanda"].values

datos_x2 = datos2["Deformacin no"].values
datos_y2 = datos2["Fuerza estnda"].values

datos_x3 = datos3["Deformacin no"].values
datos_y3 = datos3["Fuerza estnda"].values

datos_x4 = datos4["Deformacin no"].values
datos_y4 = datos4["Fuerza estnda"].values

datos_x5 = datos5["Deformacin no"].values
datos_y5 = datos5["Fuerza estnda"].values

datos_x6 = datos6["Deformacin no"].values
datos_y6 = datos6["Fuerza estnda"].values

datos_x7 = datos7["Deformacin no"].values
datos_y7 = datos7["Fuerza estnda"].values

datos_x8 = datos8["Deformacin no"].values
datos_y8 = datos8["Fuerza estnda"].values

datos_x9 = datos9["Deformacin no"].values
datos_y9 = datos9["Fuerza estnda"].values

datos_x1 = datos_x1/1000
datos_x2 = datos_x2/1000
datos_x3 = datos_x3/1000
datos_x4 = datos_x4/1000
datos_x5 = datos_x5/1000
datos_x6 = datos_x6/1000
datos_x7 = datos_x7/1000
datos_x8 = datos_x8/1000
datos_x9 = datos_x9/1000

n1 = np.argmax(datos_y1)
n2 = np.argmax(datos_y2)
n3 = np.argmax(datos_y3)
n4 = np.argmax(datos_y4)
n5 = np.argmax(datos_y5)
n6 = np.argmax(datos_y6)
n7 = np.argmax(datos_y7)
n8 = np.argmax(datos_y8)
n9 = np.argmax(datos_y9)

I_1 = np.trapz(datos_y1[:n1], datos_x1[:n1])
I0_1 = np.trapz(datos_y1[n1:], datos_x1[n1:])

I_2 = np.trapz(datos_y2[:n2], datos_x2[:n2])
I0_2 = np.trapz(datos_y2[n2:], datos_x2[n2:])

I_3 = np.trapz(datos_y3[:n3], datos_x3[:n3])
I0_3 = np.trapz(datos_y3[n3:], datos_x3[n3:])

I_4 = np.trapz(datos_y4[:n4], datos_x4[:n4])
I0_4 = np.trapz(datos_y4[n4:], datos_x4[n4:])

I_5 = np.trapz(datos_y5[:n5], datos_x5[:n5])
I0_5 = np.trapz(datos_y5[n5:], datos_x5[n5:])

I_6 = np.trapz(datos_y6[:n6], datos_x6[:n6])
I0_6 = np.trapz(datos_y6[n6:], datos_x6[n6:])

I_7 = np.trapz(datos_y7[:n7], datos_x7[:n7])
I0_7 = np.trapz(datos_y7[n7:], datos_x7[n7:])

I_8 = np.trapz(datos_y8[:n8], datos_x8[:n8])
I0_8 = np.trapz(datos_y8[n8:], datos_x8[n8:])

I_9 = np.trapz(datos_y9[:n9], datos_x9[:n9])
I0_9 = np.trapz(datos_y9[n9:], datos_x9[n9:])

I0_1 = np.absolute(I0_1)
I0_2 = np.absolute(I0_2)
I0_3 = np.absolute(I0_3)
I0_4 = np.absolute(I0_4)
I0_5 = np.absolute(I0_5)
I0_6 = np.absolute(I0_6)
I0_7 = np.absolute(I0_7)
I0_8 = np.absolute(I0_8)
I0_9 = np.absolute(I0_9)

print(I_1-I0_1,"J,",I_2-I0_2,"J,",I_3-I0_3,"J,",I_4-I0_4,"J,",I_5-I0_5,"J,",I_6-I0_6,"J,",I_7-I0_7,"J,",I_8-I0_8,"J,",I_9-I0_9,"J")


#PlotterScatter(datos_x1, datos_y1,"Golf 15 mm", "$\epsilon$ (mm)", "F(N)")
#PlotterScatter(datos_x2, datos_y2,"Goma blava 30 mm", "$\epsilon$ (mm)", "F(N)")
#PlotterScatter(datos_x3, datos_y3,"Tennis 25% - 20 mm", "$\epsilon$ (mm)", "F(N)")
#PlotterScatter(datos_x4, datos_y4,"Tennis 25% - 50 mm", "$\epsilon$ (mm)", "F(N)")
#PlotterScatter(datos_x5, datos_y5,"Tennis 75% - 20 mm", "$\epsilon$ (mm)", "F(N)")
#PlotterScatter(datos_x6, datos_y6,"Golf 8 mm", "$\epsilon$ (mm)", "F(N)")
#PlotterScatter(datos_x7, datos_y7,"Superbotadora 10 mm", "$\epsilon$ (mm)", "F(N)")
#PlotterScatter(datos_x8, datos_y8,"Tennis taula 2 mm", "$\epsilon$ (mm)", "F(N)")
#PlotterScatter(datos_x9, datos_y9,"Tennis taula 10 mm", "$\epsilon$ (mm)", "F(N)")

#Multiplotter([datos_x3,datos_x5], [datos_y3,datos_y5], [], [], "Tennis 25% vs. Tennis 75%", "$\epsilon$ (mm)", "F(N)", ["Tennis 25%","Tennis 75%"], False, True)
#Multiplotter([datos_x1,datos_x6], [datos_y1,datos_y6], [], [], "Golf 15 mm vs. Golf 8 mm", "$\epsilon$ (mm)", "F(N)", ["Golf 15 mm","Golf 8 mm"], False, True)
#Multiplotter([datos_x8,datos_x9], [datos_y8,datos_y9], [], [], "Tennis taula 2 mm vs. Tennis taula 10 mm", "$\epsilon$ (mm)", "F(N)", ["Tennis taula 2 mm","Tennis taula 10 mm"], False, True)
