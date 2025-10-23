import pygame
import world_image
import constants
from itertools import cycle
from utiles import *
from mini_map import *
from area_surface import *
from menu import *
from check_all import check_army
from army import Army
from load import *
from map_1_data import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
font = pygame.font.SysFont(None, 24)  # None = fuente por defecto, 24 = tamaño
clock = pygame.time.Clock()
zoom = 0
frame_count = 0
pygame.display.set_caption("War")

background = pygame.Surface((constants.WORLD_WIDTH, constants.WORLD_HEIGHT))
camera_x = 7000 
camera_y = 12300
punto_x = 0
punto_x_end = 0
punto_y = 0
punto_y_end = 0
show_minimap = False
loading = True
num_circles = len(all_forest)
count = 0
selected = []
running = True
loader_stop = True

world_image.areas = {"full_map": Area_surface('mundo//full_map.png', 0, 0, 0, 0, 5000, 10000, constants.WORLD_WIDTH, constants.WORLD_HEIGHT, "map"),}

#ciclo_region = cycle([ANDORTIA, FENITHA, KRYVENIA, LUMARIS, NOVRITA, OSTRAVEL, TORANILIS, VALMORINO, ERANTIA, SURICEM])

#cities = world_cities()

tiles = world_image.world_tiles()
for i in range (0, 10):
    constants.ALL_SPRITES.append([])
    for j in range (0, 5):
        constants.ALL_SPRITES[i].append([])

city = Area_surface('mundo//tiles_world.png', 7550, 12580, 1070, 80, 850, 770, constants.CITY_WIDTH, constants.CITY_HEIGHT, "city")
# ALL_CITIES.append(city)

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

    if count < num_circles:
        for matriz in all_forest[count]:
            draw_matriz(tiles, matriz[0], matriz[1], matriz[2], matriz[3], matriz[4])
    else:
        loading = False

    count += 1

    pygame.display.flip()
    clock.tick(30)

menu_obj = menu_obj()
loader = secundari_load()

tank = Army(7600, 12500, [['ejercito//blindados.png', 45, 40, 100, 235],], "tank", 35, 70, "blindado", 1, 100, "tierra", "Erantia", "capital")
plane = Army(7450, 12450, [['ejercito//blindados.png', 35, 350, 200, 190],], "caza", 100, 150, "plane", 10, 100, "aire", "Erantia", "capital")
background.blit(world_image.areas["full_map"].image, world_image.areas["full_map"].rect)
city = Area_surface('mundo//cities.png', 7650, 12570, 18, 18, 103, 94, 80, 80, "cuartel")
background.blit(city.image, city.rect)
while running:
    dt = clock.tick(30) / 1000
    frame_count += 1

    if frame_count == 30:
        frame_count = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #evento quit
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: #evento boton del mouse
            mx, my = event.pos
            mouse_mundo_x = punto_x + mx * (punto_x_end / constants.SCREEN_WIDTH)
            mouse_mundo_y = punto_y + my * (punto_y_end / constants.SCREEN_HEIGHT)
            click_zone = [int(mouse_mundo_x / ZONE), int(mouse_mundo_y / ZONE)]

            if menu_obj["menu_rect"].collidepoint(event.pos):
                for button, label, color in menu_obj["button"]:
                    rect = list(button.values())[0]
                    if rect.collidepoint(event.pos) and label == "M":
                        show_minimap = not show_minimap  # alternar minimapa

                    elif  rect.collidepoint(event.pos) and label == "Z":
                        zoom = 0 if zoom == 500 else 500


            # Comprobar si el click está dentro del minimapa
            elif constants.MINIMAP_X <= mx <= constants.MINIMAP_X + constants.MINIMAP_X_SIZE and constants.MINIMAP_Y <= my <= constants.MINIMAP_Y + constants.MINIMAP_Y_SIZE and show_minimap:
                # Convertir a coordenadas del mundo
                wx, wy = minimap_to_world(mx, my)

                # Centrar la cámara en ese punto
                camera_x = wx - constants.SCREEN_WIDTH / 2
                camera_y = wy - constants.SCREEN_HEIGHT / 2

                # Limitar cámara para que no se salga del mundo
                camera_x = max(0, min(camera_x, constants.WORLD_WIDTH - constants.SCREEN_WIDTH))
                camera_y = max(0, min(camera_y, constants.WORLD_HEIGHT - constants.SCREEN_HEIGHT))

            elif event.button == 1:  # clic izquierdo
                #print(mouse_mundo_x, mouse_mundo_y)
                if len(selected) > 0:
                    for sprite in constants.ALL_SPRITES[selected[1][1]][selected[1][0]]:
                        if sprite.id == selected[0] and sprite.move:
                            sprite.destiny = [mouse_mundo_x, mouse_mundo_y]
                            sprite.selected = True
                            selected = []
                            break
                for sprite in constants.ALL_SPRITES[click_zone[1]][click_zone[0]]:
                    if sprite.rect.collidepoint([mouse_mundo_x, mouse_mundo_y]):
                        if sprite.move:
                            sprite.destiny = []
                        selected = [sprite.id, sprite.zone]
                        print(f"Sprite {sprite.name} seleccionado: {sprite.rect.topleft} zona {sprite.zone}")
                        break
            
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_LEFT]:  camera_x -= camera_speed
        #if keys[pygame.K_RIGHT]: camera_x += camera_speed
        #if keys[pygame.K_UP]:    zoom = 2
        #if keys[pygame.K_DOWN]:  zoom = 1

    # --- Cámara con el mouse ---
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if (mouse_x >= constants.SCREEN_WIDTH - 5):
        camera_x += 20
    elif (mouse_x < 5):
        camera_x -= 20
    elif (mouse_y >= constants.SCREEN_HEIGHT - 5):
        camera_y += 20
    elif (mouse_y < 5):
        camera_y -= 20

    # Limitar para que no muestre fuera del mundo
    camera_x = max(0, min(camera_x, constants.WORLD_WIDTH - constants.SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, constants.WORLD_HEIGHT - constants.SCREEN_HEIGHT))

    end_camera_x = (camera_x + constants.SCREEN_WIDTH)
    end_camera_y = (camera_y + constants.SCREEN_HEIGHT)

    punto_x = camera_x - zoom if camera_x - zoom > 0 else 0
    dist_x = constants.SCREEN_WIDTH + (zoom * 2) < constants.WORLD_WIDTH - punto_x

    punto_x_end = constants.SCREEN_WIDTH + (zoom * 2) if dist_x else constants.SCREEN_WIDTH + (zoom * 2)

    if not dist_x:
        punto_x = constants.WORLD_WIDTH - (constants.SCREEN_WIDTH + (zoom * 2))

    zoom_y = zoom * (constants.SCREEN_HEIGHT / constants.SCREEN_WIDTH)

    punto_y = camera_y - zoom_y if camera_y - zoom_y > 0 else 0
    dist_y = constants.SCREEN_HEIGHT + (zoom_y * 2) < constants.WORLD_HEIGHT - punto_y

    punto_y_end = constants.SCREEN_HEIGHT + (zoom_y * 2) if dist_y else constants.SCREEN_HEIGHT + (zoom_y * 2)

    if not dist_y:
        punto_y = constants.WORLD_HEIGHT - (constants.SCREEN_HEIGHT + (zoom_y * 2))
    
    rect = pygame.Rect(punto_x, punto_y, punto_x_end, punto_y_end)
    sub = background.subsurface(rect).copy()
    
    central_zone = [int(int(camera_x + (constants.SCREEN_WIDTH / 2)) / ZONE), int(int(camera_y + (constants.SCREEN_HEIGHT / 2)) / ZONE)]
    current_zones = [
            [central_zone[0] - 1, central_zone[1] - 1], [central_zone[0] - 1, central_zone[1]], [central_zone[0] - 1, central_zone[1] + 1],
            [central_zone[0], central_zone[1] - 1], central_zone, [central_zone[0], central_zone[1] + 1],
            [central_zone[0] + 1, central_zone[1] - 1],[central_zone[0] + 1, central_zone[1]], [central_zone[0] + 1, central_zone[1] + 1],
        ]

     #-- Dibujando los elementos de la foresta
    for celd in current_zones:
        if 0 <= celd[0] < 5 and  0 <= celd[1] < 10:
            for sprite in constants.ALL_SPRITES[celd[1]][celd[0]]:
                sub.blit(sprite.image, (sprite.rect.topleft[0] - punto_x, sprite.rect.topleft[1] - punto_y))

    scaled = pygame.transform.scale(sub, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    screen.blit(scaled, (0, 0))

    if (show_minimap):
        draw_mini_map(screen, camera_x, camera_y, all_forest, zoom)

    menu(menu_obj, font, screen)

    if loader_stop:
        try:
            next(loader)
        except StopIteration:
            loader_stop = False
            pass

    #current_region = next(ciclo_region)
    
    check_army(ALL_ARMY, frame_count)

 	# Actualizar pantalla
    pygame.display.flip()

pygame.quit()