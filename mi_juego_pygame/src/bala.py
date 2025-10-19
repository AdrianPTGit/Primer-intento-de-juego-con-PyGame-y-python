import pygame

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))  # Tamaño de la bala
        self.image.fill((255, 255, 0))        # Color amarillo
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)             # Comenzar desde la posición del jugador
        self.velocidad = -10                   # Negativo para subir en pantalla (y disminuye)

    def update(self):
        self.rect.y += self.velocidad         # Mover la bala
        # Si sale de la pantalla, eliminar la bala
        if self.rect.bottom < 0:
            self.kill()