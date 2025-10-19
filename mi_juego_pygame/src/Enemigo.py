import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.velocidad = 5
        self.direccion = 1  # 1 = derecha, -1 = izquierda

    def update(self):
        # Mover horizontalmente
        self.rect.x += self.velocidad * self.direccion

        # Cambiar de dirección si toca los bordes de la pantalla
        if self.rect.right >= 800:  # Limite derecho (WIDTH)
            self.direccion = -1
        elif self.rect.left <= 0:   # Limite izquierdo
            self.direccion = 1