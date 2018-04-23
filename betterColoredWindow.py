#Matthew Siegel
#4/23/18
#betterColoredWindow.py - another one of these

from ggame import*
from random import randint
red = Color(0xff0000, 1)
yellow = Color(0xffff00, 1)
green = Color(0x00ff7f, 1)
blue = Color(0x0000ff, 1)
Colors = [red,yellow,green,blue]

def mouseClick(event):
    randnum = randint(1,4)
    line = LineStyle(3,Colors[randnum])
    rectangle = RectangleAsset(100,100,line,Colors[randnum])
  
    Sprite(rectangle)
    
        


App().listenMouseEvent('click', mouseClick)
App().run()

