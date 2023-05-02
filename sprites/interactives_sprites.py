# ################################################################ #
# ############################ PORTAL ############################ #
import pygame

from settings.general_settings import GENERAL
from settings.interactives_settings import SKULL, ENERGY, PORTAL
from utilities import get_sprites

portal_sheet = pygame.image.load(
    "images/interactives/portal/portal_sheet.png").convert_alpha()
PORTAL_SPRITES = get_sprites(sheet=portal_sheet,
                             number_sprites=17,
                             width=PORTAL["sprite_width"],
                             height=PORTAL["sprite_height"],
                             scale=PORTAL["size"],
                             color=GENERAL["black"])

# ################################################################ #
# ############################ ENERGY ############################ #
energy_sheet = pygame.image.load(
    "images/interactives/energy/energy_sheet.png").convert_alpha()
ENERGY_SPRITES = get_sprites(sheet=energy_sheet,
                             number_sprites=11,
                             width=ENERGY["sprite_width"],
                             height=ENERGY["sprite_height"],
                             scale=ENERGY["size"],
                             color=GENERAL["black"])

# ############################################################### #
# ############################ SKULL ############################ #
skull_sheet = pygame.image.load(
    "images/interactives/skull/skull_sheet.png").convert_alpha()
SKULL_SPRITES = get_sprites(sheet=skull_sheet,
                            number_sprites=7,
                            width=SKULL["sprite_width"],
                            height=SKULL["sprite_height"],
                            scale=SKULL["size"],
                            color=GENERAL["black"])
