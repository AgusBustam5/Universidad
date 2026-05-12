import Taller_00
def WindEquivalentForces(xeset, dhat, P):
    pass

F = 100*z

F_total = 0
F_ventanas = []

n_ventanas = poly.shape[0]
for e in range(n_ventanas):
    ind_nodos = poly[e]
    nodos = nodo[ind_nodos]

    A, xc, nhat = Quadrilateral_Props()

    P_e = 100 * xc[2] #100*z
    p_nhat = np.dot(P_e, nhat)

    if p_nhat >= 0:
        F_ventanas.append(0)
    elif p_nhat < 0:
        F_ventana = p_nhat * A # * nhat para resultado vectorial
        F_total += F_ventana
        F_ventanas.append(F_ventana)