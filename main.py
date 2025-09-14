import pygame
from constants import *
from world_image import *
from utiles import *
from mini_map import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("War")

tiles = world_tiles()

running = True

background = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
camera_x = WORLD_WIDTH // 2 - SCREEN_WIDTH // 2
camera_y = WORLD_HEIGHT - SCREEN_HEIGHT
grass = imagen_interface('mundo//tiles_world.png', 62, 1518, 200, 220, TILE_SIZE, TILE_SIZE)

for i in range (0, CANT_ZONE + 1):
        ALL_SPRITES.append([])

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #evento quit
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: #evento boton del mouse
            mx, my = event.pos

            # Comprobar si el click está dentro del minimapa
            if MINIMAP_X <= mx <= MINIMAP_X + MINIMAP_X_SIZE and MINIMAP_Y <= my <= MINIMAP_Y + MINIMAP_Y_SIZE:
                # Convertir a coordenadas del mundo
                wx, wy = minimap_to_world(mx, my)

                # Centrar la cámara en ese punto
                camera_x = wx - SCREEN_WIDTH // 2
                camera_y = wy - SCREEN_HEIGHT // 2

                # Limitar cámara para que no se salga del mundo
                camera_x = max(0, min(camera_x, WORLD_WIDTH - SCREEN_WIDTH))
                camera_y = max(0, min(camera_y, WORLD_HEIGHT - SCREEN_HEIGHT))

    # --- Cámara con el mouse ---
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if (mouse_x >= SCREEN_WIDTH - 50):
        camera_x += 20
    elif (mouse_x < 50):
        camera_x -= 20
    elif (mouse_y >= SCREEN_HEIGHT - 50):
        camera_y += 20
    elif (mouse_y < 50):
        camera_y -= 20

    # Limitar para que no muestre fuera del mundo
    camera_x = max(0, min(camera_x, WORLD_WIDTH - SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, WORLD_HEIGHT - SCREEN_HEIGHT))

    end_camera_x = (camera_x + SCREEN_WIDTH)
    end_camera_y = (camera_y + SCREEN_HEIGHT)
    
    # --- Dibujar ---
    draw_background(background, camera_x, end_camera_x, camera_y, end_camera_y, grass)

    # -- Dibujando los elementos de la foresta
    for matriz_list in all_world:
         for matriz in matriz_list:
            if (camera_x - SCREEN_WIDTH < matriz[1] < end_camera_x + SCREEN_WIDTH and 
                camera_y - SCREEN_HEIGHT < matriz[2] < end_camera_y + SCREEN_HEIGHT) :
                draw_matriz(background, tiles, matriz[0], matriz[1], matriz[2], matriz[3])
    screen.blit(background, (0, 0), ((camera_x), camera_y, SCREEN_WIDTH, SCREEN_HEIGHT))

    draw_mini_map(screen, camera_x, camera_y, all_world)

 	# Actualizar pantalla
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()