import pygame
import constants
from world_image import world_tiles, all_world
from utiles import draw_matriz, draw_background, imagen_interface
from mini_map import draw_mini_map, minimap_to_world

# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("War")

tiles = world_tiles()

running = True

background = pygame.Surface((constants.WORLD_WIDTH, constants.WORLD_HEIGHT))
camera_x = constants.WORLD_WIDTH // 2 - constants.SCREEN_WIDTH // 2
camera_y = constants.WORLD_HEIGHT - constants.SCREEN_HEIGHT
grass = imagen_interface('mundo//tiles_world.png', 62, 1518, 200, 220, constants.TILE_SIZE, constants.TILE_SIZE)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            # Ver si el click está dentro del minimapa
            if constants.MINIMAP_X <= mx <= constants.MINIMAP_X + constants.MINIMAP_X_SIZE and constants.MINIMAP_Y <= my <= constants.MINIMAP_Y + constants.MINIMAP_Y_SIZE:
                # Convertir a coordenadas del mundo
                wx, wy = minimap_to_world(mx, my)

                # Centrar la cámara en ese punto
                camera_x = wx - constants.SCREEN_WIDTH // 2
                camera_y = wy - constants.SCREEN_HEIGHT // 2

                # Limitar cámara para que no se salga del mundo
                camera_x = max(0, min(camera_x, constants.WORLD_WIDTH - constants.SCREEN_WIDTH))
                camera_y = max(0, min(camera_y, constants.WORLD_HEIGHT - constants.SCREEN_HEIGHT))

    # --- Cámara con el mouse ---
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if (mouse_x >= constants.SCREEN_WIDTH - 50):
        camera_x += 20
    elif (mouse_x < 50):
        camera_x -= 20
    elif (mouse_y >= constants.SCREEN_HEIGHT - 50):
        camera_y += 20
    elif (mouse_y < 50):
        camera_y -= 20

    # Limitar para que no muestre fuera del mundo
    camera_x = max(0, min(camera_x, constants.WORLD_WIDTH - constants.SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, constants.WORLD_HEIGHT - constants.SCREEN_HEIGHT))

    end_camera_x = (camera_x + constants.SCREEN_WIDTH)
    end_camera_y = (camera_y + constants.SCREEN_HEIGHT)
    
    # --- Dibujar ---
    draw_background(background, camera_x, end_camera_x, camera_y, end_camera_y, grass)

    # -- Dibujando los elementos de la foresta
    for matriz_list in all_world:
         for matriz in matriz_list:
            if (camera_x - constants.SCREEN_WIDTH < matriz[1] < end_camera_x + constants.SCREEN_WIDTH and 
                camera_y - constants.SCREEN_HEIGHT < matriz[2] < end_camera_y + constants.SCREEN_HEIGHT) :
                draw_matriz(background, tiles, matriz[1], matriz[2], matriz[0])

    screen.blit(background, (0, 0), ((camera_x), camera_y, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    draw_mini_map(screen, camera_x, camera_y, all_world)

 	# Actualizar pantalla
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()