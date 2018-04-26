#Matthew Siegel
#4/26/18
#vowelWords.py

words = input('Enter some words: ').split()
for word in words:
    if word[0] in 'aeiouyAEIOUY':
        print(word)