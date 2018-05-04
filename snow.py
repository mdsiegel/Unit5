#Matthew Siegel
#5/4/18
#snow.py - making snow

from ggame import *
from random import randint


WIDTH = 1000
HEIGHT = 600

#move each angt randomly up/down left and right
def step():
    for snow in data['snowList']:
        snow.x += randint(-4,3)
        snow.y += randint(-4,3)


#Putting rire ants randomly on the screen
if __name__ == '__main__':
    
    data = {}
    data['snowList'] = []
    
    white = Color(0xFFFFFF,1)
    snow = CircleAsset(20,LineStyle(1,white),white)
    
    black = Color(0x000000,1)
    line = LineStyle(3,black)
    background = RectangleAsset(WIDTH,HEIGHT,line,black)
    Sprite(background)
    
    for i in range(len(data['snowList'])):
        data['snowList'].append(Sprite(snow,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run()
    