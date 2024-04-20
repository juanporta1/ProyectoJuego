import pygame
import consts
from character import Character

pygame.init()
window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("Juego")


character_walk_sprites = []

def scale_image(image, scale):
    width = image.get_width()
    height = image.get_height()
    new_image = pygame.transform.scale(image,( width * scale, height * scale))
    return new_image    

for i in range(6):
    image = pygame.image.load(f"assets//images//characters//player//walk//Player_Walk_{i}.png")
    image = scale_image(image,consts.CHARACTER_SCALE)
    character_walk_sprites.append(image)

player_image = pygame.image.load("assets//images//characters//player//walk//Player_Walk_0.png")
player_image = scale_image(player_image,consts.CHARACTER_SCALE)
#Controlar el frame rate
clock = pygame.time.Clock()
#Definicion de variables

player = Character(x = 100,
                   y = 100,
                   animation_sprites=character_walk_sprites)
run = True
move_left = False
move_right = False
move_up = False
move_down = False    

while run:
    window.fill(consts.WINDOW_COLORBG)
    
    clock.tick(consts.FPS)

    delta_x = 0
    delta_y = 0
    
    #COntrolar movimiento del jugador
    if move_left == True:
        delta_x = -consts.CHARACTER_VELOCITY
    elif move_right == True:
        delta_x = consts.CHARACTER_VELOCITY
    
    if move_up == True:
        delta_y = -consts.CHARACTER_VELOCITY
    elif move_down == True:
        delta_y = consts.CHARACTER_VELOCITY
    
    player.draw(window)
    player.move(delta_x, delta_y)
    player.update_animation()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False
            
    pygame.display.update()
pygame.quit()