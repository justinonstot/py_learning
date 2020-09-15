import os.path
from os import path

file_path = "C:\\Users\\justino\\OneDrive\\repos\\py_learning\\"
file_name = "romeo.txt"
myfile = file_path + file_name
lineWords = []
wordCounts = dict()

try:
    fh = open(myfile)
    for line in fh:
        lineWords = line.rstrip().split()
        for word in lineWords:
             wordCounts[word] = wordCounts.get(word,0) + 1 
    print(wordCounts)
        

except FileNotFoundError:
    print('\nFile is not found\n')

except:
    print('\nSomething went wrong and we had to bail\n')