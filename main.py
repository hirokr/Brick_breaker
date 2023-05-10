# Version 1
import pygame as py 
from sys import exit

WINS = [1536,793]
WINS = [800, 600]

py.init()
screen = py.display.set_mode(WINS, py.RESIZABLE)
font = py.font.Font(None, 50)
py.display.set_caption('This Brick Breaker By HRR')
Clock = py.time.Clock()
screen.fill((111,169,196))


class Ball:
    def __init__(self) -> None:
        #floor
        self.f_width = 100
        self.f_x = 300
        self.f_y = 530
        
        #ball
        self.ball_h_w = 15
        self.ball_x = 345
        self.ball_y = 515
        self.ballFloor()

    def ballFloor(self):
        self.ball = py.Rect(self.ball_x, self.ball_y,  self.ball_h_w, self.ball_h_w)
        self.floor = py.Rect(self.f_x,self.f_y,  self.f_width, 10)
        py.draw.rect(screen, 'black', self.ball )
        py.draw.rect(screen, 'pink', self.floor)


class Brick:
    def __init__(self):
        self.b_left = WINS[0]/6 - .33 #133
        self.b_top = 60
        self.b_width = WINS[0]/6 - 11 #125.33
        self.b_height = 38
        self.top_difference = 44
        self.bricks()
        
    def bricks(self):
        b1 = [py.Rect(10 + (i * self.b_left), self.b_top, 
                    self.b_width, self.b_height) for i in range(6)]
        
        b2 = [py.Rect(10 + (i * self.b_left), 
                      (self.top_difference + self.b_top), 
                      self.b_width, self.b_height) for i in range(6)]
        
        b3 = [py.Rect(10 + (i * self.b_left), 
                    (self.top_difference*2 + self.b_top), 
                    self.b_width, self.b_height) for i in range(6)]
        self.brick_wall = [b1,b2,b3]    
            
    def brickCreate(self):
        for j in self.brick_wall:
            for i in j:
                py.draw.rect(surface = screen, 
                            color = (252, 170, 28), 
                            rect = i)
                

class Screen(Brick, Ball):
    def __init__(self) -> None:
        super().__init__()
        super(Brick, self).__init__()

    def bigScreen(self):
        #bricks
        self.b_width *= 1.92
        self.b_left *= 1.92
        self.b_height = 40
        self.b_top = 100
        self.top_difference = 60
        
        #ball 
        self.ball_h_w = 20
        self.ball_x = 760
        self.ball_y = 680
    
        #floor
        self.f_width = 200
        self.f_x = 680
        self.f_y = 700

    def smallScreen(self):

        #Bricks
        self.b_width = WINS[0]/6 - 11
        self.b_left = WINS[0]/6 - .33
        self.b_height = 38
        self.top_difference = 44

        #floor
        self.f_width = 100
        self.f_x = 300
        self.f_y = 530
        
        #ball
        self.ball_h_w = 15
        self.ball_x = 345
        self.ball_y = 515
    
    def screenChange(self,size):
        
        if size[0] > 800:
            self.bigScreen()
        else:
            self.smallScreen()

        super().bricks()
        super().ballFloor()
        
    def allBuilt(self):
        screen.fill((111,169,196))
        py.draw.rect(screen, 'black', self.ball)
        super().brickCreate()
        py.draw.rect(screen, 'pink', self.floor)


class Engine(Screen):
    def __init__(self) -> None:
        super().__init__() 
        self.game_start = False
    
    def collide(self):
    
        for i in self.brick_wall:
            for j in i:
                if j.collidepoint(self.ball.x, self.ball.y):
                    i.remove(j)
                    self.ball.x = 100


    def play(self):
        global screen
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()

                if event.type == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        py.quit()
                        exit()

                    if event.key == py.K_SPACE:
                        self.game_start = True
                        
                    if event.key == py.K_LEFT:
                        self.floor.x -= 30
                    
                    if event.key == py.K_RIGHT:
                        self.floor.x += 30

                if event.type == py.VIDEORESIZE:
                    self.new_size = event.size 
                    screen = py.display.set_mode(self.new_size, py.RESIZABLE)
                    screen.fill((111,169,196))
                    super().screenChange(self.new_size)

            if self.game_start:
                self.ball.y -= 5
            
            if self.ball.y <=0:
                self.ball.y += 5
            

            super().brickCreate()

            self.collide()

            self.allBuilt()
           
            py.display.update()
            Clock.tick(60)


a = Engine()
a.play()