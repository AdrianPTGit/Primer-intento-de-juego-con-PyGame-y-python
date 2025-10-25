import pygame

#from mi_juego_pygame.src.main import jugador, enemigos, balas
from settings import *
from player import Player
from Enemigo import Enemigo
from Enemigo_2 import *

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

def colisiones_balas_enemigos(jugador, enemigos, balas):
    # Detecta colisiones pero NO elimina al enemigo automáticamente
    impactos = pygame.sprite.groupcollide(enemigos, balas, False, True)

    for enemigo, lista_balas in impactos.items():
        for bala in lista_balas:
            # Si el enemigo tiene atributo vida, le restamos 1
            if hasattr(enemigo, "vida"):
                enemigo.vida -= 1
                if enemigo.vida <= 0:
                    enemigo.kill()
                    # 💰 Sumar puntos según tipo de enemigo
                    if isinstance(enemigo, enemigo_2):
                        jugador.puntos += 30
                    else:
                        jugador.puntos += 10
            else:
                # Si no tiene atributo vida, se comporta como antes
                enemigo.kill()
                jugador.puntos += 10


def generar_enemigos(num_enemigos, velocidad):
    nuevos_enemigos = pygame.sprite.Group()
    for i in range(num_enemigos):
        x = 100 + i * 200  # separa los enemigos horizontalmente
        y = 100
        e = enemigo_2(x, y)
        e.velocidad = velocidad  # ajusta la velocidad
        nuevos_enemigos.add(e)
    return nuevos_enemigos