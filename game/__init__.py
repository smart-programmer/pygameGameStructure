from pygame.display import set_mode
import pygame
from win32api import GetSystemMetrics

width = 928
height = GetSystemMetrics(1) - 95


screen = set_mode((width, height))
load = pygame.image.load('game/assets/load.jpeg')
screen.blit(load, (270, 265))
pygame.display.update()