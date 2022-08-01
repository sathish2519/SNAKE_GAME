from ctypes.wintypes import SIZE
import pygame
from sympy import true
from pygame.locals import *
import time

SIZE = 40  #VARIABLE SIZE of a block
class Snake:
    def __init__(self,parent_screen,length):#here parent screen is a constructor
        
        #2creating block
        self.parent_screen=parent_screen
        self.block=pygame.image.load("resources/block.jpg").convert()#convert is the method for loading image
        #4
        self.length=length
        self.x=[SIZE]*length
        self.y=[SIZE]*length #these two are the position of the block
        #3
        self.directions='down'
        
    
    def draw(self):
        self.parent_screen.fill((255,255,255))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def moveleft(self):
        self.directions='left'
    def moveright(self):
        self.directions='right'
        
    def moveup(self):
        self.directions='up'
    def movedown(self):
        self.directions='down'

    def walk(self):

        for i in range (self.length-1,0,-1) : #nothing but reverse
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.directions =='left':
            self.x[0]-=SIZE
        
        if self.directions =='right':
            self.x[0]+=SIZE
        
        if self.directions =='up':
            self.y[0]-=SIZE
        
        if self.directions =='down':
            self.y[0]+=SIZE

        self.draw()
      

#snake class ends#

#game class
class Game:
    def __init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode((1300,650)) # we are using sef here to make surface variable as class member so that we can use it in code later part.
        self.surface.fill((255,255,255))#were are making surface as class member
        self.snake=Snake(self.surface,2)
        self.snake.draw()
#game class ends
    

    def run(self):
        #any game interface has event loop any ui have event loop which is something like while loop
        running=True
        while running:
            for event in pygame.event.get():#this events do all types of operations like mouse click and keyboard
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False
                    #key events for movements
                    if event.key==K_UP:
                        self.snake.moveup()
                    if event.key==K_DOWN:
                       self.snake.movedown()
                    if event.key==K_LEFT:
                        self.snake.moveleft()
                    if event.key==K_RIGHT:
                        self.snake.moveright()
                elif event.type==QUIT:
                    running=False
            self.snake.walk()
            time.sleep(0.4)

#main method

if __name__=='__main__':
    game=Game() # creating object of the game
    game.run()
    
        

    