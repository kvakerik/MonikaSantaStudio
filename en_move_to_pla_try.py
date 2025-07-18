import pygame
import enemy
import random
import Doors
import player_move
from player_move import Boss, Projektil
from pygame.locals import *
import enemy_horizontal
import enemy_vertical
import enemy_shooter
import enemy_human
from pygame import mixer
import sys
import subprocess
import pkg_resources

required = {"rpi.gpio"}
installed = {pkg.key for pkg in pkg_resources.working_set }
missing = required - installed

JE_RPI = len(missing) == 0

if JE_RPI:
        import RPi.GPIO as GPIO

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_UP)    #11-hore
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #13-vlavo
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #15-vpravo
        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #16-dole
        GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #18-joystick


p_size = 5
bcd = 12
c = 0
cd = 1

# init pygame
pygame.init()

clock = pygame.time.Clock()

# create window
background_image = pygame.image.load("image.jpg")
background_image = pygame.transform.scale(background_image, (1920, 1080))
screen = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("pygame example")

background_levels = pygame.image.load("level_start_edit.jpg")
background_levels.convert()
background_levels = pygame.transform.scale(background_levels, (1920, 1080))

background_levell = pygame.image.load("level_left_Edit.jpg")
background_levell.convert()
background_levell = pygame.transform.scale(background_levell, (1920, 1080))

background_levelr = pygame.image.load("level_right_Edit.jpg")
background_levelr.convert()
background_levelr = pygame.transform.scale(background_levelr, (1920, 1080))

background_levele = pygame.image.load("level_end_edit.jpg")
background_levele.convert()
background_levele = pygame.transform.scale(background_levele, (1920, 1080))

bat1 = pygame.image.load('bat1.png').convert_alpha()
bat2 = pygame.image.load('bat2.png').convert_alpha()
bat3 = pygame.image.load('bat3.png').convert_alpha()
bat4 = pygame.image.load('bat4.png').convert_alpha()
bat5 = pygame.image.load('bat5.png').convert_alpha()
bat6 = pygame.image.load('bat6.png').convert_alpha()
bat7 = pygame.image.load('bat7.png').convert_alpha()
bat8 = pygame.image.load('bat8.png').convert_alpha()

menu_font = pygame.font.Font('04B_30__.TTF', 70)
text_font = pygame.font.Font('04B_30__.TTF', 40)

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()


mixer.music.load('level_music.mp3')
mixer.music.play(-1)

sound_fx = pygame.mixer.Sound('enemy_destoryed.wav')
sound_fx.set_volume(0.2)

# rooms
edead = False
dopen = False
room = 0
menu_aktivne = True
menu_poz = 1
pU = False
edead1 = False
edead2 = False
edead3 = False

text00 = False
text0 = False
text01 = False
text1 = False
text02 = False
text2 = False
text03 = False
text3 = False
text04 = False
text4 = False
texte = False
text0e = False

cd0 = 0
cd1 = 0
cd2 = 0
cd3 = 0
cd4 = 0
cd5 = 0
cde = 0

prologue = False
end_game = False
end = False
highscore = False

bossspawn = True

timer = 0
timer_end = 0

# groups
doors = pygame.sprite.Group()
boss_doors = pygame.sprite.Group()
all = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies_bullets = pygame.sprite.Group()
bats = pygame.sprite.Group()
enemyH_group = pygame.sprite.Group()

# objects :(
player_object = player_move.Player()
player_group.add(player_object)

def reset_room():
    print(room, player_object.pos_x, player_object.pos_y)
    all.empty()
    doors.empty()
    enemies.empty()
    enemies_bullets.empty()
    all.add(player_object)
    boss_doors.empty()

    if room == 1:
        d2 = Doors.door((290, 300), (35, 153), 2)
        d3 = Doors.door((1598, 300), (35, 153), 3)
        d4 = Doors.door((875, 25), (170, 130), 4)
        all.add(d3)
        all.add(d4)
        all.add(d2)
        doors.add(d3)
        doors.add(d2)
        boss_doors.add(d4)


        if  player_object.pos_y < 300:
            player_object.pos_x = 950
            player_object.pos_y = 880
            print(room, player_object.pos_x, player_object.pos_y)
        else:
            if player_object.pos_y > 800:
                player_object.pos_x = 950
                player_object.pos_y = 250
        if player_object.pos_x < 390:
            player_object.pos_x = 1500
            player_object.pos_y = 440
        else:
            if player_object.pos_x > 1500:
                player_object.pos_x = 390
                player_object.pos_y = 440

        if edead1 == False:
            for i in range(3):
                enemy_temp = enemy.Enemy1(player_object)
                enemies.add(enemy_temp)
                all.add(enemy_temp)
                bats.add(enemy_temp)

            n = enemy_shooter.Nepriatel(p_size, player_object, all, enemies_bullets)
            enemies.add(n)
            all.add(n)

            for i in range(3):
                enemy_horiz = enemy_horizontal.EnemyHorizontal()
                enemies.add(enemy_horiz)
                all.add(enemy_horiz)

            for i in range(3):
                enemy_verti = enemy_vertical.EnemyVertical()
                enemies.add(enemy_verti)
                all.add(enemy_verti)

    if room == 2:
        d1 = Doors.door((1598, 300), (35, 153), 1)
        doors.add(d1)
        all.add(d1)

        player_object.pos_x = 1570
        player_object.pos_y = 440

        if edead2 == False:

            for i in range(5):
                enemy_verti = enemy_vertical.EnemyVertical()
                enemies.add(enemy_verti)
                all.add(enemy_verti)
            for i in range(3):
                enemy_horiz = enemy_horizontal.EnemyHorizontal()
                enemies.add(enemy_horiz)
                all.add(enemy_horiz)
            for i in range(2):
                n = enemy_shooter.Nepriatel(p_size, player_object, all, enemies_bullets)
                enemies.add(n)
                all.add(n)
    if room == 3:
        d1 = Doors.door((290, 300), (35, 153), 1)
        doors.add(d1)
        all.add(d1)

        player_object.pos_x = 350
        player_object.pos_y = 440

        if edead3 == False:
            for i in range(12):
                enemy_temp = enemy.Enemy1(player_object)
                enemies.add(enemy_temp)
                all.add(enemy_temp)
                bats.add(enemy_temp)
            for i in range(3):
                enemy_horiz = enemy_horizontal.EnemyHorizontal()
                enemies.add(enemy_horiz)
                all.add(enemy_horiz)

    if room == 4:
        player_object.pos_x = 950
        player_object.pos_y = 850
        if bossspawn:
            boss = player_move.Boss(p_size, player_object, all, enemies, enemies_bullets, bats)
            enemies.add(boss)
            all.add(boss)

def show_room():
    if room == 1:
        screen.blit(background_levels, (0, 0))
    if room == 2:
        screen.blit(background_levell, (0, 0))
    if room == 3:
        screen.blit(background_levelr, (0, 0))
    if room == 4:
        screen.blit(background_levele, (0, 0))

    cycle_bats(var, bats)

var = 1

def cycle_bats(v, b):
    if v % 8 == 1:
        for enemy_bats in b:
            enemy_bats.image = bat1
    if v % 8 == 2:
        for enemy_bats in b:
            enemy_bats.image = bat2
    if v % 8 == 3:
        for enemy_bats in b:
            enemy_bats.image = bat3
    if v % 8 == 4:
        for enemy_bats in b:
            enemy_bats.image = bat4
    if v % 8 == 5:
        for enemy_bats in b:
            enemy_bats.image = bat5
    if v % 8 == 6:
        for enemy_bats in b:
            enemy_bats.image = bat6
    if v % 8 == 7:
        for enemy_bats in b:
            enemy_bats.image = bat7
    if v % 8 == 0:
        for enemy_bats in b:
            enemy_bats.image = bat8

reset_room()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if menu_aktivne:
        screen.blit(background_image, (0, 0))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_ESCAPE]:
            running = False
        if pressed_keys[K_UP]:
            menu_poz -= 1
            if menu_poz < 1:
                menu_poz = 1
        if pressed_keys[K_DOWN]:
            menu_poz += 1
            if menu_poz > 4:
                menu_poz = 4
        if pressed_keys[K_SPACE]:
            if menu_poz == 1:
                menu_aktivne = False
                prologue = True
                bossspawn = True
                cde = 0
                cd1 = 0
                cd2 = 0
                cd3 = 0
                cd4 = 0
                timer_end = 0
            if menu_poz == 2:
                menu_aktivne = False
                end_game = True
                room = 4
                bossspawn = False
                cde = 0
                reset_room()
                timer_end = 0
            if menu_poz == 3:
                with open("highscore_adv.txt") as f1:
                    lines = f1.readlines()
                    advhs = lines
                with open("highscore_arc.txt") as f2:
                    lines = f2.readlines()
                    archs = lines
                highscore = True
            if menu_poz == 4:
                running = False
        if highscore:
            highscoreadv = menu_font.render("Fastest time in adventure: ", True, [0, 0, 0])
            highscoreadv1 = menu_font.render(str(advhs) + " seconds", True, [0, 0, 0])
            highscorearc = menu_font.render("Longest time survived arcade: ", True, [0, 0, 0])
            highscorearc1 = menu_font.render(str(archs) + " seconds", True, [0, 0, 0])
            screen.blit(highscoreadv, (150, 150))
            screen.blit(highscorearc, (150, 550))
            screen.blit(highscoreadv1, (150, 300))
            screen.blit(highscorearc1, (150, 700))

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_SPACE]:
                highscore = False
        else:
            start_img = menu_font.render("Play Adventure", True, [0, 0, 0])
            screen.blit(start_img, (275, 200))
            start_img = menu_font.render("Play Arcade", True, [0, 0, 0])
            screen.blit(start_img, (275, 350))
            start_img = menu_font.render("Highscore", True, [0, 0, 0])
            screen.blit(start_img, (275, 500))
            start_img = menu_font.render("Quit", True, [0, 0, 0])
            screen.blit(start_img, (275, 650))
            if menu_poz == 1:
                pygame.draw.rect(screen, (0, 0, 0), (250, 175, 880, 115), 10, 25)
            if menu_poz == 2:
                pygame.draw.rect(screen, (0, 0, 0), (250, 325, 710, 115), 10, 25)
            if menu_poz == 3:
                pygame.draw.rect(screen, (0, 0, 0), (250, 475, 570, 115), 10, 25)
            if menu_poz == 4:
                pygame.draw.rect(screen, (0, 0, 0), (250, 625, 270, 115), 10, 25)

        pygame.time.delay(100)
    else:

        if prologue:
            cd0 += 1
            if cd0 > 0 and cd0 < 500:
                text0 = True
            if cd0 > 200:
                text00 = True
            pressed_keys = pygame.key.get_pressed()
            if cd0 > 10 and pressed_keys[K_SPACE]:
                cd0 = 500
            if cd0 > 500:
                text0 = False
                text00 = False
                room = 1
                player_object.pos_x = 950
                player_object.pos_y = 299
                player_object.vel = 2
                c = 0
                cd0 = 0
                edead1 = False
                edead2 = False
                edead3 = False
                prologue = False
                reset_room()
        else:
            timer += 1
        if edead1 and edead2 and edead3 and room == 1:
            for g in boss_doors:
                g.open = True
                g.set_colorg()

        dv = pygame.sprite.spritecollide(player_object, doors, 0)
        for d in dv:
            if d.open:
                room = d.roomn
                reset_room()
        dg = pygame.sprite.spritecollide(player_object, boss_doors, 0)
        for g in dg:
            if g.open:
                room = g.roomn
                reset_room()

        if end_game:
            timer_end += 1
            cd5 += 1
            player_object.movement()
            if cd5 > 0 and cd5 < 2000:
                if cd5 % 100 == 0:
                    for i in range(1):
                        enemy_h = enemy_human.EnemyH(player_object)
                        enemies.add(enemy_h)
                        all.add(enemy_h)
                        enemyH_group.add(enemy_h)
                        enemyH_group.velo = random.randint(5, 10)/10

            if cd5 > 2000 and cd5 < 4000:
                if cd5 % 80 == 0:
                    for i in range(1):
                        enemy_h = enemy_human.EnemyH(player_object)
                        enemies.add(enemy_h)
                        all.add(enemy_h)
                        enemyH_group.add(enemy_h)
                        enemyH_group.velo = random.randint(10, 15)/10

            if cd5 > 4000 and cd5 < 6000:
                if cd5 % 70 == 0:
                    for i in range(1):
                        enemy_h = enemy_human.EnemyH(player_object)
                        enemies.add(enemy_h)
                        all.add(enemy_h)
                        enemyH_group.add(enemy_h)
                        enemyH_group.velo = random.randint(15, 20)/10

            if cd5 > 6000 and cd5 < 8000:
                if cd5 % 65 == 0:
                    for i in range(1):
                        enemy_h = enemy_human.EnemyH(player_object)
                        enemies.add(enemy_h)
                        all.add(enemy_h)
                        enemyH_group.add(enemy_h)
                        enemyH_group.velo = random.randint(20, 25)/10

            if cd5 > 8000 and cd5 < 10000:
                if cd5 % 60 == 0:
                    for i in range(1):
                        enemy_h = enemy_human.EnemyH(player_object)
                        enemies.add(enemy_h)
                        all.add(enemy_h)
                        enemyH_group.add(enemy_h)
                        enemyH_group.velo = random.randint(30, 35)/10

            if cd5 > 10000:
                if cd5 % 50 == 0:
                    for i in range(1):
                        enemy_h = enemy_human.EnemyH(player_object)
                        enemies.add(enemy_h)
                        all.add(enemy_h)
                        enemyH_group.add(enemy_h)
                        enemyH_group.velo = random.randint(30, 30)/10

        show_room()

        y = player_object.get_pos_y()
        x = player_object.get_pos_x()

        c += cd
        if c == 15 or c == 16:
            c = 0

        pressed_key = pygame.key.get_pressed()

        if pressed_key[K_w] and c == 0:
            p = Projektil(player_object.pos_x, player_object.pos_y - 30, 1 * random.randint(-40, 40)/100, -10)
            bullets.add(p)
            all.add(p)
        else:
            if pressed_key[K_s] and c == 0:
                p = Projektil(player_object.pos_x, player_object.pos_y - player_object.size_y/2 - 30, 1 * random.randint(-40, 40)/100, 10)
                bullets.add(p)
                all.add(p)
            else:
                if pressed_key[K_d] and c == 0:
                    p = Projektil(player_object.pos_x - player_object.size_x / 2, player_object.pos_y - player_object.size_y/2, 10, 1 * random.randint(-40, 40)/100,)
                    bullets.add(p)
                    all.add(p)
                else:
                    if pressed_key[K_a] and c == 0:
                        p = Projektil(player_object.pos_x - player_object.size_x / 2, player_object.pos_y - player_object.size_y/2 - 30, -10, 1 * random.randint(-40, 40)/100)
                        bullets.add(p)
                        all.add(p)

        t = pygame.sprite.groupcollide(enemies, bullets, 0, 1)

        if t:
            sound_fx.play()

        if len(t) > 0:
            for b in t:
                b.hpl()

        if edead1:
            for l in bullets:
                l.increase_bsize()
        if len(enemies) == 0:
            if room == 1:
                cd1 += 1
                if cd1 > 0 and cd1 < 500:
                    text1 = True
                pressed_keys = pygame.key.get_pressed()
                if cd1 > 200:
                    text01 = True
                if pressed_keys[K_SPACE]:
                    cd1 = 500
                if cd1 > 500:
                    for d in doors:
                        d.open = True
                        d.set_colorg()
                        text1 = False
                        text01 = False
            if room == 2:
                cd2 += 1
                if cd2 > 0 and cd2 < 500:
                    text2 = True
                if cd2 > 200:
                    text02 = True
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_SPACE]:
                    cd2 = 500
                if cd2 > 500:
                    for d in doors:
                        d.open = True
                        d.set_colorg()
                        text2 = False
                        text02 = False
            if room == 3:

                cd3 += 1
                if cd3 > 0 and cd3 < 500:
                    text3 = True
                if cd3 > 200:
                    text03 = True
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_SPACE]:
                    cd3 = 500
                if cd3 > 500:
                    for d in doors:
                        d.open = True
                        d.set_colorg()
                        text3 = False
                        text03 = False
            if room == 4:
                if bossspawn:
                    cd4 += 1
                    if cd4 == 1:
                        timer_adv = timer
                    if cd4 > 0 and cd4 < 500:
                        text4 = True
                    if cd4 > 200:
                        text04 = True
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_SPACE]:
                        cd4 = 500
                    if cd4 > 500:
                        text4 = False
                        end_game = True
                        text04 = False
            if room == 1:
                edead1 = True
            if room == 2:
                edead2 = True
                player_object.vel = 4
            if room == 3:
                edead3 = True
                cd = 2

        if end_game:
            if pygame.sprite.spritecollideany(player_object, enemies):
                end = True
        else:
            if pygame.sprite.spritecollideany(player_object, enemies):
                menu_aktivne = True
                print("fuck")
                room = 0
                reset_room()

            if pygame.sprite.spritecollideany(player_object, enemies_bullets):
                menu_aktivne = True
                room = 0
                reset_room()
                print("fuck")

        if end:
            cde += 1
            if cde == 1:
                endtime = timer_end
            if cde > 1 and cde < 500:
                texte = True
            if cde > 200:
                text0e = True
            if cde > 500:
                menu_aktivne = True
                texte = False
                text0e = False
                end = False
                room = 0
                reset_room()
                end_game = False

        all.update()
        # for en in enemies:
        #     en.update_pos(x, y)

        all.draw(screen)
        if text0:
            screen.fill((0, 0, 0))
            prologue_text = text_font.render("You are a human and your role is to....... ", True, [255, 255, 255])
            screen.blit(prologue_text, (500, 550))
        if text00:
            prologue_text2 = text_font.render("kill the GOD OF THE SKY ZEUS", True, [255, 255, 255])
            screen.blit(prologue_text2, (450, 650))

        if text1:
            pU1_text = text_font.render("You feel more powerful.....", True, [255, 255, 255])
            screen.blit(pU1_text, (500, 550))
        if text01:
            pU1_text2 = text_font.render("As if you could shoot larger BALLS", True, [255, 255, 255])
            screen.blit(pU1_text2, (450, 650))

        if text2:
            pU1_text = text_font.render("You feel a bit lighter......", True, [255, 255, 255])
            screen.blit(pU1_text, (600, 550))
        if text02:
            pU1_text2 = text_font.render("As if you could fly", True, [255, 255, 255])
            screen.blit(pU1_text2, (650, 650))
        if text3:
            pU1_text = text_font.render("You feel full of energy......", True, [255, 255, 255])
            screen.blit(pU1_text, (550, 550))
        if text03:
            pU1_text2 = text_font.render("As if you could shoot faster", True, [255, 255, 255])
            screen.blit(pU1_text2, (550, 650))
        if text4:
            EZ_text = text_font.render("You've beaten the GOD......", True, [255, 255, 255])
            EZ_text3 = text_font.render("It took you: " + str(timer_adv/100) + " seconds", True, [255, 255, 255])
            screen.blit(EZ_text, (550, 550))
            screen.blit(EZ_text3, (550, 750))
        if text04:
            EZ_text2 = text_font.render("But you have became one!!!", True, [255, 255, 255])
            screen.blit(EZ_text2, (550, 650))
        if texte:
            screen.fill((0, 0, 0))
            endtext = text_font.render("You died.....", True, [255, 255, 255])
            screen.blit(endtext, (500, 550))
            endtext3 = text_font.render("You survived: " + str(endtime/100) + " seconds", True, [255, 255, 255])
            screen.blit(endtext3, (450, 150))
        if text0e:
            endtext2 = text_font.render("But GODS do not die...", True, [255, 255, 255])
            screen.blit(endtext2, (500, 650))

        var += 0.5

    pygame.display.flip()

    clock.tick(100)


pygame.quit()