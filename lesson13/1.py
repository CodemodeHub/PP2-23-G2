import pygame as pg
import time
 
pg.init()
 
pg.display.set_caption("Magzhan Romeo Makoster KingofCalc Sabaq")
 


 
clock = pg.time.Clock()
 
WIDTH = 800
HEIGHT = 600
FPS = 60
 
background_image = pg.image.load("./images/car.jpeg")
background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))

pg.mixer.init()
pg.mixer.music.load("./music/obnyal.mp3")
# pg.mixer.music.play(-1)
 
font = pg.font.SysFont("Times New Roman", 40, True)
 
screen = pg.display.set_mode((WIDTH, HEIGHT))
 
WHITE = (255,255,255)
RED=(255,0,0)
ORANGE=(255,128,0)
 
dx, dy = 15, 15
 
x,y=WIDTH/2, HEIGHT/2
 
running = True
lose = False
win = False
start_time = time.time()
end_time = 10
 
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN and y+30<HEIGHT:
                y += dy
            if event.key == pg.K_UP and y-30>0:
                y -= dy
            if event.key == pg.K_RIGHT and x+30<WIDTH:
                x += dx
            if event.key == pg.K_LEFT and x-30>0:
                x -= dx
                
    screen.fill(WHITE)
    screen.blit(background_image, (0,0))
    
    pg.draw.circle(screen, ORANGE, (x,y), 30)
    
    
    current_time = int(time.time() - start_time)
    if current_time == end_time:
        lose = True
        pg.mixer.music.play(-1)

        
    text = font.render(f"Time:{end_time-current_time}", False, False)
    screen.blit(text, (10, 10))
    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                lose = False
                running = False
        screen.fill(WHITE)
        pg.display.flip()
    

    # while win:
    #     # 

    pg.display.flip()
 
pg.quit()  