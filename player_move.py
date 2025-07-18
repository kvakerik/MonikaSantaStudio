import pygame
import random
from pygame.locals import *
import enemy
import enemy_shooter

import pkg_resources


required = {"rpi.gpio"}
installed = {pkg.key for pkg in pkg_resources.working_set }
missing = required - installed
JE_RPI = len(missing) == 0

if JE_RPI:
        import RPi.GPIO as GPIO




player_image = pygame.image.load('player.png')
player_image_back = pygame.image.load('player_back.png')
player_image_left = pygame.image.load('player1_left.png')

final_boss = pygame.image.load('final_boss.png')
bullet_image10 = pygame.image.load("bulllet_25.png")
bullet_image5 = pygame.image.load("bulllet_10.png")


class Projektil (pygame.sprite.Sprite):
    def __init__(self, x, y, sx, sy):
        super().__init__()
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.bullet_image = bullet_image5

        # nepriatel výzor
        self.image = self.bullet_image

        # kde sa nepriatel nachádza
        self.rect = self.image.get_rect()
        self.rect.top=self.y
        self.rect.left=self.x

    def update(self):
        self.x += self.sx
        self.y += self.sy
        self.rect.top = self.y
        self.rect.left = self.x
    def hpl(self):
        pass
    def increase_bsize(self):
        self.bullet_image = bullet_image10
        self.image = self.bullet_image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos_x = 950
        self.pos_y = 880
        self.size_x = 20
        self.size_y = 20
        self.vel = 2

        self.image = player_image

        self.rect = self.image.get_rect()
        self.rect.top = self.pos_y
        self.rect.left = self.pos_x
        # self.a = 0
        # self.b = 0

    # GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 11-hore
    # GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 13-vlavo
    # GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 15-vpravo
    # GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 16-dole
    # GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 18-joystick




    def update(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT] or (JE_RPI and GPIO.input(22) == GPIO.LOW):
            self.image = player_image_left
            self.pos_x += - self.vel
            #self.a = -1
        if pressed_key[K_RIGHT] or (JE_RPI and GPIO.input(23) == GPIO.LOW):
            self.image = player_image
            self.pos_x += self.vel
            #self.a = 1
        if pressed_key[K_UP] or (JE_RPI and GPIO.input(17) == GPIO.LOW):
            self.image = player_image_back
            self.pos_y += -self.vel
            #self.b = -1
        if pressed_key[K_DOWN] or (JE_RPI and GPIO.input(27) == GPIO.LOW):
            self.image = player_image
            self.pos_y += self.vel
            # self.b = 1
        if self.pos_x > 1585:
            self.pos_x = 1585
        if self.pos_x > 1569 and self.pos_y < 300:
            self.pos_x = 1569
        if self.pos_x > 1569 and self.pos_y > 480:
            self.pos_x = 1569
        if self.pos_x < 348 and self.pos_y < 300:
            self.pos_x = 348
        if self.pos_x < 348 and self.pos_y > 480:
            self.pos_x = 348
        if self.pos_x < 332:
            self.pos_x = 332
        if self.pos_y > 880:
            self.pos_y = 880
        if self.pos_y < 200:
            self.pos_y = 200
        self.rect.midbottom = (self.pos_x, self.pos_y)

    def get_pos_x(self):
        x = self.pos_x
        return x

    def get_pos_y(self):
        y = self.pos_y
        return y
    def movement(self):
        if self.pos_y < 400:
            self.pos_y = 400


class Boss(pygame.sprite.Sprite):
    def __init__(self, p_size, hrac, all, enemies, enemyprojektil, bats):
        super().__init__()
        self.p_size=p_size
        self.hrac = hrac
        self.all = all
        self.enemies = enemies
        self.ep = enemyprojektil
        self.bats = bats

        self.x= 900
        self.y = 300

        self.hp = 100

        #nepriatel výzor
        self.image= final_boss #final_boss
        #kde sa nepriatel nachádza
        self.rect=self.image.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x

    def update(self):
        if random.randint(1, 50) > 49:
            # vytvorenie nepriatela
            enemy_temp = enemy.Enemy1(self.hrac)
            enemy_temp.nastav_pos(random.randint(400, 1200), self.y)
            self.enemies.add(enemy_temp)
            self.all.add(enemy_temp)
            self.bats.add(enemy_temp)
        #if random.randint(1, 50) > 40:
            # vytvorenie strely
            ep = enemy_shooter.EnemyProjektil(self.p_size, self.x, self.y, self.hrac.pos_x, self.hrac.pos_y)
            self.all.add(ep)
            self.ep.add(ep)

    def hpl(self):
        self.hp -= 1


