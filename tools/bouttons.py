import pygame

def create_boutton(x, y):
    # Dessiner un bouton
    button_color = (100, 200, 100)  # Couleur verte pour le bouton
    button_rect = pygame.Rect(x, y, 100, 50)  # Position et dimensions du bouton

    # Afficher le texte du bouton (optionnel)
    font = pygame.font.Font(None, 36)  # Créez une police
    text = font.render('Pause', True, (255, 255, 255))  # Créez le texte
    text_rect = text.get_rect(center=button_rect.center)  # Centrez le texte sur le bouton
    return button_rect