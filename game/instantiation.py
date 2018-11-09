from game.classes import (Character, Background, HitBox, Game)
from game import width, height


# characters

redhair_images = {'idle':['game/assets/Character_01_Idle1.png', 'game/assets/Character_01_Idle2.png', 'game/assets/Character_01_Idle3.png',
 'game/assets/Character_01_Idle4.png', 'game/assets/Character_01_Idle5.png', 'game/assets/Character_01_Idle6.png', 'game/assets/Character_01_Idle7.png',
 'game/assets/Character_01_Idle8.png', 'game/assets/Character_01_Idle9.png', 'game/assets/Character_01_Idle10.png', 'game/assets/Character_01_Idle11.png',
  'game/assets/Character_01_Idle12.png'],
 'move_right':['game/assets/Character_01_Run_01.png', 'game/assets/Character_01_Run_02.png', 'game/assets/Character_01_Run_03.png',
 'game/assets/Character_01_Run_04.png', 'game/assets/Character_01_Run_05.png', 'game/assets/Character_01_Run_06.png',
 'game/assets/Character_01_Run_07.png', 'game/assets/Character_01_Run_08.png', 'game/assets/Character_01_Run_09.png',
 'game/assets/Character_01_Run_10.png', 'game/assets/Character_01_Run_11.png', 'game/assets/Character_01_Run_12.png',
 'game/assets/Character_01_Run_13.png', 'game/assets/Character_01_Run_14.png', 'game/assets/Character_01_Run_15.png'],
 'move_left':['game/assets/left_r1.png', 'game/assets/left_r2.png', 'game/assets/left_r3.png', 'game/assets/left_r4.png',
 'game/assets/left_r5.png', 'game/assets/left_r6.png', 'game/assets/left_r7.png', 'game/assets/left_r8.png',
 'game/assets/left_r9.png', 'game/assets/left_r10.png', 'game/assets/left_r11.png', 'game/assets/left_r12.png',
 'game/assets/left_r13.png', 'game/assets/left_r14.png', 'game/assets/left_r15.png']}

redhair = Character(width-100, 100, 22, 34, redhair_images, -19, -16)



# backgrounds
backgrounds = []


for i in range(9):
	for j in range(7):
		if i == 1:
			backgrounds.append(Background('game/assets/layer1.png', (928 * j) - 928, -99, 928, 793, 1))
		elif i == 2:
			backgrounds.append(Background('game/assets/layer2.png', (928 * j) - 928, -99, 928, 793, 2))
		elif i == 3:
			backgrounds.append(Background('game/assets/layer3.png', (928 * j) - 928, -99, 928, 793, 3))
		elif i == 4:
			backgrounds.append(Background('game/assets/layer4.png', (928 * j) - 928, -99, 928, 793, 4))
		elif i == 5:
			backgrounds.append(Background('game/assets/layer5.png', (928 * j) - 928, -99, 928, 793, 5))
		elif i == 6:
			backgrounds.append(Background('game/assets/layer6.png', (928 * j) - 928, -99, 928, 793, 6))
		elif i == 7:
			backgrounds.append(Background('game/assets/layer7.png', (928 * j) - 928, -99, 928, 793, 7))
		elif i == 8:
			backgrounds.append(Background('game/assets/layer8.png', (928 * j) - 928, -99, 928, 793, 8))
		elif i == 9:
			backgrounds.append(Background('game/assets/layer9.png', (928 * j) - 928, -99, 928, 793, 9))


# layer1 = Background('game/assets/layer1.png', 0, -99, 928, 793, 1) 
# layer1_2 = Background('game/assets/layer1.png', layer1.width, -99, 928, 793, 1)
# layer2 = Background('game/assets/layer2.png', 0, -99, 928, 793, 2) 
# layer2_2 = Background('game/assets/layer2.png', layer2.width, -99, 928, 793, 2) 
# layer3 = Background('game/assets/layer3.png', 0, -99, 928, 793, 3) 
# layer3_2 = Background('game/assets/layer3.png', layer3.width, -99, 928, 793, 3) 
# layer4 = Background('game/assets/layer4.png', 0, -99, 928, 793, 4) 
# layer4_2 = Background('game/assets/layer4.png', layer4.width, -99, 928, 793, 4) 
# layer5 = Background('game/assets/layer5.png', 0, -99, 928, 793, 5) 
# layer5_2 = Background('game/assets/layer5.png', layer5.width, -99, 928, 793, 5) 
# layer6 = Background('game/assets/layer6.png', 0, -99, 928, 793, 6) 
# layer6_2 = Background('game/assets/layer6.png', layer6.width, -99, 928, 793, 6) 
# layer7 = Background('game/assets/layer7.png', 0, -99, 928, 793, 7) 
# layer7_2 = Background('game/assets/layer7.png', layer7.width, -99, 928, 793, 7) 
# layer8 = Background('game/assets/layer8.png', 0, -99, 928, 793, 8) 
# layer8_2 = Background('game/assets/layer8.png', layer8.width, -99, 928, 793, 8) 
# layer9 = Background('game/assets/layer9.png', 0, -99, 928, 793, 9) 
# layer9_2 = Background('game/assets/layer9.png', layer9.width, -99, 928, 793, 9) 

# backgrounds = [
# 	layer1,
# 	layer1_2,
# 	layer2,
# 	layer2_2,
# 	layer3,
# 	layer3_2,
# 	layer4,
# 	layer4_2,
# 	layer5,
# 	layer5_2,
# 	layer6,
# 	layer6_2,
# 	layer7,
# 	layer7_2,
# 	layer8,
# 	layer8_2,
# 	layer9,
# 	layer9_2
# 	]






# Hitboxes / Surfaces

surface1 = HitBox(0 - 12000 / 2, height - 43, 12000, 43)
crate1 = HitBox(100, surface1.rect.top - 35, 39, 35, 'game/assets/crate.png', 4, 6)



surfaces = [surface1, crate1]
tops = [surface1]







# Game
game = Game(images=['game/assets/instructions2.png'])
game.images.append('game/assets/Pixel Art Plataformer Painted Style.png')
game.images.append('game/assets/Pixel Art Runner.png')
game.images.append('game/assets/Pixel Art Forest.png')
game.images.append('game/assets/Pixel Art Snowy Forest.png')
game.images.append('game/assets/game.jpg')
game.backgrounds = backgrounds

