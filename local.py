import sys
import h5py
from scipy import ndimage
import numpy as np
from PIL import Image

#args: file_name image_name operation op_agrs
def main():
    args = sys.argv
    n = len(args)
    match args[3]:
        case 'flip':
            flip(args[1], args[2], args[4])
        case 'crop':
            crop(args[1], args[2], args[4], args[5], args[6], args[7])
        case 'scale':
            scale(args[1], args[2], args[4], args[5])
        case 'rotate':
            if n < 6:
                args.append('True')
            rotate(args[1], args[2], args[4], args[5])

def flip(file, name, dir):
    hdf5_file = h5py.File(file, 'r')
    names = [name]
    if name == 'all':
        names = list(hdf5_file['images'].keys())
    for filename in names:
        img = np.asarray(hdf5_file['images'][filename])
        if dir == 'horizontal':
            flipped_img = np.flipud(img)
        if dir == 'vertical':
            flipped_img = np.fliplr(img)
        im = Image.fromarray(flipped_img)
        im.save('./output/flipped_'+filename+".png")

def crop(file, name, x1, x2, y1, y2):
    hdf5_file = h5py.File(file, 'r')
    names = [name]
    if name == 'all':
        names = list(hdf5_file['images'].keys())
    for filename in names:
        img = (hdf5_file['images'][filename])
        cropped_img = img[int(y1):int(y2), int(x1):int(x2)]
        im = Image.fromarray(cropped_img)
        im.save('./output/cropped_'+filename+".png")

def scale(file, name, x_factor, y_factor):
    hdf5_file = h5py.File(file, 'r')
    names = [name]
    if name == 'all':
        names = list(hdf5_file['images'].keys())
    for filename in names:
        img = np.asarray(hdf5_file['images'][filename])
        scaled_img = ndimage.zoom(img, (float(y_factor), float(x_factor), 1))
        im = Image.fromarray(scaled_img)
        im.save('./output/scaled_'+filename+".png")

def rotate(file, name, angle, reshape):
    hdf5_file = h5py.File(file, 'r')
    names = [name]
    if name == 'all':
        names = list(hdf5_file['images'].keys())
    for filename in names:
        img = np.asarray(hdf5_file['images'][filename])
        rotated_img = ndimage.rotate(img, angle=float(angle), reshape=eval(reshape))
        im = Image.fromarray(rotated_img)
        im.save('./output/rotated_'+filename+".png")

if __name__ == "__main__":
    main()