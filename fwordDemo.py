#Matthew Siegel
#4/23/18
#fwordDemo.py - Finding words that start with F

words = input('Type in some words: ').split(' ')

for item in words:
    if 'f' in item or 'F' in item:
        print(item)
