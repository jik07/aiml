from copy import deepcopy
from random import randint, choice
from player import Player

class Board:
    def __init__(self):
        self.board = [[0 for i in range(4)] for i in range(4)]
        self.player = Player()

    def add_square(self):
        open = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    open.append([i, j])
        open = choice(open)
        self.board[open[0]][open[1]] = randint(1, 2)

    def gd(self):
        if self.board == self.move("right") == self.move("left") == self.move("up") == self.move("down"):
            return 0
        for i in range(4):
            if 11 in self.board[i]:
                return 2
        return 1

    def move(self, move):
        nb = deepcopy(self.board)
        if move == "right":
            for i in range(4):
                b = []
                for j in range(4):
                    if nb[i][j] != 0:
                        b.append(nb[i][j])
                nb[i] = [0 for i in range(4-len(b))] + b
            for i in range(4):
                for j in range(2, -1, -1):
                    if nb[i][j] == nb[i][j+1] and nb[i][j] != 0:
                        nb[i][j] += 1
                        nb[i][j+1] = 0
            for i in range(4):
                b = []
                for j in range(4):
                    if nb[i][j] != 0:
                        b.append(nb[i][j])
                nb[i] = [0 for i in range(4-len(b))] + b
        if move == "left":
            for i in range(4):
                b = []
                for j in range(4):
                    if nb[i][j] != 0:
                        b.append(nb[i][j])
                nb[i] = b + [0 for i in range(4-len(b))]
            for i in range(4):
                for j in range(3):
                    if nb[i][j] == nb[i][j+1] and nb[i][j] != 0:
                        nb[i][j] += 1
                        nb[i][j+1] = 0
            for i in range(4):
                b = []
                for j in range(4):
                    if nb[i][j] != 0:
                        b.append(nb[i][j])
                nb[i] = b + [0 for i in range(4-len(b))]
        if move == "up":
            for j in range(4):
                b = []
                z = 0
                for i in range(4):
                    if nb[i][j] != 0:
                        b.append(nb[i][j])
                    else:
                        z += 1
                b = b + [0 for i in range(z)]
                for i in range(4):
                    nb[i][j] = b[i]
            for j in range(4):
                for i in range(3):
                    if nb[i][j] == nb[i+1][j] and nb[i][j] != 0:
                        nb[i][j] += 1
                        nb[i+1][j] = 0
            for j in range(4):
                b = []
                z = 0
                for i in range(4):
                    if nb[i][j] != 0:
                        b.append(nb[i][j])
                    else:
                        z += 1
                b = b + [0 for i in range(z)]
                for i in range(4):
                    nb[i][j] = b[i]
        if move == "down":
            for j in range(4):
                b = []
                z = 0
                for i in range(4):
                    if nb[i][j] != 0:
                        b.append(nb[i][j])
                    else:
                        z += 1
                b = [0 for i in range(z)] + b
                for i in range(4):
                    nb[i][j] = b[i]
            for j in range(4):
                for i in range(2, -1, -1):
                    if nb[i][j] == nb[i+1][j] and nb[i][j] != 0:
                        nb[i][j] += 1
                        nb[i+1][j] = 0
            for j in range(4):
                b = []
                z = 0
                for i in range(4):
                    if nb[i][j] != 0:
                        b.append(nb[i][j])
                    else:
                        z += 1
                b = [0 for i in range(z)] + b
                for i in range(4):
                    nb[i][j] = b[i]
        return nb

    def update(self):
        m = self.player.get_move()
        if self.move(m) == self.board:
            return self.gd()
        self.board = self.move(m)
        self.add_square()
        return self.gd()
