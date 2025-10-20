import pygame, sys
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

# --- Crear jugador ---
jugador = Player(WIDTH // 2, HEIGHT - 60)

# --- Crear grupo de enemigos ---
enemigos = pygame.sprite.Group()
for i in range(3):
    enemigo = Enemigo(100 + i * 200, 100)
    enemigos.add(enemigo)

# --- Crear grupo de sprites (todos) ---
todos_sprites = pygame.sprite.Group()
todos_sprites.add(jugador)
todos_sprites.add(enemigos)

# --- Grupo de balas ---
balas = pygame.sprite.Group()

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

    # 1️⃣ Jugador colisiona con enemigo
    if pygame.sprite.spritecollide(jugador, enemigos, False):
        print("💥 ¡Jugador tocado por enemigo!")
        running = False  # o podrías restar vida, reiniciar, etc.

    # 2️⃣ Bala impacta enemigo
    impactos = pygame.sprite.groupcollide(enemigos, balas, True, True)
    if impactos:
        print("🔥 ¡Enemigo destruido!")

    # --- Dibujar en pantalla ---
    pantalla.blit(FONDO_PANTALLA_JUEGO, (0, 0))
    todos_sprites.draw(pantalla)
    balas.draw(pantalla)

    pygame.display.flip()

pygame.quit()
sys.exit()