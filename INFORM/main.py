import pygame
import os

# inizializza pygame
pygame.init()

# dimensioni dello schermo
screen_width = 800
screen_height = 600

# imposta lo schermo
screen = pygame.display.set_mode((screen_width, screen_height))

# titolo della finestra
pygame.display.set_caption("Sfondo infinito scorrevole")

# velocià di scorrimento dello sfondo
background_speed = 1

# carica lo sfondo
background_image = pygame.image.load(os.path.join("sfondo.jpg")).convert()

# carica il personaggio
player_image = pygame.image.load(os.path.join("mario.png")).convert_alpha()

# dimensioni del personaggio
player_width = player_image.get_width()
player_height = player_image.get_height()

# posizione del personaggio
player_x = 100
player_y = 300


# funzione per disegnare lo sfondo
def draw_background(background_x):
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + screen_width, 0))


# loop del gioco
running = True
background_x = 0

while running:
    # gestione eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # movimento del personaggio
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP]:
        player_y -= 5
    if key_pressed[pygame.K_DOWN]:
        player_y += 5
    if key_pressed[pygame.K_LEFT]:
        player_x -= 5
    if key_pressed[pygame.K_RIGHT]:
        player_x += 5

    # disegna lo sfondo
    draw_background(background_x)
    background_x -= background_speed
    if background_x < -screen_width:
        background_x = 0

    # disegna il personaggio
    screen.blit(player_image, (player_x, player_y))

    # aggiorna lo schermo
    pygame.display.update()