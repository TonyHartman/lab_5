import numpy as np
import matplotlib.pyplot as plt

def julia(x_low, x_high, y_low, y_high, points_x, points_y, steps, Imc, Rec):
    re = np.linspace(x_low, x_high, points_x)
    im = np.linspace(y_low, y_high, points_y).reshape((-1, 1))
    z = np.zeros((points_x, points_y))
    z = z + re + im * 1j
    index = np.zeros((points_x, points_y))
    for step in range(steps):
        z = z ** 2 + Rec + Imc * 1j
        if step < 100:
            index[np.abs(z) > (1 + np.sqrt(1 + 4 * np.sqrt(Imc**2 + Rec**2)))/2] = step
        else:
            index[np.abs(z) > (1 + np.sqrt(1 + 4 * np.sqrt(Imc ** 2 + Rec ** 2))) / 2] = 100
    img = np.zeros((points_x, points_y))
    index = index.astype('uint8')
    gradient = np.linspace(0, 256, 100)
    gradient = gradient.astype('uint8')
    for i in range(0, points_x):
        for j in range(0, points_y):
            if np.abs(z[i, j]) <= (1 + np.sqrt(1 + 4 * np.sqrt(Imc**2 + Rec**2)))/2:
                img[i, j] = 255
            else:
                img[i, j] = gradient[index[i, j]]
    plt.imshow(img, cmap='gist_rainbow')
    plt.show()

julia(-1, 1, -1, 1, 50pwd
00, 5000, 500, -1, 0)