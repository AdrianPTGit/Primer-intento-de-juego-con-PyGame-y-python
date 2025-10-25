import pygame, sys
from Enemigo_2 import enemigo_2
from settings import *
from player import Player
from Enemigo import Enemigo
from fuciones_juego import *
import BalaEnemigo 

pygame.init()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Attack")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# --- Cargar fondo ---
FONDO_PANTALLA_JUEGO = pygame.image.load(FONDO_PATH)
FONDO_PANTALLA_JUEGO = pygame.transform.scale(FONDO_PANTALLA_JUEGO, (WIDTH, HEIGHT))

# Velocidad base de los enemigos
velocidad_enemigos = 4
# Número de enemigos por oleada
num_enemigos = 2


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
    
    # Crear dos enemigos tipo 2
    enemigo2_1 = enemigo_2(300, 200)  # posición del primer enemigo
    enemigo2_2 = enemigo_2(700, 200)  # posición del segundo enemigo

    # Agregarlos a los grupos
    enemigos.add(enemigo2_1, enemigo2_2)
    todos_sprites.add(enemigo2_1, enemigo2_2)


    # Agregarlos a los grupos
    enemigos.add(enemigo2_1, enemigo2_2)
    todos_sprites.add(enemigo2_1, enemigo2_2)

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
        colisiones_balas_enemigos(jugador, enemigos, balas)
        
        # --- Comprobar si todos los enemigos han muerto ---
        if len(enemigos) == 0:
            # Aumenta la velocidad para la siguiente oleada
            velocidad_enemigos += 1
            # Aumenta la cantidad de enemigos si quieres
            num_enemigos += 1
            # Genera nuevos enemigos
            nuevos = generar_enemigos(num_enemigos, velocidad_enemigos)
            enemigos.add(nuevos)
            todos_sprites.add(nuevos)
        # Grupos
        balas_enemigos = pygame.sprite.Group()

        # Dentro del bucle principal de juego
        for enemigo in enemigos:
        # Por ejemplo dispara cada 60 frames
            if pygame.time.get_ticks() % 1000 < 20:  # cada segundo aprox.
                if isinstance(enemigo, enemigo_2):
                    enemigo.disparar(balas_enemigos)

        # Actualizar balas de enemigos
        balas_enemigos.update()

        # Dibujar balas de enemigos
        balas_enemigos.draw(pantalla)

        # Colisión con jugador
        if pygame.sprite.spritecollide(jugador, balas_enemigos, True):
            jugador.vidas -= 1


        
        # Dibujar
        pantalla.blit(FONDO_PANTALLA_JUEGO, (0,0))
        todos_sprites.draw(pantalla)
        balas.draw(pantalla)
        pantalla.blit(font.render(f"Puntos: {jugador.puntos}", True, (255,255,255)), (10,10))
        pantalla.blit(font.render(f"Vidas: {jugador.vidas}", True, (255,255,255)), (200,10))
        pygame.display.flip()
    
pygame.quit()
sys.exit()


######################################## ver tema balas enemigos