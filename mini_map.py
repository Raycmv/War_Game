import pygame
import constants

scale_x = constants.MINIMAP_SIZE / constants.WORLD_WIDTH
scale_y = constants.MINIMAP_SIZE / constants.WORLD_HEIGHT

# fondo del minimapa
def draw_mini_map(screen, camera_x, camera_y):

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

	pygame.draw.rect(screen, (255, 196, 38), cam_rect, 1)  # borde blanco