import pygame
import os
# Configuración general del juego

# Dimensiones de la ventana
WIDTH = 1280
HEIGHT = 720

# FPS
FPS = 60

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Ruta de la imagen de fondo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONDO_PATH = os.path.join(BASE_DIR, "assets", "images", "image5.jpg")