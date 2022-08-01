from itertools import count
from prettytable import PrettyTable

# Open the filecontaining the list of words
f = open('words_2022-07-31.txt', 'r')
blob = f.readlines()
words = []
for w in blob:
    words.append(w.strip())
words = [val for val in words if val]
f.close()

# Print the length of the list
wordCount = len(words)
print("There are " + str(wordCount) + " words in the file:")

# Print the list
print(words)

# Collect the unique set of seven letters used
listLetter = []
for s in words:
    for l in s:
        listLetter.append(l)
listLetter = list(sorted(dict.fromkeys(listLetter)))
print("The seven letters in the puzzle are: " + str(listLetter))

# Collect the word lengths 
wordLength = []
for w in words:
     wordLength.append(len(w))
wordLength = list(sorted(dict.fromkeys(wordLength)))
print("The word lengths are " + str(wordLength))

# Find the length of the longest word
longest = max(words, key=len)
print("The longest word is: " + str(longest) + " with a length of " + str(len(longest)))

# find the words that have the same length
for i in wordLength:
    lenList = [item for item in words if len(item)==i]
    print("There are " + str(len(lenList)) +" "+ str(i) + "-letter words:")
#    print(lenList)

# Find the words that have the same first letter
for l in listLetter:
    letlist = [item for item in words if item.startswith(l)]
    print("There are " + str(len(letlist)) + " words that start with the letter " + str(l))
#    print(letlist)

# def num_words(string, target_len, target_let):
#     tally = 0
#     for word in words:


# # Count the number of N-letter words that start with the first letter "l"
# for l in listLetter:
#     count = 4
#     while (count < len(longest) + 1):
#         sublist = [item for item in words if (len(item)==count and item.startswith(l))]
#         print(str(l) + str(count) + " " + str(len(sublist)))
#         count = count + 1
#     print("--")
       