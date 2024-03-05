import pygame
import math

from tools.models.cuboid import Cuboid

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

screen.fill(WHITE)

def draw_vanish_point(point, rays, L):
    x, y = point
    angle_increment = 360 / rays
    for i in range(rays):
        angle = angle_increment * i
        radian = math.radians(angle)
        end_x = x + math.cos(radian) * L
        end_y = y + math.sin(radian)* L
        pygame.draw.line(screen, BLACK, (x, y), (int(end_x), int(end_y)), 1)
        


P_X_1, P_Y_1 = width/2, 200
P_X_2, P_Y_2 = width+2500, 0


running = True
c1 = Cuboid(400, 300, 100, screen=screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        c1.x -= 3
    if keys[pygame.K_RIGHT]:
        c1.x += 3
    if keys[pygame.K_UP]:
        c1.y -= 3
    if keys[pygame.K_DOWN]:
        c1.y += 3
    screen.fill(WHITE)

    
    
    draw_vanish_point((P_X_1, P_Y_1), 16, 5000)
    c1.draw([[P_X_1, P_Y_1]])
    

    pygame.display.flip()
    

pygame.quit()



