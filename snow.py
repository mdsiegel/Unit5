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
        snow.x += randint(-1,1)
        snow.y += randint(1,5)
def moreSnow():
    data['frames'] +=1
    if data['frames']%50 == 0:
        data['snowList'].append(Sprite(snow,(randint(1,WIDTH),0)))


#Putting rire ants randomly on the screen
if __name__ == '__main__':
    
    data = {}
    data['snowList'] = []
    data['frames'] = 0
    white = Color(0xFFFFFF,1)
    snow = CircleAsset(10,LineStyle(1,black),white)
    
    black = Color(0x000000,1)
    line = LineStyle(3,black)
    background = RectangleAsset(WIDTH,HEIGHT,line,black)
    Sprite(background)
    
    
    
    App().run(step)
    