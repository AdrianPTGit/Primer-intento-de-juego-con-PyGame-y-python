import pygame

class BalaEnemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 255, 0))  # amarillo
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad = 7

    def update(self):
        self.rect.y += self.velocidad  # se mueve hacia abajo
        if self.rect.top > 600:  # si sale de pantalla
            self.kill()