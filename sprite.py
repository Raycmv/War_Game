import pygame
import os
from utiles import *


base_path = os.path.dirname(__file__)

class Sprite_game(pygame.sprite.Sprite):
    def __init__(self, path, x, y, imgx, imgy, endx, endy, z, name, w, h, ident):
        super().__init__()
        self.image = self.imagen_interface(path, imgx, imgy, endx, endy, w, h)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.zone = z
        self.name = name
        self.w = w
        self.h = h
        self.id = ident

    def sprite_status(self):
        current = [self.x, self.y, self.zone, self.name, self.w, self.h, self.id]
        return current

    def imagen_interface(self, route, x, y, rw, rh, w, h):
        image_path = os.path.join(base_path,'assets//img//', route)
        image_load = pygame.image.load(image_path).convert_alpha()
        rect = pygame.Rect(x, y, rw, rh)
        image = image_load.subsurface(rect)
        image = pygame.transform.scale(image, (w, h))
        return image