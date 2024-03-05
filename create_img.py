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


draw_vanish_point([-20, 200], 100)
draw_vanish_point([width+20, 200], 100)
# Mettre à jour l'affichage
pygame.image.save(surface, 'img/output_image.png')
pygame.quit()
