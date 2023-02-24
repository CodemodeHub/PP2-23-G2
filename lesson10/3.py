import pygame as pg
import math
import random

pg.init()

pg.display.set_caption("ellipse")

WIDTH = 800
HEIGHT = 600
FPS = 100

font = pg.font.SysFont("Georgia", 18)

x, y = WIDTH // 2 + 250, HEIGHT // 2
angle = 0
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

running = True

while running:
    clock.tick(FPS)
    screen.fill((255,255,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.draw.circle(screen, (0,0,0), (WIDTH // 2, HEIGHT // 2), 250, 5)
    pg.draw.line(screen, (0,0,0), (WIDTH // 2 - 250, HEIGHT // 2),(WIDTH // 2 + 250, HEIGHT // 2), 5)
    pg.draw.line(screen, (0,0,0), (WIDTH // 2, HEIGHT // 2 - 250),(WIDTH // 2, HEIGHT // 2 + 250), 5)
    pg.draw.line(screen,(255,0,0),(x,y), (WIDTH//2, y), 5)
    pg.draw.line(screen,(0,0,255),(x,y), (x, HEIGHT // 2), 5)
    pg.draw.circle(screen,(0,255,0), (x,y), 15)
    x = WIDTH // 2 + math.cos(math.radians(angle)) * 250
    y = HEIGHT // 2 - math.sin(math.radians(angle)) * 250

    t1 = f'sin {angle % 360} = {math.sin(math.radians(angle)):.2f}'
    t2 = f'cos {angle % 360} = {math.cos(math.radians(angle)):.2f}'

    r1 = font.render(t1, True, (255,0,0))
    r2 = font.render(t2, True, (0,0,255))

    screen.blit(r1,(10, 0))
    screen.blit(r2,(10, 15))

    angle += 1
    pg.display.flip()
pg.quit()
