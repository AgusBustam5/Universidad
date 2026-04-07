import numpy as np
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
origen_2d = np.array([[0, 0]], dtype = float)
origen_3d = np.array([[0, 0, 0]], dtype = float)

#Problema 2 a)
lista_distancias_p1 = []

calculo_ej1_d1_y = -(1 + np.cos(30) * 1.5)
calculo_ej1_d1_z = np.sin(30) * 1.5
p1_d1  = [0,calculo_ej1_d1_y,calculo_ej1_d1_z]
lista_distancias_p1.append(p1_d1)

calculo_ej1_d2_y = calculo_ej1_d1_y
calculo_ej1_d2_z = calculo_ej1_d1_z
p1_d2 = [-2.5, calculo_ej1_d2_y,calculo_ej1_d2_z]
lista_distancias_p1.append(p1_d2)

p1_dt = np.array(lista_distancias_p1, dtype = float)

lista_fuerzas_p1 = []

calculo_ej1_uni_f1 = p1_d1/(np.linalg.norm(np.array(p1_d1)))
p1_f1 = 300*calculo_ej1_uni_f1
lista_fuerzas_p1.append(p1_f1)

calculo_ej1_uni_f2 = [-2, p1_d2[1], p1_d2[2]]/(np.linalg.norm(np.array([-2, p1_d2[1], p1_d2[2]])))
p1_f2 = 250*calculo_ej1_uni_f2
lista_fuerzas_p1.append(p1_f2)

p1_ft = np.array(lista_fuerzas_p1, dtype = float)

lista_momentos_p1 = []

p1_m1 = [ 0, 0, 0]
lista_momentos_p1.append(p1_m1)

p1_mt = np.array(lista_momentos_p1, dtype = float)

p1_pos_D = np.array([[-0.5, 0, 0]], dtype = float)
p1_pos_C = np.array([p1_d2], dtype = float)

sistema_a_p1 = Sistema_equivalente(p1_dt, p1_ft, p1_mt, p1_pos_D)
sistema_b_p1 = Sistema_equivalente(p1_dt, p1_ft, p1_mt, p1_pos_C)
Torsor_sistema_p1 = TorsorEquivalente(p1_dt, p1_ft, p1_mt)

print("\nResultados Problema 2, sistema 1\n")

print(" Sistema respecto a D:\n")
print("   Fuerza resultante sistema: ", sistema_a_p1[0][0])
print("   Momento resultante sistema: ", sistema_a_p1[1][0])

print("\nSistema respecto a C:\n")
print("   Fuerza resultante sistema: ", sistema_b_p1[0][0])
print("   Momento resultante sistema: ", sistema_b_p1[1][0])

print("\n Torsor sistema equivalente:\n")
print("   Fuerza resultante torsor: ", Torsor_sistema_p1[0][0])
print("   Momento tosor: ", Torsor_sistema_p1[1][0])
print("   Posicion Torsor repecto al origen: ", Torsor_sistema_p1[2][0])

#Problema 2 b)
#Numeramos de izquierda a derecha y de arriba hacia abajo

#agrupar distancias
lista_distancias_p2 = []

p2_d1  = [6, 7]
lista_distancias_p2.append(p2_d1)

p2_d2  = [12, 7]
lista_distancias_p2.append(p2_d2)

p2_d3  = [24, 7]
lista_distancias_p2.append(p2_d3)

p2_d4  = [30, 7]
lista_distancias_p2.append(p2_d4)

p2_d5  = [33, 4]
lista_distancias_p2.append(p2_d5)

p2_d6  = [3, 0]
lista_distancias_p2.append(p2_d6)

p2_d7  = [6, 0]
lista_distancias_p2.append(p2_d7)

p2_d8  = [15, 0]
lista_distancias_p2.append(p2_d8)

p2_d9  = [21, 0]
lista_distancias_p2.append(p2_d9)

p2_d10  = [33, 0]
lista_distancias_p2.append(p2_d10)

p2_dt = np.array(lista_distancias_p2, dtype = float)

#Agrupar fuerzas

lista_fuerzas_p2 = []

modulo_f_sup = np.linalg.norm(np.array([[6, 7]], dtype = float))
modulo_f_inf = np.linalg.norm(np.array([[3, 4]], dtype = float))

p2_f1 = [6 * (150/modulo_f_sup), (-7) * (150/modulo_f_sup)]
lista_fuerzas_p2.append(p2_f1)

p2_f2 = [6 * (250/modulo_f_sup), (-7) * (250/modulo_f_sup)]
lista_fuerzas_p2.append(p2_f2)

p2_f3 = [(-6) * (180/modulo_f_sup), (-7) * (180/modulo_f_sup)]
lista_fuerzas_p2.append(p2_f3)

p2_f4 = [(-6) * (125/modulo_f_sup), (-7) * (125/modulo_f_sup)]
lista_fuerzas_p2.append(p2_f4)

p2_f5 = [250, 0]
lista_fuerzas_p2.append(p2_f5)

p2_f6 = [0, -100]
lista_fuerzas_p2.append(p2_f6)

p2_f7 = [3 * (150/modulo_f_inf), (-4) * (150/modulo_f_inf)]
lista_fuerzas_p2.append(p2_f7)

p2_f8 = [0, -75]
lista_fuerzas_p2.append(p2_f8)

p2_f9 = [0, -250]
lista_fuerzas_p2.append(p2_f9)

p2_f10 = [0, -125]
lista_fuerzas_p2.append(p2_f10)

p2_ft = np.array(lista_fuerzas_p2, dtype = float)

lista_momentos_p2 = []

p2_m1 = [0, 0]
p2_mt = np.array(lista_momentos_p2, dtype = float)

p2_pos_D = np.array([[9, 4]], dtype = float)
p2_pos_C = np.array([[30, 0]], dtype = float)

sistema_a_p2 = Sistema_equivalente(p2_dt, p2_ft, p2_mt, p2_pos_D)
sistema_b_p2 = Sistema_equivalente(p2_dt, p2_ft, p2_mt, p2_pos_C)
Torsor_sistema_p2 = TorsorEquivalente(p2_dt, p2_ft, p2_mt)

print("\nResultados Problema 2, sistema 2 \n")

print(" Sistema respecto a D:  \n")
print("   Fuerza resultante sistema: ", sistema_a_p2[0][0])
print("   Momento resultante sistema: ", sistema_a_p2[1][0])

print("\n Sistema respecto a C:  \n")
print("   Fuerza resultante sistema: ", sistema_b_p2[0][0])
print("   Momento resultante sistema: ", sistema_b_p2[1][0])

print("\n Torsor sistema equivalente")
print("   Fuerza resultante torsor: ", Torsor_sistema_p2[0][0])
print("   Momento tosor: ", Torsor_sistema_p2[1][0])
print("   Posicion Torsor repecto al origen: ", Torsor_sistema_p2[2][0], "\n")

#Problema 3 a)
#queremos que la suma de momentos en el punto G sea de 0
lista_distancias_p3 = copy.deepcopy(lista_distancias_p2)
lista_fuerzas_p3 = copy.deepcopy(lista_fuerzas_p2)
lista_fuerzas_p3.pop(4)
lista_distancias_p3.pop(4)

lista_fuerzas_p3.pop(7)
lista_distancias_p3.pop(7)

p3_a_dt = np.array(lista_distancias_p3)
p3_a_ft = np.array(lista_fuerzas_p3)
p3_sistema_sin_P = Sistema_equivalente(p3_a_dt, p3_a_ft, p2_mt, np.array([[18, 0, 0]], dtype = float))
p3_mp1 = np.cross(np.array([[33-18, 4, 0]]), np.array([[1, 0, 0]]))
p3_mp2 = np.cross(np.array([[21-18, 0, 0]]), np.array([[0, -1, 0]]))
num_de_P = p3_mp1[0][2] + p3_mp2[0][2]
valor_P = -(p3_sistema_sin_P[1][0][2]/num_de_P)

print("Resultados Problema 3, a")
print("  El valor para P necesario: ", valor_P, "\n")

#Problema 3 b)

#como sabemos que al aplicar fuerzas en el origen no producen momento, podemos afirmar que la fuerza R2 es el unico que influye a este

lista_distancias_p3_b = copy.deepcopy(lista_distancias_p2)
lista_fuerzas_p3_b = copy.deepcopy(lista_fuerzas_p2)
l_d_p3_b_B = copy.deepcopy(lista_distancias_p2)
l_f_p3_b_B = copy.deepcopy(lista_fuerzas_p2)

sistema_p2_b_respecto_A = Sistema_equivalente(p2_dt, p2_ft, p2_mt, origen_2d)
momento_p2_b_respecto_A = sistema_p2_b_respecto_A[1]

sistema_p2_b_respecto_B = Sistema_equivalente(p2_dt, p2_ft, p2_mt, np.array([[36,0]], dtype = float))
momento_p2_b_respecto_B = sistema_p2_b_respecto_B[1]

fuerza_p3_b_r3_A = momento_p2_b_respecto_A[0][2]/36
fuerza_p3_b_r3_B = -momento_p2_b_respecto_B[0][2]/36

lista_distancias_p3_b.append([36, 0])
lista_fuerzas_p3_b.append([0, -fuerza_p3_b_r3_A])

l_d_p3_b_B.append([0, 0])
l_f_p3_b_B.append([0, -fuerza_p3_b_r3_B])

p3_b_dt = np.array(lista_distancias_p3_b, dtype = float)
p3_b_ft = np.array(lista_fuerzas_p3_b, dtype = float)
p3_b_mt = np.array([[0,0]], dtype = float)

p3_b_dt_B = np.array(l_d_p3_b_B, dtype = float)
p3_b_ft_B = np.array(l_f_p3_b_B, dtype = float)

sistema_p2_b_respecto_0_r3 = Sistema_equivalente(p3_b_dt, p3_b_ft, p3_b_mt, origen_2d)
sistema_p2_b_respecto_B_r1 = Sistema_equivalente(p3_b_dt_B, p3_b_ft_B, p3_b_mt, np.array([[36, 0]], dtype = float))

p3_b_fr_x = -sistema_p2_b_respecto_0_r3[0][0][0]
p3_b_fr_y = -sistema_p2_b_respecto_0_r3[0][0][1]
p3_b_fr_y_B = -sistema_p2_b_respecto_B_r1[0][0][1]

lista_distancias_p3_b.append([0, 0])
lista_fuerzas_p3_b.append([p3_b_fr_x, 0])
l_d_p3_b_B.append([0, 0])
l_f_p3_b_B.append([p3_b_fr_x, 0])

lista_distancias_p3_b.append([0, 0])
lista_fuerzas_p3_b.append([0, p3_b_fr_y])
l_d_p3_b_B.append([36, 0])
l_f_p3_b_B.append([0, p3_b_fr_y_B])

p3_b_2_dt = np.array(lista_distancias_p3_b, dtype = float)
p3_b_2_ft = np.array(lista_fuerzas_p3_b, dtype = float)
p3_b_2_dt_B = np.array(l_d_p3_b_B, dtype = float)
p3_b_2_ft_B = np.array(l_f_p3_b_B, dtype = float)

print(Sistema_equivalente(p3_b_2_dt, p3_b_2_ft, p3_b_mt, origen_2d))
print(Sistema_equivalente(p3_b_2_dt_B, p3_b_2_ft_B, p3_b_mt, np.array([[36,0]], dtype = float)))

print("Resultados Problema 3, b\n")
print(" Respecto al punto A")
print("  Valor para R1: ", f"(0, {p3_b_fr_y})")
print("  Valor para R2: ", f"({p3_b_fr_x}, 0)")
print("  Valor para R3: ", f"(0, {fuerza_p3_b_r3_A})", "\n")

print(" Respecto al punto B")
print("  Valor para R1: ", f"(0, {p3_b_fr_y_B})")
print("  Valor para R2: ", f"({p3_b_fr_x}, 0)")
print("  Valor para R3: ", f"(0, {fuerza_p3_b_r3_B})", "\n")

#Problema 3 c)

R1_max = ""
R1_min = ""
pos_max = -1
pos_min = -1
for i in range(12):
    copia_lista_distancias_puente = copy.deepcopy(lista_distancias_p2)
    copia_lista_fuerzas_puente = copy.deepcopy(lista_fuerzas_p2)
    posicion_rueda_1 = 3*i
    posicion_rueda_2 = 3*i + 3
    peso_por_rueda = -200
    copia_lista_distancias_puente.append([posicion_rueda_1, 0])
    copia_lista_distancias_puente.append([posicion_rueda_2, 0])
    copia_lista_fuerzas_puente.append([0, peso_por_rueda])
    copia_lista_fuerzas_puente.append([0, peso_por_rueda])
    p3_c_sr_dt = np.array(copia_lista_distancias_puente, dtype = float)
    p3_c_sr_ft = np.array(copia_lista_fuerzas_puente, dtype = float)
    p3_c_mt = p3_b_mt

    sistema_sin_rs_respecto_0 = Sistema_equivalente(p3_c_sr_dt, p3_c_sr_ft, p3_c_mt, origen_2d)
    momento_p3_con_camion = sistema_sin_rs_respecto_0[1][0][2]
    fuerza_r2_con_camion = -momento_p3_con_camion/36
    copia_lista_distancias_puente.append([36, 0])
    copia_lista_fuerzas_puente.append([0, fuerza_r2_con_camion])
    p3_c_cr3_dt = np.array(copia_lista_distancias_puente, dtype = float)
    p3_c_cr3_ft = np.array(copia_lista_fuerzas_puente, dtype = float)
    sistema_c_cr3 = Sistema_equivalente(p3_c_cr3_dt, p3_c_cr3_ft, p3_c_mt, origen_2d)
    p3_c_fr_r3 = -sistema_c_cr3[0][0][0]
    p3_c_fr_r1 = -sistema_c_cr3[0][0][1]

    if R1_max == "":
        R1_max = p3_c_fr_r1
        pos_max = i * 3
    elif R1_max < p3_c_fr_r1:
        R1_max = p3_c_fr_r1
        pos_max = i * 3

    if R1_min == "":
        R1_min = p3_c_fr_r1
        pos_min = i * 3
    elif R1_min > p3_c_fr_r1:
        pos_min = i * 3
        R1_min = p3_c_fr_r1
    copia_lista_distancias_puente.append([0, 0])
    copia_lista_distancias_puente.append([0, 0])
    copia_lista_fuerzas_puente.append([p3_c_fr_r3, 0])
    copia_lista_fuerzas_puente.append([0, p3_c_fr_r1])
    prueba_dt = np.array(copia_lista_distancias_puente, dtype = float)
    prueba_ft = np.array(copia_lista_fuerzas_puente, dtype = float)

print("Resultados Problema 3, c\n")
print("(Posicion referenta a la rueda trasera del camion)")
print(f"  Posicion del camion para el valor maximo de R1: ({pos_max}, 0), con R1 = (0, {R1_max})")
print(f"  Posicion del camion para el valor minimo de R1: ({pos_min}, 0), con R1 = (0, {R1_min})")