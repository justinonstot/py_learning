import os.path
from os import path

file_path = "C:\\Users\\justino\\OneDrive\\repos\\py_learning\\"
file_name = "romeo.txt"
myfile = file_path + file_name
lineWords = []
newWords = []

try:
    fh = open(myfile)
    for line in fh:
        # split line into list of words
        lineWords = line.rstrip().split()
        for word in lineWords:
            if word.lower() not in newWords:
                newWords.append(word.lower())
    newWords.sort() #creates a new version of the variable that is now sorted
    print(newWords)
    

except FileNotFoundError:
    print('\nFile is not found\n')

except:
    print('\nSomething went wrong and we had to bail\n')

