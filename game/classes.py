from pygame.image import load
from pygame import Rect


# make gravity it's own object then pass it to each character

class Character:

	def __init__(self, x, y, width, height, images, xoffset=0, yoffset=0):

		self.rect = Rect(x , y, width, height)
		self.xoffset = xoffset
		self.yoffset = yoffset
		self.images = images
		self.imageCounter = 0
		self.loadedImage = load(self.images['idle'][self.imageCounter]).convert_alpha()
		self.velocity = 0
		self.y_velocity = 0
		self.animation_counter = 0
		self.gravitational_force = 3
		self.jump_counter = 10
		self.is_jumping = False


	def animation(self, animationType):

		if self.imageCounter > len(self.images[animationType]) - 2:
			self.imageCounter = 0
		else:
			self.imageCounter += 1

		self.loadedImage = load(self.images[animationType][self.imageCounter]).convert_alpha()


	def move_horizontale(self):
		self.rect.x += self.velocity
		self.animation_counter += 1

		if self.animation_counter > 3:
			self.animation_counter = 0
			if self.velocity > 0:
				self.animation('move_right')
			elif self.velocity < 0:
				self.animation('move_left')
			elif self.velocity == 0:
				self.animation('idle')


	def gravity(self):
		self.rect.y += self.gravitational_force


	def jump(self):
		self.rect.y -= self.y_velocity








class Background:

	def __init__(self, image, x, y, width, height, layer):

		self.image = load(image).convert_alpha() # .convert_alpha() for faster bliting speed more on that here https://gamedev.stackexchange.com/questions/81280/pygame-surfaces-which-and-when-do-i-need-to-convert
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.layer = layer



	def scroll(self):
		pass





class HitBox:

	def __init__(self, x, y, width, height, image=None):

		self.rect = Rect(x, y, width, height)
		if image:
			self.image = load(image)



class Game:

	def __init__(self):
		self.screen = 'intro'
		self.images = []

	def load_image(self, index):
		image = self.images[index]
		return load(image)

