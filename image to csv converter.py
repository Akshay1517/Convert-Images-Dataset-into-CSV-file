from PIL import Image
import numpy as np
import sys
import os
import csv


def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList


filelist = createFileList('F:/AKSH/DATA SET/asl-alphabet/asl_alphabet_train/asl_alphabet_train/newfolder')

for file in filelist:
    print(file)
    img_file = Image.open(file)
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode
    img_grey = img_file.convert('L')
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    print(value)
    with open("Book1.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(value)