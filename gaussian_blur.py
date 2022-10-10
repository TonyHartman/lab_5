import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy


# функция умеет обрабатывать фотографии RGB или фото с одним цветом, параметр по умолчанию фотография RGB.
def blur(img_array, weights_array, color='RGB'):
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

def gaussian_weights (img_array, sigma):
    rows, columns = img_array.shape[0], img_array.shape[1]
    weights = np.zeros((2 * rows - 1, 2 * columns - 1))
    for j in range(0, 2 * rows - 1):
        for i in range(0, 2 * columns - 1):
            weights[j, i] = np.exp(-0.5 * (((i - (columns - 1)) ** 2 + (j - (rows - 1)) ** 2)/sigma**2))
    return weights

def gaussian_blur (img_array, sigma, color='RGB'):
    weights_array = gaussian_weights(img_array, sigma)
    return blur(img_array, weights_array, color)



#Ввод:
#На больших фотографиях программа работает долго, поэтому предлагаю использовать фотографию меньшего размера small.jpg
img = Image.open('small.jpg')
img_arr = np.array(img)
plt.imshow(gaussian_blur(img_arr, 6))
plt.show()




