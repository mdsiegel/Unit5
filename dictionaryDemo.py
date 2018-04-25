#Matthew Siegel
#4/25/18
#dictionaryDemo.py-more list practice

words = ['computer','mortify','dog','firetruck','yes','python','cat']
words.sort()

num = int(input('What number word do you want? '))
if num<=0 or num>=8:
    print('error')
else:
    print(words[num-1])
