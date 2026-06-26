import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def AssembleBf2D(node, elem):
    matriz = np.zeros((2 * len(node), len(elem)))
    for e in range(len(elem)):
        x_i = node[int(elem[e][0])][0]
        y_i = node[int(elem[e][0])][1]
        x_f = node[int(elem[e][1])][0]
        y_f = node[int(elem[e][1])][1]

        dif_x = x_f - x_i
        dif_y = y_f - y_i

        Largo = np.sqrt((dif_x) ** 2 + (dif_y) ** 2)

        cosd_x = dif_x / Largo
        cosd_y = dif_y / Largo
        
        matriz[int(elem[e][0]) * 2][e] = cosd_x
        matriz[int(elem[e][0]) * 2 + 1][e] = cosd_y

        matriz[int(elem[e][1]) * 2][e] = -cosd_x
        matriz[int(elem[e][1]) * 2 + 1][e] = -cosd_y

    return matriz

def AssembleLr2D(node, supp):
    contador = 0
    for rest in supp:
        if rest[1] == 1:
            contador += 1

        if rest[2] == 1:
            contador += 1

    matriz = np.zeros((len(node) * 2, contador))
    contador2 = 0
    for rest in range(len(supp)):
        rest_x = supp[rest][1]
        rest_y = supp[rest][2]
        nodo = supp[rest][0]
        if rest_x == 1:
            matriz[2 * int(nodo)][contador2] = 1
            contador2 += 1
        if rest_y == 1:
            matriz[2 * int(nodo) + 1][contador2] = 1
            contador2 += 1

    return matriz

def AssembleF2D(node, Fext):
    vector = np.zeros((len(node) * 2, 1))
    
    for nodo, f_x, f_y in Fext:
        vector[int(nodo) * 2] += f_x
        vector[int(nodo) * 2 + 1] += f_y
    
    return vector

def SolveTrussSystem2D(node, elem, Fext, supp):
    mat_Bf = AssembleBf2D(node, elem)
    mat_Lr = AssembleLr2D(node, supp)
    F_ext = AssembleF2D(node, Fext)

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

        Rid.append(res)
    
    Rid = np.array(Rid)
    return F_barras, R_nodos, Rid

def PlotTrussForces2D(node, elem, S):
    plt.clf()
    plt.close("all")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_aspect("equal")

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

        fuerza = S[e][0]

        color_barra = cmap(norm(fuerza))
        ax.plot(coords_x, coords_y, color=color_barra)

    coords_x_nodos = [nodo[0] for nodo in node]
    coords_y_nodos = [nodo[1] for nodo in node]
    ax.scatter(coords_x_nodos, coords_y_nodos, color="purple")

    plt.show()

def PlotSistem2D(node, elem):
    plt.clf()
    plt.close("all")

    plt.style.use("ggplot")


    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_aspect("equal")

    for e in range(len(elem)):

        n_i = node[int(elem[e][0])]
        n_f = node[int(elem[e][1])]

        coords_x = [n_i[0], n_f[0]]
        coords_y = [n_i[1], n_f[1]]

        medio_x = (coords_x[1] + coords_x[0]) / 2
        medio_y = (coords_y[1] + coords_y[0]) / 2

        ax.plot(coords_x, coords_y, color="black")
        ax.text(medio_x, medio_y, f"B{e}", color="green", fontsize=9)

    coords_x_nodos = [nodo[0] for nodo in node]
    coords_y_nodos = [nodo[1] for nodo in node]

    ax.scatter(coords_x_nodos, coords_y_nodos, color="red")

    for n in range(len(node)):
        nx, ny = node[n]

        ax.text(nx, ny, f"N{n}", color="purple", fontsize=9)
    
    plt.show()