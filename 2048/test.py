import pygame
pygame.init()
screen = pygame.display.set_mode((425, 425))
running =  True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("HI")
            if event.key == pygame.K_RIGHT:
                print("HI")
            if event.key == pygame.K_UP:
                print("HI")
            if event.key == pygame.K_DOWN:
                print("HI")
        if event.type == pygame.QUIT:
            running = False
