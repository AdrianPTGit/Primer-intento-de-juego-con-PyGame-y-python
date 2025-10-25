import pygame
from settings import *
from BalaEnemigo import *

class enemigo_2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((100,100))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad = 7 
        self.direccion = -1
        
        # Atributos
        self.velocidad = 4
        self.direccion = 1
        self.vida = 5  # 💖 enemigo con 3 vidas
        
    def update(self):
        # Mover horizontalmente
        self.rect.x += self.velocidad * self.direccion
            
        # Cambiar de direccion si toca los bordes de la pantalla
        if self.rect.right >= WIDTH: # Limite derecho (WIDTH)
            self.direccion = -1
        elif self.rect.left <= 0:   # Limite izquierdo
            self.direccion = 1
    
    def recibir_daño(self, cantidad):
        """Resta vida al enemigo y lo elimina si llega a 0."""
        self.vida -= cantidad
        if self.vida <= 0:
            self.kill()  # elimina el sprite del grupo
    
    def disparar(self, grupo_balas_enemigo):
        bala = BalaEnemigo(self.rect.centerx, self.rect.bottom)
        grupo_balas_enemigo.add(bala)