import pygame
import sys
import copy
import os
from random import choice

pow_pac = False
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
         [1, 0, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1],
         [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
         [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
         [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
         [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
         [1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
         [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 1, 2, 1, 1, 1, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
         [1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 4, 3, 1, 1, 1],
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
         [1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 4, 2, 2, 1, 2, 2, 2, 2, 1],
         [1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
         [1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
         [1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1],
         [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
         [1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1],
         [1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 4, 3, 1],
         [1, 2, 2, 2, 1, 1, 3, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1],
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
            [1, 2, 0, 2, 0, 2, 0, 2, 1, 1, 1, 1, 2, 0, 2, 0, 4, 0, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 3, 2, 2, 2, 2, 3, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]

pygame.init()
size = width, height = 620, 620
screen = pygame.display.set_mode(size)
wall_sprites = pygame.sprite.Group()
fl_sprites = pygame.sprite.Group()
pac_sprites = pygame.sprite.Group()
dot_sprites = pygame.sprite.Group()
g_sprites = pygame.sprite.Group()
tab_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('wall.png'), (620, 620))
    screen.blit(fon, (0, 0))
    font_pac = pygame.font.SysFont('arialblack', 68)
    str_rendered = font_pac.render('Pacman', 1, pygame.Color(37, 27, 17))
    str_rect = str_rendered.get_rect()
    str_rect.x = -7
    str_rect.y = 99
    screen.blit(str_rendered, str_rect)
    font = pygame.font.SysFont('comicsansms', 40)
    str_rendered = font.render('Управление:        W, A, S, D', 1, pygame.Color(37, 27, 17))
    str_rect = str_rendered.get_rect()
    str_rect.x = 20
    str_rect.y = 500
    screen.blit(str_rendered, str_rect)
    font = pygame.font.SysFont('comicsansms', 30)
    str_rendered = font.render('Приятной игры', 1, pygame.Color(37, 27, 17))
    str_rect = str_rendered.get_rect()
    str_rect.x = 195
    str_rect.y = 290
    screen.blit(str_rendered, str_rect)
    im = pygame.transform.scale(load_image('g_red.png'), (50, 50))
    screen.blit(im, (350, 120))
    im = pygame.transform.scale(load_image('g_blue.png'), (50, 50))
    screen.blit(im, (410, 120))
    im = pygame.transform.scale(load_image('g_white.png'), (50, 50))
    screen.blit(im, (470, 120))
    im = pygame.transform.scale(load_image('g_orange.png'), (50, 50))
    screen.blit(im, (530, 120))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick()


def Next_level():
    fon = pygame.transform.scale(load_image('wall.png'), (620, 620))
    screen.blit(fon, (0, 0))
    font = pygame.font.SysFont('comicsansms', 23)
    str_rendered = font.render(f'Cледующий уровень: {i}', 1, pygame.Color(37, 27, 17))
    str_rect = str_rendered.get_rect()
    str_rect.x = 180
    str_rect.y = 290
    screen.blit(str_rendered, str_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick()


def End_screen():
    fon = pygame.transform.scale(load_image('wall.png'), (620, 620))
    screen.blit(fon, (0, 0))
    font_pac = pygame.font.SysFont('arialblack', 68)
    str_rendered = font_pac.render('Pacman', 1, pygame.Color(37, 27, 17))
    str_rect = str_rendered.get_rect()
    str_rect.x = -7
    str_rect.y = 99
    screen.blit(str_rendered, str_rect)

    im = pygame.transform.scale(load_image('g_red.png'), (50, 50))
    screen.blit(im, (350, 120))
    im = pygame.transform.scale(load_image('g_blue.png'), (50, 50))
    screen.blit(im, (410, 120))
    im = pygame.transform.scale(load_image('g_white.png'), (50, 50))
    screen.blit(im, (470, 120))
    im = pygame.transform.scale(load_image('g_orange.png'), (50, 50))
    screen.blit(im, (530, 120))

    font = pygame.font.SysFont('comicsansms', 30)
    str_rendered = font.render(f'Спасибо за игру', 1, pygame.Color(37, 27, 17))
    str_rect = str_rendered.get_rect()
    str_rect.x = 190
    str_rect.y = 290
    screen.blit(str_rendered, str_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick()


def Game_Over():
    fon = pygame.transform.scale(load_image('wall.png'), (620, 620))
    screen.blit(fon, (0, 0))

    font = pygame.font.SysFont('comicsansms', 50)
    str_rendered = font.render(f'Game Over', 1, pygame.Color(37, 27, 17))
    str_rect = str_rendered.get_rect()
    str_rect.x = 185
    str_rect.y = 240
    screen.blit(str_rendered, str_rect)
    font = pygame.font.SysFont('comicsansms', 30)
    str_rect = str_rendered.get_rect()
    str_rect.x = 210
    str_rect.y = 320
    str_rendered = font.render(f'Score: {res} lvl: {i}', 1, pygame.Color(37, 27, 17))
    screen.blit(str_rendered, str_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick()


def canMove(row, col):
    if col == -1 or col == len(gameBoard[0]):
        return True
    if gameBoard[int(row)][int(col)] != 1:
        return True
    return False


class Pacman:
    def __init__(self, row, col):
        global p
        if p == 1:
            im = load_image('pacman.png')
        elif p == 2:
            im = load_image('pacman_c.png')
            print('p')
        im = pygame.transform.scale(im, (20, 20))
        self.row = row
        self.col = col
        self.dir = 0
        self.pac_sprite = pygame.sprite.Sprite()
        pac_sprites.add(self.pac_sprite)
        self.pac_sprite.image = im
        self.pac_sprite.rect = self.pac_sprite.image.get_rect()
        self.pac_sprite.mask = pygame.mask.from_surface(im)
        self.draw()

    def draw(self):
        self.pac_sprite.rect.x = self.row * square + square // 2 + left - 10
        self.pac_sprite.rect.y = self.col * square + square // 2 + top - 10
        pac_sprites.draw(screen)

    def update(self):
        global dot_sprites, res, pow_pac, running, r, cd
        if p == 1:
            imd = pygame.transform.scale(load_image('pacman.png'), (20, 20))
            self.pac_sprite.image = imd
        elif p == 2:
            imd = pygame.transform.scale(load_image('pacman_c.png'), (20, 20))
            self.pac_sprite.image = imd
        if dir == 3:
            self.pac_sprite.image = pygame.transform.flip(imd, True, False)
            r = 1
        elif dir == 2:
            if r == 1:
                self.pac_sprite.image = pygame.transform.rotate(pygame.transform.flip(imd, True, False), 90)
            elif r == 2:
                self.pac_sprite.image = pygame.transform.rotate(imd, 270)
        elif dir == 1:
            self.pac_sprite.image = imd
            r = 2
        elif dir == 0:
            if r == 1:
                self.pac_sprite.image = pygame.transform.rotate(pygame.transform.flip(imd, True, False), 270)
            elif r == 2:
                self.pac_sprite.image = pygame.transform.rotate(imd, 90)


        for elem in tab_sprites:
            if pygame.sprite.collide_mask(self.pac_sprite, elem):
                tab_sprites.remove(elem)
                pow_pac = True
                cd += 2000

        for elem in g_sprites:
            if pygame.sprite.collide_mask(self.pac_sprite, elem):
                if not pow_pac:
                    print('pacman-dead')
                    Game_Over()
                    terminate()
                if pow_pac:
                    print('ghost-dead')
                    g_sprites.remove(elem)

        if int(self.row) == self.row and int(self.col) == self.col:
            if gameBoard[int(self.row)][int(self.col)] == 2:
                gameBoard[int(self.row)][int(self.col)] = 0
                for dot in dot_sprites:
                    if dot.rect.x == self.row * square + left + 5 and \
                            dot.rect.y == self.col * square + top + 5:
                        dot_sprites.remove(dot)
                        res += 1


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
            self.im = load_image('g_red.png')
        elif color == 'blue':
            self.im = load_image('g_blue.png')
        elif color == 'orange':
            self.im = load_image('g_orange.png')
        elif color == 'white':
            self.im = load_image('g_white.png')
        self.im1 = load_image('ghost5.png')
        self.im = pygame.transform.scale(self.im, (20, 20))
        self.row = row
        self.col = col
        self.im1 = pygame.transform.scale(self.im1, (20, 20))

        self.g_sprite = pygame.sprite.Sprite()
        self.dir_g = choice((0, 1, 2, 3))
        self.g_sprite.image = self.im
        self.g_sprite.rect = self.g_sprite.image.get_rect()
        self.g_sprite.mask = pygame.mask.from_surface(self.im)
        g_sprites.add(self.g_sprite)
        self.draw()

    def draw(self):
        self.g_sprite.rect.x = self.row * square + square // 2 + left - 10
        self.g_sprite.rect.y = self.col * square + square // 2 + top - 10
        g_sprites.draw(screen)

    def update(self):
        global running
        if pow_pac:
            self.g_sprite.image = self.im1
        if not pow_pac:
            self.g_sprite.image = self.im



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
        self.draw()

    def if_turn(self):
        if self.col % 1 == 0 and self.row % 1 == 0:
            if self.dir_g == 3:
                if gameBoard[int(self.row)][int(self.col) + 1] in [0, 2, 3, 4] or gameBoard[int(self.row)][
                    int(self.col) - 1] in [0, 2, 3, 4]:
                    self.dir_g = choice((0, 2, 3))

            elif self.dir_g == 2:
                if gameBoard[int(self.row) + 1][int(self.col)] in [0, 2, 3, 4] or gameBoard[int(self.row) - 1][
                    int(self.col)] in [0, 2, 3, 4]:
                    self.dir_g = choice((1, 2, 3))

            elif self.dir_g == 1:
                if gameBoard[int(self.row)][int(self.col) + 1] in [0, 2, 3, 4] or gameBoard[int(self.row)][
                    int(self.col) - 1] in [0, 2, 3, 4]:
                    self.dir_g = choice((0, 1, 2))

            elif self.dir_g == 0:
                if gameBoard[int(self.row) + 1][int(self.col)] in [0, 2, 3, 4] or gameBoard[int(self.row) - 1][
                    int(self.col)] in [0, 2, 3, 4]:
                    self.dir_g = choice((0, 1, 3))


class Game:
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
        im_tab = load_image('tabletka.png')
        im_tab = pygame.transform.scale(im_tab, (20, 20))
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
                elif gameBoard[x][y] == 4:
                    fl = pygame.sprite.Sprite()
                    fl.image = im_fl
                    fl.rect = fl.image.get_rect()
                    fl.rect.x = x * self.cell_size + self.left
                    fl.rect.y = y * self.cell_size + self.top
                    fl_sprites.add(fl)
                    tab = pygame.sprite.Sprite()
                    tab.image = im_tab
                    tab.rect = tab.image.get_rect()
                    tab.rect.x = x * self.cell_size + self.left + 5
                    tab.rect.y = y * self.cell_size + self.top + 5
                    tab.mask = pygame.mask.from_surface(im_tab)
                    tab_sprites.add(tab)


font_all = pygame.font.SysFont('comicsansms', 25)
cd = 0
start_screen()
p = 1
game = Game(1)
r = 2
i = 1
Next_level()
game.render()
pacman = Pacman(1, 1)
ghost = Ghosts(g_coords[0][0], g_coords[0][1], 'red')
ghost2 = Ghosts(g_coords[1][0], g_coords[1][1], 'blue')
ghost3 = Ghosts(g_coords[2][0], g_coords[2][1], 'white')
ghost4 = Ghosts(g_coords[3][0], g_coords[3][1], 'orange')
running = True
n = 0
c = 0
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
    tab_sprites.draw(screen)
    ghost.draw()
    ghost2.draw()
    ghost3.draw()
    ghost4.draw()
    d = v * clock.tick() / 1000
    k += d
    u += d
    n += d

    s_r = font_all.render(f'Score: {res}      Left: {nres - res}', 1, pygame.Color(200, 200, 200))
    s_rect = s_r.get_rect()
    s_rect.x = 15
    s_rect.y = 5
    screen.blit(s_r, s_rect)

    if pow_pac:
        c += d
    if pow_pac:
        if k >= 20:
            pacman.update()
            k = 0

    else:
        if k >= 30:
            pacman.update()
            k = 0
    if c >= cd and c > 0:
        pow_pac = False
        c = 0
        cd = 0
    if n >= 60:
        if p == 1:
            p += 1
        elif p == 2:
            p = 1
        n = 0
    if u >= 30:

        ghost.update()
        ghost2.update()
        ghost3.update()
        ghost4.update()

        u = 0
    if res == nres:
        if i != len(lvls):
            i += 1
            Next_level()
            game = Game(i)
            screen.fill((0, 0, 0))
            nres = 0
            res = 0
            wall_sprites = pygame.sprite.Group()
            fl_sprites = pygame.sprite.Group()
            pac_sprites = pygame.sprite.Group()
            dot_sprites = pygame.sprite.Group()
            g_sprites = pygame.sprite.Group()
            tab_sprites = pygame.sprite.Group()
            g_coords = []
            pygame.display.flip()
            game.render()
            pacman = Pacman(1, 1)
            ghost = Ghosts(g_coords[0][0], g_coords[0][1], 'red')
            ghost2 = Ghosts(g_coords[1][0], g_coords[1][1], 'blue')
            ghost3 = Ghosts(g_coords[2][0], g_coords[2][1], 'white')
            ghost4 = Ghosts(g_coords[3][0], g_coords[3][1], 'orange')
        else:
            End_screen()
            terminate()

    pygame.display.flip()
