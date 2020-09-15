import os.path
from os import path

file_path = "C:\\Users\\justino\\OneDrive\\repos\\py_learning\\"
file_name = "words.txt"
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

    print(searchWord in wordList)


        

except FileNotFoundError:
    print('\nFile is not found\n')

except:
    print('\nSomething went wrong and we had to bail\n')