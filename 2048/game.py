from board import Board
import pygame

class Game:
    def __init__(self):
        self.board = Board()
        self.board.add_square()
        self.board.add_square()

    def run_game(self):
        pygame.init()
        screen = pygame.display.set_mode((425, 425))
        clock = pygame.time.Clock()
        running = True
        while running:
            state = self.board.update()
            if not state:
                win = False
                running = False
                continue
            if state == 2:
                win = True
                running = False
                continue
            self.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            clock.tick(60)

    def update(self, screen):
        b = self.board.board
        for i in range(4):
            for j in range(4):
                x = j * 100 + (j+1) * 5
                y = i * 100 + (i+1) * 5
                pygame.draw.rect(screen, (144, 144, 144), pygame.Rect(x, y, 100, 100))
                if b[i][j] != 0:
                    font = pygame.font.Font(pygame.font.get_default_font(), 50)
                    text = font.render(str(2**b[i][j]), True, (0, 0, 0))
                    screen.blit(text, (x, y))
