import pygame as pg

from MainColors import SAND_CLR, WATER_CLR, BARIER_CLR


def add_some_pixels(surface):
    ar = pg.PixelArray(surface)
    # sand
    for i in range (1, 15):
        ar[32,i] = SAND_CLR
    # water
    for i in range (1, 15):
        ar[44,i] = WATER_CLR
        ar[45,i] = WATER_CLR
    # add some solid BARIER
    for i in range (64):
        ar[i,63] = BARIER_CLR
    ar[41,60] = BARIER_CLR
    ar[48,60] = BARIER_CLR
    ar[42,61] = BARIER_CLR
    ar[47,61] = BARIER_CLR
    ar[43,62] = BARIER_CLR
    ar[46,62] = BARIER_CLR
    del ar
    return surface