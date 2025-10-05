# Projekt mit Kommentaren
import pygame
#importing pygame
from sys import exit
#the sys module is a part of pygame. it includes the "exit" command which will be used to shut down the game, without having to close the "while True"-loop
#initiating pygame
screen = pygame.display.set_mode((800,500))
#setting parameters for the window our game will be played in
pygame.display.set_caption("Caries Killers")
#setting our games title to "Caries Killers" which will be visible on top of our window
clock = pygame.time.Clock()
#setting a clock for controlling time aswell as the frame refreshing rate
x = 200
y = 200
#setting the x and y position of our starting point 
radius = 10
#the radius will be used for our circle element's size
vel = 15
#defining our speed for moving the circle (15 pixels/second)
while True:                                    
#opening a while loop so the window wont disappear instantly; all elements will be placed in here
    for event in pygame.event.get():
    #getting player inputs (or events) using a for-loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #using an if loop we insert the possibility to close the game; pygame.quit() can be viewed as the opposite of pygame.init()
    keys = pygame.key.get_pressed()
    #giving our keyboard the ability to give input into our game
    if keys[pygame.K_LEFT] and x - radius > 0:
       x -= vel
    if keys[pygame.K_RIGHT] and x + radius < 800:
       x += vel
    if keys[pygame.K_UP] and y - radius > 0:
       y -= vel
    if keys[pygame.K_DOWN] and y + radius < 500:
       y += vel
    #assigning two dimensional movement on the arrow keys and setting boundries 
    screen.fill((0,0,0))
    #macht Hinterrund schwarz
    pygame.draw.circle(screen,(0,0,255),(x, y), radius)
    #blauer Kreis
    pygame.display.update()
    #constantly updating the window (or display) is essential for moving images
    clock.tick(60)
    #starting the clock for time measurement and restricting refresh rate(max. is 60/scond).
    #this means that the while loop will be repeated at most 60 times per second