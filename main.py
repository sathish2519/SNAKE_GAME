from ctypes.wintypes import SIZE
from tkinter import font
import pygame
from sympy import true
from pygame.locals import *
import time
import random

SIZE = 40  #VARIABLE SIZE of a block

#APPLE CLASS
class Apple():
    def __init__(self,parent_screen):
        self.image=pygame.image.load("resources/apple.jpg").convert()#convert is the method for loading image 
        self.parent_screen=parent_screen#we are calling parent screen here to  get painted in game window
        self.x=SIZE*3
        self.y=SIZE*3
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x=random.randint(2,30)*SIZE
        self.Y=random.randint(5,16)*SIZE



class Snake:
    def __init__(self,parent_screen,length):#here parent screen is a constructor
        
        #2creating block
        self.parent_screen=parent_screen
        self.block=pygame.image.load("resources/block.jpg").convert()#convert is the method for loading image
        #4
        self.length=length
        self.x=[40]*length
        self.y=[40]*length #these two are the position of the block
        #3
        self.directions='down'


    def inclength(self):
        self.length+=1
        self.x.append(1)
        self.y.append(1)
        
    
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
        self.snake=Snake(self.surface,1)
        self.snake.draw()
        self.apple=Apple(self.surface)
        self.apple.draw()


    #collision Logic #5
    def collision(self,x1,y1,x2,y2):
        if y1>=y2 and y1<y2+SIZE:
            if x1>=x2 and x1<x2+SIZE:
                return True
        return False


    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.scoredisplay()
        pygame.display.flip()
#5 snake colliding with apple 
        if self.collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y): #checking whether the collision happens if happens we check whether the collision of apple and snake head we dont want to check body so x[0],y[0].
           #7increasing the snake length when snake eats object
            self.snake.inclength()
            self.apple.move()#6 when collision occurs we move apple to random position ,this method will be called in apple class 
#8 display score
    def scoredisplay(self):
        font=pygame.font.SysFont('vedanta',30) #pygame has font module
        score=font.render(f"your score: {self.snake.length}",True,(0,0,0))
        self.surface.blit(score,(1150,10))
                


    

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
            self.play()#method
            time.sleep(0.2)

#game class ends

#main method

if __name__=='__main__':
    game=Game() # creating object of the game
    game.run()
    
        

    