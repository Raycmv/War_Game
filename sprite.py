import pygame


class Sprite:
    def __init__(self, x, y, z, name, w, h, ident):
        self.x = x
        self.y = y
        self.zone = z
        self.name = name
        self.w = w
        self.h = h
        self.id = ident

    def sprite_status(self):
        current = [self.x, self.y, self.zone, self.name, self.w, self.h, self.id]
        return current