import numpy as np

def AssembleBf2D(node, elem):
    matriz = np.zeros((2 * len(node), len(elem)))
    for e in range(len(elem)):
        x_i = node[elem[e][0]][0]
        y_i = node[elem[e][0]][1]
        x_f = node[elem[e][1]][0]
        y_f = node[elem[e][1]][1]

        dif_x = x_f - x_i
        dif_y = y_f - y_i

        Largo = np.sqrt((dif_x) ** 2 + (dif_y) ** 2)

        cosd_x = dif_x / Largo
        cosd_y = dif_y / Largo

        matriz[elem[e][0] * 2][e] = cosd_x
        matriz[elem[e][0] * 2 + 1][e] = cosd_y

        matriz[elem[e][1] * 2][e] = -cosd_x
        matriz[elem[e][1] * 2 + 1][e] = -cosd_y

    return matriz

def AssembleLf2D(node, supp):
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
            matriz[2 * nodo][contador2] = 1
            contador2 += 1
        if rest_y == 1:
            matriz[2 * nodo + 1][contador2] = 1
            contador2 += 1

    return matriz

