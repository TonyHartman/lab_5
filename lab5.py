import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img = Image.open('water.jpg')
img_arr = np.array(img)
img_arr.shape
plt.imshow(np.transpose(img_arr, (1, 0, 2)))
plt.show()