# import pygame as pg

# from main import GUNPOWDER

# def gunpowder(surface, x,y):
#     ar = pg.PixelArray(surface)
#     if ar[x,y] == surface.map_rgb(GUNPOWDER):
#         if ar[x,y+1] == surface.map_rgb(BACKGROUND):
#             ar[x,y+1] = GUNPOWDER
#             ar[x,y] = BACKGROUND
#         elif ar[x -1, y+1] == surface.map_rgb(BACKGROUND):
#             ar[x -1, y+1] = GUNPOWDER
#             ar[x,y] = BACKGROUND
#         elif ar[x+1, y+1] == surface.map_rgb(BACKGROUND):
#             ar[x+1, y+1] = GUNPOWDER
#             ar[x,y] = BACKGROUND

#         elif ar[x,y-1] == surface.map_rgb(FIRE):
#             ar[x,y] = BACKGROUND
#             ar[x,y-1] = BACKGROUND
#             ar[x,y-2] = BACKGROUND
#             ar[x,y+1] = BACKGROUND
#             ar[x,y+2] = BACKGROUND

#             ar[x-1,y] = BACKGROUND
#             ar[x-1,y-1] = BACKGROUND
#             ar[x-1,y-2] = BACKGROUND
#             ar[x-1,y+1] = BACKGROUND
#             ar[x-1,y+2] = BACKGROUND

#             ar[x-2,y] = BACKGROUND
#             ar[x-2,y-1] = BACKGROUND
#             ar[x-2,y-2] = BACKGROUND
#             ar[x-2,y+1] = BACKGROUND
#             ar[x-2,y+2] = BACKGROUND

#             ar[x+1,y] = BACKGROUND
#             ar[x+1,y-1] = BACKGROUND
#             ar[x+1,y-2] = BACKGROUND
#             ar[x+1,y+1] = BACKGROUND
#             ar[x+1,y+2] = BACKGROUND

#             ar[x+2,y] = BACKGROUND
#             ar[x+2,y-1] = BACKGROUND
#             ar[x+2,y-2] = BACKGROUND
#             ar[x+2,y+1] = BACKGROUND
#             ar[x+2,y+2] = BACKGROUND

#         elif ar[x,y+1]== surface.map_rgb(FIRE):
#             ar[x,y] = BACKGROUND
#             ar[x,y-1] = BACKGROUND
#             ar[x,y-2] = BACKGROUND
#             ar[x,y+1] = BACKGROUND
#             ar[x,y+2] = BACKGROUND

#             ar[x-1,y] = BACKGROUND
#             ar[x-1,y-1] = BACKGROUND
#             ar[x-1,y-2] = BACKGROUND
#             ar[x-1,y+1] = BACKGROUND
#             ar[x-1,y+2] = BACKGROUND

#             ar[x-2,y] = BACKGROUND
#             ar[x-2,y-1] = BACKGROUND
#             ar[x-2,y-2] = BACKGROUND
#             ar[x-2,y+1] = BACKGROUND
#             ar[x-2,y+2] = BACKGROUND

#             ar[x+1,y] = BACKGROUND
#             ar[x+1,y-1] = BACKGROUND
#             ar[x+1,y-2] = BACKGROUND
#             ar[x+1,y+1] = BACKGROUND
#             ar[x+1,y+2] = BACKGROUND

#             ar[x+2,y] = BACKGROUND
#             ar[x+2,y-1] = BACKGROUND
#             ar[x+2,y-2] = BACKGROUND
#             ar[x+2,y+1] = BACKGROUND
#             ar[x+2,y+2] = BACKGROUND
#         elif ar[x-1,y]== surface.map_rgb(FIRE):
#             ar[x,y] = BACKGROUND
#             ar[x,y-1] = BACKGROUND
#             ar[x,y-2] = BACKGROUND
#             ar[x,y+1] = BACKGROUND
#             ar[x,y+2] = BACKGROUND

#             ar[x-1,y] = BACKGROUND
#             ar[x-1,y-1] = BACKGROUND
#             ar[x-1,y-2] = BACKGROUND
#             ar[x-1,y+1] = BACKGROUND
#             ar[x-1,y+2] = BACKGROUND

#             ar[x-2,y] = BACKGROUND
#             ar[x-2,y-1] = BACKGROUND
#             ar[x-2,y-2] = BACKGROUND
#             ar[x-2,y+1] = BACKGROUND
#             ar[x-2,y+2] = BACKGROUND

#             ar[x+1,y] = BACKGROUND
#             ar[x+1,y-1] = BACKGROUND
#             ar[x+1,y-2] = BACKGROUND
#             ar[x+1,y+1] = BACKGROUND
#             ar[x+1,y+2] = BACKGROUND

#             ar[x+2,y] = BACKGROUND
#             ar[x+2,y-1] = BACKGROUND
#             ar[x+2,y-2] = BACKGROUND
#             ar[x+2,y+1] = BACKGROUND
#             ar[x+2,y+2] = BACKGROUND
#         elif ar[x+1,y]== surface.map_rgb(FIRE):
#             ar[x,y] = BACKGROUND
#             ar[x,y-1] = BACKGROUND
#             ar[x,y-2] = BACKGROUND
#             ar[x,y+1] = BACKGROUND
#             ar[x,y+2] = BACKGROUND

#             ar[x-1,y] = BACKGROUND
#             ar[x-1,y-1] = BACKGROUND
#             ar[x-1,y-2] = BACKGROUND
#             ar[x-1,y+1] = BACKGROUND
#             ar[x-1,y+2] = BACKGROUND

#             ar[x-2,y] = BACKGROUND
#             ar[x-2,y-1] = BACKGROUND
#             ar[x-2,y-2] = BACKGROUND
#             ar[x-2,y+1] = BACKGROUND
#             ar[x-2,y+2] = BACKGROUND

#             ar[x+1,y] = BACKGROUND
#             ar[x+1,y-1] = BACKGROUND
#             ar[x+1,y-2] = BACKGROUND
#             ar[x+1,y+1] = BACKGROUND
#             ar[x+1,y+2] = BACKGROUND

#             ar[x+2,y] = BACKGROUND
#             ar[x+2,y-1] = BACKGROUND
#             ar[x+2,y-2] = BACKGROUND
#             ar[x+2,y+1] = BACKGROUND
#             ar[x+2,y+2] = BACKGROUND

#         elif ar[x+1,y-1]== surface.map_rgb(FIRE):
#             ar[x,y] = BACKGROUND
#             ar[x,y-1] = BACKGROUND
#             ar[x,y-2] = BACKGROUND
#             ar[x,y+1] = BACKGROUND
#             ar[x,y+2] = BACKGROUND

#             ar[x-1,y] = BACKGROUND
#             ar[x-1,y-1] = BACKGROUND
#             ar[x-1,y-2] = BACKGROUND
#             ar[x-1,y+1] = BACKGROUND
#             ar[x-1,y+2] = BACKGROUND

#             ar[x-2,y] = BACKGROUND
#             ar[x-2,y-1] = BACKGROUND
#             ar[x-2,y-2] = BACKGROUND
#             ar[x-2,y+1] = BACKGROUND
#             ar[x-2,y+2] = BACKGROUND

#             ar[x+1,y] = BACKGROUND
#             ar[x+1,y-1] = BACKGROUND
#             ar[x+1,y-2] = BACKGROUND
#             ar[x+1,y+1] = BACKGROUND
#             ar[x+1,y+2] = BACKGROUND

#             ar[x+2,y] = BACKGROUND
#             ar[x+2,y-1] = BACKGROUND
#             ar[x+2,y-2] = BACKGROUND
#             ar[x+2,y+1] = BACKGROUND
#             ar[x+2,y+2] = BACKGROUND
#         elif ar[x-1,y-1]== surface.map_rgb(FIRE):
#             ar[x,y] = BACKGROUND
#             ar[x,y-1] = BACKGROUND
#             ar[x,y-2] = BACKGROUND
#             ar[x,y+1] = BACKGROUND
#             ar[x,y+2] = BACKGROUND

#             ar[x-1,y] = BACKGROUND
#             ar[x-1,y-1] = BACKGROUND
#             ar[x-1,y-2] = BACKGROUND
#             ar[x-1,y+1] = BACKGROUND
#             ar[x-1,y+2] = BACKGROUND

#             ar[x-2,y] = BACKGROUND
#             ar[x-2,y-1] = BACKGROUND
#             ar[x-2,y-2] = BACKGROUND
#             ar[x-2,y+1] = BACKGROUND
#             ar[x-2,y+2] = BACKGROUND

#             ar[x+1,y] = BACKGROUND
#             ar[x+1,y-1] = BACKGROUND
#             ar[x+1,y-2] = BACKGROUND
#             ar[x+1,y+1] = BACKGROUND
#             ar[x+1,y+2] = BACKGROUND

#             ar[x+2,y] = BACKGROUND
#             ar[x+2,y-1] = BACKGROUND
#             ar[x+2,y-2] = BACKGROUND
#             ar[x+2,y+1] = BACKGROUND
#             ar[x+2,y+2] = BACKGROUND
#         elif ar[x+1,y+1]== surface.map_rgb(FIRE):
#             ar[x,y] = BACKGROUND
#             ar[x,y-1] = BACKGROUND
#             ar[x,y-2] = BACKGROUND
#             ar[x,y+1] = BACKGROUND
#             ar[x,y+2] = BACKGROUND

#             ar[x-1,y] = BACKGROUND
#             ar[x-1,y-1] = BACKGROUND
#             ar[x-1,y-2] = BACKGROUND
#             ar[x-1,y+1] = BACKGROUND
#             ar[x-1,y+2] = BACKGROUND

#             ar[x-2,y] = BACKGROUND
#             ar[x-2,y-1] = BACKGROUND
#             ar[x-2,y-2] = BACKGROUND
#             ar[x-2,y+1] = BACKGROUND
#             ar[x-2,y+2] = BACKGROUND

#             ar[x+1,y] = BACKGROUND
#             ar[x+1,y-1] = BACKGROUND
#             ar[x+1,y-2] = BACKGROUND
#             ar[x+1,y+1] = BACKGROUND
#             ar[x+1,y+2] = BACKGROUND

#             ar[x+2,y] = BACKGROUND
#             ar[x+2,y-1] = BACKGROUND
#             ar[x+2,y-2] = BACKGROUND
#             ar[x+2,y+1] = BACKGROUND
#             ar[x+2,y+2] = BACKGROUND
#         elif ar[x-1,y+1]== surface.map_rgb(FIRE):
#             ar[x,y] = BACKGROUND
#             ar[x,y-1] = BACKGROUND
#             ar[x,y-2] = BACKGROUND
#             ar[x,y+1] = BACKGROUND
#             ar[x,y+2] = BACKGROUND

#             ar[x-1,y] = BACKGROUND
#             ar[x-1,y-1] = BACKGROUND
#             ar[x-1,y-2] = BACKGROUND
#             ar[x-1,y+1] = BACKGROUND
#             ar[x-1,y+2] = BACKGROUND

#             ar[x-2,y] = BACKGROUND
#             ar[x-2,y-1] = BACKGROUND
#             ar[x-2,y-2] = BACKGROUND
#             ar[x-2,y+1] = BACKGROUND
#             ar[x-2,y+2] = BACKGROUND

#             ar[x+1,y] = BACKGROUND
#             ar[x+1,y-1] = BACKGROUND
#             ar[x+1,y-2] = BACKGROUND
#             ar[x+1,y+1] = BACKGROUND
#             ar[x+1,y+2] = BACKGROUND

#             ar[x+2,y] = BACKGROUND
#             ar[x+2,y-1] = BACKGROUND
#             ar[x+2,y-2] = BACKGROUND
#             ar[x+2,y+1] = BACKGROUND
#             ar[x+2,y+2] = BACKGROUND
#     del ar
#     return surface