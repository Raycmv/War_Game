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
def draw_background(background, range1, w, range2, h, img):
    	for y in range(range2, h, 150):
            for x in range(range1, w, 150):
                background.blit(img, (x, y))



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
def draw_matriz(screen, tiles, map_data, x, y, name):
	for i, row in enumerate(map_data):
		for j, col in enumerate(row):
			if col != "*":
				w, h = tiles[col].get_size()
				pos_x = x + j * w
				pos_y = y + i * w
				zone = (int(pos_x / ZONE) + 1) * (int(pos_y / ZONE) + 1)
				# if (len(ALL_SPRITES[zone])):
				# 	print(zone, len(ALL_SPRITES[zone]))
				obj = check_collision(zone, pos_x, pos_y, w, h)
				if (obj[0]):
					screen.blit(tiles[col], (pos_x, pos_y))
					if (obj[1] and (name == "tree" or name == "trees")):
						ALL_SPRITES[zone].append(Sprite(pos_x, pos_y, zone, "tree", w, h, str(pos_x) + str(pos_y) + str(zone)))

"""
	Genera siempre las mismas posiciones para los sprites.

	Args:
		cant (int): cantidad de coordenadas a crear.
		w (int): ancho que tendra la imagen.
		h (int): alto que tendra la imagen.

	return:
		positions (list)
"""
def generate_positions(cant, w, h):
    positions = []
    for _ in range(cant):
        x = random.randint(200, (WORLD_WIDTH - w) - 200)
        y = random.randint(20, WORLD_HEIGHT - h)
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
def random_sprites(sprite, cant, w, h, name):
    positions = generate_positions(cant, w, h)
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

def check_collision(zone, x,  y, w, h):
	data = [True, True]
	for sprite in ALL_SPRITES[zone]:
		current = sprite.sprite_status()
		if (current[6] == (str(x) + str(y) + str(zone))):
			data[1] = False
			break
		else:
			if ((x > current[0] and x < current[0] + current[4]) and ((y > current[1] and y < current[1] + current[5]) or (y < current[1] and y + h > current[1] )) ):
				data[0] = False
			elif ((y > current[1] and y < current[1] + current[5]) and ((x < current[0] and x + w > current[0] ) or (x > current[0] and x < current[0] + current[4]))):
				data[0] = False
	return data
