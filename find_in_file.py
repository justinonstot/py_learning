import os.path
from os import path

file_path = "C:\\Users\\justino\\OneDrive\\repos\\py_4_everyone\\"
file_name = "mbox-short.txt"
myfile = file_path + file_name

if path.exists(myfile):
    # print("File exists: " + myfile)
    fh = open(file_path + file_name)
    for line in fh:
        if line.startswith('From '):
            print(line)