import pygame
class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.Surface((50,50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.velocity_y = 0
        self.speed = 5
        self.jump_strength = -15
        self.on_ground = False
        self.gravity = 0.5
    
    def update(self):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx = - self.speed
        elif keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False
        
        self.velocity += self.gravity
        self.velocity_y = min(self.velocity_y, 15)
        dy += self.velocity_y
        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self, window):
        window.blit(self.image,self.rect)