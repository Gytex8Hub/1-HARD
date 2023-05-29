import pygame
import random
from pygame.locals import *

# Dimensioni della finestra di gioco
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Velocità di gioco
FPS = 60

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inizializzazione di Pygame
pygame.init()

# Creazione della finestra di gioco
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Gioco Pygame')

# Caricamento dello sfondo
bg = pygame.image.load('sfondo.jpg').convert()
background = pygame.transform.scale(bg, (1280, 720))

# Caricamento della navicella
navicella = pygame.image.load('navicella.png').convert_alpha()
spaceship = pygame.transform.scale(navicella, (100, 100))
spaceship_rect = spaceship.get_rect()
spaceship_rect.centerx = WINDOW_WIDTH // 2
spaceship_rect.centery = WINDOW_HEIGHT - 55


# Caricamento dell'immagine dell'asteroide
asteroide = pygame.image.load('asteroide.png').convert_alpha()
asteroid_image = pygame.transform.scale(asteroide, (100, 100))

# Lista degli asteroidi
asteroids = []

# Variabile per il movimento della navicella
move_left = False
move_right = False
move_up = False
move_down = False

# Funzione per generare un nuovo asteroide
def create_asteroid():
    x = random.randint(0, WINDOW_WIDTH)
    y = random.randint(-200, -50)
    speed = random.randint(2, 6)
    asteroid_rect = asteroid_image.get_rect()
    asteroid_rect.centerx = x
    asteroid_rect.centery = y
    return {
        'rect': asteroid_rect,
        'speed': speed
    }

# Funzione per disegnare gli asteroidi
def draw_asteroids():
    for asteroid in asteroids:
        window.blit(asteroid_image, asteroid['rect'])

# Funzione per controllare le collisioni tra la navicella e gli asteroidi
def check_collision():
    for asteroid in asteroids:
        if spaceship_rect.colliderect(asteroid['rect']):
            return True
    return False

# Orologio per controllare gli FPS del gioco
clock = pygame.time.Clock()


# Ciclo di gioco
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_left = True
            elif event.key == K_RIGHT:
                move_right = True
            elif event.key == K_UP:
                move_up = True
            elif event.key == K_DOWN:
                move_down = True
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_left = False
            elif event.key == K_RIGHT:
                move_right = False
            elif event.key == K_UP:
                move_up = False
            elif event.key == K_DOWN:
                move_down = False

    # Movimento della navicella
    if move_left and spaceship_rect.left > 0:
        spaceship_rect.x -= 5
    if move_right and spaceship_rect.right < WINDOW_WIDTH:
        spaceship_rect.x += 5
    if move_up and spaceship_rect.top > 0:
        spaceship_rect.y -= 5
    if move_down and spaceship_rect.bottom < WINDOW_HEIGHT:
        spaceship_rect.y += 5

    # Aggiornamento degli asteroidi
    for asteroid in asteroids:
        asteroid['rect'].y += asteroid['speed']
        if asteroid['rect'].top > WINDOW_HEIGHT:
            asteroids.remove(asteroid)

    # Generazione di nuovi asteroidi
    if random.randint(0, 100) < 5:
        asteroids.append(create_asteroid())

    # Controllo delle collisioni
    if check_collision():
        running = False
        testo = pygame.image.load('testo.png').convert_alpha()
        gameover = pygame.transform.scale(testo, (500, 500))
        gameover_rect = gameover.get_rect()
        gameover_rect.centerx = WINDOW_WIDTH // 2
        gameover_rect.centery = WINDOW_HEIGHT // 2
        pygame.time.wait(5000)

    # Disegno dei componenti
    window.blit(background, (0, 0))
    draw_asteroids()
    window.blit(spaceship, spaceship_rect)

    # Aggiornamento della finestra di gioco
    pygame.display.update()

    # Limitazione degli FPS
    clock.tick(FPS)

pygame.display.flip()


# Chiusura del gioco
pygame.quit()


