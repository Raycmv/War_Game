import pygame
from map_1_data import *
from utiles import *
from area_surface import *

def world_tiles ():

    tree1_img = ['mundo//tiles_world.png', 50, 50, 280, 280, 70, 80]
    tree2_img = ['mundo//tiles_world.png', 30, 345, 250, 340, 50, 80]
    tree3_img = ['mundo//tiles_world.png', 320, 50, 280, 280, 70, 70]
    tree4_img = ['mundo//tiles_world.png', 320, 350, 260, 340, 50, 80]
    tree5_img = ['mundo//tiles_world.png', 600, 65, 250, 330, 60, 70]

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

def world_areas():
    areas = {
        "sea_map" : Area_surface('mundo//sea_map.png', 0, 0, 0, 0, 3730, 5000, WORLD_WIDTH, WORLD_HEIGHT, "sea"),
        "land_map" : Area_surface('mundo//land_map.png', LAND_X, LAND_Y, 270, 390, 3195, 4433, LAND_WIDTH, LAND_HEIGHT, "land"),
        "full_map" : Area_surface('mundo//full_map.png', 0, 0, 0, 0, 3730, 5000, WORLD_WIDTH, WORLD_HEIGHT, "map"),
        "Andortia" : Area_surface('mundo//land_map_area.png', 354, 665, 185, 200, 1670, 1327, 4470, 5300, "Andortia"),
        "Fenitha" : Area_surface('mundo//land_map_area.png', 3575, 1005, 2543, 125, 2357, 1855, 6305, 7410, "Fenitha"),
        "Kryvenia" : Area_surface('mundo//land_map_area.png', 320, 4430, 210, 1850, 1646, 1330, 4400, 5310, "Kryvenia"),
        "Lumaris" : Area_surface('mundo//land_map_area.png', 5170, 4920, 3570, 2120, 1405, 1372, 3765, 5480, "Lumaris"),
        "Novrita" : Area_surface('mundo//land_map_area.png', 210, 9785, 360, 3575, 1356, 1325, 3640, 5300, "Novrita"),
        "Ostravel" : Area_surface('mundo//land_map_area.png', 2870, 9195, 2175, 3765, 1200, 1810, 3210, 7220, "Ostravel"),
        "Toranilis" : Area_surface('mundo//land_map_area.png', 5550, 10200, 4230, 4050, 1475, 1230, 3950, 4920, "Toranilis"),
        "Valmorino" : Area_surface('mundo//land_map_area.png', 205, 14735, 390, 5570, 1790, 1165, 4800, 4660, "Valmorino"),
        "Erantia" : Area_surface('mundo//land_map_area.png', 5400, 13950, 3980, 5410, 1570, 1490, 4205, 5955, "Erantia")
    }
    
    return areas

def world_cities():
    areas = {
        "main_city" : "",
    }
    
    return areas