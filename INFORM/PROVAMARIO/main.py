import pygame
import sys
from pygame.locals import *

pygame.init()
sfondo = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Muovere immagini')

colore = (0, 255, 255)
personaggio = pygame.image.load('supra.jpg')
#ridimensiono il personaggio
personaggio = pygame.transform.scale(personaggio, (180, 100))
x = 500
y = 150

while True:
    sfondo.fill(colore)
    sfondo.blit(personaggio, (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                print('Vai su')
                y -= 5
            elif event.key == K_DOWN:
                print('Vai giù')
                y += 5
            elif event.key == K_LEFT:
                print('Vai a sinistra')
                x -= 5
            elif event.key == K_RIGHT:
                print('Vai a destra')
                x += 5
        pygame.display.update()