import pygame as pg

from MainColors import OUTWATER_CLR, BACKGROUND_CLR, SAND_CLR, WATER_CLR

def outwater(surface, x,y):
    ar = pg.PixelArray(surface)
    if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():
        if ar[x,y] == surface.map_rgb(OUTWATER_CLR):
            if ar[x,y+1] == surface.map_rgb(BACKGROUND_CLR):
                ar[x,y+1] = OUTWATER_CLR
                ar[x,y] = BACKGROUND_CLR

            elif x > 0 and ar[x-1, y] == surface.map_rgb(BACKGROUND_CLR):
                ar[x-1, y] = OUTWATER_CLR
                ar[x,y] = BACKGROUND_CLR
            elif x+1 < surface.get_width() and ar[x+1, y] == surface.map_rgb(BACKGROUND_CLR):
                ar[x+1, y] = OUTWATER_CLR
                ar[x,y] = BACKGROUND_CLR

            elif x > 0 and ar[x-1, y+1] == surface.map_rgb(BACKGROUND_CLR):
                ar[x-1, y+1] = OUTWATER_CLR
                ar[x,y] = BACKGROUND_CLR
            elif x+1 < surface.get_width() and ar[x+1, y+1] == surface.map_rgb(BACKGROUND_CLR):
                ar[x+1, y+1] = OUTWATER_CLR
                ar[x,y] = BACKGROUND_CLR
                
            elif y > 0 and ar[x,y-1] == surface.map_rgb(SAND_CLR):
                ar[x,y-1] = OUTWATER_CLR
                ar[x,y] = SAND_CLR
            elif y > 0 and ar[x,y-1] != surface.map_rgb(BACKGROUND_CLR):
                ar[x,y] = WATER_CLR
    del ar
    return surface

