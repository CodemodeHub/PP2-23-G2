import pygame as pg
import random

pg.init()

pg.mixer.init()
pg.mixer.music.load("./music/konfuz-kajf-ty-pojmala-mp3.mp3")
pg.mixer.music.play(-1)


FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pg.display.set_mode((700,500))
pg.display.set_caption("DVD")
clock = pg.time.Clock()

running = True

x = 180
y = 70
dx = 2
dy = 2
color = WHITE

image = pg.image.load("./images/f02239b8-2e8c-4e2f-81ea-8c9dbfac60e4.jfif")
screen.blit(image,(0,0))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    clock.tick(FPS)

    pg.display.flip()

pg.quit()