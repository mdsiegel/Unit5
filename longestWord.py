#Matthew Siegel
#4/23/18
#longestWord.py - finding longest word

words = input('enter words: ').split(' ')

l = 0
longestWord = ''
for i in words:
    length = len(i)
    if length > l:
        l = len(i)
        longestWord = i
print(longestWord)
