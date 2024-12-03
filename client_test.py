import sys
import requests
import json
import os
import numpy as np
from PIL import Image

ip = 'http://54.210.245.37'

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
    names = [name]
    session = requests.Session()
    if name == 'all':
        names = session.get(ip+"/list", json=json.dumps([file])).json()
    for name in names:
        response = session.get(ip+'/flip', json=json.dumps([file, name, dir]))
        im = Image.fromarray(np.array(response.json()).astype(np.uint8))
        im.save('./output/flipped_'+name+".png")

def crop(file, name, x1, x2, y1, y2):
    names = [name]
    session = requests.Session()
    if name == 'all':
        names = session.get(ip+"/list", json=json.dumps([file])).json()
    for name in names:
        response = requests.get(ip+'/crop', json=json.dumps([file, name, x1, x2, y1, y2]))
        im = Image.fromarray(np.array(response.json()).astype(np.uint8))
        im.save('./output/cropped_'+name+".png")

def scale(file, name, x_factor, y_factor):
    names = [name]
    session = requests.Session()
    if name == 'all':
        names = session.get(ip+"/list", json=json.dumps([file])).json()
    for name in names:
        response = requests.get(ip+'/scale', json=json.dumps([file, name, x_factor, y_factor]))
        im = Image.fromarray(np.array(response.json()).astype(np.uint8))
        im.save('./output/scaled_'+name+".png")

def rotate(file, name, angle, reshape):
    names = [name]
    session = requests.Session()
    if name == 'all':
        names = session.get(ip+"/list", json=json.dumps([file])).json()
    for name in names:
        response = requests.get(ip+'/rotate', json=json.dumps([file, name, angle, reshape]))
        im = Image.fromarray(np.array(response.json()).astype(np.uint8))
        im.save('./output/rotated_'+name+".png")

if __name__ == "__main__":
    main()