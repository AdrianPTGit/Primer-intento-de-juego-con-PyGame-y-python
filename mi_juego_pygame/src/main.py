import pygame, sys
from pygame import font

from settings import *
from player import Player
from Enemigo import Enemigo

pygame.init()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi primer juego estructurado")
clock = pygame.time.Clock()

# --- Cargar fondo (asegúrate de hacerlo aquí, no en settings.py) ---
# --- Cargar fondo ---
print("Ruta fondo:", FONDO_PATH)
if not os.path.exists(FONDO_PATH):
    print("⚠️ No se encontró el fondo en:", FONDO_PATH  )
FONDO_PANTALLA_JUEGO = pygame.image.load(FONDO_PATH)
FONDO_PANTALLA_JUEGO = pygame.transform.scale(FONDO_PANTALLA_JUEGO, (WIDTH, HEIGHT))
# --- Fuente para el texto puntos ---
font = pygame.font.Font(None, 36)  # Fuente para el texto
# --- Crear jugador ---
jugador = Player(WIDTH // 2, HEIGHT - 60)

# --- Crear grupo de enemigos ---
enemigos = pygame.sprite.Group()
for i in range(10):
    enemigo = Enemigo(100 + i * 200, 100)
    enemigos.add(enemigo)

# --- Crear grupo de sprites (todos) ---
todos_sprites = pygame.sprite.Group()
todos_sprites.add(jugador)
todos_sprites.add(enemigos)

# --- Grupo de balas ---
balas = pygame.sprite.Group()

# --- Función de pantalla de inicio ---
def pantalla_inicio():
    font_titulo = pygame.font.Font(None, 72)
    font_opcion = pygame.font.Font(None, 48)

    running_inicio = True
    while running_inicio:
        pantalla.fill((0, 0, 0))  # Fondo negro

        # Dibujar título
        titulo = font_titulo.render("MI JUEGO PYGAME", True, (255, 255, 255))
        pantalla.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 150))

        # Dibujar opciones
        jugar_texto = font_opcion.render("JUGAR (J)", True, (0, 255, 0))
        salir_texto = font_opcion.render("SALIR (S)", True, (255, 0, 0))
        pantalla.blit(jugar_texto, (WIDTH // 2 - jugar_texto.get_width() // 2, 300))
        pantalla.blit(salir_texto, (WIDTH // 2 - salir_texto.get_width() // 2, 400))

        pygame.display.flip()
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:  # Jugar
                    running_inicio = False
                elif event.key == pygame.K_s:  # Salir
                    pygame.quit()
                    sys.exit()



    # --- Aquí empieza tu código del juego ---
    # Crear jugador, enemigos, grupos, bucle principal...

# --- Llamar a la pantalla de inicio antes de iniciar el juego ---
pantalla_inicio()
# --- Bucle principal ---
running = True
while running:
    clock.tick(FPS)

    # --- Manejar eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jugador.disparar(balas)

    # --- Actualizar sprites ---
    todos_sprites.update()
    balas.update()

    # --- Detección de colisiones ---

    # Jugador colisiona con enemigo
    colision = pygame.sprite.spritecollide(jugador, enemigos, False)
    if colision:
        jugador.vidas -= 1  # resta una vida
        print(f"¡Jugador tocado! Vidas: {jugador.vidas}")
        if jugador.vidas <= 0:
            print("¡Juego terminado!")
            running = False  # termina el juego
        else:
            # opcional: reposicionar jugador para no perder varias vidas de golpe
            jugador.rect.center = (WIDTH // 2, HEIGHT - 60)

    # 2️⃣ Bala impacta enemigo
    impactos = pygame.sprite.groupcollide(enemigos, balas, True, True)
    if impactos:
        for enemigo in impactos:
            jugador.puntos += 10  # 🔥 suma 10 puntos por enemigo destruido
        print(f"🔥 ¡Enemigo destruido! Puntos: {jugador.puntos}")



    # --- Dibujar en pantalla ---
    pantalla.blit(FONDO_PANTALLA_JUEGO, (0, 0))
    todos_sprites.draw(pantalla)
    balas.draw(pantalla)

    # --- Dibujar puntuación ---

    texto_puntos = font.render(f"Puntos: {jugador.puntos}", True, (255, 255, 255))
    pantalla.blit(texto_puntos, (10, 10))

    # --- Dibujar vidas ---

    texto_puntos = font.render(f"Vidas: {jugador.vidas}", True, (255, 255, 255))
    pantalla.blit(texto_puntos, (200, 10))
    pygame.display.flip()

pygame.quit()
sys.exit()