import pygame as pg

pg.init()

pg.display.set_caption("Moving by mouse")


WIDTH = 800
HEIGHT = 600
FPS = 60

pg.mixer.init()
pg.mixer.music.load("./music/konfuz-kajf-ty-pojmala-mp3.mp3")
pg.mixer.music.play(-1)

background_image = pg.image.load("./images/f02239b8-2e8c-4e2f-81ea-8c9dbfac60e4.jfif")
background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))

font = pg.font.SysFont("Times New Roman", 40, True)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

screen = pg.display.set_mode((WIDTH,HEIGHT))

clock = pg.time.Clock()

x_c, y_c = 50,50
dx, dy = 3,5

running = True
lose = False
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                pg.mixer.music.pause()
            if event.key == pg.K_s:
                pg.mixer.music.unpause()
    screen.fill(WHITE)
    screen.blit(background_image, (0,0))
    
    (x,y) = pg.mouse.get_pos()

    # pg.draw.rect(screen, BLACK,(x,550, 120, 30))
    if x < 120:
        x = 120
    
    pg.draw.rect(screen, (0,0,255),(x - 120,520, 120, 30))

    pg.draw.circle(screen, RED, (x_c,y_c), 15)
    if x_c <= 15 or x_c >= WIDTH - 15:
        dx *= -1
    if y_c <= 15:
        dy *= -1
    if x_c >= x - 120 and x_c <= x and y_c == 505:
        dy *= -1

    if y_c >= HEIGHT:
        pg.mixer.music.stop()
        lose = True

    x_c += dx
    y_c += dy

    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                lose = False
                running = False
        screen.fill(WHITE)
        text = font.render("GAME OVER", False, False)
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 80))
        pg.display.flip()

    
    pg.display.flip()

pg.quit()

