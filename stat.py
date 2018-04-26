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
        L.append(float(userInput))

L.sort()
print('Min: ',min(L))
print('Max: ',max(L))
print('Mean: ',sum(L)/len(L))
mostNum = 0
mostNumberValue = 0
for l in L:
    if L.count(l) > mostNum:
        mostNum = L.count(l)
        mostNumberValue = l
print('Mode:',mostNumberValue)
if len(L)%2 == 0:
    median1 = L[len(L)/2]
    median2 = L[(len(L)/2)-1]
    print('median:',median2)
    print('median:',median1)
else:
    median1 = L[(len(L)/2)-.5]
    print('median:',median1)


