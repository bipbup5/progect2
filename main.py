import pygame
import sys
import copy
import os
from random import choice

square = 30
top = 10
left = 10
dir = 0
v = 270
u = 0
k = 0
res = 0
nres = 0
gameBoard = []
clock = pygame.time.Clock()
g_coords = []
lvls = [[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1],
         [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
         [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
         [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
         [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
         [1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
         [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 1, 1, 1],
         [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
         [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1],
         [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 3, 1],
         [1, 1, 2, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1],
         [1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1],
         [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
         [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
         [1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1],
         [1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
         [1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
         [1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1],
         [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
         [1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1],
         [1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 3, 1],
         [1, 2, 2, 2, 1, 1, 3, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
         [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 3, 2, 2, 2, 2, 3, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 0, 2, 0, 2, 0, 2, 1, 1, 1, 1, 2, 0, 2, 0, 2, 0, 2, 1],
            [1, 2, 0, 2, 0, 2, 0, 2, 1, 1, 1, 1, 2, 0, 2, 0, 2, 0, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 3, 2, 2, 2, 2, 3, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]

pygame.init()
size = width, height = 620, 620
screen = pygame.display.set_mode(size)
wall_sprites = pygame.sprite.Group()
fl_sprites = pygame.sprite.Group()
pac_sprites = pygame.sprite.Group()
dot_sprites = pygame.sprite.Group()
g_sprites = pygame.sprite.Group()


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
        self.im = load_image('pacman.png')
        self.im = pygame.transform.scale(self.im, (20, 20))
        self.row = row
        self.col = col
        self.dir = 0
        self.pac_sprite = pygame.sprite.Sprite()
        pac_sprites.add(self.pac_sprite)
        self.pac_sprite.image = self.im
        self.pac_sprite.rect = self.pac_sprite.image.get_rect()
        self.pac_sprite.mask = pygame.mask.from_surface(self.im)
        self.draw()

    def draw(self):
        if dir == 0:
            self.pac_sprite.image = pygame.transform.rotate(self.im, 90)
        elif dir == 1:
            self.pac_sprite.image = self.im
        elif dir == 2:
            self.pac_sprite.image = pygame.transform.flip(pygame.transform.rotate(self.im, 270), True, False)
        elif dir == 3:
            self.pac_sprite.image = pygame.transform.flip(pygame.transform.rotate(self.im, 180), False, True)

        self.pac_sprite.rect.x = self.row * square + square // 2 + left - 10
        self.pac_sprite.rect.y = self.col * square + square // 2 + top - 10
        pac_sprites.draw(screen)

    def update(self):
        global dot_sprites, res
        if int(self.row) == self.row and int(self.col) == self.col:
            if gameBoard[int(self.row)][int(self.col)] == 2:
                gameBoard[int(self.row)][int(self.col)] = 0
                for dot in dot_sprites:
                    if dot.rect.x == self.row * square + left + 5 and \
                            dot.rect.y == self.col * square + top + 5:
                        dot_sprites.remove(dot)
                        res += 1
                        print(res)
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


class Ghosts:
    def __init__(self, row, col, color):
        if color == 'red':
            im = load_image('g_red.png')
        elif color == 'blue':
            im = load_image('g_blue.png')
        elif color == 'orange':
            im = load_image('g_orange.png')
        elif color == 'white':
            im = load_image('g_white.png')

        im = pygame.transform.scale(im, (20, 20))
        self.row = row
        self.col = col
        self.g_sprite = pygame.sprite.Sprite()
        g_sprites.add(self.g_sprite)
        self.dir_g = choice((0, 1, 2, 3))
        self.g_sprite.image = im
        self.g_sprite.rect = self.g_sprite.image.get_rect()
        self.g_sprite.mask = pygame.mask.from_surface(im)
        self.draw()

    def draw(self):
        self.g_sprite.rect.x = self.row * square + square // 2 + left - 10
        self.g_sprite.rect.y = self.col * square + square // 2 + top - 10
        g_sprites.draw(screen)

    def update(self):
        global running
        for elem in pac_sprites:
            if pygame.sprite.collide_mask(self.g_sprite, elem):
                pass
                running = False

        if self.dir_g == 3:
            if int(self.row) == self.row:
                if canMove(self.row - 1, self.col) and self.col % 1 == 0:
                    self.row -= 0.25
                    self.if_turn()
                    return
                else:
                    self.dir_g = choice((0, 2, 3))
                    return
            else:
                self.row -= 0.25
                self.if_turn()
                return
        elif self.dir_g == 2:
            if int(self.col) == self.col:
                if canMove(self.row, self.col + 1) and self.row % 1.0 == 0:
                    self.col += 0.25
                    self.if_turn()
                    return
                else:
                    self.dir_g = choice((1, 2, 3))
                    return
            else:
                self.col += 0.25
                self.if_turn()
                return
        elif self.dir_g == 1:
            if int(self.row) == self.row:
                if canMove(self.row + 1, self.col) and self.col % 1.0 == 0:
                    self.row += 0.25
                    self.if_turn()
                    return
                else:
                    self.dir_g = choice((0, 1, 2))
                    return
            else:
                self.row += 0.25
                self.if_turn()
                return
        elif self.dir_g == 0:
            if int(self.col) == self.col:
                if canMove(self.row, self.col - 1) and self.row % 1.0 == 0:
                    self.col -= 0.25
                    self.if_turn()
                else:
                    self.dir_g = choice((0, 1, 3))
                    return
            else:
                self.col -= 0.25
                self.if_turn()
                return

    def if_turn(self):
        if self.col % 1 == 0 and self.row % 1 == 0:
            if self.dir_g == 3:
                if gameBoard[int(self.row)][int(self.col) + 1] in [0, 2] or gameBoard[int(self.row)][
                    int(self.col) - 1] in [0, 2]:
                    self.dir_g = choice((0, 2, 3))

            elif self.dir_g == 2:
                if gameBoard[int(self.row) + 1][int(self.col)] in [0, 2] or gameBoard[int(self.row) - 1][
                    int(self.col)] in [0, 2]:
                    self.dir_g = choice((1, 2, 3))

            elif self.dir_g == 1:
                if gameBoard[int(self.row)][int(self.col) + 1] in [0, 2] or gameBoard[int(self.row)][
                    int(self.col) - 1] in [0, 2]:
                    self.dir_g = choice((0, 1, 2))

            elif self.dir_g == 0:
                if gameBoard[int(self.row) + 1][int(self.col)] in [0, 2] or gameBoard[int(self.row) - 1][
                    int(self.col)] in [0, 2]:
                    self.dir_g = choice((0, 1, 3))


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
        global g_coords, nres
        screen.fill((0, 0, 0))
        im_fl = load_image('floor3.png')
        im_fl = pygame.transform.scale(im_fl, (30, 30))
        im_wall = load_image('wall.png')
        im_wall = pygame.transform.scale(im_wall, (30, 30))
        im_dot = load_image('dot.png')
        im_dot = pygame.transform.scale(im_dot, (20, 20))
        for y in range(self.height):
            for x in range(self.width):
                if gameBoard[x][y] == 3:
                    fl = pygame.sprite.Sprite()
                    fl.image = im_fl
                    fl.rect = fl.image.get_rect()
                    fl.rect.x = x * self.cell_size + self.left
                    fl.rect.y = y * self.cell_size + self.top
                    fl_sprites.add(fl)
                    g_coords.append((x, y))
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
                elif gameBoard[x][y] == 2:
                    fl = pygame.sprite.Sprite()
                    fl.image = im_fl
                    fl.rect = fl.image.get_rect()
                    fl.rect.x = x * self.cell_size + self.left
                    fl.rect.y = y * self.cell_size + self.top
                    fl_sprites.add(fl)
                    dot = pygame.sprite.Sprite()
                    dot.image = im_dot
                    dot.rect = dot.image.get_rect()
                    dot.rect.x = x * self.cell_size + self.left + 5
                    dot.rect.y = y * self.cell_size + self.top + 5
                    dot_sprites.add(dot)
                    nres += 1


game = Game(1)

i = 1

game.render()
pacman = Pacman(1, 1)
ghost = Ghosts(g_coords[0][0], g_coords[0][1], 'red')
ghost2 = Ghosts(g_coords[1][0], g_coords[1][1], 'blue')
ghost3 = Ghosts(g_coords[2][0], g_coords[2][1], 'white')
ghost4 = Ghosts(g_coords[3][0], g_coords[3][1], 'orange')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT and pygame.key.get_pressed():
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
    dot_sprites.draw(screen)
    pacman.draw()
    ghost.draw()
    ghost2.draw()
    ghost3.draw()
    ghost4.draw()
    d = v * clock.tick() / 1000
    k += d
    u += d
    if k >= 30:
        pacman.update()
        k = 0

    if u >= 30:
        ghost.update()
        ghost2.update()
        ghost3.update()
        ghost4.update()
        u = 0
    if res == nres:
        i += 1
        game = Game(i)
        screen.fill((0, 0, 0))
        wall_sprites = pygame.sprite.Group()
        fl_sprites = pygame.sprite.Group()
        pac_sprites = pygame.sprite.Group()
        dot_sprites = pygame.sprite.Group()
        g_sprites = pygame.sprite.Group()
        g_coords = []
        pygame.display.flip()
        game.render()
        pacman = Pacman(1, 1)
        ghost = Ghosts(g_coords[0][0], g_coords[0][1], 'red')
        ghost2 = Ghosts(g_coords[1][0], g_coords[1][1], 'blue')
        ghost3 = Ghosts(g_coords[2][0], g_coords[2][1], 'white')
        ghost4 = Ghosts(g_coords[3][0], g_coords[3][1], 'orange')
        nres = 0
        res = 0
    pygame.display.flip()
