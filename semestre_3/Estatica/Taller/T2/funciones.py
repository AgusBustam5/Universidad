import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.cm as cm

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
        pos = int(nodo)
        x.append(node[pos][0])
        y.append(node[pos][1])
    
    inicio_x = x[0]
    inicio_y = y[0]
    x.append(inicio_x)
    y.append(inicio_y)

    plt.plot(x, y, color="red")

def PolyProps2D(e, node, poly):
    poligono = poly[e]
    x = []
    y = []

    for nodo in poligono:
        pos = int(nodo)
        x.append(node[pos][0])
        y.append(node[pos][1])

    inicio_x = x[0]
    inicio_y = y[0]
    x.append(inicio_x)
    y.append(inicio_y)

    Area = 0
    sum_centroide_x = 0
    sum_centroide_y = 0
    for n in range(len(x) - 1):
        Area += (x[n] * y[n + 1] - x[n + 1] * y[n]) / 2
        sum_centroide_x += (x[n] + x[n + 1]) * (x[n] * y[n + 1] - x[n + 1] * y[n])
        sum_centroide_y += (y[n] + y[n + 1]) * (x[n] * y[n + 1] - x[n + 1] * y[n])
    
    centroide_x = sum_centroide_x / (6 * Area)
    centroide_y = sum_centroide_y / (6 * Area)

    return Area, centroide_x, centroide_y

#Preguntar por show()
def Plot2DGeometry(node, poly):
    for pol in range(len(poly)):
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

def PlotPoligono_Fuerza_2D(e, node, poly):
    orden = poly[e]
    nodos_poligono = []
    for n in orden:
        pol = int(n)
        nodos_poligono.append(node[pol])
    
    vertices_poligono = np.array(nodos_poligono)
    poligono = Polygon(vertices_poligono, closed=True)
    return poligono


def Plot2DForces(node, poly, s):
    fig, ax = plt.subplots()
    parches = []
    for e in range(len(poly)):
        poligono = PlotPoligono_Fuerza_2D(e, node, poly)
        parches.append(poligono)

    p = PatchCollection(parches, cmap="plasma")
    magnitudes = [np.linalg.norm(f) for f in s]

    p.set_array(np.array(magnitudes))
    ax.add_collection(p)
    ax.autoscale()
    plt.colorbar(p, label="Magnitud Fuerzas")
    plt.show()
    pass

def MassCenter(node, poly, rho):
    masa = 0
    sumas_x = 0
    sumas_y = 0

    for e in range(len(poly)):
        area, cent_x, cent_y = PolyProps2D(e, node, poly)
        masa_poli = area * rho[e]
        masa += masa_poli
        sumas_x = masa_poli * cent_x
        sumas_y = masa_poli * cent_y

    cem_x = sumas_x / masa
    cem_y = sumas_y / masa
    return masa, (cem_x, cem_y)

def FuerzaPoligonoP2(node, poly):
    lista_fuerzas = []
    lista_posiciones = []
    mayor_fuerza = None
    for e in range(len(poly)):
        area, cent_x, cent_y = PolyProps2D(e, node, poly)
        x = float(cent_x)
        y = float(cent_y)
        posicion_fuerza = [x, y, 0]
        f_dist = 2*np.sin(x) + np.cos(y) + 3 * ((np.e) ** (-1/2 * (x ** 2 + y ** 2)))
        f_res = f_dist * area
        fuerza = float(f_res)
        F = [0, 0, -fuerza]
        lista_fuerzas.append(F)
        lista_posiciones.append(posicion_fuerza)
        if mayor_fuerza is None:
            mayor_fuerza = fuerza
            elem = e
        elif mayor_fuerza < fuerza:
            mayor_fuerza = fuerza
            elem = e

    return lista_posiciones, lista_fuerzas, elem

def PolyPlot3D(e, node, poly, ax):
    poligono = poly[e]
    x = []
    y = []
    z = []
    for nodo in poligono:
        pos = int(nodo)
        x.append(node[pos][0])
        y.append(node[pos][1])
        z.append(node[pos][2])
    
    inicio_x = x[0]
    inicio_y = y[0]
    inicio_z = z[0]
    x.append(inicio_x)
    y.append(inicio_y)
    z.append(inicio_z)

    ax.plot(x, y, z, color="red")

def Plot3DGeometry(node, poly):
    figure_p3 = plt.figure()
    ax = figure_p3.add_subplot(111, projection="3d")
    for e in range(len(poly)):
        PolyPlot3D(e, node, poly, ax)

def Quadrilateral_Props(xeset):
    v1 = np.array(xeset[0] - xeset[1])
    v2 = np.array(xeset[0] - xeset[3])
    cruz = np.cross(v1, v2)
    area = np.linalg.norm(cruz)
    v_normal_director = cruz / area
    x_sum += 0
    y_sum += 0
    z_sum += 0
    for punto in xeset:
        x_sum += punto[0]
        y_sum += punto[1]
        z_sum += punto[2]

    x = x_sum / 4
    y = y_sum / 4
    z = z_sum / 4

    posicion = (x, y, z)
    return area, posicion, v_normal_director

def Plot3DForces(node, poly, s):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    poligonos = []
    for vertice in poly:
        poligono = []
        for nodo in vertice:
            punt = node[int(nodo)]
            poligono.append(punt)
        poligonos.append(poligono)
    
    cmap = cm.plasma
    valores = [cmap(fuerza) for fuerza in s]
    coleccion = Poly3DCollection(poligonos, facecolors=valores)

    ax.add_collection3d(coleccion)

    plt.show()

def WindPressure(alpha, h, v0, z):
    velocidad = v0 * ((z / h) ** alpha)
    presion = 0.613 * (velocidad ** 2)
    return presion

def WindEquivalentForces(xeset, dhat, P):
    area, posicion, v_normal_director = Quadrilateral_Props(xeset)
    fuerza = area * P
    vector_fuerza = fuerza * dhat
    punto = np.dot(vector_fuerza, v_normal_director)
    if punto < 0:
        #Proyeccion vectorial de dhat en la normal del ventanal
        mod_director = np.linalg.norm(v_normal_director)
        proy_dhat = (punto / (mod_director ** 2)) * v_normal_director
        return proy_dhat