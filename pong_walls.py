import pygame
import random
from paddle import Paddle
from ball import Ball

def main():

    pygame.init()

    pygame.display.set_caption("my pong")


    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    XVELOCITY = 5
    YVELOCITY = 5
    FPS = 30
    #surface  
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill((0,0,0))
    #double buffering stage updates together; update them at once
    pygame.display.update()

    #walls
    #rect(surface, color, rect) -> rect
    #rect(left,top), (width, height)) -> rect
    fgcolor = pygame.Color("white")
    bgcolor = pygame.Color("black")
    
    #top wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0),(WIDTH, BORDER)))
    #left wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0),(BORDER, HEIGHT)))
    #bottom wall
    NEW = HEIGHT - BORDER
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,HEIGHT-BORDER),(WIDTH, HEIGHT)))

    #Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -XVELOCITY
    vy0 = YVELOCITY

    #TODO: +/- degree/random for 45 angle
    randomNumber = random.randint(0,2)
    #go up
    if randomNumber == 0:
        vy0 = YVELOCITY
    #go down    
    elif randomNumber == 1:
        vy0 = -YVELOCITY
    #go straight    
    else:
        vy0 = 0


    b0 = Ball(x0,y0, vx0, vy0, screen, fgcolor, bgcolor, WIDTH, HEIGHT, BORDER)
    b0.show(fgcolor)

    vy0 = -5

    pygame.display.update()


    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            
            pygame.display.update()
            clock.tick(FPS)
            

            #Ball
            b0.update()

if __name__=="__main__":
    # call the main function
    main()    

    #TODO:
    #Put gif of ball colliding in readme