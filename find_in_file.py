import os.path
from os import path

file_path = "C:\\Users\\justino\\OneDrive\\repos\\py_learning\\"
file_name = "mbox-short.txt"
myfile = file_path + file_name
searchWord = 'louis'
successCounter = 0

if path.exists(myfile):
    # print("File exists: " + myfile)
    fh = open(file_path + file_name)
    for line in fh:
        if line.startswith('From ') and searchWord not in line:
             pass
        elif line.startswith('From ') and searchWord in line:
             print(line)
             successCounter +=1
    if successCounter == 0:
        print('\n Search Term Was NOT found in file!\n')

else:
    print("\nERROR ENCOUNTERED: File not found!\n")