import pygame
import math
from sprite import *
from utiles import *
from constants import *

class Army(Sprite_game):
    def __init__(self,  x, y, image_list, name, w, h, type, velocity, healt, surf_area, region, city):
        # image_list es una lista de 8 imágenes (una por dirección)
        self.images = image_list
        self.original_image = super().imagen_interface(image_list[0][0], image_list[0][1], image_list[0][2], image_list[0][3], image_list[0][4], w, h)
        self.direction = []  # Comienza mirando "al Este" (0°)
        self.angle = 0
        self.giro = False
        self.distancy = 0
        self.surf_area = surf_area
        self.region = region
        self.velocity = velocity
        self.healt = healt
        self.city = city
        self.new_zone = []
        self.destiny = None
        self.move = True
        self.selected = False
        self.velocity_x = 0
        self.velocity_y = 0
        super().__init__(image_list[0][0], x, y, image_list[0][1], image_list[0][2], image_list[0][3], image_list[0][4], name, w, h, type)

        ALL_SPRITES[self.zone[1]][self.zone[0]].append(self)
        ALL_ARMY.append(self)

    def update_img(self, val):
        self.image = super().imagen_interface(self, image_list[val][0], image_list[val][1], image_list[val][2], image_list[val][3], image_list[val][4], w, h)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def update_zone(self):
        self.new_zone = [int(self.rect.topleft[0] / ZONE), int(self.rect.topleft[1] / ZONE)]

        if self.new_zone[0] != self.zone[0] or self.new_zone[1] != self.zone[1]:
            ALL_SPRITES[self.zone[1]][self.zone[0]].remove(self)
            ALL_SPRITES[self.new_zone[1]][self.new_zone[0]].append(self)
            self.zone = self.new_zone

    def update_destiny(self, x, y):
        self.destiny = pygame.Vector2(x, y)

    def sprite_data(self):
        return [self.type, self.name, self.id, self.surf_area, self.region, self.healt]

    def sprite_direction(self):
        return [self.x, self.y, self.angle, self.direction_index, self.velocity, self.type, self.surf_area]


    def move_sprite(self, fc):
        """Mueve el sprite hacia su destino."""
        if not self.destiny:
            return

        if self.selected and self.destiny:
            self.giro = False
            self.selected = False

        self.direction = (self.destiny - pygame.Vector2(self.rect.center))
        self.distancy = self.direction.length()

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        self.velocity_x = self.direction.x * self.velocity
        self.velocity_y = self.direction.y * self.velocity
        
        self.rotate()

        if not self.selected and self.giro and fc == 0:
            self.rect.x += self.velocity_x
            self.rect.y += self.velocity_y
            #print(f"destino {self.destiny} direccion {self.destiny - pygame.Vector2(self.rect.center)} direccion normalizada {self.direction} distancia {self.distancy} ")
            #print(self.rect.x, self.velocity_x, self.rect.y, self.velocity_y)

        if self.distancy < 5 and not self.selected:
            # Llega al destino
            self.rect.center = (int(self.destiny[0]), int(self.destiny[1]))
            self.destiny = None
            self.direction = []
            self.distancy = 0
            self.giro = False
            return
        
    def rotate(self):
        # Calcula el ángulo en grados (atan2(y, x) con y positivo hacia abajo)
        target_angle = math.degrees(math.atan2(self.direction[1], self.direction[0]))
        target_angle += 90

        angle_diff = (target_angle - self.angle + 180) % 360 - 180

        if angle_diff > 1:
            self.angle += 0.2
        elif angle_diff < -1:
            self.angle -= 0.2
        else:
            self.angle = target_angle
            self.giro = True

        self.image = pygame.transform.rotate(self.original_image, - self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)
        #print(f"Self.Angulo {self.angle} destino: {self.destiny} direction {self.direction} coordenadas actuales {self.rect.topleft}")