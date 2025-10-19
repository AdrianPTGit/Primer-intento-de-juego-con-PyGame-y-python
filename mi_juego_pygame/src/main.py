import pygame, sys
from settings import *
from player import Player
from Enemigo import Enemigo
from settings import FONDO_PANTALLA_JUEGO

pygame.init()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi primer juego estructurado")
clock = pygame.time.Clock()

# Crear jugador
jugador = Player(WIDTH // 2, HEIGHT // 2)

# Crear enemigo
enemigo = Enemigo(WIDTH // 2, HEIGHT // 4)  # Cambié Y para que no esté encima del jugador

# Crear grupo de sprites y añadir ambos
todos_sprites = pygame.sprite.Group()
todos_sprites.add(jugador)
todos_sprites.add(enemigo)

# Grupo de balas
balas = pygame.sprite.Group()


# Bucle principal
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Disparar al presionar espacio
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jugador.disparar(balas)

    # Actualizar todos los sprites            
    todos_sprites.update()
    balas.update()

    # Dibujar en pantalla
    pantalla.blit(FONDO_PANTALLA_JUEGO, (0, 0))
    todos_sprites.draw(pantalla)
    balas.draw(pantalla)

    pygame.display.flip()

pygame.quit()
sys.exit()
