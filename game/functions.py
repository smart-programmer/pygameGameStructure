import pygame
from game import screen
from game.instantiation import (layer1, layer2, layer3, layer4, layer5,
	layer6, layer7, layer8, layer9, surfaces)


def draw_backgrounds():
	screen.blit(layer1.image, (layer1.x, layer1.y))
	screen.blit(layer2.image, (layer2.x, layer2.y))
	screen.blit(layer3.image, (layer3.x, layer3.y))
	screen.blit(layer4.image, (layer4.x, layer4.y))
	screen.blit(layer5.image, (layer5.x, layer5.y))
	screen.blit(layer6.image, (layer6.x, layer6.y))
	screen.blit(layer7.image, (layer7.x, layer7.y))
	screen.blit(layer8.image, (layer8.x, layer8.y))
	screen.blit(layer9.image, (layer9.x, layer9.y))



def draw_hitboxes():
	pygame.draw.rect(screen, (255, 255, 255), surfaces[0], 2)
	pygame.draw.rect(screen, (255, 255, 255), surfaces[1], 2)




# def test_collisions(main, objects):

# 	for object in objects:
# 		if main.colliderect(object):
# 			if main.rect.bottom < object.rect.top - 2:
# 				main.rect.bottom = object.rect.top:

# 			if main.rect.right 

	