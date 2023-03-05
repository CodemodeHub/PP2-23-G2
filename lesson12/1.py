import pygame as pg

pg.init()

pg.display.set_caption("Moving by mouse")

pg.mixer.init()
pg.mixer.music.load("./music/konfuz-kajf-ty-pojmala-mp3.mp3")
pg.mixer.music.play(-1)

WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)

screen = pg.display.set_mode((WIDTH,HEIGHT))

clock = pg.time.Clock()

running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(WHITE)
    
    (x,y) = pg.mouse.get_pos()

    pg.draw.circle(screen, BLACK, (x,y), 30)

    pg.display.flip()

pg.quit()

