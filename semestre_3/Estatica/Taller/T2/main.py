from funciones import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os.path
path_actual = os.path.dirname(__file__)
nodos_p1 = np.array([
    [0, 0], #0
    [0, 3], #1
    [0, 6], #2
    [0, 9], #3
    [0, 12],#4
    [0, 15],#5
    [0, 18],#6
    [0, 21],#7
    [0, 24],#8
    [0, 27],#9
    [0, 30],#10
    [0, 33],#11
    [0, 36],#12
    [4, 3], #13
    [4, 9], #14
    [4, 15],#15
    [4, 21],#16
    [4, 27],#17
    [4, 33],#18
    [7, 6], #19
    [7, 12],#20
    [7, 18],#21
    [7, 24],#22
    [7, 30] #23
])

elementos_p1 = np.array([
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
])

fuerzas_p1 = np.array([
    [-300, 150], #0
    [0, 0], #1
    [0, 0], #2
    [0, 0], #3
    [0, 0],#4
    [0, 0],#5
    [0, 0],#6
    [0, 0],#7
    [0, 0],#8
    [0, 0],#9
    [0, 0],#10
    [0, 0],#11
    [0, 150],#12
    [150, 0], #13
    [150, 0], #14
    [0, 0],#15
    [300, 0],#16
    [0, 0],#17
    [-150, 0],#18
    [0, -750], #19
    [0, 0],#20
    [0, -100],#21
    [0, 0],#22
    [0, 300] #23
])

carga_distribuida_p1 = np.array([
    [0, -30],
    [0, -30],
    [0, -30],
    [0, -30],
    [0, -30],
    [0, -30],
    [0, -30],
    [0, -30],
    [0, -30],
    [0, -30],
    [0, -30],
    [0, -30], # fin
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0]
])
momento = np.array([[0, 0]])
r, f = NodalForces(nodos_p1, elementos_p1, fuerzas_p1, carga_distribuida_p1)
F_resultante, momento_torsor, posicion_torsor = TorsorEquivalente(r, f, momento)
plt.scatter(posicion_torsor[0][0], posicion_torsor[0][1], color="red", s=75, label="posicion torsor")
PlotReticulado(nodos_p1, elementos_p1)

#Utilar ecuacion recta en base a vector R
x = np.linspace(-3, 36, 100)
pendiente = (F_resultante[0][1]/F_resultante[0][0])
desplazamiento_y = posicion_torsor[0][1] - (pendiente * (posicion_torsor[0][0]))
recta_torsor = desplazamiento_y + pendiente * x
plt.plot(x, recta_torsor, color="green", label="Recta Torsor", linestyle="--")
plt.axis([-1, 37, -1, 8])
plt.grid(True)
#plt.show()
print("Problema 1.B), solucion:")
print(f"El vector de la fuerza resultante es:  {F_resultante[0]}")
print(f"El momento torsor del sistema es:  {momento_torsor[0]}")
print(f"La posicion del torsor es:  {posicion_torsor[0]}\n")

#Problema 2

plt.clf()
plt.figure()
poly_2_lista = []
path_poly_2 = os.path.join(path_actual, "POLY.txt")
with open(path_poly_2, encoding="utf-8") as file:
    for line in file:
        linea_str = line.strip()
        linea_lista = linea_str.split(" ")
        x = float(linea_lista[0])
        y = float(linea_lista[1])
        z = float(linea_lista[2])
        poly_2_lista.append([x, y, z])

poly_2 = np.array(poly_2_lista)

node_2_list = []
path_node_2 = os.path.join(path_actual, "NODE.txt")
with open(path_node_2, encoding="utf-8") as file:
    for line in file:
        linea_str = line.strip()
        linea_lista = linea_str.split(" ")
        x = float(linea_lista[0])
        y = float(linea_lista[1])
        node_2_list.append([x, y])

node_2 = np.array(node_2_list)

Area_p2, x_cent_p2, y_cent_p2 = Props2DGeometry(node_2, poly_2) #Calculo Area y centroides
plt.grid(True)

print(f"Problema 2,B,a):")
print(f"Area Total figura:  {Area_p2}")
print(f"Coordenadas centroide:  ({x_cent_p2}, {y_cent_p2})\n")

Plot2DGeometry(node_2, poly_2)
plt.show()

rho_2_lista = []
path_rho_2 = os.path.join(path_actual, "rho.txt")
with open(path_rho_2) as file:
    for line in file:
        linea_str = line.strip()
        num = float(linea_str)
        rho_2_lista.append([num])
    
rho_2 = np.array(rho_2_lista)

masa_total_p2, cem_p2 = MassCenter(node_2, poly_2, rho_2)
print(f"Pregunta 2,B,b):")
print(f"Masa total: {masa_total_p2}")
print(f"Ubicacion centro de masa: ({cem_p2[0][0]}, {cem_p2[1][0]})")

momento_3d = np.array([[0, 0, 0]], dtype=float)
r_f_dist_p2, f_dist_p2, elem_res = FuerzaPoligonoP2(node_2, poly_2)
sis_equi_p2 = TorsorEquivalente(r_f_dist_p2, f_dist_p2, momento_3d)
F_res_p2 = sis_equi_p2[0][0]
posicion_aplicacion_p2 = sis_equi_p2[2][0]
pos_x = posicion_aplicacion_p2[0]
pos_y = posicion_aplicacion_p2[1]
pos_z = posicion_aplicacion_p2[2]
print(f"Problema 2,B,c):")
print(f"La fuerza resultante de las cargas es:  {F_res_p2}")
print(f"La fuerza equivalente se aplica en el punto: ({pos_x}, {pos_y}, {pos_z})\n")


Plot2DForces(node_2, poly_2, f_dist_p2)
print(f"Pregunta 2,B,d):")
print(f"Indice de elemento resultante:  {elem_res}")

#Problema 3

plt.clf()

poly_3_lista = []
path_poly_3 = os.path.join(path_actual, "POLY2.txt")
with open(path_poly_3, encoding="utf-8") as file:
    for line in file:
        linea_str = line.strip()
        linea_lista = linea_str.split(" ")
        x = float(linea_lista[0])
        y = float(linea_lista[1])
        z = float(linea_lista[2])
        poly_3_lista.append([x, y, z])

poly_3 = np.array(poly_3_lista)

node_3_list = []
path_node_3 = os.path.join(path_actual, "NODE2.txt")
with open(path_node_3, encoding="utf-8") as file:
    for line in file:
        linea_str = line.strip()
        linea_lista = linea_str.split(" ")
        x = float(linea_lista[0])
        y = float(linea_lista[1])
        z = float(linea_lista[2])
        node_3_list.append([x, y, z])

node_3 = np.array(node_3_list)

alpha_p3 = 0.16
h_p3 = 15

v_0_p3_1 = 12
vd_p3_1 = np.array([[-1, 0, 0]])
v_0_p3_2 = 25
vd_p3_2 = np.array([[0.5, -(0.5 * np.sqrt(3)), 0]])
v_0_p3_3 = 8
vd_p3_3 = np.array([[0.5, (0.5 * np.sqrt(3)), 0]])
estructura_p3 = []
for nod in poly_3:
    poligono = []
    for punto in nod:
        p_poligono = node_3[int(punto)]
        poligono.append(p_poligono)
    
Plot3DForces(node_3, poly_3, )
plt.show()