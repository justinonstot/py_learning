word = 'brontosaurus'

d = dict()

# count the number of occurences of each letter in a string stored in "word"

#for letter in word:
#    if letter not in d: # add a letter to the dict if not already there
#        d[letter] = 1
#    else:
#        d[letter] += 1
    

for letter in word:
    d[letter] = d.get(letter,0) + 1 #get the value for the key "letter" and store the value plus 1 or 0 plus 1

print(d)