import pygame

class Player:
    def get_move(self):
        for event in pygame.event.get()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return "left"
            if event.key == pygame.K_RIGHT:
                return "right"
            if event.key == pygame.K_UP:
                return "up"
            if event.key == pygame.K_DOWN:
                return "down"
