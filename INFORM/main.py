import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((400, 300))
pygame.display.set_caption('Titolo della finestra')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print("L'utente ha premuto un tasto sulla tastiera")
            if event.key == K_w:
                print("L'utente vuole andare avanti")
            if event.key == K_s:
                print("L'utente vuole andare indietro")
            if event.key == K_d:
                print("L'utente vuole andare a desta")
            if event.key == K_a:
                print("L'utente vuole andare a sinistra")
            if event.key == K_r:
                print("L'utente vuole ricaricare l'arma")
            if event.key == K_LSHIFT:
                print("L'utente si vuole accovacciare")
            if event.key == K_SPACE:
                print("L'utente vuole saltare")
    pygame.display.update()
