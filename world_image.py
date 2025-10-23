import pygame
from map_1_data import *
from utiles import *
from area_surface import *

def world_tiles ():

    tree1_img = ['mundo//tiles_world.png', 50, 50, 280, 280, 70, 90]
    tree2_img = ['mundo//tiles_world.png', 30, 345, 250, 340, 50, 90]
    tree3_img = ['mundo//tiles_world.png', 320, 50, 280, 280, 70, 70]
    tree4_img = ['mundo//tiles_world.png', 320, 350, 260, 340, 50, 90]
    tree5_img = ['mundo//tiles_world.png', 600, 65, 250, 330, 70, 80]

    tiles = {
        "O": tree1_img,
        "P": tree2_img,
        "Q": tree3_img,
        "R": tree4_img,
        "S": tree5_img,

    }
    return tiles


areas = {}

def world_cities():
    areas = {
        "main_city" : "",
    }
    
    return areas