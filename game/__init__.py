from pygame.display import set_mode
from win32api import GetSystemMetrics

width = 928
height = GetSystemMetrics(1) - 95


screen = set_mode((width, height))