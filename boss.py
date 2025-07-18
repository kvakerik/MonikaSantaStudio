import random
import pygame
import enemy
import enemy_shooter

from pygame.locals import *

running = True
pygame.init()
FPS= pygame.time.Clock()
screen=pygame.display.set_mode([1000,1000])
pygame.display.set_caption("projektil")
c = 0
bcd = 7
p_size = 5

class Boss(pygame.sprite.Sprite):
    def __init__(self, p_size, hrac, all, enemies, enemyprojektil):
        super().__init__()
        self.p_size=p_size
        self.hrac = hrac
        self.all = all
        self.enemies = enemies
        self.ep = enemyprojektil

        self.x= random.randint(100,800)
        self.y = random.randint(100,800)

        #nepriatel výzor
        self.image= pygame.Surface ((80,80))
        self.image.fill((255,30,30))
        #kde sa nepriatel nachádza
        self.rect=self.image.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x

    def update(self):
        if random.randint(1, 50) > 49:
            # vytvorenie nepriatela
            enemy_temp = enemy.Enemy1(self.hrac)
            enemy_temp.nastav_pos(self.x, self.y)
            self.enemies.add(enemy_temp)
            self.all.add(enemy_temp)
        if random.randint(1, 50) > 49:
            # vytvorenie strely
            ep = enemy_shooter.EnemyProjektil(self.p_size, self.x, self.y, self.hrac.pos_x, self.hrac.pos_y)
            self.all.add(ep)
            self.ep.add(ep)




class Projektil (pygame.sprite.Sprite):
    def __init__(self, x, y, sx, sy):
        super().__init__()
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        global p_size

        # nepriatel výzor
        self.image = pygame.Surface((p_size, p_size))
        self.image.fill((255, 0, 0 ))

        # kde sa nepriatel nachádza
        self.rect = self.image.get_rect()
        self.rect.top=self.y
        self.rect.left=self.x

    def update(self):
        self.x += self.sx
        self.y += self.sy
        self.rect.top = self.y
        self.rect.left = self.x


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos_x = 450
        self.pos_y = 450
        self.size_x = 20
        self.size_y = 20

        self.image = pygame.Surface((self.size_x, self.size_x))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.top = self.pos_y
        self.rect.left = self.pos_x

    def update(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            self.pos_x += -2
        if pressed_key[K_RIGHT]:
            self.pos_x += 2
        if pressed_key[K_UP]:
            self.pos_y += -2
        if pressed_key[K_DOWN]:
            self.pos_y += 2
        self.rect.top = self.pos_y
        self.rect.left = self.pos_x

   # get_pos_x(self):
   # return self.pos_x

   # get_pos_y(self):
   # return self.pos_y

all = pygame.sprite.Group()

bullets = pygame.sprite.Group()

player_group = pygame.sprite.Group()
p1 = Player()
all.add(p1)
player_group.add(p1)

nepriatela=pygame.sprite.Group()
ep=pygame.sprite.Group()

for i in range(1):
    n=Boss(p_size, p1, all, nepriatela,ep)
    nepriatela.add(n)
    all.add(n)
    print(len(nepriatela))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    c += 1
    if c == bcd:
        c = 0

    screen.fill((255, 255, 255))

    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_w] and c == 0:
        p = Projektil(p1.pos_x + p1.size_x/2 - p_size/2, p1.pos_y + p1.size_y/2 - p_size/2, 0, -10)
        bullets.add(p)
        all.add(p)
    else:
        if pressed_key[K_s] and c == 0:
            p = Projektil(p1.pos_x + p1.size_x/2 - p_size/2, p1.pos_y + p1.size_y/2 - p_size/2, 0, 10)
            bullets.add(p)
            all.add(p)
        else:
            if pressed_key[K_d] and c == 0:
                p = Projektil(p1.pos_x + p1.size_x/2 - p_size/2, p1.pos_y + p1.size_y/2 - p_size/2, 10, 0)
                bullets.add(p)
                all.add(p)
            else:
                if pressed_key[K_a] and c == 0:
                    p = Projektil(p1.pos_x + p1.size_x/2 - p_size/2, p1.pos_y + p1.size_y/2 - p_size/2, -10, 0)
                    bullets.add(p)
                    all.add(p)

    if pygame.sprite.groupcollide(bullets, nepriatela, 1, 1):
        print("strelil si")
        if len(nepriatela) == 0:
            print("zabil si")
    if pygame.sprite.spritecollideany(p1, nepriatela):
        print("dotykli sa")






    all.update()
    all.draw(screen)

    FPS.tick(60)
    pygame.display.flip()

pygame.quit()
