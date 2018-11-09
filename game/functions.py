import pygame


def draw_backgrounds(backgrounds, screen):
	for background in backgrounds:
		screen.blit(background.image, (background.x, background.y))



def draw_hitboxes():
	pygame.draw.rect(screen, (255, 255, 255), surfaces[0], 2)
	pygame.draw.rect(screen, (255, 255, 255), surfaces[1], 2)




# def test_collisions(main, objects):

# 	for object in objects:
# 		if main.colliderect(object):
# 			if main.rect.bottom < object.rect.top - 2:
# 				main.rect.bottom = object.rect.top:

# 			if main.rect.right 

	