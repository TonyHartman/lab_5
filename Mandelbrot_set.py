import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(x_low, x_high, y_low, y_high, points_x, points_y, steps):
    re = np.linspace(x_low, x_high, points_x)
    im = np.linspace(y_low, y_high, points_y).reshape((-1, 1))
    c = re + im * 1j
    z = np.zeros((points_x, points_y))
    index = np.zeros((points_x, points_y))
    for step in range(steps):
        z = z ** 2 + c
        index[np.abs(z) > 2] = step
    img = np.zeros((points_x, points_y))
    index = index.astype('uint8')
    gradient = np.linspace(0, 256, steps)
    gradient = gradient.astype('uint8')
    for i in range(0, points_x):
        for j in range(0, points_y):
            if np.abs(z[i, j]) < 100:
                img[i, j] = 255
        else:
            img[i, j] = gradient[index[i, j]]
    plt.imshow(img, cmap='turbo')
    plt.show()

mandelbrot(0.3, 0.37, 0.38, 0.55, 2000, 2000, 100)