import pygame
from game import screen
from game.instantiation import redhair, surfaces, game
from game.functions import draw_backgrounds, draw_hitboxes


pygame.init()

clock = pygame.time.Clock()



look = True

def main():

	global look
	hitbox_index = 0

	
	while True:
		x = redhair.hitbox.rect.x
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
					hitbox_index = redhair.hitbox.bottom_rect.collidelist(surfaces)
					print(hitbox_index)
					if hitbox_index != -1:
						if redhair.hitbox.rect.colliderect(surfaces[hitbox_index].top_rect):
							# print(2)
							redhair.is_jumping = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_d:
					redhair.velocity -= 4

				elif event.key == pygame.K_a:
					redhair.velocity += 4

			
		if game.screen == 'game':
			redhair.jumping_system()


			draw_backgrounds()
			# draw_hitboxes()
			redhair.move_horizontale()


			# put to three rects around every object that way you know which side the player is hitting by testing which rects of the three he's colliding with the top one or the left on or the right one
			if redhair.hitbox.rect.colliderect(surfaces[0]):
				redhair.hitbox.rect.bottom = surfaces[0].rect.top
			if redhair.hitbox.rect.colliderect(surfaces[1].rect):

				# if redhair.rect.right > surfaces[1].rect.left and redhair.rect.left < surfaces[1].rect.left: # it works الحمد لله
				# 	redhair.rect.right = surfaces[1].rect.left
				# elif redhair.rect.left < surfaces[1].rect.right and redhair.rect.right > surfaces[1].rect.right:
				# 	redhair.rect.left = surfaces[1].rect.right

				# elif redhair.rect.bottom > surfaces[1].rect.top and redhair.rect.top < surfaces[1].rect.top:
				# 	redhair.rect.bottom = surfaces[1].rect.top
				# elif redhair.rect.top > surfaces[1].rect.bottom and redhair.rect.bottom < surfaces[1].rect.bottom:
				# 	redhair.rect.top = surfaces[1].rect.bottom
				if redhair.hitbox.rect.colliderect(surfaces[1].righ_rect):
					redhair.hitbox.rect.left = surfaces[1].righ_rect.left
				elif redhair.hitbox.rect.colliderect(surfaces[1].left_rect):
					redhair.hitbox.rect.right = surfaces[1].left_rect.left
				elif redhair.hitbox.rect.colliderect(surfaces[1].top_rect):
					redhair.hitbox.rect.bottom = surfaces[1].top_rect.top
				elif redhair.hitbox.rect.colliderect(surfaces[1].bottom_rect):
					redhair.hitbox.rect.top = surfaces[1].bottom_rect.top

			# print(redhair.hitbox.rect.bottomright)

				


			# pygame.draw.rect(screen, (255, 255, 0), redhair.hitbox.rect, 2)
			screen.blit(surfaces[1].image, (surfaces[1].rect.x, surfaces[1].rect.y))
			screen.blit(redhair.loadedImage, (redhair.hitbox.rect.x + redhair.xoffset, redhair.hitbox.rect.y + redhair.yoffset))
			# # pygame.draw.rect(screen, (255, 255, 0), surfaces[1], 2)
			# pygame.draw.rect(screen, (255, 255, 0), surfaces[1].bottom_rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), surfaces[1].righ_rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), surfaces[1].left_rect, 2)
			# pygame.draw.rect(screen, (255, 255, 0), surfaces[1].top_rect, 2)
			
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