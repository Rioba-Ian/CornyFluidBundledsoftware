import pygame
from random import randint

# There will be a paddle; a simple rectangle that moves left or right in the screen, attempting to catch balls falling from the top of the screen. 

pygame.init()

# initializing variables to account for the number of balls caught and total dropped 

score = 0
total = 0

# The font to write the scores 

myfont = pygame.font.SysFont('monospace', 50)

# making dictionaries with settings for everything

display = {
    "width":800,
    "height":600
}
paddle = {
    "width":200,
    "height":20,
    "x":300,
    "y":500,
    "velocity":20
}
ball = {
    "radius":15,
    "y":30,
    "x":randint(0,display['width']),
    "velocity":10
}

# create a window and launch the game
# It will use the 800 width and 600 height
win = pygame.display.set_mode((display['width'],display['height']))

"""The paddle"""
"""We need to understand that for pygame, the top-left corner is (0,0) and x increases as you go right, while y increases as you move down"""

while True:
    # We shall set the loop running for 100 milliseconds, that is 10 times per second
    pygame.time.delay(100)
    # the background of the window - white
    win.fill((255,255,255))

    # Pygame loop to run continuosly, and breaks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    # keys interaction
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle['x'] -= paddle['velocity']

    if keys[pygame.K_RIGHT]:
        paddle['x'] += paddle['velocity']

    ball['y'] += ball['velocity']
    pygame.draw.circle(win, (0,0,255), (ball['x'], ball['y']),ball['radius'])

    """The scoring of points"""

    # We learn if the ball has hit the level of the paddle, by checking if the ball's radius + it's position on the y axis is equal to the position of the paddle


    if ball["y"] + ball["radius"] >= paddle["y"]:
        if ball["x"] > paddle["x"] and ball["x"] < paddle["x"] + paddle["width"]:
            score += 1
        total += 1
        ball["y"] = 0
        ball["x"] = randint(0, display["width"])


    pygame.draw.rect(win, (255,0,0),(paddle['x'],paddle['y'],paddle['width'],paddle['height']))
    pygame.display.update()
    textsurface = myfont.render('score:{0}/{1}'.format(score,total),False,(0,0,0))
    win.blit(textsurface, (10,10))

    """We shall add this inside the loop 
    ball['y'] += ball['velocity']
    pygame.draw.circle(win, (0,0,255), (ball['x'], ball['y']),ball['radius'])

    We are increasing the y-cordinate of the ball by its velocity and drawing the ball again in every cycle of the loop
    """

    
    


