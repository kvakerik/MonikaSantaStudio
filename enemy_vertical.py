import pygame
import random
from pygame.locals import *

troll = pygame.image.load('whatver_this_is_supposed_to_be.png')
troll_back = pygame.image.load('whatver_this_is_supposed_to_be_back.png')


class EnemyVertical(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posY = random.randint(250, 400)
        self.posX = random.randint(400, 1300)
        # size
        self.image = troll


        self.rect = self.image.get_rect()
        self.velo = 2
        # pos
        self.rect.left = self.posX
        self.rect.top = self.posY

        self.hp = 1                                             #zmenit10

    def update(self):

        self.posY += self.velo

        if self.velo > 0:
            self.image = troll
        elif self.velo < 0:
            self.image = troll_back
        if self.posY > 850 or self.posY < 160:
            self.velo = -self.velo

        self.rect.top = self.posY
        self.rect.left = self.posX

        if self.hp == 0:
            self.kill()
    def hpl(self):
        self.hp -= 1
