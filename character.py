import pygame
import consts

class Character():
    
    def __init__(self, x, y,animation_sprites):
        self.flip = False
        self.animaton_srpites = animation_sprites
        self.frame_index = 0
        self.image = animation_sprites[self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.shape = pygame.Rect(0, 0 , consts.CHARACTER_WIDTH, consts.CHARACTER_HEIGHT)
        self.shape.center = (x, y)
        self.velocity = consts.CHARACTER_VELOCITY
 

        
    def update_animation(self):
        cooldown_animation = 150
        self.image = self.animaton_srpites[self.frame_index]
        
        if (pygame.time.get_ticks() - self.update_time) >= cooldown_animation:
            if self.frame_index == len(self.animaton_srpites) - 1:
                self.frame_index = 0
            else:    
                self.frame_index += 1 
            self.update_time = pygame.time.get_ticks()
    
    def move(self,window,stair,floor, is_floor_one):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and self.shape.x - 5 > 0:
                self.shape.x -= consts.CHARACTER_VELOCITY
                self.flip = True
        
        if keys[pygame.K_d] and self.shape.x + 5 < window.get_size()[0] - self.shape.width:
                self.shape.x += consts.CHARACTER_VELOCITY
                self.flip = False
            
        if keys[pygame.K_w] and self.shape.y - 5 > 0 and stair:
            self.shape.y -= consts.CHARACTER_VELOCITY 
            
        if keys[pygame.K_s] and stair and not is_floor_one:
            self.shape.y += consts.CHARACTER_VELOCITY
        
        if not stair and not floor:
            self.shape.y += consts.CHARACTER_VELOCITY
            
        
    def draw(self, window,color):
        self.image_flip = pygame.transform.flip(self.image, flip_x=self.flip, flip_y=False)
        window.blit(self.image_flip, self.shape)
        pygame.draw.rect(window, color, self.shape,width=1)
        
    
        