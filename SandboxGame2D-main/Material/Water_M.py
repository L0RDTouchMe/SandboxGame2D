import pygame as pg
import random
from MainColors import WATER_CLR, BACKGROUND_CLR, SAND_CLR, OUTWATER_CLR

randx = random.randrange(-1, 2)

def water(surface, x, y):
    ar = pg.PixelArray(surface)
    if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():
        if ar[x, y] == surface.map_rgb(WATER_CLR):
            if ar[x, y+1] == surface.map_rgb(BACKGROUND_CLR):
                ar[x, y+1] = WATER_CLR
                ar[x, y] = BACKGROUND_CLR
                
            elif x+1 < surface.get_width() and ar[x+1, y] == surface.map_rgb(BACKGROUND_CLR):
                ar[x+1, y] = OUTWATER_CLR
                ar[x, y] = BACKGROUND_CLR
            elif x > 0 and ar[x-1, y] == surface.map_rgb(BACKGROUND_CLR):
                ar[x-1, y] = OUTWATER_CLR
                ar[x, y] = BACKGROUND_CLR


            elif x > 0 and ar[x-1, y+1] == surface.map_rgb(BACKGROUND_CLR):
                ar[x-1, y+1] = WATER_CLR
                ar[x, y] = BACKGROUND_CLR
            elif x+1 < surface.get_width() and ar[x+1, y+1] == surface.map_rgb(BACKGROUND_CLR):
                ar[x+1, y+1] = WATER_CLR
                ar[x, y] = BACKGROUND_CLR

            elif y > 0 and ar[x, y-1] == surface.map_rgb(SAND_CLR):
                ar[x, y-1] = WATER_CLR
                ar[x, y] = SAND_CLR
            elif y > 0 and ar[x, y-1] == surface.map_rgb(BACKGROUND_CLR):
                ar[x, y] = OUTWATER_CLR

    del ar
    return surface