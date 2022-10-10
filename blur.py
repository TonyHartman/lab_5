import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy

def blur(img_array, weights_array, color='RGB'):
    #функция умеет обрабатывать фотографии RGB или фото с одним цветом, параметр по умолчанию фотография RGB.
    weights_array_norm = weights_array.astype('float')
    img_array_blur = img_array.astype('float')
    weights_array_norm /= weights_array_norm.sum()
    if color != 'RGB':
        img_array_blur = scipy.ndimage.convolve(img_array_blur, weights_array_norm)
    else:
        for k in range(0, 3):
            img_array_blur_col = [[i[k] for i in j] for j in img_array_blur]
            img_array_blur_col = scipy.ndimage.convolve(img_array_blur_col, weights_array_norm)
            for j in range(0, img_array_blur_col.shape[0]):
                for i in range(0, img_array_blur_col.shape[1]):
                    img_array_blur[j, i, k] = img_array_blur_col[j, i]
    img_array_blur[img_array_blur > 255] = 255
    img_array_blur = img_array_blur.astype('uint8')
    return img_array_blur


#Вызов:
img = Image.open('water.jpg')
img_arr = np.array(img)
#усреднение для получения серого цвета
#img_arr = img_arr.mean(axis=2)

weights_arr = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ], dtype=float)
plt.imshow(blur(img_arr, weights_arr))
plt.show()