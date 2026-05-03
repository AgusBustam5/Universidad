import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi*2, 100)
y1 = np.sin(x)
y2 = 0.2*np.cos(10*x + 0.3)
y3 = y1 + y2

x_index = 0
y_index = 0

for i in range(len(x)):
    if y3[i] > y_index:
        y_index = y3[i]
        x_index = x[i]

plt.figure()

plt.plot(x, y1, color = "purple", linewidth = 2,linestyle = "-", label = "g1")
plt.plot(x, y2, color = "green", linewidth = 2, linestyle = "--", label = "g2")
plt.plot(x, y3, color = "red", linewidth = 2, linestyle = "--", label = "g3")

plt.scatter(x_index, y_index, s = 100, color = "blue", edgecolor = "black", label = "puntos")

plt.text(x_index, y_index,f"Max: (round(y_index, 2))")
plt.title("Grafico 1")
plt.xlabel("Valor de X")
plt.ylabel("Valor de Y")
plt.legend()
plt.show()