import numpy as np
import matplotlib.pyplot as plt
def distancia(vect1, vect2):
    v3 = vect2 - vect1
    dis = np.dot(v3,v3)**(1/2)
    return dis
v1_ini = []
v2_ini = []
for i in range(3):
    cord = input(f"selecciona la coordenada {i} del vector 1:")
    cord = float(cord)
    v1_ini.append(cord)
for i in range(3):
    cord = input(f"selecciona la coordenada {i} del vector 2:")
    cord = float(cord)
    v2_ini.append(cord)
print(v1_ini)
v1 = np.array(v1_ini)
v2 = np.array(v2_ini)
distancia_f = distancia(v1,v2)
print(f"la distancia entre los puntos A y B es de {distancia_f}")