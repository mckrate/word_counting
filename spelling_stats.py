from itertools import count
from prettytable import PrettyTable

# Open the file containing the list of words
f = open('words_2022-07-24.txt', 'r')
blob = f.readlines()
words = []
for w in blob:
    words.append(w.strip())
words = [val for val in words if val]
f.close()

# Print the length of the list
print("There are " + str (len(words)) + " words in the file")

# Print the list
print(words)

# Collect the unique set of seven letters used
listLetter = []
letterdict = {}

for s in words:
    for l in s:
        listLetter.append(l)
listLetter = list(dict.fromkeys(listLetter))

# Sort the list of unique letters and print it
listLetter.sort()
print("The seven letters in the puzzle are: " + str(listLetter))

# Find the length of the longest word
longest = max(words, key=len)
print("The longest word is: " + str(longest) + " with a length of " + str(len(longest)))

# Find the number of N-letter words 
count = 4
while (count < len(longest)+1):
    lenlist = [item for item in words if len(item)==count]
    print("There are " + str(len(lenlist)) +" "+ str(count) + "-letter words:")
#    print(lenlist)
    count = count + 1

# Find the words that have the same first letter
for l in listLetter:
    letlist = [item for item in words if item.startswith(l)]
    print("There are " + str(len(letlist)) + " words that start with the letter " + str(l))
#    print(letlist)

# Count the number of N-letter words that start with the first letter "l"
for l in listLetter:
    count = 4
    while (count < len(longest) + 1):
        sublist = [item for item in words if (len(item)==count and item.startswith(l))]
        print(str(l) + str(count) + " " + str(len(sublist)))
        count = count + 1
    print("--")
       