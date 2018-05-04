#Matthew Siegel
#5/4/18
#snow.py - making snow

from ggame import *
from random import randint


WIDTH = 1000
HEIGHT = 600

def step():
    moreSnow()
    for snow in data['snowList']:
        snow.x += randint(-1,3)
        snow.y += randint(-1,3)
def moreSnow():
    data['frames'] +=1
    if data['frames']%10 == 0:
        data['snowList'].append(Sprite(snow,(randint(1,WIDTH),randint(1,HEIGHT))))


#Putting rire ants randomly on the screen
if __name__ == '__main__':
    
    data = {}
    data['snowList'] = []
    
    white = Color(0xFFFFFF,1)
    snow = CircleAsset(50,LineStyle(1,black),white)
    
    black = Color(0x000000,1)
    line = LineStyle(3,black)
    background = RectangleAsset(WIDTH,HEIGHT,line,black)
    Sprite(background)
    
    
    
    App().run(step)
    