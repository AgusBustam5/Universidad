import numpy as np
import matplotlib.pyplot as plt

xy = np.array([[0,10],[2,3],[9,3],[3,-1],[6,-8],[0,-4],[-6,-8],[3,-1],[-9,3],[-2,3],[0,10]])
xy = np.vstack([xy,[0,0]])
vectorx = xy[:, 0]
vectory = xy[:, 1]

plt.figure()
plt.plot(vectorx,vectory)
plt.show()