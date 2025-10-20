import pygame
# Importa la librería Pygame para manejar gráficos, sprites y eventos de teclado
from bala import Bala
from settings import *

# Definimos la clase Player, que hereda de pygame.sprite.Sprite
# Esto permite que el jugador sea un "sprite" y pueda ser manejado por grupos de sprites
class Player(pygame.sprite.Sprite):
    # Método constructor que se ejecuta al crear una instancia de Player
    def __init__(self, x, y):
        super().__init__()  # Llama al constructor de la clase Sprite
        self.image = pygame.Surface((40, 40))  # Crea una superficie de 40x40 píxeles que representará al jugador
        self.image.fill((255, 0, 0))  # Rellena la superficie con color rojo (RGB)
        self.rect = self.image.get_rect()  # Obtiene un rectángulo que delimita la superficie (útil para colisiones y posición)
        self.rect.center = (x, y)  # Posiciona el centro del rectángulo en las coordenadas (x, y) que recibimos
        self.velocidad = 5  # Velocidad de movimiento del jugador en píxeles por frame

        self.puntos = 0  # <-- NUEVO atributo de puntuación


    # Método update se llama automáticamente cada frame cuando usamos un grupo de sprites
    def update(self):
        keys = pygame.key.get_pressed()  # Obtiene un diccionario con el estado de todas las teclas
        if keys[pygame.K_LEFT]:  # Si la tecla de flecha izquierda está presionada
            self.rect.x -= self.velocidad  # Mueve el rectángulo del jugador a la izquierda
        if keys[pygame.K_RIGHT]:  # Si la tecla de flecha derecha está presionada
            self.rect.x += self.velocidad  # Mueve el rectángulo del jugador a la derecha
        if keys[pygame.K_UP]:  # Si la tecla de flecha arriba está presionada
            self.rect.y -= self.velocidad  # Mueve el rectángulo del jugador hacia arriba
        if keys[pygame.K_DOWN]:  # Si la tecla de flecha abajo está presionada
            self.rect.y += self.velocidad  # Mueve el rectángulo del jugador hacia abajo

            # --- Limitar movimiento a los bordes de la pantalla ---
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    # Método para disparar
    def disparar(self, grupo_balas):
        # Crea una bala en la posición superior del jugador
        bala = Bala(self.rect.centerx, self.rect.top)
        grupo_balas.add(bala)

