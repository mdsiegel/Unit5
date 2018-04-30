#Matthew Siegel
#4/30/18
#toDoList.py - Making a to do list

print('Functions are add, delete, and print')

Quit = False
L = []
while Quit == False:
    text = input('>')
    if text[0] == 'add':
        L.append(text[1:len(text)])
    if text[0] == 'delete':
        L.remove(text[1:len(text)])
    if text[0] == 'print':
        print(L)
    if text[0] == 'quit':
        Quit = True