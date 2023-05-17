# SFONDO MOBILE

import pygame
import pygame as py
import math

clock = py.time.Clock()
FrameHeight = 600
FrameWidth = 1200
navicella = py.image.load('navicella.png')
navicella = py.transform.scale(navicella, (100, 100))
x = 10
y = 50
# finestra
py.display.set_caption("sfondo scorrevole infinito")
screen = py.display.set_mode((FrameWidth, FrameHeight))
# immagine
bg = py.image.load("sfondo.jpg").convert()
# punto di partenza dello scroll
scroll = 0
# calcolo per la ripetizione dei blocchi dello sfondo
tiles = math.ceil(FrameWidth / bg.get_width()) + 1
# blocco principale
while 1:
    # imposto la velocità
    clock.tick(33)
    # append i quadrati di immagine
    i = 0
    while (i < tiles):
        screen.blit(bg, (bg.get_width() * i
                         + scroll, 0))
        i += 1
    # scroll
    scroll -= 6
    # reset dello scroll
    if abs(scroll) > bg.get_width():
        scroll = 0
    # fine dello scroll
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()
    screen.blit(navicella, (y, x))
    py.display.update()
py.quit()
