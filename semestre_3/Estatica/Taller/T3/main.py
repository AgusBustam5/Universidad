from funciones2D import *
from funciones3D import *
import os.path
import numpy as np

# Problema 1 b.1)

nodos_p1_b_1 = np.array([
    [0, 0],
    [3, 0],
    [6, 0],
    [9, 0],
    [1.5, 2],
    [4.5, 2],
    [7.5, 2]
], dtype=float)

elem_p1_b_1 = np.array([
    [0, 1],
    [1, 2],
    [2, 3],
    [4, 0],
    [4, 1],
    [4, 5],
    [5, 1],
    [5, 2],
    [5, 6],
    [6, 2],
    [6, 3]
], dtype=float)

Fext_p1_b_1 = np.array([
    [2, 0, 5],
    [4, 7 * np.cos(np.radians(75)), -7 * np.sin(np.radians(75))],
    [5, 0, -4],
    [6, -9 * np.cos(np.pi / 6), -9 * np.sin(np.pi / 6)]
], dtype=float)

supp_p1_b_1 = np.array([
    [0, 1, 1],
    [3, 0, 1]
], dtype=float)

PlotSistem2D(nodos_p1_b_1, elem_p1_b_1)

print("\nProblema 1 b.1)")
print("\n Matriz input nodos:")
for nodo in nodos_p1_b_1:
    if nodo[0] % 1 != 0:
        print(f"  | {nodo[0]}   {nodo[1]} |")
    else:
        print(f"  | {nodo[0]}     {nodo[1]} |")

print("\n Matriz input elementos:")
for e in elem_p1_b_1:
    print(f"  | {e[0]}   {e[1]} |")

print("\n Matriz input soportes:")
for sup in supp_p1_b_1:
    print(f"  | {sup[0]}   {sup[1]}   {sup[2]} |")

print("\n Matriz input Fext:")
for fu in Fext_p1_b_1:
    print(f"  | {fu[0]}   {fu[1]}   {fu[2]} |")

S_p1_b_1, R_p1_b_1, Rid_p1_b_1 = SolveTrussSystem2D(nodos_p1_b_1, elem_p1_b_1, Fext_p1_b_1, supp_p1_b_1)

print("\n Vector S:")
for val in S_p1_b_1:
    print(f"  {val}")

print("\n Vector R:")
for val in R_p1_b_1:
    print(f"  {val}")

print("\n  Matriz Rid:")
for fil in Rid_p1_b_1:
    print(f"  | {fil[0]}   {fil[1]}   {fil[2]} |")

PlotTrussForces2D(nodos_p1_b_1, elem_p1_b_1, S_p1_b_1)

# Problema 1_b.2
nodos_p1_b_2 = np.array([
    [0, 0], #0[0, 0],
    [3, 0], #1[3, 0],
    [6, 0], #2[6, 0],
    [9, 0], #3[9, 0],
    [12, 0],#4[12, 0],
    [15, 0],#5[15, 0],
    [18, 0],#6[18, 0],
    [21, 0],#7[21, 0],
    [24, 0],#8[24, 0],
    [27, 0],#9[27, 0],
    [30, 0],#10[30, 0],
    [33, 0],#11[33, 0],
    [36, 0],#12[36, 0],
    [3, 4], #13[3, 4],
    [9, 4], #14[9, 4],
    [15, 4],#15[15, 4],
    [21, 4],#16[21, 4],
    [27, 4],#17[27, 4],
    [33, 4],#18[33, 4],
    [6, 7], #19[6, 7],
    [12, 7],#20[12, 7],
    [18, 7],#21[18, 7],
    [24, 7],#22[24, 7],
    [30, 7] #23[30, 7]
], dtype=float)

elem_p1_b_2 = np.array([
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 8],
    [8, 9],
    [9, 10],
    [10, 11],
    [11, 12], # distribuida_1
    [13, 0],
    [13, 1],
    [13, 2],
    [14, 2],
    [14, 3],
    [14, 4],
    [15, 4],
    [15, 5],
    [15, 6],
    [16, 6],
    [16, 7],
    [16, 8],
    [17, 8],
    [17, 9],
    [17, 10],
    [18, 10],
    [18, 11],
    [18, 12],
    [19, 13],
    [19, 2],
    [19, 14],
    [19, 20],
    [20, 4],
    [20, 15],
    [20, 21],
    [21, 6],
    [21, 22],
    [22, 16],
    [22, 8],
    [22, 23],
    [23, 17],
    [23, 10],
    [23, 18]
], dtype=float)

lista_fuerzas_p2 = []

modulo_f_sup = np.linalg.norm(np.array([[6, 7]], dtype = float))
modulo_f_inf = np.linalg.norm(np.array([[3, 4]], dtype = float))

mult_x_in = 3 / modulo_f_inf
mult_y_in = 4 / modulo_f_inf
mult_x_sup = 6 / modulo_f_sup
mult_y_sup = 7 / modulo_f_sup

Fext_p1_b_2 = np.array(
    [
        [1, 0, 100],
        [2, mult_x_in * 150, -mult_y_in * 150],
        [5, 0, -75],
        [7, 0, -250],
        [11, 0, -125],
        [18, 250, 0],
        [19, mult_x_sup * 150, -mult_y_sup * 150],
        [20, mult_x_sup * 250, -mult_y_sup * 250],
        [22, -mult_x_sup * 180, -mult_y_sup * 180],
        [23, -mult_x_sup * 125, -mult_y_sup * 125]
    ], dtype=float)

supp_p1_b_2 = np.array(
    [
        [0, 1, 1],
        [12, 0, 1]
    ], dtype=float)

PlotSistem2D(nodos_p1_b_2, elem_p1_b_2)

print("\nProblema 1 b.2)")
print("\n Matriz input nodos:")
for nodo in nodos_p1_b_2:
    if nodo[0] % 1 != 0:
        print(f"  {nodo[0]} |  {nodo[1]} \\")
    else:
        print(f"  {nodo[0]}  |  {nodo[1]} \\")

print("\n Matriz input elementos:")
for e in elem_p1_b_2:
    print(f" {e[0]}  | {e[1]} \\")

print("\n Matriz input soportes:")
for sup in supp_p1_b_2:
    print(f"  {sup[0]} %  {sup[1]}  % {sup[2]} \\")

print("\n Matriz input Fext:")
for fu in Fext_p1_b_2:
    print(f"  {fu[0]}  | {fu[1]} |  {fu[2]} \\")

S_p1_b_2, R_p1_b_2, Rid_p1_b_2 = SolveTrussSystem2D(nodos_p1_b_2, elem_p1_b_2, Fext_p1_b_2, supp_p1_b_2)

print("\n Vector S:")
for val in S_p1_b_2:
    print(f"  {val}")

print("\n Vector R:")
for val in R_p1_b_2:
    print(f"  {val}")

print("\n  Matriz Rid:")
for fil in Rid_p1_b_2:
    print(f"  {fil[0]} |  {fil[1]} |  {fil[2]} \\")

PlotTrussForces2D(nodos_p1_b_2, elem_p1_b_2, S_p1_b_2)

# Problema 2_b.1)
nodos_p2_b_1 = np.array(
    [
        [0, -4, 0],
        [0, 4, 0],
        [3, 0, 0],
        [1, 0, -6]
    ], dtype=float)

elem_p2_b_1 = np.array(
    [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 2],
        [1, 3],
        [2, 3]
    ], dtype=float)

Fext_p2_b_1 = np.array(
    [
        [3, 0, 0, -100]
    ], dtype=float)

supp_p2_b_1 = np.array(
    [
        [0, 1, 0, 1],
        [1, 1, 1, 1],
        [2, 0, 0, 1]
    ], dtype=float)

PlotSistem3D(nodos_p2_b_1, elem_p2_b_1)

print("\nProblema 2 b.1)")
print("\n Matriz input nodos:")
for nodo in nodos_p2_b_1:
    if nodo[0] % 1 != 0:
        print(f"  | {nodo[0]}   {nodo[1]}   {nodo[2]} |")
    else:
        print(f"  | {nodo[0]}   {nodo[1]}   {nodo[2]} |")

print("\n Matriz input elementos:")
for e in elem_p2_b_1:
    print(f"  | {e[0]}   {e[1]} |")

print("\n Matriz input soportes:")
for sup in supp_p2_b_1:
    print(f"  | {sup[0]}   {sup[1]}   {sup[2]}   {sup[3]} |")

print("\n Matriz input Fext:")
for fu in Fext_p2_b_1:
    print(f"  | {fu[0]}   {fu[1]}   {fu[2]}   {fu[3]} |")

S_p2_b_1, R_p2_b_1, Rid_p2_b_1 = SolveTrussSystem3D(nodos_p2_b_1, elem_p2_b_1, Fext_p2_b_1, supp_p2_b_1)

print("\n Vector S:")
for val in S_p2_b_1:
    print(f"  {val}")

print("\n Vector R:")
for val in R_p2_b_1:
    print(f"  {val}")

print("\n  Matriz Rid:")
for fil in Rid_p2_b_1:
    print(f"  | {fil[0]}   {fil[1]}   {fil[2]}   {fil[3]} |")

PlotTrussForces3D(nodos_p2_b_1, elem_p2_b_1, S_p2_b_1)

# Problema 2 b.2
path_actual = os.path.dirname(__file__)
lista_nodos_p2_b_2 = []
path_nodos_p2_b_2 = os.path.join(path_actual, "NODE3.txt")
with open(path_nodos_p2_b_2, encoding="utf-8") as file:
    for line in file:
        linea_str = line.strip()
        linea_lista = linea_str.split()
        x = linea_lista[0]
        y = linea_lista[1]
        z = linea_lista[2]
        lista_nodos_p2_b_2.append([x, y, z])

nodos_p2_b_2 = np.array(lista_nodos_p2_b_2, dtype=float)

lista_elem_p2_b_2 = []
path_elem_p2_b_2 = os.path.join(path_actual, "ELEM3.txt")
with open(path_elem_p2_b_2, encoding="utf-8") as file:
    for line in file:
        linea_str = line.strip()
        linea_lista = linea_str.split()
        n_i = linea_lista[0]
        n_f = linea_lista[1]
        lista_elem_p2_b_2.append([n_i, n_f])

elem_p2_b_2 = np.array(lista_elem_p2_b_2, dtype=float)

lista_Fext_p2_b_2 = []
path_Fext_p2_b_2 = os.path.join(path_actual, "Fext3.txt")
with open(path_Fext_p2_b_2, encoding="utf-8") as file:
    for line in file:
        linea_str = line.strip()
        linea_lista = linea_str.split()
        nodo_af = linea_lista[0]
        F_x = linea_lista[1]
        F_y = linea_lista[2]
        F_z = linea_lista[3]
        lista_Fext_p2_b_2.append([nodo_af, F_x, F_y, F_z])

Fext_p2_b_2 = np.array(lista_Fext_p2_b_2, dtype=float)

lista_supp_p2_b_2 = []
path_supp_p2_b_2 = os.path.join(path_actual, "SUPP3.txt")
with open(path_supp_p2_b_2, encoding="utf-8") as file:
    for line in file:
        linea_str = line.strip()
        linea_lista = linea_str.split()
        nodo_rest = linea_lista[0]
        R_x = linea_lista[1]
        R_y = linea_lista[2]
        R_z = linea_lista[3]
        lista_supp_p2_b_2.append([nodo_rest, R_x, R_y, R_z])

supp_p2_b_2 = np.array(lista_supp_p2_b_2, dtype=float)

PlotSistem3D(nodos_p2_b_2, elem_p2_b_2)

print("\nProblema 2 b.2)")
print("\n Matriz input nodos:")
for nodo in nodos_p2_b_2:
    if nodo[0] % 1 != 0:
        print(f" {nodo[0]}  | {nodo[1]}  | {nodo[2]} \\")
    else:
        print(f" {nodo[0]} |  {nodo[1]} |  {nodo[2]} \\")

print("\n Matriz input elementos:")
for e in elem_p2_b_2:
    print(f"  {e[0]} |  {e[1]} \\")

print("\n Matriz input soportes:")
for sup in supp_p2_b_2:
    print(f" {sup[0]} |  {sup[1]}  | {sup[2]} |  {sup[3]} \\")

print("\n Matriz input Fext:")
for fu in Fext_p2_b_2:
    print(f"  | {fu[0]} |  {fu[1]}  | {fu[2]}  | {fu[3]} \\")

S_p2_b_2, R_p2_b_2, Rid_p2_b_2 = SolveTrussSystem3D(nodos_p2_b_2, elem_p2_b_2, Fext_p2_b_2, supp_p2_b_2)

print("\n Vector S:")
for val in S_p2_b_2:
    print(f"  {val}")

print("\n Vector R:")
for val in R_p2_b_2:
    print(f"  {val}")

print("\n  Matriz Rid:")
for fil in Rid_p2_b_2:
    print(f" {fil[0]} |  {fil[1]}  | {fil[2]}  | {fil[3]} \\")

PlotTrussForces3D(nodos_p2_b_2, elem_p2_b_2, S_p2_b_2)

#Problema 3
#Por calculos hechos a mano queremos que el puenmte se asemeje a la parbola
#Descrita por f(x) = -0,004x^2 + 0,54x
#entonces definimos una funcion referente a esta parabola
#Bajo prueba y error vemos que debemos dividir la parabola en 18 tramos rectos

def funcion_parabola(x):
    ecuacion = -0.004 * (x ** 2) + 0.54*x
    return ecuacion

x_por_calle = 135 / 18

lista_nodos_p3 = []

for n in range(18):
    pos_x = x_por_calle * n
    pos_y = funcion_parabola(pos_x)
    lista_nodos_p3.append([pos_x, pos_y])

lista_nodos_p3.append([135, 0])
lista_para_soportes = copy.deepcopy(lista_nodos_p3)

for nodo_x, nodo_y in lista_para_soportes:
    x_nodo_nuevo = nodo_x
    y_nodo_nuevo = nodo_y + 9.5
    lista_nodos_p3.append([x_nodo_nuevo, y_nodo_nuevo])

nodos_p3 = np.array(lista_nodos_p3, dtype=float)

#Deberiamos tener (tramos + 1) * 2 cantidad de nodos

lista_elem_p3 = []
for n in range(18):
    elem_calle = [n, n + 1]
    lista_elem_p3.append(elem_calle)

for n in range(9):
    actual = 19 + n
    elem_sup_iz_1 = [actual, n]
    elem_sup_iz_2 = [actual, n + 1]
    elem_sup_iz_3 = [actual, actual + 1]
    lista_elem_p3.append(elem_sup_iz_1)
    lista_elem_p3.append(elem_sup_iz_2)
    lista_elem_p3.append(elem_sup_iz_3)

lista_elem_p3.append([28, 9])
lista_elem_p3.append([28, 29])

for n in range(8):
    actual = 29 + n
    elem_sup_d_1 = [actual, n + 9]
    elem_sup_d_2 = [actual, n + 10]
    elem_sup_d_3 = [actual, actual + 1]
    lista_elem_p3.append(elem_sup_d_1)
    lista_elem_p3.append(elem_sup_d_2)
    lista_elem_p3.append(elem_sup_d_3)

lista_elem_p3.append([37, 17])
lista_elem_p3.append([37, 18])

elem_p3 = np.array(lista_elem_p3)

PlotSistem2D(nodos_p3, elem_p3)

supp_p3 = np.array([
    [0, 0, 1],
    [18, 1, 1]
], dtype=float)

n_elem_p3 = len(elem_p3)
Comp_max_elem = np.zeros(n_elem_p3)
Trac_max_elem = np.zeros(n_elem_p3)

comp_maxad_e_p3 = []

for i in range(19):
    n = i
    Comp_max = 0
    Trac_max = 0
    Fext_temp_p3 = np.array([[n, 0 , 240]], dtype=float)
    S_p3, R_p3, Rid_p3 = SolveTrussSystem2D(nodos_p3, elem_p3, Fext_temp_p3, supp_p3)
    PlotTrussForces2D(nodos_p3, elem_p3, S_p3)

    for num_e in range(n_elem_p3):
        fuerza_elem = S_p3[num_e][0]
        if fuerza_elem < Comp_max_elem[num_e]:
            Comp_max_elem[num_e] = fuerza_elem
        if fuerza_elem > Trac_max_elem[num_e]:
            Trac_max_elem[num_e] = fuerza_elem

    for Reaccion in S_p3:
        if Reaccion < Comp_max:
            Comp_max = Reaccion
        
        if Reaccion > Trac_max:
            Trac_max = Reaccion
    
    print(f"Traccion Maxima posición {i}:   {Trac_max}")
    print(f"Compresion Maxima posición {i}:   {Comp_max}\n")

    cumple_condicion = True


    for num_e in range(n_elem_p3):
        nod_ini_elem = nodos_p3[int(elem_p3[num_e][0])]
        nod_fin_elem = nodos_p3[int(elem_p3[num_e][1])]
        Largo_elem = np.linalg.norm(nod_fin_elem - nod_ini_elem)

        max_comp_elem = (24000 *((np.pi) ** 2))/(Largo_elem ** 2)
        comp_maxad_e_p3.append(max_comp_elem)
        f_elem = S_p3[num_e][0]

        if f_elem > 0 and abs(f_elem) > 2750:
            cumple_condicion = False
        elif f_elem < 0 and abs(f_elem) > max_comp_elem:
            cumple_condicion = False

    print(max_comp_elem)

    if cumple_condicion:
        print("El puente logro superar la carga en la posicion {n}")
    else:
        print("El puente no logro superar la carga en la posicion {n}")

print("\nDatos para tabla (Problema 3):")
print(f" Elemento | Cmax | Cadm | Tmax | Tadm | Fsc | Fst")
for el in range(n_elem_p3):
    comp_max_tab = comp_maxad_e_p3[el] if comp_maxad_e_p3[el] < 2750 else 2750
    trac_max_tab = 2750
    Fact_sc = Comp_max_elem[el] / comp_max_tab
    Fact_st = Trac_max_elem[el] / trac_max_tab
    print(f"{el} | {round(abs(Comp_max_elem[el]), 3)} | {round(comp_max_tab, 3)} | {round(Trac_max_elem[el], 3)} | {round(trac_max_tab, 3)} | {round(abs(Fact_sc), 3)} | {round(Fact_st, 3)} \\")