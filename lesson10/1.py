import pygame as pg

pg.init()

pg.display.set_caption("ellipse")

WIDTH = 800
HEIGHT = 600
FPS = 100

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

x = 15
y = 15
dx = 5
dy = 6
running = True

while running:
    clock.tick(FPS)
    screen.fill((255,255,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x -= dx
            if event.key == pg.K_RIGHT:
                x += dx
            if event.key == pg.K_UP:
                y -= dy
            if event.key == pg.K_DOWN:
                y += dy
    pg.draw.ellipse(screen, (34,123,215), (x % WIDTH, y % HEIGHT, 60,35))
    pg.display.flip()
pg.quit()
