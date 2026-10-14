import pygame
import random
pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0,0,0))
pygame.display.set_caption("My Game")

player = pygame.surface.Surface((100, 100))
player.fill((255,255,255))
player = pygame.image.load("imgs.png/New Piskel-1.png").convert_alpha()
player = pygame.transform.scale(player, (300, 300))

#sets the player's starting postition and speed
player_x = 100
player_y = 100
player_speed = 2


falling_object = pygame.surface.Surface((100, 100))
falling_object.fill((0,255,255))

#sets the falling object's starting position and speed
falling_object_x = 350
falling_object_y = 0
falling_object_speed = 0.5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    falling_object_y += falling_object_speed   
    
    window.fill((0,0,255))
    window.blit(player, (player_x, player_y))
    window.blit(falling_object, (falling_object_x, falling_object_y))
    pygame.display.flip()
    

