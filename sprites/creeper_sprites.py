import pygame

from settings.general_settings import BAT_SPRITE_WIDTH, BAT_SPRITE_HEIGHT, BAT_SIZE, GENERAL, \
    FISH_SPRITE_WIDTH, FISH_SPRITE_HEIGHT, FISH_SIZE
from utilities import get_sprites

# ############################################################# #
# ############################ BAT ############################ #
bat_sheet = pygame.image.load(
    "images/creepers/bat/bat_walk.png").convert_alpha()
BAT_SPRITES = get_sprites(sheet=bat_sheet,
                          number_sprites=7,
                          width=BAT_SPRITE_WIDTH,
                          height=BAT_SPRITE_HEIGHT,
                          scale=BAT_SIZE,
                          color=GENERAL["black"])
bat_sheet_flipped = pygame.image.load(
    "images/creepers/bat/bat_walk_flipped.png").convert_alpha()
BAT_SPRITES_FLIPPED = get_sprites(sheet=bat_sheet_flipped,
                                  number_sprites=7,
                                  width=BAT_SPRITE_WIDTH,
                                  height=BAT_SPRITE_HEIGHT,
                                  scale=BAT_SIZE,
                                  color=GENERAL["black"])

# ############################################################## #
# ############################ FISH ############################ #
fish_sheet = pygame.image.load(
    "images/creepers/fish/fish_walk.png").convert_alpha()
FISH_SPRITES = get_sprites(sheet=fish_sheet,
                           number_sprites=6,
                           width=FISH_SPRITE_WIDTH,
                           height=FISH_SPRITE_HEIGHT,
                           scale=FISH_SIZE,
                           color=GENERAL["black"])
fish_sheet_flipped = pygame.image.load(
    "images/creepers/fish/fish_walk_flipped.png").convert_alpha()
FISH_SPRITES_FLIPPED = get_sprites(sheet=fish_sheet_flipped,
                                   number_sprites=6,
                                   width=FISH_SPRITE_WIDTH,
                                   height=FISH_SPRITE_HEIGHT,
                                   scale=FISH_SIZE,
                                   color=GENERAL["black"])
