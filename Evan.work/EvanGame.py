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

        self.momentumX = 0
        self.momentumY = 0
        self.image = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.image.convert_alpha() #optimise for alpha
        self.image.set_colorkey(alpha) #set alpha
        
        self.rect = self.image.get_rect()

    def control(self, x, y):
        #controlplayermovement
        self.momentumX += x
        self.momentumY += y

    def update(self):
        #updatespriteposition
        currentX = self.rect.x
        nextX = currentX + self.momentumX
        self.rect.x = nextX

        currentY = self.rect.y
        nextY = currentY + self.momentumY
        self.rect.y = nextY
             



'''SETUP'''
#code runs once
screenX =980
screenY =670

alpha = (0, 255, 0)
black = (1, 1, 1)
white = (255, 255, 255)

fps = 40
afps = 4
clock = pygame.time.Clock()
pygame.init()

main = True

screen = pygame.display.set_mode([screenX, screenY])


player = Player()
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10  #how fast to move

             






'''MAINLOOP'''
#code runs many times
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit
            main = false
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
            if event.key == pygame.K_LEFT:
                print('left stop')
                player.control(movesteps, 0)
            if event.key == pygame.K_RIGHT:
                print('right stop')
                player.control(-movesteps, 0)
                if event.key == pygame.K_UP:
                    print('jump stop')


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('left')
                    player.control(movesteps, 0)
                if event.keyt == pygame.K_RIGHT:
                    print('right')
                    player.control(movesteps, 0)
                if event.key == pygeme.K_UP:
                    print('jump')

        screen.fill((66, 244, 217))
        player.update() #update player position
        movingsprites.draw(screen)  #draw player

        pygame.display.flip()
        clock.tick(fps)
        
