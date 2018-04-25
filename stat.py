#Matthew Siegel
#4/25/18
#stat.py- findind stats of a list

L = []
noQ = True
print('Enter a list of numbers and enter q when finished')
while noQ == True:
    userInput = input('>')
    if userInput == 'q':
        noQ = False
    else:
        L.append(int(userInput))

print('Min: ',min(L))
    
    
