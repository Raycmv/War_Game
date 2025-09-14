import pygame
from constants import *


# fondo del minimapa
def draw_mini_map(screen, camera_x, camera_y, all_world):

	miniMap = pygame.Rect(MINIMAP_X, MINIMAP_Y, MINIMAP_X_SIZE, MINIMAP_Y_SIZE)
	pygame.draw.rect(screen, (50, 50, 50), miniMap)
	pygame.draw.rect(screen, (255, 0, 0), miniMap, 1)

	# mx = int(player.x * SCALE_X)
	# my = int(player.y * SCALE_Y)
	# pygame.draw.circle(screen, (0, 255, 0), (SCREEN_WIDTH - MINIMAP_SIZE - 10 + mx, 10 + my), 3)

	# # enemigos
	# for enemy in enemies:
	#     mx = int(enemy.x * SCALE_X)
	#     my = int(enemy.y * SCALE_Y)
	#     pygame.draw.circle(screen, (255, 0, 0), (SCREEN_WIDTH - MINIMAP_SIZE - 10 + mx, 10 + my), 2)


	cam_rect = pygame.Rect((camera_x * SCALE_X) + SCREEN_WIDTH - MINIMAP_X_SIZE,
		(camera_y * SCALE_Y) + SCREEN_HEIGHT - MINIMAP_Y_SIZE - 9,
                       SCREEN_WIDTH * SCALE_X, SCREEN_HEIGHT * SCALE_Y - 5)

	for matriz_imgs in all_world:
		for matriz in matriz_imgs:
		    mx = int(matriz[1] * SCALE_X)
		    my = int(matriz[2] * SCALE_Y)
		    if (matriz[3] == "trees") :
		    	t = 0
		    	for x in range(9):
		    		if x % 2 == 0:
		    			t = 5
		    		else:
		    			t = 0
		    		pygame.draw.circle(screen, (0, 255, 0), (SCREEN_WIDTH - MINIMAP_X_SIZE + mx + x * 5, 
		    	SCREEN_HEIGHT - MINIMAP_Y_SIZE + my + t), 2)
		    elif (matriz[3] == "tree") :
		    	pygame.draw.circle(screen, (0, 255, 0), (SCREEN_WIDTH - MINIMAP_X_SIZE + mx, 
		    	SCREEN_HEIGHT - MINIMAP_Y_SIZE + my), 2)

	pygame.draw.rect(screen, (255, 196, 38), cam_rect, 1)  # borde blanco

"""
	Convierte coordenadas del minimapa -> mundo
	mx: Coordenada x del minimap.
	my: Coordenada y del minimap.

	return:
		wx: Coordenada x del mundo.
		wy: Coordenada y del mundo.
"""
def minimap_to_world(mx, my):
    wx = int((mx - MINIMAP_X) * WORLD_WIDTH / MINIMAP_X_SIZE)
    wy = int((my - MINIMAP_Y) * WORLD_HEIGHT / MINIMAP_Y_SIZE)
    return wx, wy