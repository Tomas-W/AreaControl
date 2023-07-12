import os
import sys

import pygame

from settings.general_settings import FLAMING_SKULL_SIZE, BULLET_SIZE, BOMB_SPRITE_WIDTH, \
    BOMB_SPRITE_HEIGHT, BOMB_SIZE, GENERAL
from utilities.helpers import get_sprites

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

flaming_skull_image = pygame.image.load(
    os.path.join(base_dir, "./images/projectiles/flaming_skull.png")).convert_alpha()
FLAMING_SKULL_SPRITE = pygame.transform.rotozoom(flaming_skull_image,
                                                 False,
                                                 FLAMING_SKULL_SIZE)

bullet_image = pygame.image.load(
    os.path.join(base_dir, "./images/projectiles/bullet_blue.png")).convert_alpha()
BULLET_SPRITE = pygame.transform.rotozoom(bullet_image,
                                          False,
                                          BULLET_SIZE)

bomb_sheet = pygame.image.load(
    os.path.join(base_dir, "./images/projectiles/bomb_sheet.png")).convert_alpha()
BOMB_SPRITES = get_sprites(sheet=bomb_sheet,
                           number_sprites=8,
                           width=BOMB_SPRITE_WIDTH,
                           height=BOMB_SPRITE_HEIGHT,
                           scale=BOMB_SIZE,
                           color=GENERAL["black"])

bomb_explosion_sheet = pygame.image.load(
    os.path.join(base_dir, "./images/projectiles/bomb_explosion_sheet.png")).convert_alpha()
BOMB_EXPLOSION_SPRITES = get_sprites(sheet=bomb_explosion_sheet,
                                     number_sprites=14,
                                     width=BOMB_SPRITE_WIDTH,
                                     height=BOMB_SPRITE_HEIGHT,
                                     scale=BOMB_SIZE * 3,
                                     color=GENERAL["black"])
