import numpy as np

def Sistema_equivalente(r, F, M, x):
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

def TorsorEquivalente(r, F, M):
    fuerza_momento = Sistema_equivalente(r, F, M, np.array([[0, 0, 0]]))
    R = fuerza_momento[0]
    M_o = fuerza_momento[1]
    modulo_fuerza = np.linalg.norm(R)
    momento_torsor = (np.dot(R[0], M_o[0])/(modulo_fuerza**2))*R

    return momento_torsor
    pass
lista_distancias = []
d1  = [0,0,0.3]
lista_distancias.append(d1)
dt = np.array(lista_distancias, dtype = float)

lista_fuerzas = []
f1 = [0,-100, 0]
lista_fuerzas.append(f1)
ft = np.array(lista_fuerzas, dtype = float)

lista_momentos = []
m1 = [-75, 0, 0]
lista_momentos.append(m1)
mt = np.array(lista_momentos, dtype = float)

print(dt,ft,mt)

origen = np.array([[0, 0.5, 0]], dtype = float)
print(Sistema_equivalente(dt, ft, mt, origen))
print(TorsorEquivalente(dt,ft,mt))