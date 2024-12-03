import h5py
import numpy as np
import glob
from PIL import Image

hdf5_file = h5py.File("images.h5", 'w')
images = glob.glob('./img/*.png')
for index, file in enumerate(images):
    image = Image.open(file)
    image_data = np.asarray(image, dtype='uint8')
    dataset = hdf5_file.create_dataset('images/'+file.split('\\')[1].replace('.png', ''), data=image_data, dtype='uint8')
    dataset.attrs['NAME'] = images
    dataset.attrs['CLASS'] = np.string_("IMAGE")
hdf5_file.close()
