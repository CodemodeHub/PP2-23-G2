import pygame as pg
import math
pg.init()

clock = pg.time.Clock()

FPS = 10
WIDTH = 800
HEIGHT = 600

WHITE = (255,255,255)

font = pg.font.SysFont("Georgia", 18)



running = True
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Polygon')
while running:
    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    points = [(100,100), (200,200),(456,456)]
    pg.draw.polygon(screen, (123,213,32), points, 10)
    r2 = font.render("Bon Aqua", True, (0,0,0))
    screen.blit(r2, (50, 50))
    pg.display.flip()

pg.quit()