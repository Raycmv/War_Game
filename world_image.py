import pygame
from map_1_data import *
from utiles import *

def world_tiles ():

    tree1_img = ['mundo//tiles_world.png', 50, 50, 280, 280, 60, 70]
    tree2_img = ['mundo//tiles_world.png', 30, 345, 250, 340, 40, 70]
    tree3_img = ['mundo//tiles_world.png', 320, 50, 280, 280, 60, 60]
    tree4_img = ['mundo//tiles_world.png', 320, 350, 260, 340, 40, 70]
    tree5_img = ['mundo//tiles_world.png', 600, 65, 250, 330, 50, 60]

    tiles = {
        "O": tree1_img,
        "P": tree2_img,
        "Q": tree3_img,
        "R": tree4_img,
        "S": tree5_img,

    }
    return tiles

def world_random(mask):
    all_world = [
        random_sprites("O", 50, "tree", mask),
        random_sprites("P", 50, "tree", mask),
        random_sprites("Q", 50, "tree", mask),
        random_sprites("R", 50, "tree", mask),
        random_sprites("S", 50, "tree", mask),
        all_forest
    ]
    return all_world
