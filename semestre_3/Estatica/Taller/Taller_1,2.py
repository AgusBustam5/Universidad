import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
xy = np.array([[0,0],[1,0],[1,4],[4,4],[4,0],[5,0],[5,5]])
xy = np.vstack([xy, [0,0]])
print(x1)
print(x2)
vectorx = xy[:,0]
vectory = xy[0,:]
x = np.array([1,2,3,4,5,6])
print(x[0:3])

plt.figure()
plt.plot(vectorx,vectory)
plt.show()