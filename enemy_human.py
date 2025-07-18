import pygame
import random
from pygame.locals import *

player_image = pygame.image.load('player.png')

class EnemyH(pygame.sprite.Sprite):
    def __init__(self, hrac):
        super().__init__()
        self.hrac = hrac
        self.posX = random.randint(350, 1400)
        self.posY = random.randint(200, 300)
        self.hp = 1                                   #zmenit 5

        self.image = player_image
        self.rect = self.image.get_rect()
        self.velo = random.randint(5, 10)/10
        # pos
        self.rect.left = self.posX
        self.rect.top = self.posY

    def nastav_pos(self, x, y):
        self.posX = x
        self.posY = y
        self.rect.left = self.posX
        self.rect.top = self.posY

    def update(self):
        player_x = self.hrac.pos_x
        player_y = self.hrac.pos_y

        self.rect.top = self.posY
        self.rect.left = self.posX

        if (player_x - 5) > self.posX:
            self.posX += self.velo
        elif (player_x - 5) < self.posX:
            self.posX -= self.velo
        elif (player_x - 5) == self.posX:
            pass

        if (player_y - 25) > self.posY:
            self.posY += self.velo
        elif (player_y - 25) < self.posY:
            self.posY -= self.velo
        elif (player_y - 25) == self.posY:
            pass
        if self.hp == 0:
            self.kill()

    def hpl(self):
        self.hp -= 1
        print(self.hp)