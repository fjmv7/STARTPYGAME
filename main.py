import pygame
import constantes
from personaje import personaje

player = personaje(50, 50)

pygame.init()
ancho = constantes.ANCHO_VENTANA
alto = constantes.ALTO_VENTANA

ventana = pygame.display.set_mode((ancho, alto))

pygame.display.set_caption("mi primer juego")
run = True

while run:

    player.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.k_a:
                print("izquierda")
            if event.key == pygame.k_d:
                print("izquierda")
            if event.key == pygame.k_w:
                print("arriba")
            if event.key == pygame.k_s:
                print("abajo")

    pygame.display.update()

pygame.quit()
