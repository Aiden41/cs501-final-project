import requests
import json
from PIL import Image
import numpy as np

ip = 'http://54.210.245.37'

def main():
    while(1):
        response = requests.get(ip+'/files')
        print("Current files in S3:")
        for index, file in enumerate(response.json()):
            print(str(index+1) + " " + str(file))
        print("Enter the number of the file you want to view:")
        file_to_get = response.json()[int(input())-1]
        response = requests.get(ip+'/list', json=json.dumps([file_to_get]))
        for index, file in enumerate(response.json()):
            print(str(index+1) + " " + str(file))
        print("Enter the operation command: ")
        args = input().split()
        n = len(args)
        match args[1]:
            case 'flip':
                flip(file_to_get, args[0], args[2])
            case 'crop':
                crop(file_to_get, args[0], args[2], args[3], args[4], args[5])
            case 'scale':
                scale(file_to_get, args[0], args[2], args[3])
            case 'rotate':
                if n < 4:
                    args.append('True')
                rotate(file_to_get, args[0], args[2], args[3])
        print()

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