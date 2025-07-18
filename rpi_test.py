#!/usr/bin/python3

# git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
# cd Adafruit_Python_ADS1x15
# sudo python3 setup.py install

import pkg_resources
import pygame

required = {'rpi.gpio'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

JE_RPI = len(missing) == 0

if JE_RPI:
    print('RPI')
    # tlacitka
    import RPi.GPIO as GPIO

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # pinout
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # 11
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # 13
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # 15
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # 16
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # 18

    # joystick
    import Adafruit_ADS1x15
    adc = Adafruit_ADS1x15.ADS1115()

# inicializacia
pygame.init()

# casovanie
hodiny = pygame.time.Clock()

# vytvor okno
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("pygame priklad")

# game loop
running = True
while running:
    # spracuj udalosti
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

    # rpi
    if JE_RPI:
        if GPIO.input(17) == GPIO.LOW:
            print('dolava')
        if GPIO.input(22) == GPIO.LOW:
            print('doprava')
        if GPIO.input(27) == GPIO.LOW:
            print('hore')
        if GPIO.input(23) == GPIO.LOW:
            print('dole')
        if GPIO.input(24) == GPIO.LOW:
            print('joystick')

        values = [0]*4
        for i in range(4):
            values[i] = adc.read_adc(i, gain=1)
        print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))

    # vymaz obrazovku
    screen.fill((255, 255, 255))

    # kresli daco
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # doublebuffer
    pygame.display.flip()

    # pockaj kolko treba
    hodiny.tick(10)     # FPS

# koniec
pygame.quit()
