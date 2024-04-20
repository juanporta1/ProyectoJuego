import pygame
import consts
from character import Character

pygame.init()
player = Character(x = 50, y = 50)

window = pygame.display.set_mode((consts.WIDTH_WINDOW, consts.HEIGHT_WINDOW))
pygame.display.set_caption("Juego")
run = True

while run:
    
    player.draw(window)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
            
    pygame.display.update()
pygame.quit()