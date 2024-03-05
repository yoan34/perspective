import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonction pour dessiner un polygone en fonction de points
def draw_polygon(surface, points, color):
    pygame.draw.polygon(surface, color, points, 0)

# Points du cube en 3D (x, y, z)
cube_points = [(x, y, z) for x in (100, 300) for y in (100, 300) for z in (100, 300)]

# Fonction de projection simple (ignorer la perspective pour simplifier)
def project_3d_to_2d(x, y, z):
    # Ici, on ignore simplement la coordonnée z pour la projection
    return x, y

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)

    # Projection des points du cube en 2D et dessin des faces
    # Pour un vrai projet, vous devriez trier les faces ici
    projected_points = [project_3d_to_2d(x, y, z) for x, y, z in cube_points]
    print(projected_points)
    # Dessinez les faces du cube ici en utilisant draw_polygon
    draw_polygon(screen, projected_points, WHITE)
    # Vous devez déterminer les points corrects pour chaque face et dessiner chacune d'elles.

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
sys.exit()