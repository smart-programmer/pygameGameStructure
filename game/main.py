import pygame
from game import screen
from game.instantiation import redhair, surfaces, game
from game.functions import draw_backgrounds, draw_hitboxes


pygame.init()

clock = pygame.time.Clock()



look = True

def main():

	global look

	
	while True:
		x = redhair.rect.x
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				game.screen = 'game'
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d:	
					redhair.velocity += 4

				elif event.key == pygame.K_a:
					redhair.velocity -= 4

				elif event.key == pygame.K_w:
					redhair.gravity_counter = 0
					redhair.gravitational_force = 0
					redhair.y_velocity -= 7 
					redhair.is_jumping = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_d:
					redhair.velocity -= 4

				elif event.key == pygame.K_a:
					redhair.velocity += 4


			# if event.type == pygame.KEYDOWN:
			# 	game.screen = 'game'

			# if redhair.is_jumping:
			# 	if redhair.gravity_counter == 10:
			# 		redhair.gravitational_force = 3
			# 		redhair.y_velocity += 7
			# 		redhair.is_jumping = False
			# 	else: 
			# 		redhair.gravity_counter += 1

		if game.screen == 'game':
			redhair.gravity()
			# redhair.jump()
			draw_backgrounds()
			# draw_hitboxes()
			redhair.move_horizontale()


			# put to three rects around every object that way you know which side the player is hitting by testing which rects of the three he's colliding with the top one or the left on or the right one
			if redhair.rect.colliderect(surfaces[0]):
				redhair.rect.bottom = surfaces[0].rect.top
			if redhair.rect.colliderect(surfaces[1].rect):
				redhair.rect.x = x
				print(redhair.rect.right, surfaces[1].rect.left)


			# pygame.draw.rect(screen, (255, 255, 0), redhair.rect, 2)
			screen.blit(surfaces[1].image, (surfaces[1].rect.x, surfaces[1].rect.y))
			screen.blit(redhair.loadedImage, (redhair.rect.x + redhair.xoffset, redhair.rect.y + redhair.yoffset))
			# pygame.draw.rect(screen, (255, 255, 0), surfaces[1], 2)
			
		else:
			screen.blit(game.load_image(0), (0, 0))



		pygame.display.update()
		clock.tick(60)








# x,y
# top, left, bottom, right
# topleft, bottomleft, topright, bottomright
# midtop, midleft, midbottom, midright
# center, centerx, centery
# size, width, height
# w,h



# rect1.right = 10
# rect2.center = (20,30)



# hero = hero.move(10, 0)