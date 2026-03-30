import numpy as np

def Sistema_equivalente(r: np.array(list[list[int]]), F: np.array(list[list[int]]), M: np.array(list[list[int]]), x: np.array(list[int])):
    fuerza_resultante = np.array([[0,0,0]], dtype=float)
    for i in range(len(F)):
        fuerza_resultante += F[i]
    momentos_de_fuerzas = np.array([[0,0,0]], dtype = float)
    for i in range(len(r)):
        pos_final = r[i] - x
        momento_actual = np.cross(pos_final,F[i])
        momentos_de_fuerzas += momento_actual
    momentos_libres = np.array([[0, 0, 0]], dtype = float)
    for i in range(len(M)):
        momentos_libres += M[i]
    momento_final = momentos_de_fuerzas + momentos_libres
    return fuerza_resultante, momento_final
r1  = np.array([[0,0,0.3]], dtype = float)

f1 = np.array([[0,-100, 0]], dtype = float)

m1 = np.array([[-75, 0, 0]], dtype = float)

origen = np.array([[0, 0.5, 0]], dtype = float)
print(Sistema_equivalente(r1, f1, m1, origen))