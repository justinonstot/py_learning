import os.path, string
from os import path

file_path = "C:\\Users\\justino\\OneDrive\\repos\\py_learning\\"
file_name = "romeo-full.txt"
myfile = file_path + file_name
wordList = dict()


#store each word in a dictionary and count the number of occurrences of each unique word

try:
    fh = open(myfile)       #open the file
    for line in fh:         #iterate through each line of file
        line=line.rstrip()      #strip off whitespace on the right
        line=line.translate(line.maketrans('','', string.punctuation)) #remove punctuation marks
        line=line.lower()       #lower case all words
        words = line.split()
        for word in words:
            if word not in wordList:
                wordList[word] = wordList[word] = 1
            else:
                wordList[word] += 1
    for w in sorted(wordList, key=wordList.get, reverse=False):
        print(w, wordList[w])

        
        
except FileNotFoundError:
    print('\nFile is not found: ', myfile)

#except:
 #   print('\nSomething went wrong and we had to bail\n')