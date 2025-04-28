import pygame
import constantes

class Personaje:
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, constantes.COLOR, self.forma)
    
    def movimiento(self, delta_x, delta_y):
        # Movimiento en X
        self.forma.x += delta_x
        # Movimiento en Y
        self.forma.y += delta_y
        