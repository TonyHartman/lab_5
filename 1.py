import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img = Image.open('water.jpg')
img_arr = np.array(img)
img_arr = img_arr.mean(axis=2)
plt.imshow(np.transpose(img_arr, (1, 0)), cmap='gray')
plt.show()
