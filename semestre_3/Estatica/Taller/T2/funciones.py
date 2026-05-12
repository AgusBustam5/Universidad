import numpy as np
import matplotlib.pyplot as plt
import copy

def Sistema_equivalente(r, F, M, x):
    dimension = len(r[0])
    fuerza_resultante = np.array([[0,0,0]], dtype=float)
    momentos_de_fuerzas = np.array([[0,0,0]], dtype = float)
    momentos_libres = np.array([[0, 0, 0]], dtype = float)
    for i in range(len(F)):
        if dimension == 3:
            fuerza_resultante += F[i]
        elif dimension == 2:
            fuerza_resultante += np.array([[F[i][0], F[i][1], 0]], dtype = float)
    for i in range(len(r)):
        if dimension == 3:
            pos_final = r[i] - x
            momento_actual = np.cross(pos_final,F[i])
        elif dimension == 2:
            pos_final = np.array([[r[i][0], r[i][1], 0]], dtype = float) - np.array([[x[0][0], x[0][1], 0]], dtype = float)
            momento_actual = np.cross(pos_final,np.array([[F[i][0], F[i][1], 0]], dtype = float))
        momentos_de_fuerzas += momento_actual
    for i in range(len(M)):
        if dimension == 3:
            momentos_libres += M[i]
        elif dimension == 2:
            momentos_libres += np.array([[M[i][0], M[i][1], 0]], dtype = float)
    momento_final = momentos_de_fuerzas + momentos_libres
    return fuerza_resultante, momento_final

def TorsorEquivalente(r, F, M):
    dimension = len(r[0])
    fuerza_momento = Sistema_equivalente(r, F, M, np.array([[0, 0, 0]], dtype = float))
    R = fuerza_momento[0]
    M_o = fuerza_momento[1]
    modulo_fuerza = np.linalg.norm(R)
    momento_torsor = (np.dot(R[0], M_o[0])/(modulo_fuerza**2)) * R
    posicion_torsor_perpendicular = np.cross(R, M_o)/(modulo_fuerza**2)
    #Buscamos interseccion con z = 0, mediante la ecuacion del eje central
    posicion_torsor_perpendicular_z = posicion_torsor_perpendicular[0][dimension - 1]
    Resultante_fuerzas_z_y = R[0][dimension - 1]
    if Resultante_fuerzas_z_y == 0:
        return R, momento_torsor, posicion_torsor_perpendicular
    posicion_z_y_perpendicular = posicion_torsor_perpendicular[0][dimension - 1]
    t = -(posicion_z_y_perpendicular/Resultante_fuerzas_z_y) 
    if dimension == 3:
        posicion_x = posicion_torsor_perpendicular[0][0] + t * R[0][0]
        posicion_y = posicion_torsor_perpendicular[0][1] + t * R[0][1]
        posicion_torsor = np.array([[posicion_x, posicion_y, 0]], dtype = float)
    elif dimension == 2:
        posicion_x = posicion_torsor_perpendicular[0][0] + t * R[0][0]
        posicion_torsor = np.array([[posicion_x, 0, 0]], dtype = float)
    return R, momento_torsor, posicion_torsor

def NodalForces(node, elem, f_ext, q_ext):
    lista_fuerzas = []
    lista_r = []
    
    #Fuerzas externas y sus respectivas posiciones
    for n in range(len(node)):
        if 0 != f_ext[n][0] or 0 != f_ext[n][1]:
            lista_fuerzas.append(f_ext[n])
            lista_r.append(node[n])
    
    for f in range(len(elem)):
        if q_ext[f][0] != 0 or q_ext[f][1] != 0:
            p_inicio = elem[f][0]
            p_final = elem[f][1]
            inicio = node[p_inicio]
            final = node[p_final]
            vector = final - inicio
            distancia = np.linalg.norm(vector)
            fuerza_total = distancia * q_ext[f]
            fuerza_nodo = fuerza_total / 2
            lista_fuerzas.append(fuerza_nodo)
            lista_r.append(inicio)
            lista_fuerzas.append(fuerza_nodo)
            lista_r.append(final)
        
    return np.array(lista_r), np.array(lista_fuerzas)

def PlotReticulado(node, elem):
    x = []
    y = []
    for num_nodo in elem:
        nodo1_x = node[num_nodo[0]][0]
        nodo1_y = node[num_nodo[0]][1]
        nodo2_x = node[num_nodo[1]][0]
        nodo2_y = node[num_nodo[1]][1]
        coord_x = np.array([nodo1_x, nodo2_x])
        coord_y = np.array([nodo1_y, nodo2_y])
        x.append(coord_x)
        y.append(coord_y)
        plt.plot(coord_y, coord_x, color="black")
    return [x, y]

def PolyPlot2D(e, node, poly):
    poligono = poly[e]
    x = []
    y = []

    for nodo in poligono:
        x.append(node[nodo, 0])
        y.append(node[nodo, 1])
    
    inicio_x = x[0]
    inicio_y = y[0]
    x.append(inicio_x)
    y.append(inicio_y)

    plt.plot(x, y, color="red")
    plt.show()


def PolyProps2D(e, node, poly):
    poligono = poly[e]
    x = []
    y = []

    for nodo in poligono:
        x.append(node[nodo, 0])
        y.append(node[nodo, 1])

    inicio_x = x[0]
    inicio_y = y[0]
    x.append(inicio_x)
    y.append(inicio_y)

    Area = 0
    sum_centroide_x = 0
    sum_centroide_y = 0
    for n in range(len(n) - 1):
        Area += (x[n] * y[n + 1] - x[n + 1] * y[n]) / 2
        sum_centroide_x += (x[n] + x[n + 1]) * (x[n] * y[n + 1] - x[n + 1] * y[n])
        sum_centroide_y += (y[n] + y[n + 1]) * (x[n] * y[n + 1] - x[n + 1] * y[n])
    
    centroide_x = sum_centroide_x / (6 * Area)
    centroide_y = sum_centroide_y / (6 * Area)

    return Area, centroide_x, centroide_y

#Preguntar por show()
def Plot2DGeometry(node, poly):
    for pol in poly:
        PolyPlot2D(pol, node, poly)

def Props2DGeometry(node, poly):
    Area = 0
    sum_centroides_x_area = 0
    sum_centroides_y_area = 0
    for p in range(len(poly)):
        datos = PolyProps2D(p, node, poly)
        Area += datos[0]
        sum_centroides_x_area += datos[1] * datos[0]
        sum_centroides_y_area += datos[2] * datos[0]
    
    centroide_x = sum_centroides_x_area / Area
    centroide_y = sum_centroides_y_area / Area

    return Area, centroide_x, centroide_y

def Plot2DForces(node, poly, s):
    