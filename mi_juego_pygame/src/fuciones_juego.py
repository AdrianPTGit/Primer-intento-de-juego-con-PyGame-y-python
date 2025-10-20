import pygame
from settings import *
from player import Player
from Enemigo import Enemigo

def inicializar_juego():
    jugador = Player(WIDTH // 2, HEIGHT - 60)

    enemigos = pygame.sprite.Group()
    for i in range(10):
        enemigo = Enemigo(100 + i * 200, 100)
        enemigos.add(enemigo)

    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jugador)
    todos_sprites.add(enemigos)

    balas = pygame.sprite.Group()

    return jugador, enemigos, todos_sprites, balas