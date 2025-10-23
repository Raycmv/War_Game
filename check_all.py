import pygame


def check_region ():
	pass

def check_army(region, fc):
	for sprite in region:
		if sprite.destiny:
			sprite.move_sprite(fc)
		sprite.update_zone()