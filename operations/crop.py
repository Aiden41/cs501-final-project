import h5py
import numpy as np
from matplotlib import pyplot as plt

hdf5_file = h5py.File("images.h5", 'r')
img = (hdf5_file['images']['1'])
x1 = 0
x2 = 1200
y1 = 0
y2 = 900
cropped_img = img[y1:y2, x1:x2]
plt.imshow(cropped_img)
plt.show()