import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
os.chdir(os.path.dirname(os.path.abspath(__file__)))


#Reutilizamos las funciones de la tarea 1
def Sistema_Equivalente(r, F, M, x):
    Fr=np.array([0,0,0], dtype=float)
    Mr=np.array([0,0,0], dtype=float)
    dimension=len(x)
    if dimension==2:
        x=np.array([x[0],x[1],0],dtype=float)
    elif dimension==3:
        x=np.array(x,dtype=float)
    for i in range(len(F)):
        if dimension==3:
            r_iteracion= np.array(r[i], dtype=float)
            f_iteracion= np.array(F[i], dtype=float)
            m_iteracion= np.array(M[i], dtype=float)
        elif dimension==2:
            r_iteracion=np.array([r[i][0],r[i][1],0],dtype=float)
            f_iteracion=np.array([F[i][0],F[i][1],0],dtype=float)
            m_iteracion=np.array([0,0,M[i]], dtype=float)
        Fr+=f_iteracion
        Mr+=m_iteracion+np.cross(r_iteracion-x,f_iteracion)
    if dimension==3:
        return Fr, Mr
    else:
        return Fr[:2], Mr[2]

def TorsorEquivalente(r, F, M):
    Fr=np.array([0,0,0], dtype=float)
    Mr=np.array([0,0,0], dtype=float)
    dimension=len(F[0])
    for i in range(len(F)):
        if dimension==3:
            r_iteracion= np.array(r[i], dtype=float)
            f_iteracion= np.array(F[i], dtype=float)
            m_iteracion= np.array(M[i], dtype=float)
        elif dimension==2:
            r_iteracion=np.array([r[i][0],r[i][1],0],dtype=float)
            f_iteracion=np.array([F[i][0],F[i][1],0],dtype=float)
            m_iteracion=np.array([0,0,M[i]], dtype=float)
        Fr+=f_iteracion
        Mr+=m_iteracion+np.cross(r_iteracion,f_iteracion)
    magnitud_cuadrado=np.dot(Fr,Fr)
    punto=np.cross(Fr,Mr)/magnitud_cuadrado
    mom_torsor=(np.dot(Mr,Fr)/magnitud_cuadrado)*Fr
    if dimension==3:
        at=punto-(punto[2]/Fr[2])*Fr
        return Fr, mom_torsor, at
    elif dimension==2:
        at=punto-(punto[1]/Fr[1])*Fr
        return Fr[:2], mom_torsor[2], at[:2]

#1.a)
#Esta funcion recibe la informacion de los nodos, barras y cargas de la estructura
#y retorna las fuerzas equivalentes con sus posiciones
def NodalForces(NODE, ELEM, Fext, Qext):
    r=[]
    F=[]
    #Primero agregamos las fuerzas puntuales que actuan directamente en los nodos
    for i in range(len(NODE)):
        if np.any(Fext[i]!=0):
            r.append(NODE[i])
            F.append(Fext[i])
    #Luego convertimos las cargas distribuidas en fuerzas puntuales equivalentes
    #Para una carga uniforme, la fuerza equivalente es q*L, repartida en mitades en cada nodo
    for e in range(len(ELEM)):
        if np.any(Qext[e]!=0):
            n1=ELEM[e][0]
            n2=ELEM[e][1]
            L=np.linalg.norm(NODE[n2]-NODE[n1])
            F_eq=Qext[e]*L/2
            r.append(NODE[n1])
            F.append(F_eq)
            r.append(NODE[n2])
            F.append(F_eq)
    return r, F

#1.b)
#Esta funcion grafica la estructura reticulada con sus nodos y barras
def PlotReticulado(NODE, ELEM, mostrar_numeros=False):
    fig, ax=plt.subplots(figsize=(12,6))
    for e in range(len(ELEM)):
        n1=ELEM[e][0]
        n2=ELEM[e][1]
        ax.plot([NODE[n1][0],NODE[n2][0]], [NODE[n1][1],NODE[n2][1]], 'b-', linewidth=1.5)
        if mostrar_numeros:
            xm=(NODE[n1][0]+NODE[n2][0])/2
            ym=(NODE[n1][1]+NODE[n2][1])/2
            ax.text(xm, ym, str(e), color='red', fontsize=7, ha='center', va='bottom')
    for i in range(len(NODE)):
        ax.plot(NODE[i][0], NODE[i][1], 'ko', markersize=4)
        if mostrar_numeros:
            ax.text(NODE[i][0], NODE[i][1], str(i), color='green', fontsize=7, ha='right')
    ax.set_aspect('equal')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_title('Problema 1: Reticulado y eje del torsor')
    ax.grid(True, alpha=0.3)
    return fig, ax

#Definimos los parametros del problema
a=3
b=4
F_val=150
q=30

#Construimos los nodos de la estructura: 13 nodos inferiores y 11 superiores
NODE_P1=[]
for i in range(13):
    NODE_P1.append([i*a, 0])
for i in range(1,12):
    NODE_P1.append([i*a, b])
NODE_P1=np.array(NODE_P1, dtype=float)

#Construimos los elementos: cordon inferior, cordon superior, montantes y diagonales
ELEM_P1=[]
for i in range(12):
    ELEM_P1.append([i, i+1])
for i in range(10):
    ELEM_P1.append([13+i, 13+i+1])
for i in range(11):
    ELEM_P1.append([i+1, 13+i])
for i in range(11):
    ELEM_P1.append([i, 13+i])
    ELEM_P1.append([i+2, 13+i])
ELEM_P1=np.array(ELEM_P1)

#Definimos las cargas puntuales segun la figura 2(a)
Fext_P1=np.zeros((len(NODE_P1),2))
Fext_P1[0] +=[- 2*F_val, F_val]
Fext_P1[12]+=[0, F_val]
Fext_P1[13]+=[F_val, -5*F_val]
Fext_P1[14]+=[F_val, 0]
Fext_P1[18]+=[2*F_val, -(2/3)*F_val]
Fext_P1[21]+=[0, 2*F_val]
Fext_P1[23]+=[F_val, 0]

#Definimos la carga distribuida sobre el cordon inferior segun la figura 2(b)
Qext_P1=np.zeros((len(ELEM_P1),2))
for i in range(12):
    Qext_P1[i]=[0,-q]

#Calculamos las fuerzas nodales equivalentes y luego el torsor
r_P1, F_P1=NodalForces(NODE_P1, ELEM_P1, Fext_P1, Qext_P1)
M_P1=[0]*len(F_P1)
Fr_P1, Mt_P1, at_P1=TorsorEquivalente(r_P1, F_P1, M_P1)

print("Problema 1:")
print("Fuerza Resultante:", Fr_P1)
print("Momento Torsor:", Mt_P1)
print("Vector posicion at:", at_P1)

#Graficamos el reticulado junto al eje del torsor
fig1, ax1=PlotReticulado(NODE_P1, ELEM_P1)
#El eje del torsor es una recta que pasa por at_P1 y es paralela a Fr_P1
t=np.linspace(-10,10,100)
dir_torsor=Fr_P1/np.linalg.norm(Fr_P1)
eje_x=at_P1[0]+t*dir_torsor[0]
eje_y=at_P1[1]+t*dir_torsor[1]
ax1.plot(eje_x, eje_y, 'r-', linewidth=2.5, label=f'Eje del torsor  at=({at_P1[0]:.2f}, {at_P1[1]:.2f}) m')
ax1.plot(at_P1[0], at_P1[1], 'r*', markersize=12)
ax1.legend(loc='upper right')
plt.tight_layout()
plt.savefig('P1_reticulado_torsor.png', dpi=150)
plt.show()

#2.a)
#Esta funcion grafica un poligono dado su indice en la malla
def PolyPlot2D(e, NODE, POLY, ax=None, color='steelblue', alpha=0.6):
    if ax is None:
        fig, ax=plt.subplots()
    nodos_poly=POLY[e]
    coords=NODE[nodos_poly]
    coords_cerrado=np.vstack([coords, coords[0]])
    ax.fill(coords_cerrado[:,0], coords_cerrado[:,1], color=color, alpha=alpha)
    ax.plot(coords_cerrado[:,0], coords_cerrado[:,1], 'k-', linewidth=0.5)
    return ax

#2.b)
#Esta funcion calcula el area y centroide de un poligono usando el teorema de Green-Stokes
def PolyProps2D(e, NODE, POLY):
    nodos=POLY[e]
    coords=NODE[nodos]
    x=coords[:,0]
    y=coords[:,1]
    #Agregamos el vertice adicional VN+1 que es una replica del primero
    x_ext=np.append(x, x[0])
    y_ext=np.append(y, y[0])
    A=0.5*np.sum(x_ext[:-1]*y_ext[1:]-x_ext[1:]*y_ext[:-1])
    xc=(1/(6*A))*np.sum((x_ext[:-1]+x_ext[1:])*(x_ext[:-1]*y_ext[1:]-x_ext[1:]*y_ext[:-1]))
    yc=(1/(6*A))*np.sum((y_ext[:-1]+y_ext[1:])*(x_ext[:-1]*y_ext[1:]-x_ext[1:]*y_ext[:-1]))
    return abs(A), xc, yc

#2.c)
#Esta funcion grafica toda la estructura usando PolyCollection para mayor eficiencia
def Plot2DGeometry(NODE, POLY, ax=None):
    if ax is None:
        fig, ax=plt.subplots(figsize=(10,8))
    verts=[NODE[POLY[e]] for e in range(len(POLY))]
    col=PolyCollection(verts, facecolor='steelblue', edgecolor='k', linewidth=0.2, alpha=0.6)
    ax.add_collection(col)
    ax.autoscale()
    ax.set_aspect('equal')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_title('Problema 2: Geometria del componente')
    ax.grid(True, alpha=0.3)
    return ax

#2.d)
#Esta funcion calcula el area total y el centroide de la estructura completa
def Props2DGeometry(NODE, POLY):
    At=0
    sum_Ax=0
    sum_Ay=0
    for e in range(len(POLY)):
        A, xc, yc=PolyProps2D(e, NODE, POLY)
        At+=A
        sum_Ax+=A*xc
        sum_Ay+=A*yc
    X_bar=sum_Ax/At
    Y_bar=sum_Ay/At
    return At, X_bar, Y_bar

#2.e)
#Esta funcion grafica un mapa de calor sobre la estructura segun las fuerzas en cada poligono
def Plot2DForces(NODE, POLY, S, ax=None):
    if ax is None:
        fig, ax=plt.subplots(figsize=(10,8))
    norm=mcolors.Normalize(vmin=np.min(S), vmax=np.max(S))
    cmap=cm.jet
    verts=[NODE[POLY[e]] for e in range(len(POLY))]
    colores=[cmap(norm(S[e])) for e in range(len(POLY))]
    col=PolyCollection(verts, facecolors=colores, edgecolor='none')
    ax.add_collection(col)
    ax.autoscale()
    sm=cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ax=ax, label='Fuerza resultante [N]')
    ax.set_aspect('equal')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_title('Problema 2: Mapa de calor de fuerzas por poligono')
    ax.grid(True, alpha=0.3)
    return ax

#2.f)
#Esta funcion calcula la masa total y el centro de masa de la estructura
def MassCenter(NODE, POLY, rho):
    Mt=0
    sum_mx=0
    sum_my=0
    for e in range(len(POLY)):
        A, xc, yc=PolyProps2D(e, NODE, POLY)
        m=rho[e]*A
        Mt+=m
        sum_mx+=m*xc
        sum_my+=m*yc
    Xct=np.array([sum_mx/Mt, sum_my/Mt])
    return Mt, Xct

#Cargamos los archivos de datos (deben estar en la misma carpeta que main.py)
NODE_2=np.loadtxt('NODE.txt')
POLY_2=np.loadtxt('POLY.txt', dtype=int) #los indices ya son 0-based
rho_2=np.loadtxt('rho.txt')

#2.a) Calculamos el area total y el centroide de la estructura
At, X_bar, Y_bar=Props2DGeometry(NODE_2, POLY_2)
print("\nProblema 2:")
print("2.a)")
print("Area total:", At, "m^2")
print("Centroide:", X_bar, Y_bar)

#2.b) Calculamos la masa total y el centro de masa
Mt, Xct=MassCenter(NODE_2, POLY_2, rho_2)
print("\n2.b)")
print("Masa total:", Mt, "kg/m")
print("Centro de masa:", Xct)
#El centro de masa difiere del centroide porque las densidades no son uniformes
#Si todas las densidades fueran iguales, ambos puntos coincidirian

#2.c) Calculamos la fuerza resultante y su punto de aplicacion
#Evaluamos la carga w en el centroide de cada poligono y multiplicamos por su area
def w(x, y):
    return 2*np.sin(x)+np.cos(y)+3*np.exp(-0.5*(x**2+y**2))

r_fuerzas=[]
S_vec=np.zeros(len(POLY_2))
for e in range(len(POLY_2)):
    Ae, xce, yce=PolyProps2D(e, NODE_2, POLY_2)
    si=w(xce, yce)*Ae
    S_vec[e]=si
    r_fuerzas.append([xce, yce, 0])

#Como las fuerzas son perpendiculares al plano, usamos la funcion en 3D con la fuerza en z
F_fuerzas=[[0,0,si] for si in S_vec]
M_fuerzas=[[0,0,0]]*len(F_fuerzas)
Fr_c, Mr_c=Sistema_Equivalente(r_fuerzas, F_fuerzas, M_fuerzas, [0,0,0])
#El punto de aplicacion se obtiene a partir del momento resultante
x_ap=-Mr_c[1]/Fr_c[2]
y_ap=Mr_c[0]/Fr_c[2]
print("\n2.c)")
print("Fuerza resultante:", Fr_c[2], "N")
print("Punto de aplicacion:", x_ap, y_ap)

#2.d) Graficamos la pieza y el mapa de calor
idx_max=int(np.argmax(S_vec))
Ae_max, xce_max, yce_max=PolyProps2D(idx_max, NODE_2, POLY_2)
print("\n2.d)")
print("Elemento con mayor fuerza: POLY[", idx_max, "] con fuerza:", S_vec[idx_max], "N")

fig2a, ax2a=plt.subplots(figsize=(10,8))
Plot2DGeometry(NODE_2, POLY_2, ax=ax2a)
ax2a.plot(X_bar, Y_bar, 'r*', markersize=12, label=f'Centroide ({X_bar:.2f}, {Y_bar:.2f})')
ax2a.plot(Xct[0], Xct[1], 'g^', markersize=10, label=f'Centro de masa ({Xct[0]:.2f}, {Xct[1]:.2f})')
ax2a.legend(loc='lower left')
plt.tight_layout()
plt.savefig('P2_geometria.png', dpi=150)
plt.show()

fig2b, ax2b=plt.subplots(figsize=(10,8))
Plot2DForces(NODE_2, POLY_2, S_vec, ax=ax2b)
ax2b.plot(xce_max, yce_max, 'w*', markersize=12, label=f'Max: POLY[{idx_max}]')
ax2b.legend(loc='upper right')
plt.tight_layout()
plt.savefig('P2_mapa_calor.png', dpi=150)
plt.show()

#Problema 3

#Cargamos los archivos del edificio
NODE_3=np.loadtxt('NODE2.txt')
POLY_3=np.loadtxt('POLY2.txt').astype(int)
#Verificamos si los indices son 0-based o 1-based
if POLY_3.min()>0:
    POLY_3=POLY_3-1

#3.a) Esta funcion grafica la estructura 3D
def Plot3DGeometry(NODE, POLY, ax=None, color='lightblue', alpha=0.3):
    if ax is None:
        fig=plt.figure(figsize=(10,10))
        ax=fig.add_subplot(111, projection='3d')
    verts=[NODE[POLY[e]] for e in range(len(POLY))]
    col=Poly3DCollection(verts, alpha=alpha, facecolor=color, edgecolor='gray', linewidth=0.2)
    ax.add_collection3d(col)
    ax.set_xlim(NODE[:,0].min(), NODE[:,0].max())
    ax.set_ylim(NODE[:,1].min(), NODE[:,1].max())
    ax.set_zlim(NODE[:,2].min(), NODE[:,2].max())
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_zlabel('z [m]')
    return ax

#3.b) Esta funcion calcula el area, centroide y normal de un cuadrilatero
#Lo hacemos dividiendo el cuadrilatero en dos triangulos
def QuadrilateralProps(xeset):
    p1=xeset[0]
    p2=xeset[1]
    p3=xeset[2]
    p4=xeset[3]
    #Triangulo 1: p1, p2, p3
    normal1=np.cross(p2-p1, p3-p1)
    A1=0.5*np.linalg.norm(normal1)
    xc1=(p1+p2+p3)/3
    #Triangulo 2: p1, p3, p4
    normal2=np.cross(p3-p1, p4-p1)
    A2=0.5*np.linalg.norm(normal2)
    xc2=(p1+p3+p4)/3
    A=A1+A2
    if A<1e-14:
        return 0.0, np.zeros(3), np.array([0,0,1], dtype=float)
    Xc=(A1*xc1+A2*xc2)/A
    #La normal la calculamos con las diagonales del cuadrilatero
    normal=np.cross(p3-p1, p4-p2)
    mag=np.linalg.norm(normal)
    if mag<1e-14:
        return A, Xc, np.array([0,0,1], dtype=float)
    nhat=normal/mag
    return A, Xc, nhat

#3.c) Esta funcion grafica la estructura 3D con un mapa de calor de presiones
def Plot3DForces(NODE, POLY, S, ax=None):
    if ax is None:
        fig=plt.figure(figsize=(10,10))
        ax=fig.add_subplot(111, projection='3d')
    norm=mcolors.Normalize(vmin=np.min(S), vmax=np.max(S))
    cmap=cm.jet
    verts=[NODE[POLY[e]] for e in range(len(POLY))]
    colores=[cmap(norm(S[e])) for e in range(len(POLY))]
    col=Poly3DCollection(verts, alpha=0.8, linewidth=0)
    col.set_facecolor(colores)
    col.set_edgecolor('none')
    ax.add_collection3d(col)
    ax.set_xlim(NODE[:,0].min(), NODE[:,0].max())
    ax.set_ylim(NODE[:,1].min(), NODE[:,1].max())
    ax.set_zlim(NODE[:,2].min(), NODE[:,2].max())
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_zlabel('z [m]')
    sm=cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ax=ax, label='Presion [N/m^2]', shrink=0.5)
    return ax

#Esta funcion calcula la presion del viento a una altura z
#Usamos el perfil de viento de la norma con alpha=0.16 para costa
def WindPressure(alpha, h, v0, z):
    if z<=0:
        return 0.0
    v_z=v0*(z/h)**alpha
    P=0.613*v_z**2
    return P

#Esta funcion calcula la fuerza equivalente del viento sobre un ventanal
#Solo se considera la componente perpendicular al ventanal, y solo si el viento lo enfrenta
def WindEquivalentForces(xeset, dhat, alpha, h, v0):
    A, Xc, nhat=QuadrilateralProps(xeset)
    if A<1e-14:
        return 0.0, A, Xc, nhat
    z_centroide=Xc[2]
    P=WindPressure(alpha, h, v0, z_centroide)
    dhat=np.array(dhat, dtype=float)
    dhat=dhat/np.linalg.norm(dhat)
    dot=np.dot(dhat, nhat)
    #Si el producto punto es positivo, el viento viene desde atras y no afecta al ventanal
    if dot>=0:
        return 0.0, A, Xc, nhat
    #Solo la componente perpendicular del viento genera presion sobre el ventanal
    P_efectiva=P*abs(dot)
    s=P_efectiva*A
    return s, A, Xc, nhat

#Graficamos la geometria completa del edificio
fig3a=plt.figure(figsize=(10,10))
ax3a=fig3a.add_subplot(111, projection='3d')
Plot3DGeometry(NODE_3, POLY_3, ax=ax3a)
ax3a.set_title('Burj Khalifa - Geometria completa')
plt.tight_layout()
plt.savefig('P3_geometria_burj.png', dpi=150)
plt.show()

#Definimos el punto de interes y los parametros del viento
x0=np.array([0,0,0], dtype=float)
alpha_wind=0.16
h_ref=15.0

#Definimos los tres casos de viento
casos=[
    ["I",   12, np.array([-1, 0, 0], dtype=float)],
    ["II",  25, np.array([0.5, -0.5*np.sqrt(3), 0], dtype=float)],
    ["III",  8, np.array([0.5,  0.5*np.sqrt(3), 0], dtype=float)],
]

print("\nProblema 3:")
print(f"{'Caso':<6} {'Fr_x':>14} {'Fr_y':>14} {'Fr_z':>14} {'Mr_x':>14} {'Mr_y':>14} {'Mr_z':>14}")
print("-"*92)

for caso in casos:
    nombre=caso[0]
    v0=caso[1]
    dhat=caso[2]/np.linalg.norm(caso[2])

    r_list=[]
    F_list=[]
    S_caso=np.zeros(len(POLY_3))

    for e in range(len(POLY_3)):
        nodos=POLY_3[e]
        xeset=NODE_3[nodos]
        s, A, Xc, nhat=WindEquivalentForces(xeset, dhat, alpha_wind, h_ref, v0)
        S_caso[e]=s
        if s>0:
            #La fuerza actua en direccion -nhat (el viento empuja hacia adentro)
            F_elem=s*(-nhat)
            r_list.append(Xc)
            F_list.append(F_elem)

    M_list=[[0,0,0]]*len(F_list)
    Fr, Mr=Sistema_Equivalente(r_list, F_list, M_list, x0)
    print(f"  {nombre:<4} {Fr[0]:>14.4f} {Fr[1]:>14.4f} {Fr[2]:>14.4f} {Mr[0]:>14.4f} {Mr[1]:>14.4f} {Mr[2]:>14.4f}")

    fig3b=plt.figure(figsize=(10,10))
    ax3b=fig3b.add_subplot(111, projection='3d')
    Plot3DForces(NODE_3, POLY_3, S_caso, ax=ax3b)
    ax3b.set_title(f'Burj Khalifa - Presiones caso {nombre} (v0={v0} m/s)')
    plt.tight_layout()
    plt.savefig(f'P3_presiones_caso_{nombre}.png', dpi=150)
    plt.show()