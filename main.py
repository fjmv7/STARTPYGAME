import pygame
import constantes
from personaje import Personaje

pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Mi Primer Juego")

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# Creación del personaje
player = Personaje(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2)

# Variables de movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# Bucle principal del juego
run = True
while run:
    # Control de FPS
    reloj.tick(constantes.FPS)
    
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Detección de teclas presionadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
        
        # Detección de teclas liberadas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
    
    # Cálculo del movimiento
    delta_x = 0
    delta_y = 0
    
    if mover_derecha:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo:
        delta_y = constantes.VELOCIDAD
    
    # Aplicar movimiento
    player.movimiento(delta_x, delta_y)
    
    # Dibujar
    ventana.fill(constantes.COLOR_BG)
    player.dibujar(ventana)
    
    # Actualizar pantalla
    pygame.display.update()

pygame.quit()