import h5py
import numpy as np
from matplotlib import pyplot as plt

hdf5_file = h5py.File("images.h5", 'r')
img = np.asarray(hdf5_file['images']['1'])
left = True
if not left:
    flipped_img = np.flipud(img)
else:
    flipped_img = np.fliplr(img)
plt.imshow(flipped_img)
plt.show()