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

run = True
move_left = False
move_right = False
move_up = False
move_down = False    

stair = pygame.Rect(300,0,50,400)
stairs = [stair]

def detect_floor(floors,player):
    stay_floor = False
    is_floor_one = False
    if floors[0].top == player.shape.bottom:
        is_floor_one = True
        stay_floor = True
    else:
        for i in range(1,len(floors)):
            if floors[i].top == player.shape.bottom:
                stay_floor = True
    return (stay_floor,is_floor_one)

def detect_stairs(stairs,player):
    for i in stairs:    
        if player.shape.left >= i.left - 10 and player.shape.right <= i.right + 10:
            stay_stair = True
            break
        else:
            stay_stair = False
    return stay_stair

floor1 = pygame.Rect(0,400, 800,200)
floor2 = pygame.Rect(0,300, 800,30) 
floor3 = pygame.Rect(0,150, 800,30) 
floors = [floor1,floor2,floor3]
while run:
    window.blit(assets.parallax_bg, (0,0))
    
    clock.tick(consts.FPS)
    
    
    pygame.draw.rect(surface=window,color=(0,0,0),rect=floor1)
    pygame.draw.rect(surface=window,color=(0,0,0),rect=floor2)
    pygame.draw.rect(surface=window,color=(0,0,0),rect=floor3)
    pygame.draw.rect(rect=stair,color=(255,255,255),surface=window)
    
    player.draw(window,(255,255,0))
    player.update_animation()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    stay_stair = detect_stairs(stairs,player)       
    stay_floor,is_floor_one = detect_floor(floors,player)        
    
                                      
    player.move(window,stay_stair,stay_floor,is_floor_one)    
            
    pygame.display.update()
pygame.quit()