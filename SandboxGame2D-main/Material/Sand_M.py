import pygame as pg

from MainColors import SAND_CLR, BACKGROUND_CLR

def sand(surface, x,y):
    ar = pg.PixelArray(surface)
    if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():
        if ar[x,y] == surface.map_rgb(SAND_CLR):
            if ar[x,y+1] == surface.map_rgb(BACKGROUND_CLR):
                ar[x,y+1] = SAND_CLR
                ar[x,y] = BACKGROUND_CLR
            elif x > 0 and ar[x-1, y+1]  == surface.map_rgb(BACKGROUND_CLR):
                ar[x -1, y+1] = SAND_CLR
                ar[x,y] = BACKGROUND_CLR
            elif x+1 < surface.get_width() and ar[x+1, y+1] == surface.map_rgb(BACKGROUND_CLR):
                ar[x+1, y+1] = SAND_CLR
                ar[x,y] = BACKGROUND_CLR
    del ar
    return surface