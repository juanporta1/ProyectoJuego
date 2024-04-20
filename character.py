import pygame

class Character():
    
    def __init__(self, x, y):
        self.shape = pygame.Rect(0, 0 , 20, 20)
        self.shape.center = (x, y)
        
    def draw(self, window):
        pygame.draw.rect(window, (255,255,0), self.shape)