import pygame
pygame.init()
from pygame import surface
from pygame.locals import *

#class
class door(pygame.sprite.Sprite):
    def __init__(self, pos, size, roomn):
        super().__init__()

        self.color = [255, 0, 0]

        self.image = pygame.Surface((size[0], size[1]))
        self.image.fill((self.color))
        self.rect = self.image.get_rect()

        self.posX = pos[0]
        self.posY = pos[1]
        self.rect.left = self.posX
        self.rect.top = self.posY
        self.roomn = roomn
        self.open = False
    def set_colorg(self):
        self.color = [0, 255, 0]
        self.image.fill((self.color))
    def set_colorr(self):
        self.color = [255, 0, 0]
        self.image.fill((self.color))

