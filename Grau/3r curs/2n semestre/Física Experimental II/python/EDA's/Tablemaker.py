#Application to create Latex tables
#Author: Iker Lomas Javaloyes
#Version 2.0

import sympy as sp
import itertools

#Función para convertir a Latex
def latex(x): return sp.latex(x).replace("±", "\pm")

#Crea una tabla desde una EDA a Latex
def TablemakerLatex(EDA):
    #Elimino lo que no me interesa de la conevrsión a Latex
    i = latex(EDA.x_rounded)
    i = i.replace("ext{","")
    i = i.replace("\mathtt","")
    i = i.replace("}}","$")
    i = i.replace("\  ","")
    i = i.replace("t","p")
    i = i.replace("{","$")
    i = i.replace("{\p", "")
    i = i.replace("\p", "")
    i = i.replace("m", "\pm")
    i = i.replace("\lefp[","")
    i = i.replace("r","k")
    i = i.replace("\kighp]", "")
    #Separo la array
    i = i.split(',')
    n = len(i)
    #Mismo proceso pero para la y
    j = latex(EDA.y_rounded)
    j = j.replace("ext{","")
    j = j.replace("\mathtt","")
    j = j.replace("}}","$")
    j = j.replace("\  ","")
    j = j.replace("t","p")
    j = j.replace("{","$")
    j = j.replace("{\p", "")
    j = j.replace("\p", "")
    j = j.replace("m", "\pm")
    j = j.replace("\lefp[","")
    j = j.replace("r","k")
    j = j.replace("\kighp]", "")

    j = j.split(',')
    n = len(j)
    
    #Pongo la sección
    print("\n ---------------------------------------------------------------------" )
    texto = "TABLA DE LATEX\n"
    print(texto.center(70))
    #Creo la tabla de Latex
    print("\\begin{table}[H]")
    print("\centering")
    print("\scalebox{1}{")
    print("\\begin{tabular}{| c | c |}")
    print("\hline")
    print("$x$ & $y$\\\\")
    print("\hline")
    for k in range(0,n):
        print(i[k], "&", j[k], '\\\\')
    print("\hline")
    print("\end{tabular}}")
    print("\caption{Caption}")
    print("\label{Label}")
    print("\end{table}\n")

#Crea una tabla desde las columnas de una EDA. El input dede de ser una lista de EDAs.(x o y)_rounded. Ejemplo : [Hilo2.x_rounded, Hilo2.y_rounded, Hilo3.y_rounded]
def MultiTablemakerLatex(LEDAs):
    #Comprobación del mimso número de datos
    n0 = len(LEDAs)
    n1 = len(LEDAs[0])
    for i in range(0,n0):
        m = len(LEDAs[i])
        if m !=n1:
            print("No se puede hacer ya que no hay el mismo número de argumentos")
            exit()
        else:
            continue

    #Elimino lo que no me interesa de la conevrsión a Latex
    Datos = []
    for k in range(0,n0):
        i = latex(LEDAs[k])
        i = i.replace("ext{","")
        i = i.replace("\mathtt","")
        i = i.replace("}}","$")
        i = i.replace("\  ","")
        i = i.replace("t","p")
        i = i.replace("{","$")
        i = i.replace("{\p", "")
        i = i.replace("\p", "")
        i = i.replace("m", "\pm")
        i = i.replace("\lefp[","")
        i = i.replace("r","k")
        i = i.replace("\kighp]", "")
        #Separo la array
        i = i.split(',')
        Datos.append(i)
    
    #Pongo la sección
    print("\n ---------------------------------------------------------------------" )
    texto = "TABLA DE LATEX\n"
    print(texto.center(70))
    #Creo la tabla de Latex
    print("\\begin{table}[H]")
    print("\centering")
    print("\scalebox{1}{")
    print("\\begin{tabular}{",end="")
    #Pone las columnas
    Columnas = list(itertools.repeat("c",n0))
    for i in range(0,n0):
        print(f"|{Columnas[i]}",end="")
    print("|}")
    
    #Pongo los encabezados
    print("\hline")
    Titulos = []
    for i in range(0,n0):
        Titulos.append(f"x_{{{i}}}")
    for i in range(0,n0):
        print(f"${Titulos[i]}$", end="")
        if i == n0-1:
            continue
        else:
            print(" & ", end="")
            continue 
    print("\\\\")
    print("\hline")

    #Pongo las columnas de datos
    m = 0
    for i in range(0,n1):
        m = 0
        while m != n0:
            print(f"{Datos[m][i]}", end="")
            m = m + 1
            if m == n0:
                print(" \\\\")
                continue
            else:
                print(" & ", end="")
            continue
    
    #Termino de poner lo que falta para completar la tabla
    print("\hline")
    print("\end{tabular}}")
    print("\caption{Caption}")
    print("\label{Label}")
    print("\end{table}\n")