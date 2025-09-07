import pygame
import constants
from map_1_data import all_forest
from utiles import draw_matriz, imagen_interface, draw_background

# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("War")

running = True
CHUNK_SIZE = 16
TILE_SIZE = 38

background = pygame.Surface((constants.WORLD_WIDTH, constants.WORLD_HEIGHT))
camera_x, camera_y = constants.WORLD_WIDTH // 2 - constants.SCREEN_WIDTH // 2, constants.WORLD_HEIGHT

grass = imagen_interface('mundo//tiles_world.png', 137, 326, TILE_SIZE, TILE_SIZE, 20, 20)
small_stone = imagen_interface('mundo//tiles_world.png', 148, 445, 20, 20, 10, 15)
tree1_img = imagen_interface('mundo//tiles_world.png', 80, 70, 140, 250, 120, 140)
tree2_img = imagen_interface('mundo//tiles_world.png', 360, 70, 140, 250, 120, 180)
tree3_img = imagen_interface('mundo//tiles_world.png', 550, 85, 150, 280, 120, 180)
wood_img = imagen_interface('mundo//tiles_world.png', 158, 796, 10, 40, 10, 70)

tiles = {
    "S": small_stone,
    "O": tree1_img,
    "P": tree2_img,
    "Q": tree3_img,
    "M": wood_img
}

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    
    for matriz in all_forest:
        draw_matriz(background, tiles, matriz[1], matriz[2], matriz[0])

    screen.blit(background, (0, 0), ((camera_x), camera_y, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # rect2 = pygame.Rect(100, 100, 80, 120)
    # # Dibujar la imagen
    # screen.blit(wood_img, rect2)
    # # Dibujar el borde del rectángulo (en rojo, 1 píxeles de grosor)
    # pygame.draw.rect(screen, (255, 0, 0), rect2, 1)

 	# Actualizar pantalla
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()