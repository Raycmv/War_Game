import pygame
import os
from utiles import *

base_path = os.path.dirname(__file__)

class Area_surface():
    def __init__(self, path, x, y, imgx, imgy, endx, endy, w, h, name):
        self.image = imagen_interface(path, imgx, imgy, endx, endy, w, h)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.name = name