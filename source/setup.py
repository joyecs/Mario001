import pygame
from . import config
from . import tools

pygame.init()
SCREEN = pygame.display.set_mode((config.SCREEN_W, config.SCREEN_H))

GRAPHICS = tools.load_graphics('resources/graphics')