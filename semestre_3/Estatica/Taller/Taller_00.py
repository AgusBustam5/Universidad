import numpy as np

def Quadrilateral_Props(xeset):
    N1 = xeset[0]
    N2 = xeset[1]
    N3 = xeset[2]
    N4 = xeset[3]

    v1_2 = N2 - N1
    v1_4 = N4 - N1

    v_perp = np.cross(v1_2, v1_4)

    A = np.linalg.norm
    nhat = v_perp / A

    xc = np.mean(xeset)

    return A, xc, nhat


def WindEquivalentForces(xeset, dhat, P):
    pass
#F = 100*z

node = np.array([
    [0, 0, 0],
    [3, 0, 0],
    [3, 3, 0],
    [0, 7, 0],
    [0, 0, 6],
    [3, 0, 6],
    [3, 3, 6],
    [0, 7, 6]], dtype=float)

poly = np.array([
    [0, 1, 5, 4],
    [1, 2, 6, 5],
    [2, 3, 7, 6],
    [3, 0, 4, 7]], dtype=int)

F_total = 0
F_ventanas = []
n_ventanas = poly.shape[0]
for e in range(n_ventanas):
    ind_nodos = poly[e]
    nodos = node[ind_nodos]
    A, xc, nhat = Quadrilateral_Props(node)
    P_e = 100 * xc[2] #100*z
    p_nhat = np.dot(P_e, nhat)
    if p_nhat >= 0:
        F_ventanas.append(0)
    elif p_nhat < 0:
        F_ventana = p_nhat * A # * nhat para resultado vectorial
        F_total += F_ventana
        F_ventanas.append(F_ventana)