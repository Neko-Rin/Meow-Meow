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
player_rect= player_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

star_surf= pygame.image.load(join('space shooter', 'images', 'star.png')).convert_alpha()
star_position= [(randint(0,WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)) for _ in range (20)]

meteor_surf= pygame.image.load(join('space shooter', 'images', 'meteor.png')).convert_alpha()
meteor_rect=meteor_surf.get_frect(center= (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

laser_surf= pygame.image.load (join('space shooter', 'images', 'laser.png'))
laser_rect= laser_surf.get_frect(bottomleft= (WINDOW_WIDTH-20, WINDOW_HEIGHT-20))
#creates an array with 20 items with each item having a set of coords

at_rightedge= False
at_leftedge = True
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
    if player_rect.right <= WINDOW_WIDTH and at_leftedge:
        player_rect.right += 2
        if player_rect.right == WINDOW_WIDTH:
            at_rightedge= True
            at_leftedge= False
    if at_rightedge:
        player_rect.right -= 2
        if player_rect.left == 0:
            at_rightedge= False
            at_leftedge= True
    display.blit(player_surf,player_rect)
    display.blit(meteor_surf, meteor_rect) 
    display.blit(laser_surf, laser_rect)       
        #updates display "pygame.display.update()" updates the whole window. While the filp lets you only update a part of it.
    pygame.display.update()

#ending pygame
pygame.quit()
