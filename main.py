import pygame
import consts
from character import Character
import assets
import copy

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

player = Character(x = 20,
                   y = 380,
                   animation_sprites=character_walk_sprites)

enemy = Character(x = 300,
                    y = 100,
                    animation_sprites=character_walk_sprites)

run = True
move_left = False
move_right = False
move_up = False
move_down = False    

def move(player):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and player.shape.x - 1 > 0:
            player.shape.x -= consts.CHARACTER_VELOCITY
    
    if keys[pygame.K_d] and player.shape.x + 1 < window.get_size()[0] - player.shape.width:
            player.shape.x += consts.CHARACTER_VELOCITY
        
    if keys[pygame.K_w] and player.shape.y - 1 > 0:
        player.shape.y -= consts.CHARACTER_VELOCITY 
        
    if keys[pygame.K_s] and player.shape.y + 1 < window.get_size()[1] - player.shape.height - 200:
        player.shape.y += consts.CHARACTER_VELOCITY 
        
enemy = Character(x = 300,
                  y= 100,
                  animation_sprites=character_walk_sprites)

piso = pygame.Rect(0,400, 800,200)

while run:
    window.blit(assets.parallax_bg, (0,0))
    
    clock.tick(consts.FPS)
    
    player.draw(window,(255,255,0))
    player.update_animation()
    enemy.draw(window,(0,0,0))
    enemy.update_animation()
    pygame.draw.rect(surface=window,color=(0,0,0),rect=piso)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            
    move(player)    
            
    pygame.display.update()
pygame.quit()