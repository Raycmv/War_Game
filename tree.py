import pygame
from sprite import *
from constants import *

class Tree(Sprite_game):
    def __init__(self, path, x, y, imgx, imgy, endx, endy, name, w, h, type):
        self.move = False

        super().__init__(path, x, y, imgx, imgy, endx, endy, name, w, h, type)
        ALL_SPRITES[self.zone[1]][self.zone[0]].append(self)