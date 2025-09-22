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

background = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
camera_x = 3750 
camera_y = 17510

sea_map_img = imagen_interface('mundo//sea_map.png', 0, 0, 3730, 5000, WORLD_WIDTH, WORLD_HEIGHT)
sea_map_mask = pygame.mask.from_surface(sea_map_img)

land_map_img2 = imagen_interface('mundo//land_map2.png', 0, 0, 3730, 5000, WORLD_WIDTH, WORLD_HEIGHT)

land_map_img = imagen_interface('mundo//land_map.png', 225, 300, 3315, 4560, LAND_WIDTH, LAND_HEIGHT)
land_map_mask = pygame.mask.from_surface(land_map_img)


background.blit(sea_map_img, (0, 0))
background.blit(land_map_img, (380, 1150))
background.blit(land_map_img2, (0, 0))

tiles = world_tiles()

for i in range (0, CANT_ZONE + 1):
        ALL_SPRITES.append([])

all_world = world_random(sea_map_mask)

loading = True
num_circles = len(all_world)
count = 1

while loading:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loading = False

    screen.fill((20, 20, 20))

    # Dibujar los círculos en línea
    for i in range(num_circles):
        x = 550 + i * 50   # separación horizontal
        y = 300           # alineados en la misma fila

        if i <= count:  
            color = (255, 0, 0)  # activo (azul)
        else:
            color = (80, 80, 80)     # apagado (gris)

        pygame.draw.circle(screen, color, (x, y), 20)

    if count < len(all_world):
        for matriz in all_world[count]:
            draw_matriz(background, tiles, matriz[0], matriz[1], matriz[2], matriz[3])
    else:
        loading = False

    count += 1

    pygame.display.flip()
    clock.tick(30)

# Estado del minimapa
show_minimap = False

# Ícono minimapa (rectángulo clickeable)
minimap_icon_rect = pygame.Rect(60, ICONS_Y, ICON_SIZE, ICON_SIZE)
menu_rect = pygame.Rect(50, SCREEN_HEIGHT - MENU_HEIGHT, SCREEN_WIDTH - 100, MENU_HEIGHT)

running = True

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

            elif minimap_icon_rect.collidepoint(event.pos):
                show_minimap = not show_minimap  # alternar minimapa

    # --- Cámara con el mouse ---
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if (mouse_x >= SCREEN_WIDTH - 5):
        camera_x += 20
    elif (mouse_x < 5):
        camera_x -= 20
    elif (mouse_y >= SCREEN_HEIGHT - 5):
        camera_y += 20
    elif (mouse_y < 5):
        camera_y -= 20

    # Limitar para que no muestre fuera del mundo
    camera_x = max(0, min(camera_x, WORLD_WIDTH - SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, WORLD_HEIGHT - SCREEN_HEIGHT))

    end_camera_x = (camera_x + SCREEN_WIDTH)
    end_camera_y = (camera_y + SCREEN_HEIGHT)

    central_zone = (int((camera_x + (SCREEN_WIDTH / 2)) / ZONE) + 1) * (int((camera_y + (SCREEN_HEIGHT / 2)) / ZONE) + 1)
    current_zones = [central_zone - 10, central_zone, central_zone + 10, central_zone + 1, central_zone - 1]

    # -- Dibujando los elementos de la foresta
    # for celd in current_zones:
    #     if 0 < celd < 31:
    #         for sprite in ALL_SPRITES[celd]:
    #             background.blit(sprite.image, (sprite.x, sprite.y))
                
    screen.blit(background, (0, 0), ((camera_x), camera_y, SCREEN_WIDTH, SCREEN_HEIGHT))

    # --- Dibujar barra de menú ---
    pygame.draw.rect(screen, GRAY, menu_rect)

    # Dibujar ícono de minimapa
    pygame.draw.rect(screen, BLACK, minimap_icon_rect, 2)  # borde
    pygame.draw.rect(screen, BLUE, minimap_icon_rect.inflate(-10, -10))  # ícono

    if (show_minimap):
        draw_mini_map(screen, camera_x, camera_y, all_world)

 	# Actualizar pantalla
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()