import matplotlib.pyplot as plt
import numpy as np

# Create a 10x10 array of random data
data = np.random.rand(10, 10)
print(data)

plt.imshow(data, cmap='viridis')
plt.colorbar()  # Adds a legend for the color scale
plt.show()
