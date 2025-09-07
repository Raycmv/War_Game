import pygame
import constants

scale_x = constants.MINIMAP_SIZE / constants.WORLD_WIDTH
scale_y = constants.MINIMAP_SIZE / constants.WORLD_HEIGHT

# fondo del minimapa
def draw_mini_map(screen, camera_x, camera_y, matriz_imgs):

	miniMap = pygame.Rect(constants.SCREEN_WIDTH - constants.MINIMAP_SIZE - 10, constants.SCREEN_HEIGHT - constants.MINIMAP_SIZE - 10, constants.MINIMAP_SIZE, constants.MINIMAP_SIZE)
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


	cam_rect = pygame.Rect((camera_x * scale_x) + constants.SCREEN_WIDTH - constants.MINIMAP_SIZE - 9,
		(camera_y * scale_y) + constants.SCREEN_HEIGHT - constants.MINIMAP_SIZE - 9,
                       constants.SCREEN_WIDTH * scale_x - 5, constants.SCREEN_HEIGHT * scale_y - 5)

	for matriz in matriz_imgs:
	    mx = int(matriz[1] * scale_x)
	    my = int(matriz[2] * scale_y)
	    if (matriz[3] == "trees") :
	    	t = 0
	    	for x in range(5):
	    		if x % 2 == 0:
	    			t = x
	    		else:
	    			t = 0
	    		pygame.draw.circle(screen, (0, 255, 0), (constants.SCREEN_WIDTH - constants.MINIMAP_SIZE - 9 + mx + x * 5, 
	    	constants.SCREEN_HEIGHT - constants.MINIMAP_SIZE - 9 + my + t * 5), 2)
	    else:
	    	pygame.draw.circle(screen, (0, 255, 0), (constants.SCREEN_WIDTH - constants.MINIMAP_SIZE - 9 + mx, 
	    	constants.SCREEN_HEIGHT - constants.MINIMAP_SIZE - 9 + my), 2)

	pygame.draw.rect(screen, (255, 196, 38), cam_rect, 1)  # borde blanco