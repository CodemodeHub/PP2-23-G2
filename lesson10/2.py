import pygame as pg
import random

pg.init()

pg.display.set_caption("game for eyes")

WIDTH = 800
HEIGHT = 600
FPS = 1000

x = 0
y = 0
dx, dy = 3, 3

rect_x = 10
rect_y = 10

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
running = True
screen.fill((255,255,255))
while running:
    clock.tick(FPS)
    # screen.fill((255,255,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.draw.rect(screen, color, (x + dx,y + dy, rect_x, rect_y ))
    x += dx
    y += dy

    if x >= WIDTH - rect_x or x <= 0:
        dx *= -1
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if y  >= HEIGHT - rect_y or y <= 0:
        dy *= -1
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
    pg.display.flip()
pg.quit()
