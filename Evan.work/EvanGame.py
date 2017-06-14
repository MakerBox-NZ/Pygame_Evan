#!/usr/env python3
#by evan
#thanks to my cake and all the snorlaxxians who helped
import pygame 
import sys
import os

'''OBJECTS'''
#put classes and functions here
class Player(pygame.sprite.Sprite):
    #spawn a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.rect = self.image.get_rect()
             



'''SETUP'''
#code runs once
screenX =960
screenY =720

fps = 40
afps = 4
Clock = pygame.time.clock()
pygame.init()

main = True

screen = pygame.display.set_mode([screenX, screenY])
             






'''MAINLOOP'''
#code runs many times
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.keyup:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False    

        screen.fill(blue)

        pygame.display.flip()
        clock.tick(fps)
        
