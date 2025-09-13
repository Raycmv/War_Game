import pygame
import constants

scale_x = constants.MINIMAP_X_SIZE / constants.WORLD_WIDTH
scale_y = constants.MINIMAP_Y_SIZE / constants.WORLD_HEIGHT

# fondo del minimapa
def draw_mini_map(screen, camera_x, camera_y, all_world):

	miniMap = pygame.Rect(constants.MINIMAP_X, constants.MINIMAP_Y, constants.MINIMAP_X_SIZE, constants.MINIMAP_Y_SIZE)
	pygame.draw.rect(screen, (50, 50, 50), miniMap)
	pygame.draw.rect(screen, (255, 0, 0), miniMap, 1)

	# mx = int(player.x * scale_x)
	# my = int(player.y * scale_y)
	# pygame.draw.circle(screen, (0, 255, 0), (SCREEN_WIDTH - MINIMAP_SIZE - 10 + mx, 10 + my), 3)

	# # enemigos
	# for enemy in enemies:
	#     mx = int(enemy.x * scale_x)
	#     my = int(enemy.y * scale_y)
	#     pygame.draw.circle(screen, (255, 0, 0), (SCREEN_WIDTH - MINIMAP_SIZE - 10 + mx, 10 + my), 2)


	cam_rect = pygame.Rect((camera_x * scale_x) + constants.SCREEN_WIDTH - constants.MINIMAP_X_SIZE,
		(camera_y * scale_y) + constants.SCREEN_HEIGHT - constants.MINIMAP_Y_SIZE - 9,
                       constants.SCREEN_WIDTH * scale_x, constants.SCREEN_HEIGHT * scale_y - 5)

	for matriz_imgs in all_world:
		for matriz in matriz_imgs:
		    mx = int(matriz[1] * scale_x)
		    my = int(matriz[2] * scale_y)
		    if (matriz[3] == "trees") :
		    	t = 0
		    	for x in range(9):
		    		if x % 2 == 0:
		    			t = 5
		    		else:
		    			t = 0
		    		pygame.draw.circle(screen, (0, 255, 0), (constants.SCREEN_WIDTH - constants.MINIMAP_X_SIZE + mx + x * 5, 
		    	constants.SCREEN_HEIGHT - constants.MINIMAP_Y_SIZE + my + t), 2)
		    elif (matriz[3] == "tree") :
		    	pygame.draw.circle(screen, (0, 255, 0), (constants.SCREEN_WIDTH - constants.MINIMAP_X_SIZE + mx, 
		    	constants.SCREEN_HEIGHT - constants.MINIMAP_Y_SIZE + my), 2)

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
    wx = int((mx - constants.MINIMAP_X) * constants.WORLD_WIDTH / constants.MINIMAP_X_SIZE)
    wy = int((my - constants.MINIMAP_Y) * constants.WORLD_HEIGHT / constants.MINIMAP_Y_SIZE)
    return wx, wy