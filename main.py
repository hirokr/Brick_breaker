# Version 1
import pygame as py 
from sys import exit
import math

WINS = [800,800]

py.init()
screen = py.display.set_mode(WINS)
font = py.font.Font(None, 50)
py.display.set_caption('This Brick Breaker By HRR')
clock = py.time.Clock
screen.fill((111,169,196))

class Screen:
    def __init__(self) -> None:
        pass
        

class Engine(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.game = True
    
    def play(self):
        while self.game:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.game = False

            py.display.flip()
            clock.tick(60)

if __name__ == 'main':
    a = Engine()
    a.play()