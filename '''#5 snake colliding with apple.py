'''#5 snake colliding with apple 
        if self.collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y): #checking whether the collision happens if happens we check whether the collision of apple and snake head we dont want to check body so x[0],y[0].
           #7increasing the snake length when snake eats object
            self.playsound("ding")
            self.snake.inclength()
            self.apple.move()#6 when collision occurs we move apple to random position ,this method will be called in apple class 




            #  8 snake colliding with itself
        for i in range(3,self.snake.length):
            if self.collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                self.playsound("glass_break")
                raise "COLLISION OCCUR"'''




                #8 display score
    def scoredisplay(self):
        font=pygame.font.SysFont('arial',30) #pygame has font module
        score=font.render(f"Your Current Score: {self.snake.length}",True,(0,0,0))
        self.surface.blit(score,(1020,10))
                

#9snake collision with itself
    def gameover(self):
        self.bgimage()
        self.surface.fill(BGCOLOR)
        font=pygame.font.SysFont('arial',30) #pygame has font module
        line2=font.render(f"GAME OVER! YOUR SCORE IS: {self.snake.length}",True,(0,0,0))
        self.surface.blit(line2,(100,50))
        line3=font.render("Press Enter If You Want To Continue > Press Esc If You Want To Quit",True,(0,0,0))
        self.surface.blit(line3,(200,200))
        pygame.display.flip() #we use flip in pygame when ever we do changes in ui, it refreshes the ui
    pause=True
#reset method
    def reset(self):
        self.snake=Snake(self.surface,1)
        self.apple=Apple(self.surface)