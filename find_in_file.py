import os.path
from os import path

file_path = "C:\\Users\\justino\\OneDrive\\repos\\py_learning\\"
file_name = "mbox-short.txt"
myfile = file_path + file_name
searchWord = 'louis'
successCounter = 0

# We will accumulate the lines of interest in a list for later usage
lineBuilder = []

if path.exists(myfile):
    fh = open(file_path + file_name)
    for line in fh:
        if line.startswith('From ') and searchWord not in line:
             pass
        elif line.startswith('From ') and searchWord in line:
            line = line.rstrip()
            print(line)
            lineBuilder.append(line) # var is not used currently but may need in future
            successCounter +=1
    if successCounter == 0:
        print('\n Search Term Was NOT found in file!\n')
    
    # print("\nResults of query: \n", lineBuilder)
    
else:
    print("\nERROR ENCOUNTERED: File not found!\n")