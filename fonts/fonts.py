import os
import sys

import pygame


base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

TINY_FONT = pygame.font.Font(os.path.join(base_dir, "fonts/PublicPixel.ttf"), 11)
SMALL_FONT = pygame.font.Font(os.path.join(base_dir, "fonts/PublicPixel.ttf"), 15)
MEDIUM_FONT = pygame.font.Font(os.path.join(base_dir, "fonts/PublicPixel.ttf"), 30)
LARGE_FONT = pygame.font.Font(os.path.join(base_dir, "fonts/PublicPixel.ttf"), 45)
FONT_COLOR = (255, 255, 255)
