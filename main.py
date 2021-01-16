import pygame
import sys
import copy
import os


square = 30
top = 10
left = 10
dir = 0
v = 360
k = 0
gameBoard = []
clock = pygame.time.Clock()

lvls = [[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]

pygame.init()
size = width, height = 620, 620
screen = pygame.display.set_mode(size)


wall_sprites = pygame.sprite.Group()
fl_sprites = pygame.sprite.Group()
pac_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def canMove(row, col):
    if col == -1 or col == len(gameBoard[0]):
        return True
    if gameBoard[int(row)][int(col)] != 1:
        return True
    return False


class Pacman:
    def __init__(self, row, col):
        im = load_image('pacman.png')
        im = pygame.transform.scale(im, (20, 20))
        self.row = row
        self.col = col
        self.dir = 0
        self.pac_sprite = pygame.sprite.Sprite()
        pac_sprites.add(self.pac_sprite)
        self.pac_sprite.image = im
        self.pac_sprite.rect = self.pac_sprite.image.get_rect()
        self.draw()

    def draw(self):
        self.pac_sprite.rect.x = self.row * square + square // 2 + left - 10
        self.pac_sprite.rect.y = self.col * square + square // 2 + top - 10
        pac_sprites.draw(screen)
        # pygame.draw.circle(screen, (255, 255, 255), (self.row * square + square // 2 + left, self.col * square + square // 2 + top),
        #                    square // 4)

    def update(self):
        if dir == 3:
            if int(self.row) == self.row:
                if canMove(self.row - 1, self.col) and self.col % 1 == 0:
                    self.row -= 0.25
                    return
            else:
                self.row -= 0.25
                return
        elif dir == 2:
            if int(self.col) == self.col:
                if canMove(self.row, self.col + 1) and self.row % 1.0 == 0:
                    self.col += 0.25
                    return
            else:
                self.col += 0.25
                return
        elif dir == 1:
            if int(self.row) == self.row:
                if canMove(self.row + 1, self.col) and self.col % 1.0 == 0:
                    self.row += 0.25
                    return
            else:
                self.row += 0.25
                return
        elif dir == 0:
            if int(self.col) == self.col:
                if canMove(self.row, self.col - 1) and self.row % 1.0 == 0:
                    self.col -= 0.25
            else:
                self.col -= 0.25


class Game:
    # создание поля
    def __init__(self, lvl):
        global gameBoard
        self.width = 20
        self.height = 20
        self.left = left
        self.top = top
        self.cell_size = square
        self.current_lvl = lvl - 1
        gameBoard = copy.deepcopy(lvls[self.current_lvl])

    def render(self):
        im_fl = load_image('floor3.png')
        im_fl = pygame.transform.scale(im_fl, (30, 30))
        im_wall = load_image('wall.png')
        im_wall = pygame.transform.scale(im_wall, (30, 30))
        for y in range(self.height):
            for x in range(self.width):
                if gameBoard[x][y] == 0:
                    fl = pygame.sprite.Sprite()
                    fl.image = im_fl
                    fl.rect = fl.image.get_rect()
                    fl.rect.x = x * self.cell_size + self.left
                    fl.rect.y = y * self.cell_size + self.top
                    fl_sprites.add(fl)
                elif gameBoard[x][y] == 1:
                    wall = pygame.sprite.Sprite()
                    wall.image = im_wall
                    wall.rect = wall.image.get_rect()
                    wall.rect.x = x * self.cell_size + self.left
                    wall.rect.y = y * self.cell_size + self.top
                    wall_sprites.add(wall)


game = Game(1)
pacman = Pacman(1, 1)
running = True
game.render()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT and pygame.key.get_pressed() :
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
    screen.fill((0, 0, 0))
    fl_sprites.draw(screen)
    wall_sprites.draw(screen)
    pacman.draw()
    k += v * clock.tick() / 1000
    if k >= 30:
        pacman.update()
        k = 0
    pygame.display.flip()
