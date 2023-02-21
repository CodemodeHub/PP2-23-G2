import pygame as pg
import math
pg.init()

clock = pg.time.Clock()

FPS = 10
WIDTH = 800
HEIGHT = 500

GREEN = (102, 204, 0)

running = True
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('STADIUM')
while running:
    screen.fill(GREEN)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.draw.line(screen, (255, 255, 255), (0, 20), (800, 20), 4)
    pg.draw.line(screen, (255, 255, 255), (0, 480), (800, 480), 4)
    pg.draw.line(screen, (255, 255, 255), (400, 20), (400, 480), 4)
    pg.draw.line(screen, (255, 255, 255), (0, 115), (90, 115), 4)
    pg.draw.line(screen, (255, 255, 255), (90, 115), (90, 345), 4)
    pg.draw.line(screen, (255, 255, 255), (0, 345), (90, 345), 4)
    pg.draw.line(screen, (255, 255, 255), (800, 115), (710, 115), 4)
    pg.draw.line(screen, (255, 255, 255), (710, 115), (710, 345), 4)
    pg.draw.line(screen, (255, 255, 255), (710, 345), (800, 345), 4)
    pg.draw.circle(screen, (255, 255, 255), (400, 250), 55, 4)
    pg.draw.line(screen, (255, 255, 255), (0, 150), (30, 150), 4)
    pg.draw.line(screen, (255, 255, 255), (30, 150), (30, 315), 4)
    pg.draw.line(screen, (255, 255, 255), (30, 315), (0, 315), 4)
    pg.draw.line(screen, (255, 255, 255), (800, 150), (770, 150), 4)
    pg.draw.line(screen, (255, 255, 255), (770, 150), (770, 315), 4)
    pg.draw.line(screen, (255, 255, 255), (770, 315), (800, 315), 4)
    pg.draw.arc(screen, (255, 255, 255), (50, 185, 90, 90), math.pi * 3 /2, math.pi/2, 4)
    pg.draw.arc(screen, (255, 255, 255), (660, 185, 90, 90), math.pi/2, math.pi*3/2, 4)
    pg.display.flip()
pg.quit()