import numpy as np
import copy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors

def AssembleBf3D(node, elem):
    matriz = np.zeros((3 * len(node), len(elem)))
    for e in range(len(elem)):
        x_i = node[int(elem[e][0])][0]
        y_i = node[int(elem[e][0])][1]
        z_i = node[int(elem[e][0])][2]

        x_f = node[int(elem[e][1])][0]
        y_f = node[int(elem[e][1])][1]
        z_f = node[int(elem[e][1])][2]

        dif_x = x_f - x_i
        dif_y = y_f - y_i
        dif_z = z_f - z_i

        Largo = np.sqrt((dif_x) ** 2 + (dif_y) ** 2 + (dif_z) ** 2)

        cosd_x = dif_x / Largo
        cosd_y = dif_y / Largo
        cosd_z = dif_z / Largo
        
        matriz[int(elem[e][0]) * 3][e] = cosd_x
        matriz[int(elem[e][0]) * 3 + 1][e] = cosd_y
        matriz[int(elem[e][0]) * 3 + 2][e] = cosd_z

        matriz[int(elem[e][1]) * 3][e] = -cosd_x
        matriz[int(elem[e][1]) * 3 + 1][e] = -cosd_y
        matriz[int(elem[e][1]) * 3 + 2][e] = -cosd_z

    return matriz

def AssembleLr3D(node, supp):
    contador = 0
    for rest in supp:
        if rest[1] == 1:
            contador += 1

        if rest[2] == 1:
            contador += 1
        
        if rest[3] == 1:
            contador += 1

    matriz = np.zeros((len(node) * 3, contador))
    contador2 = 0
    for rest in range(len(supp)):
        nodo, rest_x, rest_y, rest_z = supp[rest]
        if rest_x == 1:
            matriz[3 * int(nodo)][contador2] = 1
            contador2 += 1
        if rest_y == 1:
            matriz[3 * int(nodo) + 1][contador2] = 1
            contador2 += 1
        
        if rest_z == 1:
            matriz[3 * int(nodo) + 2][contador2] = 1
            contador2 += 1
    return matriz

def AssembleF3D(node, Fext):
    vector = np.zeros((len(node) * 3, 1))
    
    for nodo, f_x, f_y, f_z in Fext:
        vector[int(nodo) * 3] += f_x
        vector[int(nodo) * 3 + 1] += f_y
        vector[int(nodo) * 3 + 2] += f_z

    return vector

def SolveTrussSystem3D(node, elem, Fext, supp):
    mat_Bf = AssembleBf3D(node, elem)
    mat_Lr = AssembleLr3D(node, supp)
    F_ext = AssembleF3D(node, Fext)

    mat_glob = np.hstack((mat_Bf, mat_Lr))
    sistema_resuelto = np.linalg.solve(mat_glob, F_ext)

    F_barras = sistema_resuelto[:len(elem)]
    R_nodos = sistema_resuelto[len(elem):]
    mat_iter = R_nodos.flatten().tolist()
    supp_ref = copy.deepcopy(supp)

    Rid = []
    for res in supp_ref:
        if res[1] == 1:
            res[1] = mat_iter.pop(0)
        
        if res[2] == 1:
            res[2] = mat_iter.pop(0)
        
        if res[3] == 1:
            res[3] = mat_iter.pop(0)

        Rid.append(res)
    
    Rid = np.array(Rid)
    return F_barras, R_nodos, Rid

def PlotTrussForces3D(node, elem, S):
    plt.clf()
    plt.close("all")

    fig, ax = plt.subplots()
    ax = fig.add_subplot(111, projection="3d")

    plt.style.use("ggplot")

    fuerzas = [S[e][0] for e in range(len(elem))]
    f_minima = min(fuerzas)
    f_maxima = max(fuerzas)
    modulo_maximo = max(abs(f_minima), abs(f_maxima))
    if modulo_maximo == 0:
        modulo_maximo = 1

    norm = mcolors.TwoSlopeNorm(vmin=-modulo_maximo, vcenter=0, vmax=modulo_maximo)
    cmap = plt.cm.seismic

    for e in range(len(elem)):

        n_i = node[int(elem[e][0])]
        n_f = node[int(elem[e][1])]

        coords_x = [n_i[0], n_f[0]]
        coords_y = [n_i[1], n_f[1]]
        coords_z = [n_i[2], n_f[2]]

        fuerza = S[e][0]

        color_barra = cmap(norm(fuerza))
        ax.plot(coords_x, coords_y, coords_z ,color=color_barra)

    coords_x_nodos = [nodo[0] for nodo in node]
    coords_y_nodos = [nodo[1] for nodo in node]
    coords_z_nodos = [nodo[2] for nodo in node]

    ax.scatter(coords_x_nodos, coords_y_nodos, coords_z_nodos, color="purple")

    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")

    plt.show()

def PlotSistem3D(node, elem):
    plt.clf()
    plt.close("all")
    
    fig, ax = plt.subplots()
    ax = fig.add_subplot(111, projection="3d")

    for e in range(len(elem)):

        n_i = node[int(elem[e][0])]
        n_f = node[int(elem[e][1])]

        coords_x = [n_i[0], n_f[0]]
        coords_y = [n_i[1], n_f[1]]
        coords_z = [n_i[2], n_f[2]]

        medio_x = (coords_x[1] + coords_x[0]) / 2
        medio_y = (coords_y[1] + coords_y[0]) / 2
        medio_z = (coords_z[1] + coords_z[0]) / 2

        ax.plot(coords_x, coords_y, coords_z, color="black")
        ax.text(medio_x, medio_y, medio_z, f"B{e}", color="green", fontsize=9)

    coords_x_nodos = [nodo[0] for nodo in node]
    coords_y_nodos = [nodo[1] for nodo in node]
    coords_z_nodos = [nodo[2] for nodo in node]

    ax.scatter(coords_x_nodos, coords_y_nodos, coords_z_nodos, color="red")

    for n in range(len(node)):
        nx, ny, nz = node[n]

        ax.text(nx, ny, nz, f"N{n}", color="purple", fontsize=9)
    
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")

    plt.show()