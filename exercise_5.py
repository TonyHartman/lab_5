import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 1000)
y = x[::-1].reshape(-1, 1)
img = x**2 + (y + 1 - np.sqrt(np.abs(x)))**2 - 1
plt.imshow(img, cmap='Reds_r')
plt.show()