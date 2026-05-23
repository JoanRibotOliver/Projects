#Application to create several graphs in one
#Author: Iker Lomas Javaloyes
#Version 2.2

import itertools
import matplotlib.pyplot as plt
import numpy as np

#Multiplotter for EDAs
def MultiplotterEDAs(LEDAs, Titulo="", x_label="", y_label="", lr=False, linestyle='--', Label=[], Color=False):
    #Número de datos
    n = len(LEDAs)
    nl = len(Label)
    k = 0

    #Creamos el ax
    fig, ax = plt.subplots()

    #Lista de Colores para Lluc
    Colors = ["red", "pink", "orange", "purple", "green", "blue", "lightskyblue", "brown", "grey"]
    ncl = len(Colors)

    if Color == True:
        if nl == 0:
            for i in range(0,n):
                if k == ncl:
                    k = 0                  
                ax.errorbar(LEDAs[i].XY['x'] , LEDAs[i].XY['y'], xerr = LEDAs[i].δXY['x'], yerr = LEDAs[i].δXY['y'], marker = 'o', capsize = 2, capthick = 0.4, elinewidth = 0.4, linestyle = "", zorder = 10, ecolor = 'black', label=f"$x_{i}$", color=Colors[k])
                k = k + 1
                if lr == True:
                    ax.axline((0, LEDAs[i].A), slope = LEDAs[i].B, color = Colors[i], linestyle='--')
        else:
            for i in range(0,n):
                if k == ncl:
                    k = 0
                ax.errorbar(LEDAs[i].XY['x'] , LEDAs[i].XY['y'], xerr = LEDAs[i].δXY['x'], yerr = LEDAs[i].δXY['y'], marker = 'o', capsize = 2, capthick = 0.4, elinewidth = 0.4, linestyle = "", zorder = 10, ecolor = 'black', label=Label[i], color=Colors[k])
                k = k + 1
                if lr == True:
                    ax.axline((0, LEDAs[i].A), slope = LEDAs[i].B, color = Colors[i], linestyle=linestyle)
    else:
        if nl == 0:
            for i in range(0,n):
                ax.errorbar(LEDAs[i].XY['x'] , LEDAs[i].XY['y'], xerr = LEDAs[i].δXY['x'], yerr = LEDAs[i].δXY['y'], marker = 'o', capsize = 2, capthick = 0.4, elinewidth = 0.4, linestyle = "", zorder = 10, ecolor = 'black', label=f"$x_{i}$")    
                if lr == True:
                    ax.axline((0, LEDAs[i].A), slope = LEDAs[i].B, color = 'black', linestyle='--')
        else:
            for i in range(0,n):
                ax.errorbar(LEDAs[i].XY['x'] , LEDAs[i].XY['y'], xerr = LEDAs[i].δXY['x'], yerr = LEDAs[i].δXY['y'], marker = 'o', capsize = 2, capthick = 0.4, elinewidth = 0.4, linestyle = "", zorder = 10, ecolor = 'black', label=Label[i] )    
                if lr == True:
                    ax.axline((0, LEDAs[i].A), slope = LEDAs[i].B, color = 'black', linestyle=linestyle)
    
    #Texto
    plt.title(Titulo, fontdict = {'fontsize': 12, 'fontweight': 'medium'})
    plt.xlabel(x_label, fontsize = 12) 
    plt.ylabel(y_label, fontsize = 12)

    #Grid
    ax.grid(visible = True, linestyle = '--', linewidth = 0.4, alpha = 0.6, zorder = 1)

    #Leyenda
    ax.legend(fancybox = False, shadow = True, edgecolor = 'black')

    plt.show()

def Multiplotter(Datos_x, Datos_y, Errores_x=[], Errores_y=[], Titulo="", x_label="", y_label="", Label=[], Lineas=False, Color=False):
    #Número de datos
    nx = len(Datos_x)
    ny = len(Datos_y)
    Enx = len(Errores_x)
    Eny = len(Errores_y)
    nl = len(Label)
    k = 0

    #Comprobamos número de argumentos
    for g in range(0,nx):
        if len(Datos_x[g]) != len(Datos_y[g]):
            print("No se puede hacer ya que no hay el mismo número de argumentos en los datos")
            exit()
        if Enx != 0:
            if len(Errores_x[g]) != len(Datos_x[g]):
                print("No se puede hacer ya que no hay el mismo número de argumentos en los datos x y en los errores x")
                exit()
            if len(Errores_x[g]) != len(Errores_y[g]):
                print("No se puede hacer ya que no hay el mismo número de argumentos en los errores")
                exit()
        if Eny != 0:
            if len(Errores_y[g]) != len(Datos_y[g]):
                print("No se puede hacer ya que no hay el mismo número de argumentos en los datos y y en los errores y")
                exit()
    
    #Creamos lista de errores 0 por si no hay error
    if Enx == 0:
        Errores_x = []
        for j in range(0,nx):
            Lista = list(itertools.repeat(0,len(Datos_x[j])))
            Errores_x.append(Lista)
    if Eny == 0:
        Errores_y = []
        for j in range(0,ny):
            Lista = list(itertools.repeat(0,len(Datos_y[j])))
            Errores_y.append(Lista)
    
    #Ajustamos el tamaño de los puntos
    Size = []
    for j in range(0,nx):
        Lista = list(itertools.repeat(2,len(Datos_x[j])))
        Size.append(Lista)

    #Creamos el ax
    fig, ax = plt.subplots()

    #Lista de Colores para LLuc
    Colors = ["red", "pink", "orange", "purple", "green", "blue", "lightskyblue", "brown", "grey"]
    ncl = len(Colors)

    if Color == True:
        if nl == 0:
            for j in range(0,nx):
                if k == ncl:
                    k = 0                  
                ax.errorbar(Datos_x[j], Datos_y[j], xerr =Errores_x[j], yerr = Errores_y[j], marker = 'o', markersize=2, capsize = 2, capthick = 0.4, elinewidth = 0.4, linestyle = "", zorder = 10, ecolor = 'black', label=f"$x_{j}$", color=Colors[k])
                k = k + 1
                if Lineas == True:
                    ax.plot(Datos_x[j], Datos_y[j], color=Colors[k-1])                
        else:
            for j in range(0,nx):
                if k == ncl:
                    k = 0
                ax.errorbar(Datos_x[j], Datos_y[j], xerr =Errores_x[j], yerr =Errores_y[j], marker = 'o', markersize=2, capsize = 2, capthick = 0.4, elinewidth = 0.4, linestyle = "", zorder = 10, ecolor = 'black', label=Label[j], color=Colors[k])
                k = k + 1
                if Lineas == True:
                    ax.plot(Datos_x[j], Datos_y[j], color=Colors[k-1])
    else:
        if nl == 0:
            for j in range(0,nx):
                ax.errorbar(Datos_x[j], Datos_y[j], xerr =Errores_x[j], yerr =Errores_y[j], marker = 'o', markersize=2, capsize = 2, capthick = 0.4, elinewidth = 0.4, linestyle = "", zorder = 10, ecolor = 'black', label=f"$x_{j}$")
                if Lineas == True:
                    ax.plot(Datos_x[j], Datos_y[j])
        else:
            for j in range(0,nx):
                ax.errorbar(Datos_x[j], Datos_y[j], xerr =Errores_x[j], yerr =Errores_y[j], marker = 'o', markersize=2, capsize = 2, capthick = 0.4, elinewidth = 0.4, linestyle = "", zorder = 10, ecolor = 'black', label=Label[j] )
                if Lineas == True:
                    ax.plot(Datos_x[j], Datos_y[j])
    
    #Texto
    plt.title(Titulo, fontdict = {'fontsize': 12, 'fontweight': 'medium'})
    plt.xlabel(x_label, fontsize = 12) 
    plt.ylabel(y_label, fontsize = 12)

    #Grid
    ax.grid(visible = True, linestyle = '--', linewidth = 0.4, alpha = 0.6, zorder = 1)

    #Leyenda
    ax.legend(fancybox = False, shadow = True, edgecolor = 'black')

    plt.show()

def PlotterScatter(Datos_x, Datos_y, Titulo="", x_label="", y_label=""):
    fig, ax = plt.subplots()
    ax.scatter(Datos_x,Datos_y)
    #Texto
    plt.title(Titulo, fontdict = {'fontsize': 12, 'fontweight': 'medium'})
    plt.xlabel(x_label, fontsize = 12) 
    plt.ylabel(y_label, fontsize = 12)
    ax.grid(visible = True, linestyle = '--', linewidth = 0.4, alpha = 0.6, zorder = 1)
    plt.show()
