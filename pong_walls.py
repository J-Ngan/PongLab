import pygame

def main():

    pygame.init()

    pygame.display.set_caption("my pong")


    WIDTH = 800
    HEIGHT = 400
    #surface  
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill((0,0,0))
    #double buffering stage updates together; update them at once
    pygame.display.update()

    #walls
    #rect(surface, color, rect) -> rect
    #rect(left,top), (width, height)) -> rect
    wcolor = pygame.Color("white")
    BORDER = 15
    #top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH, BORDER)))
    #left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(BORDER, HEIGHT)))
    #bottom wall
    NEW = HEIGHT - BORDER
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT-BORDER),(WIDTH, HEIGHT)))
    #pygame.draw.rect(screen, ocolor, pygame.Rect((0,HEIGHT),(WIDTH, HEIGHT-20)))

    #ask question on why height-20 works on 1st and not 2nd 

    pygame.display.update()


    # define a variable to control the main loop
    running = True
        
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
if __name__=="__main__":
    # call the main function
    main()    
