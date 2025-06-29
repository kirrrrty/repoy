import pygame
pygame.init()
info = pygame.display.Info()
SCREEN_HEIGHT = info.current_h
SCREEN_WIDTH = info.current_w
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()
window.fill((255, 165, 0))
pygame.display.set_caption("REpio")
running = True
bg_img = pygame.image.load("assets/cave.png")
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
while running:
    pygame.display.update()
    clock.tick(60)
    window.blit(bg_img, (0, 0))
pygame.quit()