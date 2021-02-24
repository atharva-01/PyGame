import pygame
import sys

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0,0,0)
GREEN = (0,255,0)
fps = 60
ballRadius = 20
ballx = ballRadius
bally = ballRadius
speed = [1,1]

def animate_ball():
    global ballx, bally
    ballx += speed[0]
    bally += speed[1]
    check_boundary()

def check_boundary():
    if ballx + ballRadius > SCREEN_WIDTH or ballx - ballRadius < 0 :
        speed[0] *= -1
    if bally + ballRadius > SCREEN_HEIGHT or bally - ballRadius < 0:
        speed[1] *= -1


def gameloop():
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    pygame.display.set_caption(" Ball Animation")
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(BLACK)
        pygame.draw.circle(screen, GREEN, (ballx,bally), ballRadius)
        animate_ball()
        pygame.display.update()
        clock.tick(fps)


gameloop()