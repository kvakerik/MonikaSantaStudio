import pygame
import random
from pygame.locals import *

minotaur = pygame.image.load('minotaur.png')
minotaur_right = pygame.image.load('minotaur_right.png')


class EnemyHorizontal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posX = random.choice([random.randint(350, 400), random.randint(1200, 1250)])
        self.posY = random.randint(300, 600)
        # size
        self.image = minotaur

        self.rect = self.image.get_rect()
        self.velo = 2
        # pos
        self.rect.left = self.posX
        self.rect.top = self.posY

        self.hp = 1                #zmenit10

    def update(self):

        self.posX += self.velo
        if self.velo > 0:
            self.image = minotaur_right
        elif self.velo < 0:
            self.image = minotaur
        if self.posX > 1500 or  self.posX < 350:
            self.velo = -self.velo

        self.rect.top = self.posY
        self.rect.left = self.posX

        if self.hp == 0:
            self.kill()

    def hpl(self):
        self.hp -= 1

