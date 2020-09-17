import os.path
from os import path

file_path = "C:\\Users\\justino\\OneDrive\\repos\\py_learning\\"
file_name = "romeo.txt"
myfile = file_path + file_name
lineWords = []
wordList = dict()
counter = 0

try:
    fh = open(myfile)
    for line in fh:
        lineWords = line.rstrip().split()
        for word in lineWords:
            if word not in wordList:
                wordList[word] = counter
                counter += 1
    
    searchWord = input("Select word to check for: ")
    print("The word you search for is: " + searchWord)

    if searchWord in wordList:
        print('"' + searchWord + '" was found in the text.')
    else:
        print('"' + searchWord + '" was  NOT FOUND in the text.')


        

except FileNotFoundError:
    print('\nFile is not found: ', myfile)

except:
    print('\nSomething went wrong and we had to bail\n')