from random import randint, choice
from player import Player
import pygame

class Board:
    def __init__(self):
        self.board = [[0 for i in range(4)] for i in range(4)]
        add_square()
        add_square()
        self.player = Player()

    def update(self):
        move = self.player.get_move()
        if move == "right":
            for i in range(4):
                for j in range(2, -1, -1):
                    if self.board[i][j] == self.board[i][j+1] and self.board[i][j] != 0:
                        self.board[i][j] += 1
                        self.board[i][j+1] = 0
            for i in range(4):
                b = []
                for j in range(4):
                    if self.board[i][j] != 0:
                        b.append(self.board[i][j])
                self.board[i] = [0 for i in range(4-len(b))] + b
        if move = "left":
            for i in range(4):
                for j in range(3):
                    if self.board[i][j] == self.board[i][j+1] and self.board[i][j] != 0:
                        self.board[i][j] += 1
                        self.board[i][j+1] = 0
            for i in range(4):
                b = []
                for i in range(4):
                    if self.board[i][j] != 0:
                        b.append(self.board[i][j])
                self.board[i] = b + [0 for i in range(4-len(b))]
        if move = "up":
            for j in range(4):
                for i in range(3):
                    if self.board[i][j] == self.board[i+1][j] and self.board[i][j] != 0:
                        self.board[i][j] += 1
                        self.board[i][j+1] = 0
        if move = "down":
            pass

    def add_square(self):
        open = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    open.append([i, j])
        open = choice(open)
        self.board[open[0]][open[1]] = randint(1, 2)
