from multiprocessing import Event
from turtle import textinput
import pygame as  pg
import pygame
import random
import time

pygame.init()

#сделать удалятор
#копировщик
#телепортер
#динамит )

REZ_X = 64
REZ_Y = 64
RENDER_REZ_X  = 512
RENDER_REZ_Y = 512

BACKGROUND = pg.Color (189, 183, 107)
BLACK = pg.Color (0,0,0)
BARIER = pg.Color(47, 79, 79)
WATER  = pg.Color (0,0,255)
OUTWATER = pg.Color (65, 105, 225)
FIRE = pg.Color (178, 34, 34)
GUNPOWDER = pg.Color (85, 107, 47)


def add_some_pixels(surface):
    ar = pg.PixelArray(surface)
    # sand
    for i in range (1, 15):
        ar[32,i] = BLACK
    # water
    for i in range (1, 15):
        ar[44,i] = WATER
        ar[45,i] = WATER
    # add some solid BARIER
    for i in range (64):
        ar[i,63] = BARIER
    ar[41,60] = BARIER
    ar[48,60] = BARIER
    ar[42,61] = BARIER
    ar[47,61] = BARIER
    ar[43,62] = BARIER
    ar[46,62] = BARIER
    del ar
    return surface

def gunpowder(surface, x,y):
    ar = pg.PixelArray(surface)
    if ar[x,y] == surface.map_rgb(GUNPOWDER):
        if ar[x,y+1] == surface.map_rgb(BACKGROUND):
            ar[x,y+1] = GUNPOWDER
            ar[x,y] = BACKGROUND
        elif ar[x -1, y+1] == surface.map_rgb(BACKGROUND):
            ar[x -1, y+1] = GUNPOWDER
            ar[x,y] = BACKGROUND
        elif ar[x+1, y+1] == surface.map_rgb(BACKGROUND):
            ar[x+1, y+1] = GUNPOWDER
            ar[x,y] = BACKGROUND

        elif ar[x,y-1] == surface.map_rgb(FIRE):
            ar[x,y] = BACKGROUND
            ar[x,y-1] = BACKGROUND
            ar[x,y-2] = BACKGROUND
            ar[x,y+1] = BACKGROUND
            ar[x,y+2] = BACKGROUND

            ar[x-1,y] = BACKGROUND
            ar[x-1,y-1] = BACKGROUND
            ar[x-1,y-2] = BACKGROUND
            ar[x-1,y+1] = BACKGROUND
            ar[x-1,y+2] = BACKGROUND

            ar[x-2,y] = BACKGROUND
            ar[x-2,y-1] = BACKGROUND
            ar[x-2,y-2] = BACKGROUND
            ar[x-2,y+1] = BACKGROUND
            ar[x-2,y+2] = BACKGROUND

            ar[x+1,y] = BACKGROUND
            ar[x+1,y-1] = BACKGROUND
            ar[x+1,y-2] = BACKGROUND
            ar[x+1,y+1] = BACKGROUND
            ar[x+1,y+2] = BACKGROUND

            ar[x+2,y] = BACKGROUND
            ar[x+2,y-1] = BACKGROUND
            ar[x+2,y-2] = BACKGROUND
            ar[x+2,y+1] = BACKGROUND
            ar[x+2,y+2] = BACKGROUND

        elif ar[x,y+1]== surface.map_rgb(FIRE):
            ar[x,y] = BACKGROUND
            ar[x,y-1] = BACKGROUND
            ar[x,y-2] = BACKGROUND
            ar[x,y+1] = BACKGROUND
            ar[x,y+2] = BACKGROUND

            ar[x-1,y] = BACKGROUND
            ar[x-1,y-1] = BACKGROUND
            ar[x-1,y-2] = BACKGROUND
            ar[x-1,y+1] = BACKGROUND
            ar[x-1,y+2] = BACKGROUND

            ar[x-2,y] = BACKGROUND
            ar[x-2,y-1] = BACKGROUND
            ar[x-2,y-2] = BACKGROUND
            ar[x-2,y+1] = BACKGROUND
            ar[x-2,y+2] = BACKGROUND

            ar[x+1,y] = BACKGROUND
            ar[x+1,y-1] = BACKGROUND
            ar[x+1,y-2] = BACKGROUND
            ar[x+1,y+1] = BACKGROUND
            ar[x+1,y+2] = BACKGROUND

            ar[x+2,y] = BACKGROUND
            ar[x+2,y-1] = BACKGROUND
            ar[x+2,y-2] = BACKGROUND
            ar[x+2,y+1] = BACKGROUND
            ar[x+2,y+2] = BACKGROUND
        elif ar[x-1,y]== surface.map_rgb(FIRE):
            ar[x,y] = BACKGROUND
            ar[x,y-1] = BACKGROUND
            ar[x,y-2] = BACKGROUND
            ar[x,y+1] = BACKGROUND
            ar[x,y+2] = BACKGROUND

            ar[x-1,y] = BACKGROUND
            ar[x-1,y-1] = BACKGROUND
            ar[x-1,y-2] = BACKGROUND
            ar[x-1,y+1] = BACKGROUND
            ar[x-1,y+2] = BACKGROUND

            ar[x-2,y] = BACKGROUND
            ar[x-2,y-1] = BACKGROUND
            ar[x-2,y-2] = BACKGROUND
            ar[x-2,y+1] = BACKGROUND
            ar[x-2,y+2] = BACKGROUND

            ar[x+1,y] = BACKGROUND
            ar[x+1,y-1] = BACKGROUND
            ar[x+1,y-2] = BACKGROUND
            ar[x+1,y+1] = BACKGROUND
            ar[x+1,y+2] = BACKGROUND

            ar[x+2,y] = BACKGROUND
            ar[x+2,y-1] = BACKGROUND
            ar[x+2,y-2] = BACKGROUND
            ar[x+2,y+1] = BACKGROUND
            ar[x+2,y+2] = BACKGROUND
        elif ar[x+1,y]== surface.map_rgb(FIRE):
            ar[x,y] = BACKGROUND
            ar[x,y-1] = BACKGROUND
            ar[x,y-2] = BACKGROUND
            ar[x,y+1] = BACKGROUND
            ar[x,y+2] = BACKGROUND

            ar[x-1,y] = BACKGROUND
            ar[x-1,y-1] = BACKGROUND
            ar[x-1,y-2] = BACKGROUND
            ar[x-1,y+1] = BACKGROUND
            ar[x-1,y+2] = BACKGROUND

            ar[x-2,y] = BACKGROUND
            ar[x-2,y-1] = BACKGROUND
            ar[x-2,y-2] = BACKGROUND
            ar[x-2,y+1] = BACKGROUND
            ar[x-2,y+2] = BACKGROUND

            ar[x+1,y] = BACKGROUND
            ar[x+1,y-1] = BACKGROUND
            ar[x+1,y-2] = BACKGROUND
            ar[x+1,y+1] = BACKGROUND
            ar[x+1,y+2] = BACKGROUND

            ar[x+2,y] = BACKGROUND
            ar[x+2,y-1] = BACKGROUND
            ar[x+2,y-2] = BACKGROUND
            ar[x+2,y+1] = BACKGROUND
            ar[x+2,y+2] = BACKGROUND

        elif ar[x+1,y-1]== surface.map_rgb(FIRE):
            ar[x,y] = BACKGROUND
            ar[x,y-1] = BACKGROUND
            ar[x,y-2] = BACKGROUND
            ar[x,y+1] = BACKGROUND
            ar[x,y+2] = BACKGROUND

            ar[x-1,y] = BACKGROUND
            ar[x-1,y-1] = BACKGROUND
            ar[x-1,y-2] = BACKGROUND
            ar[x-1,y+1] = BACKGROUND
            ar[x-1,y+2] = BACKGROUND

            ar[x-2,y] = BACKGROUND
            ar[x-2,y-1] = BACKGROUND
            ar[x-2,y-2] = BACKGROUND
            ar[x-2,y+1] = BACKGROUND
            ar[x-2,y+2] = BACKGROUND

            ar[x+1,y] = BACKGROUND
            ar[x+1,y-1] = BACKGROUND
            ar[x+1,y-2] = BACKGROUND
            ar[x+1,y+1] = BACKGROUND
            ar[x+1,y+2] = BACKGROUND

            ar[x+2,y] = BACKGROUND
            ar[x+2,y-1] = BACKGROUND
            ar[x+2,y-2] = BACKGROUND
            ar[x+2,y+1] = BACKGROUND
            ar[x+2,y+2] = BACKGROUND
        elif ar[x-1,y-1]== surface.map_rgb(FIRE):
            ar[x,y] = BACKGROUND
            ar[x,y-1] = BACKGROUND
            ar[x,y-2] = BACKGROUND
            ar[x,y+1] = BACKGROUND
            ar[x,y+2] = BACKGROUND

            ar[x-1,y] = BACKGROUND
            ar[x-1,y-1] = BACKGROUND
            ar[x-1,y-2] = BACKGROUND
            ar[x-1,y+1] = BACKGROUND
            ar[x-1,y+2] = BACKGROUND

            ar[x-2,y] = BACKGROUND
            ar[x-2,y-1] = BACKGROUND
            ar[x-2,y-2] = BACKGROUND
            ar[x-2,y+1] = BACKGROUND
            ar[x-2,y+2] = BACKGROUND

            ar[x+1,y] = BACKGROUND
            ar[x+1,y-1] = BACKGROUND
            ar[x+1,y-2] = BACKGROUND
            ar[x+1,y+1] = BACKGROUND
            ar[x+1,y+2] = BACKGROUND

            ar[x+2,y] = BACKGROUND
            ar[x+2,y-1] = BACKGROUND
            ar[x+2,y-2] = BACKGROUND
            ar[x+2,y+1] = BACKGROUND
            ar[x+2,y+2] = BACKGROUND
        elif ar[x+1,y+1]== surface.map_rgb(FIRE):
            ar[x,y] = BACKGROUND
            ar[x,y-1] = BACKGROUND
            ar[x,y-2] = BACKGROUND
            ar[x,y+1] = BACKGROUND
            ar[x,y+2] = BACKGROUND

            ar[x-1,y] = BACKGROUND
            ar[x-1,y-1] = BACKGROUND
            ar[x-1,y-2] = BACKGROUND
            ar[x-1,y+1] = BACKGROUND
            ar[x-1,y+2] = BACKGROUND

            ar[x-2,y] = BACKGROUND
            ar[x-2,y-1] = BACKGROUND
            ar[x-2,y-2] = BACKGROUND
            ar[x-2,y+1] = BACKGROUND
            ar[x-2,y+2] = BACKGROUND

            ar[x+1,y] = BACKGROUND
            ar[x+1,y-1] = BACKGROUND
            ar[x+1,y-2] = BACKGROUND
            ar[x+1,y+1] = BACKGROUND
            ar[x+1,y+2] = BACKGROUND

            ar[x+2,y] = BACKGROUND
            ar[x+2,y-1] = BACKGROUND
            ar[x+2,y-2] = BACKGROUND
            ar[x+2,y+1] = BACKGROUND
            ar[x+2,y+2] = BACKGROUND
        elif ar[x-1,y+1]== surface.map_rgb(FIRE):
            ar[x,y] = BACKGROUND
            ar[x,y-1] = BACKGROUND
            ar[x,y-2] = BACKGROUND
            ar[x,y+1] = BACKGROUND
            ar[x,y+2] = BACKGROUND

            ar[x-1,y] = BACKGROUND
            ar[x-1,y-1] = BACKGROUND
            ar[x-1,y-2] = BACKGROUND
            ar[x-1,y+1] = BACKGROUND
            ar[x-1,y+2] = BACKGROUND

            ar[x-2,y] = BACKGROUND
            ar[x-2,y-1] = BACKGROUND
            ar[x-2,y-2] = BACKGROUND
            ar[x-2,y+1] = BACKGROUND
            ar[x-2,y+2] = BACKGROUND

            ar[x+1,y] = BACKGROUND
            ar[x+1,y-1] = BACKGROUND
            ar[x+1,y-2] = BACKGROUND
            ar[x+1,y+1] = BACKGROUND
            ar[x+1,y+2] = BACKGROUND

            ar[x+2,y] = BACKGROUND
            ar[x+2,y-1] = BACKGROUND
            ar[x+2,y-2] = BACKGROUND
            ar[x+2,y+1] = BACKGROUND
            ar[x+2,y+2] = BACKGROUND
    del ar
    return surface


def fire(surface, x,y):
    ar = pg.PixelArray(surface)
    randx = random.randrange(-1, 2)
    if ar[x,y] == surface.map_rgb(FIRE):
        if ar[x,y-1] == surface.map_rgb(BACKGROUND):
            ar[x,y] = BACKGROUND
            ar[x+(randx),y-1] = FIRE
            ar[x+(randx),y-1] = FIRE
        elif ar[x,y-1] != surface.map_rgb(BACKGROUND):
            ar[x,y] = BACKGROUND
    del ar
    return surface

def sand(surface, x,y):
    ar = pg.PixelArray(surface)
    if ar[x,y] == surface.map_rgb(BLACK):
        if ar[x,y+1] == surface.map_rgb(BACKGROUND):
            ar[x,y+1] = BLACK
            ar[x,y] = BACKGROUND
        elif ar[x -1, y+1] == surface.map_rgb(BACKGROUND):
            ar[x -1, y+1] = BLACK
            ar[x,y] = BACKGROUND
        elif ar[x+1, y+1] == surface.map_rgb(BACKGROUND):
            ar[x+1, y+1] = BLACK
            ar[x,y] = BACKGROUND
    del ar
    return surface

def outwater(surface, x,y):
    ar = pg.PixelArray(surface)
    if ar[x,y] == surface.map_rgb(OUTWATER):
        if ar[x,y+1] == surface.map_rgb(BACKGROUND):
            ar[x,y+1] = OUTWATER
            ar[x,y] = BACKGROUND
        elif ar[x -1, y+1] == surface.map_rgb(BACKGROUND):
            ar[x -1, y+1] = OUTWATER
            ar[x,y] = BACKGROUND
        elif ar[x+1, y+1] == surface.map_rgb(BACKGROUND):
            ar[x+1, y+1] = OUTWATER
            ar[x,y] = BACKGROUND
        elif ar[x-1, y] == surface.map_rgb(BACKGROUND):
            ar[x-1, y] = OUTWATER
            ar[x,y] = BACKGROUND
        elif ar[x+1, y] == surface.map_rgb(BACKGROUND):
            ar[x+1, y] = OUTWATER
            ar[x,y] = BACKGROUND
        elif ar[x,y-1] == surface.map_rgb(BLACK):
            ar[x,y-1] = OUTWATER
            ar[x,y] = BLACK
        elif ar[x,y-1] != surface.map_rgb(BACKGROUND):
            ar[x,y] = WATER
    del ar
    return surface


def water(surface, x,y):
    ar = pg.PixelArray(surface)
    if ar[x,y] == surface.map_rgb(WATER):
        
        if ar[x,y+1] == surface.map_rgb(BACKGROUND):
            ar[x,y+1] = WATER
            ar[x,y] = BACKGROUND
        elif ar[x -1, y+1] == surface.map_rgb(BACKGROUND):
            ar[x -1, y+1] = WATER
            ar[x,y] = BACKGROUND
        elif ar[x+1, y+1] == surface.map_rgb(BACKGROUND):
            ar[x+1, y+1] = WATER
            ar[x,y] = BACKGROUND
        elif ar[x-1, y] == surface.map_rgb(BACKGROUND):
            ar[x-1, y] = OUTWATER
            ar[x,y] = BACKGROUND
        elif ar[x+1, y] == surface.map_rgb(BACKGROUND):
            ar[x+1, y] = WATER
            ar[x,y] = BACKGROUND
        elif ar[x,y-1] == surface.map_rgb(BLACK):
            ar[x,y-1] = WATER
            ar[x,y] = BLACK
        elif ar[x,y-1] == surface.map_rgb(BACKGROUND):
            ar[x,y] = OUTWATER
    del ar
    return surface

def physics(surface):
    for x in range(REZ_X):
        for y in range(REZ_Y-1, 0, -1):
            surface = sand(surface, x, y)
            surface = water(surface, x, y)
            surface = outwater(surface, x, y)
            surface = fire(surface, x, y)
            surface = gunpowder(surface, x, y)
    return surface

def reset_state(surface):
    surface.fill(BACKGROUND)
    add_some_pixels(surface)

def main():
    pg.init()
    pg.display.set_mode((RENDER_REZ_X, RENDER_REZ_Y))
    surface = pg.Surface((REZ_X, REZ_Y))
    reset_state(surface)
    pg.display.flip()
    clock = pg.time.Clock()

    while 1:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                raise SystemExit
            if event.type in [pg.KEYDOWN]:
                if event.key == pg.K_SPACE:
                    reset_state(surface)
                if event.key == pg.K_1:
                    material = BARIER
                if event.key == pg.K_2:
                    material = WATER
                if event.key == pg.K_3:
                    material = BLACK
                if event.key == pg.K_4:
                    material = OUTWATER
                if event.key == pg.K_5:
                    material = FIRE
                if event.key == pg.K_6:
                    material = GUNPOWDER

            if event.type == pg.MOUSEBUTTONDOWN:
                xmp, ymp = pg.mouse.get_pos()
                xmp1 = xmp//8
                ymp1 = ymp//8
                ar = pg.PixelArray(surface)
                for i in range (ymp1, ymp1+1):
                    ar[xmp1,i] = material

        surface = physics(surface)
        screen = pg.display.get_surface()
        # do up scaling
        pg.transform.scale(surface, (RENDER_REZ_X, RENDER_REZ_Y), screen)
        pg.display.update()
        clock.tick(60) # fps
    pg.quit()



if __name__ == "__main__":
    main()


