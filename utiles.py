import pygame
import random
import os
from constants import *
from sprite import *

random.seed(42)

base_path = os.path.dirname(__file__)


"""
    Carga las imagenes desde la ruta donde esta el proyecto y la retorna a la escala especificada

    Args:
        route (string): Nombre de la imagen completo.
        x (int): coordenada x de la imagen en el png
        y (int): coordenada y de la imagen en el png
        rw (int): ancho del recuadro que se tomara.
        ry (int): alto del recuadro que se tomara.
        w (int): Ancho.
        h (int): Alto.

    Returns:
        Sprite
"""
def imagen_interface(route, x, y, rw, rh, w, h):
	image_path = os.path.join(base_path,'assets//img//', route)
	image_load = pygame.image.load(image_path).convert_alpha()
	rect = pygame.Rect(x, y, rw, rh)
	image = image_load.subsurface(rect)
	image = pygame.transform.scale(image, (w, h))
	return image


"""
	dibuja la imagen dada en el background del chunk donde este la camara

	Arg:
	background: zona donde se dibujara la imagen.
	range1 (int): coordenada inicial de la x.
	w (int): ancho que tendra la imagen.
	range2 (int): cordenada inicial de la y.
	h (int): alto que tendra la imagen.
	img: la imagen a dibujar. 

	return:
		None
"""
# def draw_background(background, range1, w, range2, h, img):
#     for y in range(range2, h, 150):
#     	for x in range(range1, w, 150):
#     		if (LAND_X <= x <= LAND_WIDTH  and LAND_Y<= y <= LAND_HEIGHT):
#     			background.blit(img, (x, y))



"""
	Dibuja una imagen por cada letra de la matriz dada.

	Args:
		screen (pygame.Surface): Superficie donde se dibujará la figura.
		tiles: Las imagenes que se utilizara para cada tiles.
		x (int): Coordenada eje x.
		y (int): Coordenada eje y.
		map_data: Matriz a dibujar.

	return:
		None
"""
def draw_matriz(background, tiles, map_data, x, y, name):
	for i, row in enumerate(map_data):
		for j, col in enumerate(row):
			if col != "*":
				w, h = tiles[col][5], tiles[col][6]
				pos_x = x + j * w
				pos_y = y + i * h
				zone = (int(pos_x / ZONE) + 1) * (int(pos_y / ZONE) + 1)
				if (check_zone(zone, pos_x, pos_y) == False):
					img = imagen_interface(tiles[col][0], tiles[col][1], tiles[col][2], tiles[col][3], tiles[col][4], w, h)
					background.blit(img, (pos_x, pos_y))
					
# new_sprite = Sprite_game(tiles[col][0], pos_x, pos_y, tiles[col][1], tiles[col][2], tiles[col][3], tiles[col][4], zone, "tree", w, h, str(pos_x) + str(pos_y) + str(zone))
# ALL_SPRITES[zone].append(new_sprite)

"""
	Genera siempre las mismas posiciones para los sprites.

	Args:
		cant (int): cantidad de coordenadas a crear.
		w (int): ancho que tendra la imagen.
		h (int): alto que tendra la imagen.

	return:
		positions (list)
"""
def generate_positions(cant, mask):
	positions = []
	for _ in range(cant):
		x = random.randint(500, LAND_WIDTH - 500)
		y = random.randint(500, LAND_HEIGHT - 500)
		if (mask.get_at((x, y)) == 0):
			positions.append((x, y))
	return positions


"""
	Crea una matriz de sprites en posiciones fijas aleatorias.

	Args:
		cant (int): cantidad de coordenadas a crear.
		size (int): Tamaño del sprite.

	return:
		positions (list)
"""
def random_sprites(sprite, cant, name, mask):
    positions = generate_positions(cant, mask)
    sprites = []
    for pos in positions:
        sprites.append([sprite, pos[0], pos[1], name])
    return sprites

"""
	Reviza las coordenadas de los elementos de la zona dada para ver si colaicionan.

	Args:
		zone (int): zona en la que se comparara las coordenadas.
		x (int): Coordenada x a comparar.
		y (int): Coordenada y a comparar.
		w (int): ancho del objeto.
		h (int): alto del objeto.

	return:
		data (list): False si hay coalicion y False si ya existe. 
"""

def check_zone(zone, x,  y):
	for sprite in ALL_SPRITES[zone]:
		if (sprite.id == (str(x) + str(y) + str(zone))):
			return True
	return False

"""
	Reviza las coordenadas de los elementos de la zona dada para ver si colaicionan. 
"""

def check_masks_collision(self, other_sprite):
        offset = (other_sprite.rect.x - self.rect.x, other_sprite.rect.y - self.rect.y)
        return self.mask.overlap(other_sprite.mask, offset) is not None

def check_mask_area(area, point):
	print(area.get_at(point) == 1)
	return area.get_at(point) == 1