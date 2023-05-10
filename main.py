# Version 1
import pygame as py 
from sys import exit

WINS = [800,600]

py.init()
screen = py.display.set_mode(WINS, py.RESIZABLE)
font = py.font.Font(None, 50)
py.display.set_caption('This Brick Breaker By HRR')
Clock = py.time.Clock()
screen.fill((111,169,196))


class Screen:
    def __init__(self) -> None:
        self.ball = py.Rect(100,50,10, 10)
        self.brick = py.Rect(100,160,200, 30)
        py.draw.rect(screen, 'black', self.ball)
        py.draw.rect(screen, 'yellow', self.brick)
        


class Engine(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.game = True 
    
    def play(self):
        while self.game:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.game = False
                if event.type == py.VIDEORESIZE:
                    self.new_size = event.size 
                    screen = py.display.set_mode(self.new_size, py.RESIZABLE)
                    screen.fill('red')
                    a = Screen()

            py.display.update()
            Clock.tick(60)


a = Engine()
a.play()