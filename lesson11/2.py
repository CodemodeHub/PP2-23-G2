import pygame
import random

pygame.init()

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("DVD")
clock = pygame.time.Clock()

running = True

x = 180
y = 70
dx = 2
dy = 2
color = WHITE

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    clock.tick(FPS)
    
    x += dx
    y += dy

    if x > 520 or x < 0:
        dx *= -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if y > 430 or y < 0:
        dy *= -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    pygame.draw.ellipse(screen, color, (x, y, 180, 70))
    font = pygame.font.SysFont('verdana', 58, True, True)
    text = font.render("DVD", True, BLACK)
    screen.blit(text, (x + 22, y))
    pygame.display.flip()

pygame.quit()