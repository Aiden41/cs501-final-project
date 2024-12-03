from flask import Flask, request, jsonify, make_response
import os
import h5py
from scipy import ndimage
import numpy as np
import json

app = Flask(__name__)

@app.route("/files", methods=["GET"])
def get_files():
    files = os.listdir("bucket/")
    return jsonify(files)

@app.route("/file", methods=["GET"])
def get_file():
    filename = str(request.data.decode('utf-8'))
    with open("bucket/" + filename, 'rb') as file:
        file_data = file.read()
        response = make_response()
        response.data = file_data
        return response

@app.route("/list", methods=["GET"])
def list_names():
    data = json.loads(request.json)
    file = "bucket/" + data[0]
    hdf5_file = h5py.File(file, 'r')
    names = list(hdf5_file['images'].keys())
    return jsonify(names)

@app.route("/flip", methods=["GET"])
def flip():
    data = json.loads(request.json)
    file = "bucket/" + data[0]
    name = data[1]
    dir = data[2]
    hdf5_file = h5py.File(file, 'r')
    img = np.asarray(hdf5_file['images'][name])
    if dir == 'horizontal':
        flipped_img = np.flipud(img)
    if dir == 'vertical':
        flipped_img = np.fliplr(img)
    response = make_response()
    response.data = json.dumps(flipped_img.tolist())
    return response

@app.route("/crop", methods=["GET"])
def crop():
    data = json.loads(request.json)
    file = "bucket/" + data[0]
    name = data[1]
    x1 = data[2]
    x2 = data[3]
    y1 = data[4]
    y2 = data[5]
    hdf5_file = h5py.File(file, 'r')
    img = (hdf5_file['images'][name])
    cropped_img = img[int(y1):int(y2), int(x1):int(x2)]
    response = make_response()
    response.data = json.dumps(cropped_img.tolist())
    return response

@app.route("/scale", methods=["GET"])
def scale():
    data = json.loads(request.json)
    file = "bucket/" + data[0]
    name = data[1]
    x_factor = data[2]
    y_factor = data[3]
    hdf5_file = h5py.File(file, 'r')
    img = np.asarray(hdf5_file['images'][name])
    scaled_img = ndimage.zoom(img, (float(y_factor), float(x_factor), 1))
    response = make_response()
    response.data = json.dumps(scaled_img.tolist())
    return response

@app.route("/rotate", methods=["GET"])
def rotate():
    data = json.loads(request.json)
    file = "bucket/" + data[0]
    name = data[1]
    angle = data[2]
    reshape = data[3]
    hdf5_file = h5py.File(file, 'r')
    img = np.asarray(hdf5_file['images'][name])
    rotated_img = ndimage.rotate(img, angle=float(angle), reshape=eval(reshape))
    response = make_response()
    response.data = json.dumps(rotated_img.tolist())
    return response

if __name__ == "__main__":
    app.run()