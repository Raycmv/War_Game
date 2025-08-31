# Example file showing a circle moving on screen
import pygame

from map_data import Map_matriz

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1500, 780))
clock = pygame.time.Clock()

pygame.display.set_caption("War")

running = True

Tiles = {
    "G": grass_tile,
    "W": water_tile,
    "P": path_tile
}

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for y, row in enumerate(map_data):
	    for x, col in enumerate(row):
	        screen.blit(tiles[col], (x*TILE_SIZE, y*TILE_SIZE))

 	# Actualizar pantalla
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()