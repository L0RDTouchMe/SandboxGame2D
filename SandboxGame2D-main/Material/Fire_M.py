import pygame as pg
import random

from MainColors import FIRE_CLR, BACKGROUND_CLR

def fire(surface, x,y):
    ar = pg.PixelArray(surface)
    randx = random.randrange(-1, 2)
    if ar[x,y] == surface.map_rgb(FIRE_CLR):
        if ar[x,y-1] == surface.map_rgb(BACKGROUND_CLR):
            ar[x,y] = BACKGROUND_CLR
            ar[x+(randx),y-1] = FIRE_CLR
            ar[x+(randx),y-1] = FIRE_CLR
        elif ar[x,y-1] != surface.map_rgb(BACKGROUND_CLR):
            ar[x,y] = BACKGROUND_CLR
    del ar
    return surface
