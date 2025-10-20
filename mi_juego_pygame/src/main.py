import pygame, sys
from settings import *
from player import Player
from Enemigo import Enemigo
from fuciones_juego import *

pygame.init()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Attack")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# --- Cargar fondo ---
FONDO_PANTALLA_JUEGO = pygame.image.load(FONDO_PATH)
FONDO_PANTALLA_JUEGO = pygame.transform.scale(FONDO_PANTALLA_JUEGO, (WIDTH, HEIGHT))

# --- Función de pantalla de inicio ---
def pantalla_inicio():
    font_titulo = pygame.font.Font(None, 72)
    font_opcion = pygame.font.Font(None, 48)
    running_inicio = True

    while running_inicio:
        pantalla.fill((0,0,0))
        titulo = font_titulo.render("Cosmic Attack", True, (255,255,255))
        pantalla.blit(titulo, (WIDTH//2 - titulo.get_width()//2, 150))
        jugar_texto = font_opcion.render("JUGAR (J)", True, (0,255,0))
        salir_texto = font_opcion.render("SALIR (S)", True, (255,0,0))
        pantalla.blit(jugar_texto, (WIDTH//2 - jugar_texto.get_width()//2, 300))
        pantalla.blit(salir_texto, (WIDTH//2 - salir_texto.get_width()//2, 400))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    running_inicio = False
                elif event.key == pygame.K_s:
                    pygame.quit()
                    sys.exit()

# --- Bucle externo que controla reinicios ---
running = True
while running:
    pantalla_inicio()  # Mostrar pantalla de inicio
    jugador, enemigos, todos_sprites, balas = inicializar_juego()

    juego_activo = True
    while juego_activo:
        clock.tick(FPS)
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego_activo = False
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jugador.disparar(balas)

        # Actualizar
        todos_sprites.update()
        balas.update()

        # Colisiones jugador-enemigos
        colision = pygame.sprite.spritecollide(jugador, enemigos, False)
        if colision:
            jugador.vidas -= 1
            if jugador.vidas <= 0:
                juego_activo = False  # termina partida
            else:
                jugador.rect.center = (WIDTH//2, HEIGHT-60)

        # Colisiones balas-enemigos
        impactos = pygame.sprite.groupcollide(enemigos, balas, True, True)
        for enemigo in impactos:
            jugador.puntos += 10

        # Dibujar
        pantalla.blit(FONDO_PANTALLA_JUEGO, (0,0))
        todos_sprites.draw(pantalla)
        balas.draw(pantalla)
        pantalla.blit(font.render(f"Puntos: {jugador.puntos}", True, (255,255,255)), (10,10))
        pantalla.blit(font.render(f"Vidas: {jugador.vidas}", True, (255,255,255)), (200,10))
        pygame.display.flip()

pygame.quit()
sys.exit()