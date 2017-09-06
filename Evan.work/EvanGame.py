#!/usr/env python3
#by evan
#thanks to my cake
import pygame 
import sys
import os
import pygame.freetype #load fonts

'''OBJECTS'''
#put classes and functions here

def stats(score):
    #display text, 1, color (rgb)
    text_score = myfont.render("score: "+str(score), 1, (250,147,248))
    screen.blit(text_score, (4, 4))

class Platform(pygame.sprite.Sprite):
    #x location, y location, imgw, imgh, img file)
    def __init__(self,xloc,yloc,imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([imgw, imgh])
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.blockpic = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

        #paint image into blocks
        self.image.blit(self.blockpic,(0,0),(0,0,imgw,imgh))

    def level1():
        #create level 1
        platform_list = pygame.sprite.Group()
        block = Platform(0, 542, 768, 118,os.path.join('images','block0.png'))
        platform_list.add(block)                                    
        return platform_list #at end of function level1
 
class Player(pygame.sprite.Sprite):
    #spawn a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.momentumX = 0
        self.momentumY = 0

        #gravity variables\
        self.collide_delta = 0
        self.jump_delta = 6

        self.score = 0
        self.damage = 0 #player is hit
        
        self.image = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.image.convert_alpha() #optimise for alpha
        self.image.set_colorkey(alpha) #set alpha
        
        self.rect = self.image.get_rect()

    def control(self, x, y):
        #controlplayermovement
        self.momentumX += x
        self.momentumY += y

    def update(self, enemy_list):

        self.score = 0 #set score

        #updatespriteposition
        currentX = self.rect.x
        nextX = currentX + self.momentumX
        self.rect.x = nextX

        currentY = self.rect.y
        nextY = currentY + self.momentumY
        self.rect.y = nextY

        #gravity
        if self.collide_delta < 6 and self.jump_delta < 6:
            self.jump_delta = 6*2
            self.momentumY -=33 #how high to jump

            self.collide_delta +=6
            self.jump_delta += 6

    
        #collisions
        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)

        '''for enemy in enemy_hit_list:
            self.score -= 1
            print(self.score)'''

        if self.damage == 0:
            for enemy in enemy_hit_list:
                if not self.rect.contains(enemy):
                    self.damage = self.rect.colliderect(enemy)
                    print(self.score)

        if self.damage == 1:
            idx = self.rect.collidelist(enemy_hit_list)
            if idx == -1:

                self.score -= 1 #subtract 1 hp
        
        
        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        if self.momentumX > 0:
            for block in block_hit_list:
                self.rect.y =  currentY
                self.rect.x = currentX+9
                self.momentumY = 0
                self.collide_delta = 0 #stopjumping

        if self.momentumY > 0:
            for block in block_hit_list:
                self.rect.y = currentY
                self.momentumY = 0
                self.collide_delta = 0 #stopjumping

    def jump (self, platform_list):
        self.jump_delta = 0

    def gravity(self):
        self.momentumY += 3.2 #how fast player fall

        if self.rect.y > 960 and self.momentumY  >= 0:
            self.momentumY = 0
            self.rect.y = screenY-20

class Enemy (pygame.sprite.Sprite):
    #spawn enemy
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def move(self):
        #enemy movement
        if self.counter >= 0 and self.counter <= 30:
            self.rect.x += 2
        elif self.counter >= 30 and self.counter <= 60:
            self.rect.x -= 2
        else:
            self.counter = 0
            print('reset')

        self.counter += 1
             



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
pygame.font.init() #start free type

font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "FONTS", "amazdoom.ttf")
font_size = 64
myfont = pygame.font.Font(font_path, font_size)

main = True

screen = pygame.display.set_mode([screenX, screenY])

backdropRect = screen.get_rect()

platform_list = Platform.level1() #set stage to level 1

player = Player()
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10  #how fast to move

#enemy code
enemy = Enemy(100,50, 'enemy.png')
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)


             






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
                player.jump(platform_list)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
                player.control(-movesteps, 0)
            if event.key == pygame.K_RIGHT:
                print('right')
                player.control(movesteps, 0)
            if event.key == pygame.K_UP:
                print('jump')

    screen.fill((66, 244, 217))
    platform_list.draw(screen) #draw platforms on screen
    player.gravity() #check gravity
    player.update(enemy_list) #update player position
    movingsprites.draw(screen)  #draw player

    enemy_list.draw(screen) #refresh enemies
    enemy.move() #move sprite

    stats(player.score) #draw text

    pygame.display.flip()
    clock.tick(fps)
    
