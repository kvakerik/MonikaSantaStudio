import math
import random
import pygame

class Nepriatel(pygame.sprite.Sprite):
    def __init__(self, p_size, hrac, all, enemyprojektil):
        super().__init__()
        self.p_size = p_size
        self.hrac = hrac
        self.all = all
        self.enemyprojektil = enemyprojektil
        self.x= random.randint(350,1600)
        self.y = random.randint(250,900)
        self.a = random.randint (-1,1)
        self.b= random.randint (-1,1)
        #nepriatel výzor
        self.image= pygame.Surface ((30,30))
        self.image.fill((255,30,30))
        #kde sa nepriatel nachádza
        self.rect=self.image.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x
        self.hp = 25
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
    def update_pos(self, player_x, player_y):
        pass



class EnemyProjektil (pygame.sprite.Sprite):
    def __init__(self, p_size, x, y, hx, hy):
        super().__init__()
        self.posX = x
        self.posY = y

        self.image = pygame.Surface((p_size, p_size))
        self.image.fill((255, 0, 0))

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
