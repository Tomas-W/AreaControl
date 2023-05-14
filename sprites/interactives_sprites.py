import os
import sys

import pygame

from settings.general_settings import GENERAL, ENERGY_SIZE, PORTAL_SIZE, PORTAL_SPRITE_WIDTH, \
    SKULL_SPRITE_WIDTH, SKULL_SPRITE_HEIGHT, ENERGY_SPRITE_HEIGHT, ENERGY_SPRITE_WIDTH, \
    PORTAL_SPRITE_HEIGHT, SKULL_SIZE, COIN_SPRITE_WIDTH, COIN_SPRITE_HEIGHT, COIN_SIZE
from utilities import get_sprites

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# ################################################################ #
# ############################ PORTAL ############################ #
portal_sheet = pygame.image.load(
    os.path.join(base_dir, "images/interactives/portal/portal_sheet.png")).convert_alpha()
PORTAL_SPRITES = get_sprites(sheet=portal_sheet,
                             number_sprites=17,
                             width=PORTAL_SPRITE_WIDTH,
                             height=PORTAL_SPRITE_HEIGHT,
                             scale=PORTAL_SIZE,
                             color=GENERAL["black"])

# ################################################################ #
# ############################ ENERGY ############################ #
energy_sheet = pygame.image.load(
    os.path.join(base_dir, "images/interactives/energy/energy_sheet.png")).convert_alpha()
ENERGY_SPRITES = get_sprites(sheet=energy_sheet,
                             number_sprites=11,
                             width=ENERGY_SPRITE_WIDTH,
                             height=ENERGY_SPRITE_HEIGHT,
                             scale=ENERGY_SIZE,
                             color=GENERAL["black"])

# ############################################################### #
# ############################ SKULL ############################ #
skull_sheet = pygame.image.load(
    os.path.join(base_dir, "images/interactives/skull/skull_sheet.png")).convert_alpha()
SKULL_SPRITES = get_sprites(sheet=skull_sheet,
                            number_sprites=7,
                            width=SKULL_SPRITE_WIDTH,
                            height=SKULL_SPRITE_HEIGHT,
                            scale=SKULL_SIZE,
                            color=GENERAL["black"])

# ############################################################## #
# ############################ COIN ############################ #
coin_sheet = pygame.image.load(
    os.path.join(base_dir, "images/interactives/coin/coin_sheet.png")).convert_alpha()
COIN_SPRITES = get_sprites(sheet=coin_sheet,
                            number_sprites=6,
                            width=COIN_SPRITE_WIDTH,
                            height=COIN_SPRITE_HEIGHT,
                            scale=COIN_SIZE,
                            color=GENERAL["black"])
