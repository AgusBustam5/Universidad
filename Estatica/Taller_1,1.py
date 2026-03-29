import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi*2, 100)
y1 = np.sin(x)
y2 = 0.2*np.cos(10*x + 0.3)
y3 = y1 + y2

plt.figure()

fig, ax = plt.subplots(2,2)#mas de un grafico en una pestaña
ax[0,0].plot(x,y1,color="red",linewidth = 2, label = "g1")
ax[0,1].plot(x,y2,color="blue",linewidth = 2, label = "g2")
ax[1,0].plot(x,y3,color="green",linewidth = 2, label = "g3")

ax[1,1].plot(x,y1,color="red",linewidth = 2, label = "g1")
ax[1,1].plot(x,y2,color="blue",linewidth = 2, label = "g2")
ax[1,1].plot(x,y3,color="green",linewidth = 2, label = "g3")

ax[0,1].set_xlim([0,np.pi/2])

plt.show()
