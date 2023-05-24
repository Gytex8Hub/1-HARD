# SFONDO MOBILE

import pygame
import pygame as py
import math
import sys

from pygame import Surface, SurfaceType

clock = py.time.Clock()
FrameHeight = 600
FrameWidth = 1200
navicella = py.image.load('navicella.jpg ')
navicella = py.transform.scale(navicella, (100, 100))
x = 10
y = 50
# finestra
py.display.set_caption("sfondo scorrevole infinito")
screen = py.display.set_mode((FrameWidth, FrameHeight))
# immagine


bg = py.image.load('../pythonProject2/sfondo.jpg')
pi = py.transform.scale(bg, (1200, 600))
# punto di partenza dello scroll
scroll = 0
# calcolo per la ripetizione dei blocchi dello sfondo
tiles = math.ceil(FrameWidth / pi.get_width()) + 1
# blocco principale

x2 = 10
y2 = 50

while 1:
    # imposto la velocità
    clock.tick(30)
    # append i quadrati di immagine
    i = 0
    while (i < tiles):
        screen.blit(pi, (pi.get_width() * i
                         + scroll, 0))
        i += 1
    # scroll
    scroll -= 6
    # reset dello scroll
    if abs(scroll) > pi.get_width():
        scroll = 0
    # fine dello scroll
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()
    screen.blit(navicella, (x, y))
    py.display.update()



    pi.blit(navicella, (x2, y2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()  # checking pressed keys

    if keys[pygame.K_UP]:
        if y2 > 0:
            y2 -= 1
    if keys[pygame.K_DOWN]:
        if y2 < 500:
            y2 += 1




    pygame.display.update()
    #py.quit()