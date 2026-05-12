from funciones import *
import numpy as np
import matplotlib.pyplot as plt
nodos = np.array([
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

elementos = np.array([
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

fuerzas = np.array([
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

carga_distribuida = np.array([
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
plt.figure()
momento = np.array([[0, 0]])
r, f = NodalForces(nodos, elementos, fuerzas, carga_distribuida)
F_resultante, momento_torsor, posicion_torsor = TorsorEquivalente(r, f, momento)
plt.scatter(posicion_torsor[0][0], posicion_torsor[0][1], color="red", s=75, label="posicion torsor")
coords = PlotReticulado(nodos, elementos)

#Utilar ecuacion recta en base a vector R
x = np.linspace(-3, 36, 100)
pendiente = (F_resultante[0][1]/F_resultante[0][0])
desplazamiento_y = posicion_torsor[0][1] - (pendiente * (posicion_torsor[0][0]))
recta_torsor = desplazamiento_y + pendiente * x
plt.plot(x, recta_torsor, color="green", label="Recta Torsor", linestyle="--")
plt.axis([-1, 37, -1, 8])
plt.grid(True)
plt.show()
print("Problema 1.B), solucion:\n")
print(f"El vector de la fuerza resultante es:  {F_resultante[0]}")
print(f"El momento torsor del sistema es:  {momento_torsor[0]}")
print(f"La posicion del torsor es:  {posicion_torsor[0]}")

#Problema 2

plt.clf()