#Matthew Siegel
#4/30/18
#toDoList.py - Making a to do list

print('Functions are add, delete, and print')

Quit = False
L = []
while Quit == False:
    text = input('>')
    if text[0:3] == 'add':
        L.append(text[3:len(text)])
    if text[0:6] == 'delete':
        L.remove(text[6:len(text)])
    if text[0:5] == 'print':
        for l in L:
            print(l)
    if text[0:4] == 'quit':
        Quit = True