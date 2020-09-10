import os.path
from os import path

file_path = "C:\\Users\\justino\\OneDrive\\repos\\py_learning\\"
# file_name = input("\nEnter a file name: \n")  #"mbox-short.txt"
file_name = "mbox-short.txt"
myfile = file_path + file_name
lineWords = []
newWords = []

try:
    fh = open(myfile)
    for line in fh:
        # split line into list of words
        line =  line.rstrip()
        if line.startswith('From '):
            lineWords = line.split()
            newWords.append(lineWords[1])

    # turn our newWords list into a dictionary to remove duplicates        
    newWords = list(dict.fromkeys(newWords)) 
    
    for email in newWords:
        print("\n", email)

    print("\n\nNumber of distinct email addresses: ", len(newWords), "\n")

 

except FileNotFoundError:
    print('\nFile is not found\n')

except:
    print('\nSomething went wrong and we had to bail\n')
