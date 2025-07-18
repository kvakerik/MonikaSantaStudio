import math
import random
import pygame

shooter_image = pygame.image.load('shooter.png')
enemy_bullet = pygame.image.load('bulllet_yellow.png')

class Nepriatel(pygame.sprite.Sprite):
    def __init__(self, p_size, hrac, all, enemyprojektil):
        super().__init__()
        self.p_size = p_size
        self.hrac = hrac
        self.all = all
        self.enemyprojektil = enemyprojektil
        self.x= random.randint(350,1550)
        self.y = random.randint(350,500)
        self.a = random.randint (-1,1)
        self.b= random.randint (-1,1)
        #nepriatel výzor
        self.image= shooter_image
        #kde sa nepriatel nachádza
        self.rect=self.image.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x
        self.hp = 1                             #zmeniť 25
    def update(self):
        if random.randint(1, 50) > 49:
            # vystrel
            ep = EnemyProjektil(self.p_size, self.x, self.y, self.hrac.pos_x, self.hrac.pos_y)
            self.all.add(ep)
            self.enemyprojektil.add(ep)

        if self.hp == 0:
            self.kill()

    def hpl(self):
        self.hp -= 1



class EnemyProjektil (pygame.sprite.Sprite):
    def __init__(self, p_size, x, y, hx, hy):
        super().__init__()
        self.posX = x
        self.posY = y

        self.image = enemy_bullet

        c= math.sqrt((hx-x)**2+(hy-y)**2)
        self.dx= (hx-x)/c * 4
        self.dy= (hy-y)/c * 4

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

    def update(self):
        self.posX += self.dx
        self.posY += self.dy
        self.rect.top = self.posY
        self.rect.left = self.posX



