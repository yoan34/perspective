import pygame
import math

# Initialisation de Pygame
pygame.init()

infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen_size = (width, height)

surface = pygame.Surface((1920, 1360))
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Dessin en perspective")


BLACK = (200, 200, 200)
WHITE = (255, 255, 255)

surface.fill(WHITE)

def draw_vanish_point(point, rays):
    L = 10000
    x, y = point
    angle_increment = 360 / rays
    for i in range(rays):
        angle = angle_increment * i
        radian = math.radians(angle)
        end_x = x + math.cos(radian) * L
        end_y = y + math.sin(radian)* L
        pygame.draw.line(surface, BLACK, (x, y), (int(end_x), int(end_y)), 1)

for i in range(14):
    pygame.draw.circle(surface, BLACK, (550, 560), 40*i, 1)
for i in range(9):
    pygame.draw.circle(surface, BLACK, (1500, 420), 50*i, 1)
    
for i in range(6):
    pygame.draw.circle(surface, BLACK, (1650, 1100), 50*i, 1)
for i in range(6):
    pygame.draw.circle(surface, BLACK, (1140, 1100), 50*i, 1)
for i in range(5):
    pygame.draw.circle(surface, BLACK, (180, 1150), 40*i, 1)
for i in range(4):
    pygame.draw.circle(surface, BLACK, (480, 1220), 40*i, 1)
for i in range(4):
    pygame.draw.circle(surface, BLACK, (750, 1220), 40*i, 1)

# Mettre à jour l'affichage
pygame.image.save(surface, 'img/circle/output_image.png')
pygame.quit()
