from random import randint
import pygame
from os.path import join
#initating pygame
pygame.init()

#Creates display
WINDOW_WIDTH, WINDOW_HEIGHT=  1280,720
display= pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("MEOW")
running=True

#plain surface
surf= pygame.Surface((100,200))
surf.fill('orange')

#importing image
player_surf= pygame.image.load(join('space shooter', 'images','player.png' )).convert_alpha()
# join from os.path allows you to create the directory base on the device
#creates frect, frect stores data as float while rect stores as int
player_surface= player_surf.get_frect(topleft=(0,0))
star_surf= pygame.image.load(join('space shooter', 'images', 'star.png')).convert_alpha()
#creates an array with 20 items with each item having a set of coords
star_position= [(randint(0,WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)) for i in range (20)]

x=0
#keeps the display up
while running:
    #event loop
    for event in pygame.event.get():
        
        #check if the game was closed out and ends the code
        if event.type == pygame.QUIT:
            running=False
        #draw the game
    display.fill('black')
    for pos in star_position:
        display.blit(star_surf,pos)
    display.blit(player_surf,player_surface)        
        #updates display "pygame.display.update()" updates the whole window. While the filp lets you only update a part of it.
    pygame.display.update()

#ending pygame
pygame.quit()
