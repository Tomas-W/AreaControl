import os
import sys

import pygame

from settings.general_settings import GENERAL, ENERGY_SIZE, PORTAL_SIZE, PORTAL_SPRITE_WIDTH, \
    SKULL_SPRITE_WIDTH, SKULL_SPRITE_HEIGHT, ENERGY_SPRITE_HEIGHT, ENERGY_SPRITE_WIDTH, \
    PORTAL_SPRITE_HEIGHT, SKULL_SIZE, COIN_SPRITE_WIDTH, COIN_SPRITE_HEIGHT, COIN_SIZE, \
    HEALTH_POTION_SPRITE_WIDTH, HEALTH_POTION_SPRITE_HEIGHT, HEALTH_POTION_SIZE, DOOR_SPRITE_WIDTH, \
    DOOR_SIZE, DOOR_SPRITE_HEIGHT
from utilities.general import get_sprites

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

# ####################################################################### #
# ############################ HEALTH POTION ############################ #
health_potion_sheet = pygame.image.load(
    os.path.join(base_dir, "images/interactives/health/health_potion_sheet.png")).convert_alpha()
HEALTH_POTION_SPRITES = get_sprites(sheet=health_potion_sheet,
                                    number_sprites=13,
                                    width=HEALTH_POTION_SPRITE_WIDTH,
                                    height=HEALTH_POTION_SPRITE_HEIGHT,
                                    scale=HEALTH_POTION_SIZE,
                                    color=GENERAL["black"])

# ############################################################### #
# ############################ DOORS ############################ #
door_red_sheet = pygame.image.load(
    os.path.join(base_dir, "images/interactives/doors/door_red.png")).convert_alpha()
DOOR_RED_SPRITES = get_sprites(sheet=door_red_sheet,
                               number_sprites=6,
                               width=DOOR_SPRITE_WIDTH,
                               height=DOOR_SPRITE_HEIGHT,
                               scale=DOOR_SIZE,
                               color=GENERAL["black"])

door_blue_sheet = pygame.image.load(
    os.path.join(base_dir, "images/interactives/doors/door_blue.png")).convert_alpha()
DOOR_BLUE_SPRITES = get_sprites(sheet=door_blue_sheet,
                                number_sprites=6,
                                width=DOOR_SPRITE_WIDTH,
                                height=DOOR_SPRITE_HEIGHT,
                                scale=DOOR_SIZE,
                                color=GENERAL["black"])

door_green_sheet = pygame.image.load(
    os.path.join(base_dir, "images/interactives/doors/door_green.png")).convert_alpha()
DOOR_GREEN_SPRITES = get_sprites(sheet=door_green_sheet,
                                 number_sprites=6,
                                 width=DOOR_SPRITE_WIDTH,
                                 height=DOOR_SPRITE_HEIGHT,
                                 scale=DOOR_SIZE,
                                 color=GENERAL["black"])

door_yellow_sheet = pygame.image.load(
    os.path.join(base_dir, "images/interactives/doors/door_yellow.png")).convert_alpha()
DOOR_YELLOW_SPRITES = get_sprites(sheet=door_yellow_sheet,
                                  number_sprites=6,
                                  width=DOOR_SPRITE_WIDTH,
                                  height=DOOR_SPRITE_HEIGHT,
                                  scale=DOOR_SIZE,
                                  color=GENERAL["black"])
