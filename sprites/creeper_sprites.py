import pygame

from settings.general_settings import BAT_SPRITE_WIDTH, BAT_SPRITE_HEIGHT, BAT_SIZE, GENERAL
from utilities import get_sprites

# ############################################################# #
# ############################ BAT ############################ #
bat_sheet = pygame.image.load(
    "images/creepers/bat_sheet.png").convert_alpha()
BAT_SPRITES = get_sprites(sheet=bat_sheet,
                          number_sprites=7,
                          width=BAT_SPRITE_WIDTH,
                          height=BAT_SPRITE_HEIGHT,
                          scale=BAT_SIZE,
                          color=GENERAL["black"])
bat_sheet_flipped = pygame.image.load(
    "images/creepers/bat_sheet_flipped.png").convert_alpha()
BAT_SPRITES_FLIPPED = get_sprites(sheet=bat_sheet_flipped,
                                  number_sprites=7,
                                  width=BAT_SPRITE_WIDTH,
                                  height=BAT_SPRITE_HEIGHT,
                                  scale=BAT_SIZE,
                                  color=GENERAL["black"])
