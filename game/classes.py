from pygame.image import load
from pygame import Rect


# make gravity it's own object then pass it to each character

class Character:

	def __init__(self, x, y, width, height, images, xoffset=0, yoffset=0):

		self.hitbox = HitBox(x, y, width, height, top_ffset=4, height_offset=6) #Rect(x , y, width, height)
		self.xoffset = xoffset
		self.yoffset = yoffset
		self.images = images
		self.imageCounter = 0
		self.loadedImage = load(self.images['idle'][self.imageCounter]).convert_alpha()
		self.velocity = 0
		self.y_velocity = 5
		self.animation_counter = 0
		self.gravitational_force = 3
		self.jump_counter = 0
		self.is_jumping = False


	def animation(self, animationType):

		if self.imageCounter > len(self.images[animationType]) - 2:
			self.imageCounter = 0
		else:
			self.imageCounter += 1

		self.loadedImage = load(self.images[animationType][self.imageCounter]).convert_alpha()


	def move_horizontale(self):
		self.hitbox.rect.x += self.velocity
		self.hitbox = HitBox(self.hitbox.rect.x, self.hitbox.rect.y, self.hitbox.rect.width, self.hitbox.rect.height, top_ffset=4, height_offset=6)
		self.animation_counter += 1

		if self.animation_counter > 3:
			self.animation_counter = 0
			if self.velocity > 0:
				self.animation('move_right')
			elif self.velocity < 0:
				self.animation('move_left')
			elif self.velocity == 0:
				self.animation('idle')

			# if you want a more robust system don't call animation here but call it in the game loop so you can call it for any animation you want


	def gravity(self):
		self.hitbox.rect.y += self.gravitational_force

		if self.gravitational_force != 0:
			self.hitbox = HitBox(self.hitbox.rect.x, self.hitbox.rect.y, self.hitbox.rect.width, self.hitbox.rect.height, top_ffset=4, height_offset=6)

	def jump(self):
		self.hitbox.rect.y -= self.y_velocity 
		self.hitbox = HitBox(self.hitbox.rect.x, self.hitbox.rect.y, self.hitbox.rect.width, self.hitbox.rect.height, top_ffset=4, height_offset=6)

	def jumping_system(self):
		if not self.is_jumping:
			self.gravity()
		elif self.jump_counter < 10:
			self.jump()
			self.jump_counter += 1
		else:
			self.jump_counter = 0
			self.is_jumping = False

# redhair.gravity()
			# if redhair.is_jumping:
			# 	if redhair.jump_counter == 0:
			# 		redhair.gravitational_force = 0
			# 	if redhair.jump_counter < 10:
			# 		redhair.jump()
			# 		redhair.jump_counter += 1
			# 		if redhair.jump_counter % 2 == 0:
			# 			redhair.gravitational_force += 1
			# 	else:
			# 		redhair.jump_counter = 0
			# 		redhair.is_jumping = False
			# 		redhair.gravitational_force += 1







class Background:

	def __init__(self, image, x, y, width, height, layer):

		self.image = load(image).convert_alpha() # .convert_alpha() for faster bliting speed more on that here https://gamedev.stackexchange.com/questions/81280/pygame-surfaces-which-and-when-do-i-need-to-convert
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.layer = layer



	def scroll(self, speed):
		self.x += speed



# x,y
# top, left, bottom, right
# topleft, bottomleft, topright, bottomright
# midtop, midleft, midbottom, midright
# center, centerx, centery
# size, width, height
# w,h

class HitBox:

	def __init__(self, x, y, width, height, image=None, top_ffset=0, height_offset=0):

		self.rect = Rect(x, y, width, height)
		self.top_rect = Rect(self.rect.left, self.rect.midtop[1], self.rect.w, 1)
		self.bottom_rect = Rect(self.rect.left, self.rect.midbottom[1], self.rect.w, 1)
		self.right_rect = Rect(self.rect.midright[0], self.rect.top + top_ffset, 1, self.rect.h - height_offset)
		self.left_rect = Rect(self.rect.midleft[0], self.rect.top + top_ffset, 1, self.rect.h - height_offset)
		# offsets here are to keep the hitbox smooth
		self.image = image

		if image:
			self.load_image = load(image).convert_alpha()



class Game:

	def __init__(self, images):
		self.images = images
		self.indices_of_hit_list = []
		self.backgrounds = []

	def load_image(self, index):
		image = self.images[index]
		return load(image).convert_alpha()

	def scene_move_backgrounds(self, direction):
		for background in self.backgrounds:
			if direction == "right":
				background.scroll(background.layer)
			else:
				background.scroll(-background.layer)

	def move_world(self, objects, speed, direction):
		self.scene_move_backgrounds(direction)
		for index, obj in enumerate(objects):
			obj.rect.x += speed
			objects[index] = HitBox(obj.rect.x, obj.rect.y, obj.rect.width, obj.rect.height, obj.image, 4, 6)

		return objects

