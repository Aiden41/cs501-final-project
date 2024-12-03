import h5py
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt

hdf5_file = h5py.File("images.h5", 'r')
img = np.asarray(hdf5_file['images']['1'])
# times_to_flip = 1
# left = (0,1)
# right = (1,0)
angle = 45
reshape = False
rotated_img = ndimage.rotate(img, angle=angle, reshape=reshape)
#rotated_img = np.rot90(img, k=times_to_flip, axes=left)
plt.imshow(rotated_img)
plt.show()
