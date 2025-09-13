import pygame
import random
import os
import constants

random.seed(42)

base_path = os.path.dirname(__file__)

"""
    Carga las imagenes desde la ruta donde esta el proyecto y la retorna a la escala especificada

    Args:
        route (string): Nombre de la imagen completo.
        x (int): coordenada x de la imagen en el png
        y (int): coordenada y de la imagen en el png
        rw(int): ancho del recuadro que se tomara.
        ry(int): alto del recuadro que se tomara.
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
	range1: coordenada inicial de la x.
	w: ancho que tendra la imagen.
	h: alto que tendra la imagen.
	range2: cordenada inicial de la y.
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
		x : Coordenada eje x.
		y : Coordenada eje y.
		map_data: Matriz a dibujar.

	return:
		None
"""
def draw_matriz(screen, tiles, x, y, map_data):
    	for i, row in enumerate(map_data):
    		for j, col in enumerate(row):
    			if col != "*":
    				w, h = tiles[col].get_size()
    				pos_x = x + j * w
    				pos_y = y + i * w
    				screen.blit(tiles[col], (pos_x, pos_y))


"""
	Genera siempre las mismas posiciones para los sprites.

	Args:
		cant (int): cantidad de coordenadas a crear.
		w: ancho que tendra la imagen.
		h: alto que tendra la imagen.

	return:
		positions (list)
"""
def generate_positions(cant, w, h):
    positions = []
    for _ in range(cant):
        x = random.randint(10, constants.WORLD_WIDTH - w)
        y = random.randint(10, constants.WORLD_HEIGHT - h)
        positions.append((x, y))
    return positions

"""
	Crea una matriz de sprites en posiciones fijas aleatorias.

	Args:
		cant (int): cantidad de coordenadas a crear.
		size: Tamaño del sprite.

	return:
		positions (list)
"""
def random_sprites(sprite, cant, w, h, name):
    positions = generate_positions(cant, w, h)
    sprites = []
    for pos in positions:
        sprites.append([sprite, pos[0], pos[1], name])
    return sprites