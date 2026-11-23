import pygame
from modules import * 

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Pygame")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_w:
                img2.y -= 10
            if event.key == pygame.K_a:
                img2.x -= 10
            if event.key == pygame.K_d:
                img2.x += 10
            if event.key == pygame.K_s:
                img2.y += 10
    screen.fill("#515151")

    img1.show_image(screen)
    img2.show_image(screen)
    pygame.display.flip()
