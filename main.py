import pygame
import math

from tools.bouttons import create_boutton

# Initialisation de Pygame
pygame.init()

# Définir la taille de l'écran pour A4 - 595 x 842 pixels
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Dessin en perspective")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

POINT_1 = (-50, 300)
POINT_2 = (width+50, 300)
screen.fill(WHITE)
pygame.draw.circle(screen, RED, POINT_1, 2)

def draw_vanish_point(point, rays):
    L = 10000
    x, y = point
    angle_increment = 360 / rays
    for i in range(rays):
        angle = angle_increment * i
        radian = math.radians(angle)
        end_x = x + math.cos(radian) * L
        end_y = y + math.sin(radian)* L
        pygame.draw.line(screen, BLACK, (x, y), (int(end_x), int(end_y)), 1)


btn = create_boutton(50, 50)
btn_restart = create_boutton(50, 100)

P_X_1, P_Y_1 = -2500, 0
P_X_2, P_Y_2 = width+2500, 0



running = True
paused = False

SPEED = 2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if btn_restart.collidepoint(event.pos):
                SPEED += 1


    screen.fill(WHITE)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        P_X_1 += SPEED
        P_X_2 += SPEED
    if keys[pygame.K_RIGHT]:
        P_X_1 -= SPEED
        P_X_2 -= SPEED
    if keys[pygame.K_UP]:
        P_Y_1 += SPEED
        P_Y_2 += SPEED
    if keys[pygame.K_DOWN]:
        P_Y_1 -= SPEED
        P_Y_2 -= SPEED
    pygame.draw.rect(screen, GREEN, btn_restart)
    draw_vanish_point((P_X_1, P_Y_1), 200)
    draw_vanish_point((P_X_2, P_Y_2), 200)

    pygame.display.flip()
    

pygame.quit()
