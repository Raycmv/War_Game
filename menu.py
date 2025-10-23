import pygame
from constants import *

def menu_obj():
	obj = {
		"menu_rect": pygame.Rect(50, SCREEN_HEIGHT - MENU_HEIGHT, SCREEN_WIDTH - 100, MENU_HEIGHT),
		"button": [
			[{"minimap_icon_rect": pygame.Rect(60, ICONS_Y, ICON_SIZE, ICON_SIZE)}, "M", "BLUE"],
			[{"zoommap_icon_rect": pygame.Rect(90, ICONS_Y, ICON_SIZE, ICON_SIZE)}, "Z", "RED"]
		]
	}
	return obj

def menu(obj, font, screen):
	# --- Dibujar barra de menú ---
    pygame.draw.rect(screen, GRAY, obj["menu_rect"])

    for button, label, color in obj["button"]:
    	new_rect = list(button.values())[0]
    	pygame.draw.rect(screen, BLACK, new_rect, 2)  # borde
    	pygame.draw.rect(screen, color, new_rect.inflate(-2, -2))  # ícono

    	minimap_texto = font.render(label, True, (255, 255, 255))
    	minimap_texto_rect = minimap_texto.get_rect(center = list(button.values())[0].center)
    	screen.blit(minimap_texto, minimap_texto_rect)
