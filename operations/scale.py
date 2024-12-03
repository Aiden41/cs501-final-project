import h5py
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt

hdf5_file = h5py.File("images.h5", 'r')
img = np.asarray(hdf5_file['images']['1'])
x_factor = 1
y_factor = 1
scaled_img = ndimage.zoom(img, (y_factor, x_factor, 1))
plt.imshow(scaled_img)
plt.show()