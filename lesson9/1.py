import pygame as pg
import math
pg.init()

clock = pg.time.Clock()

FPS = 10
WIDTH = 800
HEIGHT = 600

WHITE = (255,255,255)


running = True
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('CodeMode')
while running:
    screen.fill((255,255,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.draw.line(screen, (187,38,99), (300,30),(300,300), 5)
    pg.draw.circle(screen, (0,0,255),(400,300),50, 8)
    pg.draw.ellipse(screen, (30,97,106),(400,400, 100,40))
    # pg.draw.arc(screen, (40,255,40),(0,0, 800,600), 0,  math.pi / 2)
    pg.display.flip()
pg.quit()