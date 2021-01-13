import pygame
import copy
import os

square = 30
spriteRatio = 3 / 2
dir = 0
v = 120
k = 0
clock = pygame.time.Clock()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except Exception:
        print('Файл не найден')
        return False
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at(())
        image.set_colorkey()
    else:
        image = image.convert_alpha()
    return image


class Pacman:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.dir = 0

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.row * square + square // 2, self.col * square + square // 2),
                           square // 4)

    def update(self):
        if dir == 3:
            if canMove(self.row - 1, self.col):
                self.row -= 1
                return
        elif dir == 2:
            if canMove(self.row, self.col + 1):
                self.col += 1
                return
        elif dir == 1:
            if canMove(self.row + 1, self.col):
                self.row += 1
                return
        elif dir == 0:
            if canMove(self.row, self.col - 1):
                self.col -= 1


originalGameBoard = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                     [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                     [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                     [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                     [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                     [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                     [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                     [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                     [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                     [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
                     [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                     [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                     [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                     [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
gameBoard = copy.deepcopy(originalGameBoard)

(width, height) = (len(gameBoard) * square, len(gameBoard[0]) * square)
screen = pygame.display.set_mode((width, height))


def renderBoard():
    screen.fill((0, 0, 0))
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[0])):
            if gameBoard[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 255), (j * square, i * square, square, square))
            elif gameBoard[i][j] == 0:
                pass
                # pygame.draw.circle(screen, (255, 255, 255), (j * square + square // 2, i * square + square // 2),
                # square // 8)

    pygame.display.update()


def canMove(row, col):
    if col == -1 or col == len(gameBoard[0]):
        return True
    if gameBoard[int(row)][int(col)] != 1:
        return True
    return False


pacman = Pacman(1, 1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dir = 0
            elif event.key == pygame.K_d:
                dir = 1
            elif event.key == pygame.K_s:
                dir = 2
            elif event.key == pygame.K_a:
                dir = 3
        k += v * clock.tick() / 1000
        renderBoard()
        pacman.draw()
        if k >= 30:
            pacman.update()
            k = 0
        pygame.display.flip()

