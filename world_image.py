import pygame
from map_1_data import all_forest
from utiles import *

def world_tiles ():
    tree1_img = imagen_interface('mundo//tiles_world.png', 50, 50, 280, 280, 130, 160)
    tree2_img = imagen_interface('mundo//tiles_world.png', 30, 345, 250, 340, 120, 180)
    tree3_img = imagen_interface('mundo//tiles_world.png', 320, 50, 280, 280, 130, 160)
    tree4_img = imagen_interface('mundo//tiles_world.png', 320, 350, 260, 340, 130, 200)
    tree5_img = imagen_interface('mundo//tiles_world.png', 600, 65, 250, 330, 130, 200)
    small_rock = imagen_interface('mundo//tiles_world.png', 115, 785, 40, 20, 20, 10)
    medium_rock = imagen_interface('mundo//tiles_world.png', 120, 745, 40, 20, 20, 10)
    group1_rock = imagen_interface('mundo//tiles_world.png', 385, 740, 90, 70, 40, 30)
    group2_rock = imagen_interface('mundo//tiles_world.png', 385, 740, 90, 70, 40, 30)

    tiles = {
        "A": small_rock,
        "B": medium_rock,
        "C": group1_rock,
        "D": group2_rock,
        "O": tree1_img,
        "P": tree2_img,
        "Q": tree3_img,
        "R": tree4_img,
        "S": tree5_img,
    }
    return tiles


all_world = [
    random_sprites("A", 200, 20, 10, "rock"), 
    random_sprites("B", 200, 20, 10, "rock"), 
    random_sprites("C", 20, 20, 10, "rock"), 
    random_sprites("D", 20, 20, 10, "rock"),
    random_sprites("O", 20, 130, 160, "tree"),
    random_sprites("P", 10, 120, 180, "tree"),
    random_sprites("Q", 10, 130, 160, "tree"),
    random_sprites("R", 10, 130, 200, "tree"),
    random_sprites("S", 10, 130, 200, "tree"),
    all_forest
]
