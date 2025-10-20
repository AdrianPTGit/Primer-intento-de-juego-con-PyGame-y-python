
## 🧩  Instalar PyCharm Community con Snap (fácil y rápido)
1️⃣ Instala Snap (si no lo tienes)
```bash
sudo apt update
sudo apt install snapd -y
sudo systemctl enable --now snapd.socket
```
2️⃣ Instala PyCharm Community
```bash
sudo snap install pycharm-community --classic
```
3️⃣ Ejecuta PyCharm
```bash
pycharm-community
```

## 🧱 1. Crear un entorno virtual

> Es buena práctica trabajar dentro de un entorno virtual para mantener tus dependencias limpias.

- Ejecuta en la carpeta donde quieras tu proyecto (por ejemplo pygame_juego):

```bash
mkdir pygame_juego
cd pygame_juego
python3 -m venv venv
```
Luego activa el entorno:
- 🔹 Linux / macOS

```bash
source venv/bin/activate
```
- 🔹 Windows
```bash
venv\Scripts\activate
```
## 🧩 2. Instalar Pygame

Con el entorno activado, instala Pygame con pip:
```bash
pip install pygame
```

## 💻 3. Crear tu primer archivo

Crea un archivo llamado main.py con este código básico:

```python
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi primer juego con Pygame")

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.fill(NEGRO)
    pygame.draw.circle(pantalla, ROJO, (400, 300), 50)
    pygame.display.flip()


```

## 🧱 4. Estructura recomendada

Crea una carpeta llamada mi_juego_pygame con esta estructura:

```bash
mi_juego_pygame/
│
├── assets/               # Recursos del juego
│   ├── images/           # Imágenes, sprites
│   ├── sounds/           # Efectos de sonido
│   └── music/            # Música de fondo
│
├── src/                  # Código fuente
│   ├── main.py           # Punto de entrada
│   ├── settings.py       # Configuración (tamaño, FPS, colores)
│   ├── player.py         # Clase del jugador
│   ├── enemy.py          # Clase de enemigos
│   └── utils.py          # Funciones auxiliares
│
├── venv/                 # (Opcional) entorno virtual
│
└── requirements.txt      # Dependencias del proyecto
```
## ⚙️ 4.1. Crear la estructura

Si estás en Linux o macOS:
```bash
mkdir -p mi_juego_pygame/assets/{images,sounds,music} mi_juego_pygame/src
cd mi_juego_pygame
python3 -m venv venv
source venv/bin/activate
pip install pygame
echo "pygame" > requirements.txt
```
En Windows (PowerShell):
```bash
mkdir mi_juego_pygame, mi_juego_pygame\assets, mi_juego_pygame\assets\images, mi_juego_pygame\assets\sounds, mi_juego_pygame\assets\music, mi_juego_pygame\src
cd mi_juego_pygame
python -m venv venv
venv\Scripts\activate
pip install pygame
echo pygame > requirements.txt
```


# nombres juego

🎯 Clásicos / Retro

Space Blaster

Alien Invaders

Galactic Defender

Star Shooter

Cosmic Attack

⚡ Impactantes / Acción

Astro Annihilator

Alien Exterminator

Zero Gravity Assault

Meteor Strike

Orbit Obliterator

🛸 Creativos / Divertidos

Zap! Alien Wars

Martian Madness

Laser vs Aliens

Space Kaboom!

Cosmo Chaos

🌌 Épicos / Aventureros

Galaxion: The Final Battle

Star Frontier

Void Raiders

Celestial Clash

Nebula Nemesis