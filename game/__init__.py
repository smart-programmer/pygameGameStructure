from pygame.display import set_mode
import pygame
from win32api import GetSystemMetrics
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)

width = GetSystemMetrics(0)
height = GetSystemMetrics(1) - 30 #70 if you want the ui tape to appear or make it less than 39 if you don't


screen = set_mode((width, height))
load = pygame.image.load('game/assets/load.jpeg')
screen.blit(load, (270, 265))
pygame.display.update()