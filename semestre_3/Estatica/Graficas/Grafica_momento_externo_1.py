import numpy as np
import matplotlib.pyplot as plt

# Definir los tramos de la viga (x)
x_tramo1 = np.linspace(58, 72, 500)
x_tramo2 = np.linspace(72, 74, 100)

# Ecuaciones de Corte V(x)
V_tramo1 = np.full_like(x_tramo1, -1.25)
V_tramo2 = np.full_like(x_tramo2, -1.25)

# Ecuaciones de Momento M(x)
# Tramo 1: arranca en 0 en x=58
M_tramo1 = -1.25 * (x_tramo1 - 58) 

# Tramo 2: arranca en el valor anterior (-17.5) menos el salto del torque (0.3) = -17.8
M_tramo2 = -1.25 * (x_tramo2 - 72) - 17.8 

# --- Configuración del Gráfico ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Gráfico de Corte V(x)
ax1.plot(x_tramo1, V_tramo1, 'b-', lw=2)
ax1.plot(x_tramo2, V_tramo2, 'b-', lw=2)
ax1.fill_between(np.concatenate([x_tramo1, x_tramo2]), np.concatenate([V_tramo1, V_tramo2]), 0, color='blue', alpha=0.1)
ax1.axhline(0, color='black', lw=1)
ax1.set_ylabel('Corte V (ton)')
ax1.set_title('Diagrama de Corte: Constante e inalterado por el torque')
ax1.grid(True, linestyle='--', alpha=0.6)

# Gráfico de Momento M(x)
ax2.plot(x_tramo1, M_tramo1, 'r-', lw=2)
ax2.plot(x_tramo2, M_tramo2, 'r-', lw=2)
# Dibujar el salto vertical en x=72
ax2.plot([72, 72], [-17.5, -17.8], 'r--', lw=2, label='Salto por torque aplicado (0.3 ton·m)')
# Dibujar el cierre en el empotramiento en x=74
ax2.plot([74, 74], [-20.3, 0], 'g--', lw=2, label='Reacción del muro (+20.3 ton·m)')

ax2.fill_between(np.concatenate([x_tramo1, x_tramo2]), np.concatenate([M_tramo1, M_tramo2]), 0, color='red', alpha=0.1)
ax2.axhline(0, color='black', lw=1)
ax2.set_xlabel('Posición x (m)')
ax2.set_ylabel('Momento M (ton·m)')
ax2.set_title('Diagrama de Momento: Caída abrupta manteniendo la pendiente')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()