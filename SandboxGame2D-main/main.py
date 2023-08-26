from multiprocessing import Event
from turtle import textinput
import pygame as pg
import pygame
import random
import time

from MainColors import *

from Material.Fire_M import fire
from Material.Outwater_M import outwater 
from Material.Sand_M import sand
from Material.Water_M import water

from Map_1 import add_some_pixels


pygame.init()

#сделать удалятор
#копировщик
#телепортер
#динамит )

REZ_X = 64
REZ_Y = 64
RENDER_REZ_X  = 512
RENDER_REZ_Y = 512



def physics(surface):
    for x in range(REZ_X):
        for y in range(REZ_Y-1, 0, -1):
            surface = sand(surface, x, y)
            surface = water(surface, x, y)
            surface = outwater(surface, x, y)
            surface = fire(surface, x, y)
    return surface

def reset_state(surface):
    surface.fill(BACKGROUND_CLR)
    add_some_pixels(surface)

def main():

    print()

    pg.init()
    pg.display.set_mode((RENDER_REZ_X, RENDER_REZ_Y))
    surface = pg.Surface((REZ_X, REZ_Y))
    reset_state(surface)
    pg.display.flip()
    clock = pg.time.Clock()
    material = BACKGROUND_CLR
    
    while True:
        
        for event in pg.event.get():
        
            if event.type == pg.QUIT:
                raise SystemExit
            if event.type in [pg.KEYDOWN]:
                if event.key == pg.K_SPACE:
                    reset_state(surface)
                if event.key == pg.K_1:
                    material = BARIER_CLR
                if event.key == pg.K_2:
                    material = WATER_CLR
                if event.key == pg.K_3:
                    material = SAND_CLR
                if event.key == pg.K_4:
                    material = OUTWATER_CLR
                if event.key == pg.K_5:
                    material = FIRE_CLR
                if event.key == pg.K_0:
                    material = BACKGROUND_CLR

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


