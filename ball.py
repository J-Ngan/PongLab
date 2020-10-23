import pygame

class Ball:
    RADIUS = 10

    def __init__ (self, x, y, vx, vy, screen, fgcolor, bgcolor, WIDTH, HEIGHT, BORDER):
        
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.BORDER = BORDER

    def show(self,color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)
    
    def update(self):
        self.show(self.bgcolor)
    
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)

        #TODO:
        #Check if ball is in collision(wall position)
        #flip the velocity
         
        #For wall left and right
        if self.x + self.vx <= self.BORDER or self.x + self.vx >= self.WIDTH:
            self.vx = self.vx * -1

        #For wall top and bottom
        if self.y + self.vy <= self.BORDER or self.y + self.vy >= self.HEIGHT - self.BORDER:
            self.vy = self.vy * -1   

        pygame.draw.rect(self.screen, self.fgcolor, pygame.Rect((0,0),(self.WIDTH, self.BORDER)))
        pygame.draw.rect(self.screen, self.fgcolor, pygame.Rect((0,0),(self.BORDER, self.HEIGHT)))
        pygame.draw.rect(self.screen, self.fgcolor, pygame.Rect((0,self.HEIGHT-self.BORDER),(self.WIDTH, self.HEIGHT)))



