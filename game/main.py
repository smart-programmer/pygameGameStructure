import pygame
from game import screen
from game.instantiation import redhair, surfaces, game
from game.functions import draw_backgrounds, draw_hitboxes


pygame.init()

clock = pygame.time.Clock()




def main():

	global surfaces
	
	while True:
		x = redhair.hitbox.rect.x
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				if len(game.images) != 0:
					del(game.images[-1])
					

				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d:	
					redhair.velocity += 4

				elif event.key == pygame.K_a:
					redhair.velocity -= 4
				elif event.key == pygame.K_w:
					if len(game.indices_of_hit_list) != 0:
						for index in game.indices_of_hit_list:
							if redhair.hitbox.bottom_rect.colliderect(surfaces[index]):
								redhair.is_jumping = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_d:
					redhair.velocity -= 4

				elif event.key == pygame.K_a:
					redhair.velocity += 4

		if len(game.images) == 0:
			redhair.jumping_system()


			draw_backgrounds(game.backgrounds, screen)
			# draw_hitboxes()
			redhair.move_horizontale()
			if redhair.velocity < 0:
				# game.scene_move_backgrounds('right')
				surfaces = game.move_world(surfaces, 9, 'right')
			elif redhair.velocity > 0:
				# game.scene_move_backgrounds('left')
				surfaces = game.move_world(surfaces, -9, 'left')


			# put to three rects around every object that way you know which side the player is hitting by testing which rects of the three he's colliding with the top one or the left on or the right one
			# if redhair.hitbox.rect.colliderect(surfaces[0]):
			# 	redhair.hitbox.rect.bottom = surfaces[0].rect.top
			# if redhair.hitbox.rect.collidelist(surfaces):
			if len(redhair.hitbox.rect.collidelistall(surfaces)) != 0:

				game.indices_of_hit_list = redhair.hitbox.rect.collidelistall(surfaces)
				print(game.indices_of_hit_list)
				for index in game.indices_of_hit_list:

					if redhair.hitbox.rect.colliderect(surfaces[index].right_rect):
						redhair.hitbox.rect.left = surfaces[index].right_rect.left
					elif redhair.hitbox.rect.colliderect(surfaces[index].left_rect):
						redhair.hitbox.rect.right = surfaces[index].left_rect.left
					elif redhair.hitbox.rect.colliderect(surfaces[index].top_rect):
						redhair.hitbox.rect.bottom = surfaces[index].top_rect.top
					elif redhair.hitbox.rect.colliderect(surfaces[index].bottom_rect):
						redhair.hitbox.rect.top = surfaces[index].bottom_rect.top

				


			# pygame.draw.rect(screen, (255, 255, 0), surfaces[0].top_rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), redhair.hitbox.rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), redhair.hitbox.top_rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), redhair.hitbox.bottom_rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), redhair.hitbox.right_rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), redhair.hitbox.left_rect, 2)
			screen.blit(surfaces[1].load_image, (surfaces[1].rect.x, surfaces[1].rect.y))
			# screen.blit(redhair.loadedImage, (redhair.hitbox.rect.x + redhair.xoffset, redhair.hitbox.rect.y + redhair.yoffset))
			screen.blit(redhair.loadedImage, (redhair.hitbox.rect.x + redhair.xoffset, redhair.hitbox.rect.y + redhair.yoffset))
			# # pygame.draw.rect(screen, (255, 255, 0), surfaces[1], 2)
			pygame.draw.rect(screen, (255, 255, 0), surfaces[1].bottom_rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), surfaces[1].right_rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), surfaces[1].left_rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), surfaces[1].top_rect, 2)
			
		else:
			screen.blit(game.load_image(-1), (0, 0))



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










	# if redhair.rect.right > surfaces[1].rect.left and redhair.rect.left < surfaces[1].rect.left: # it works الحمد لله
				# 	redhair.rect.right = surfaces[1].rect.left
				# elif redhair.rect.left < surfaces[1].rect.right and redhair.rect.right > surfaces[1].rect.right:
				# 	redhair.rect.left = surfaces[1].rect.right

				# elif redhair.rect.bottom > surfaces[1].rect.top and redhair.rect.top < surfaces[1].rect.top:
				# 	redhair.rect.bottom = surfaces[1].rect.top
				# elif redhair.rect.top > surfaces[1].rect.bottom and redhair.rect.bottom < surfaces[1].rect.bottom:
				# 	redhair.rect.top = surfaces[1].rect.bottom