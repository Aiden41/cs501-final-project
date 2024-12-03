import h5py
import numpy as np
from matplotlib import pyplot as plt

hdf5_file = h5py.File("images.h5", 'r')
img = np.asarray(hdf5_file['images']['1'])
x_factor = 2
y_factor = 2
up = True
down = False
if down:
    scaled_img = img[::x_factor, ::y_factor]
if up:
    scaled_img = np.kron(img, np.ones((y_factor,x_factor,1))).astype('uint8')
plt.imshow(scaled_img)
plt.show()