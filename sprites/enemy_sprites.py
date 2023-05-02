import pygame

from settings.enemy_settings import SKULL_COLLECTOR_SIZE, RUSHER_SIZE, GOLEM_SIZE
from settings.general_settings import GENERAL, SKULL_COLLECTOR_SPRITE_WIDTH, \
    SKULL_COLLECTOR_SPRITE_HEIGHT, RUSHER_SPRITE_WIDTH, RUSHER_SPRITE_HEIGHT, GOLEM_SPRITE_WIDTH, \
    GOLEM_SPRITE_HEIGHT
from utilities import get_sprites

# ######################################################################### #
# ############################ SKULL COLLECTOR ############################ #
skull_collector_walk_sheet = pygame.image.load(
    "images/enemies/skull_collector/walk_sheet.png").convert_alpha()
SKULL_COLLECTOR_WALK_SPRITES = get_sprites(sheet=skull_collector_walk_sheet,
                                           number_sprites=8,
                                           width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                           height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                           scale=SKULL_COLLECTOR_SIZE,
                                           color=GENERAL["black"])
skull_collector_walk_sheet_flipped = pygame.image.load(
    "images/enemies/skull_collector/walk_sheet_flipped.png").convert_alpha()
SKULL_COLLECTOR_WALK_SPRITES_FLIPPED = get_sprites(sheet=skull_collector_walk_sheet_flipped,
                                                   number_sprites=8,
                                                   width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                                   height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                                   scale=SKULL_COLLECTOR_SIZE,
                                                   color=GENERAL["black"])

skull_collector_shoot_sheet = pygame.image.load(
    "images/enemies/skull_collector/shoot_sheet.png").convert_alpha()
SKULL_COLLECTOR_SHOOT_SPRITES = get_sprites(sheet=skull_collector_shoot_sheet,
                                            number_sprites=13,
                                            width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                            height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                            scale=SKULL_COLLECTOR_SIZE,
                                            color=GENERAL["black"])
skull_collector_shoot_sheet_flipped = pygame.image.load(
    "images/enemies/skull_collector/shoot_sheet_flipped.png").convert_alpha()
SKULL_COLLECTOR_SHOOT_SPRITES_FLIPPED = get_sprites(sheet=skull_collector_shoot_sheet_flipped,
                                                    number_sprites=13,
                                                    width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                                    height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                                    scale=SKULL_COLLECTOR_SIZE,
                                                    color=GENERAL["black"])

skull_collector_death_sheet = pygame.image.load(
    "images/enemies/skull_collector/death_sheet.png").convert_alpha()
SKULL_COLLECTOR_DEATH_SPRITES = get_sprites(sheet=skull_collector_death_sheet,
                                            number_sprites=9,
                                            width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                            height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                            scale=SKULL_COLLECTOR_SIZE,
                                            color=GENERAL["black"])

# ################################################################ #
# ############################ RUSHER ############################ #
rusher_idle_sheet = pygame.image.load(
    "images/enemies/rusher/idle_sheet.png").convert_alpha()
RUSHER_IDLE_SPRITES = get_sprites(sheet=rusher_idle_sheet,
                                  number_sprites=9,
                                  width=RUSHER_SPRITE_WIDTH,
                                  height=RUSHER_SPRITE_HEIGHT,
                                  scale=RUSHER_SIZE,
                                  color=GENERAL["black"])
rusher_idle_sheet_flipped = pygame.image.load(
    "images/enemies/rusher/idle_sheet_flipped.png").convert_alpha()
RUSHER_IDLE_SPRITES_FLIPPED = get_sprites(sheet=rusher_idle_sheet_flipped,
                                          number_sprites=9,
                                          width=RUSHER_SPRITE_WIDTH,
                                          height=RUSHER_SPRITE_HEIGHT,
                                          scale=RUSHER_SIZE,
                                          color=GENERAL["black"])

rusher_run_sheet = pygame.image.load(
    "images/enemies/rusher/run_sheet.png").convert_alpha()
RUSHER_RUN_SPRITES = get_sprites(sheet=rusher_run_sheet,
                                 number_sprites=6,
                                 width=RUSHER_SPRITE_WIDTH,
                                 height=RUSHER_SPRITE_HEIGHT,
                                 scale=RUSHER_SIZE,
                                 color=GENERAL["black"])
rusher_run_sheet_flipped = pygame.image.load(
    "images/enemies/rusher/run_sheet_flipped.png").convert_alpha()
RUSHER_RUN_SPRITES_FLIPPED = get_sprites(sheet=rusher_run_sheet_flipped,
                                         number_sprites=6,
                                         width=RUSHER_SPRITE_WIDTH,
                                         height=RUSHER_SPRITE_HEIGHT,
                                         scale=RUSHER_SIZE,
                                         color=GENERAL["black"])

rusher_strike_sheet = pygame.image.load(
    "images/enemies/rusher/strike_sheet.png").convert_alpha()
RUSHER_STRIKE_SPRITES = get_sprites(sheet=rusher_strike_sheet,
                                    number_sprites=12,
                                    width=RUSHER_SPRITE_WIDTH,
                                    height=RUSHER_SPRITE_HEIGHT,
                                    scale=RUSHER_SIZE,
                                    color=GENERAL["black"])
rusher_strike_sheet_flipped = pygame.image.load(
    "images/enemies/rusher/strike_sheet_flipped.png").convert_alpha()
RUSHER_STRIKE_SPRITES_FLIPPED = get_sprites(sheet=rusher_strike_sheet_flipped,
                                            number_sprites=12,
                                            width=RUSHER_SPRITE_WIDTH,
                                            height=RUSHER_SPRITE_HEIGHT,
                                            scale=RUSHER_SIZE,
                                            color=GENERAL["black"])

rusher_death_sheet = pygame.image.load(
    "images/enemies/rusher/death_sheet.png").convert_alpha()
RUSHER_DEATH_SPRITES = get_sprites(sheet=rusher_death_sheet,
                                   number_sprites=23,
                                   width=RUSHER_SPRITE_WIDTH,
                                   height=RUSHER_SPRITE_HEIGHT,
                                   scale=RUSHER_SIZE,
                                   color=GENERAL["black"])

# ############################################################### #
# ############################ GOLEM ############################ #
golem_walk_sheet = pygame.image.load(
    "images/enemies/golem/walk_sheet.png").convert_alpha()
GOLEM_WALK_SPRITES = get_sprites(sheet=golem_walk_sheet,
                                 number_sprites=16,
                                 width=GOLEM_SPRITE_WIDTH,
                                 height=GOLEM_SPRITE_HEIGHT,
                                 scale=GOLEM_SIZE,
                                 color=GENERAL["black"])
golem_walk_sheet_flipped = pygame.image.load(
    "images/enemies/golem/walk_sheet_flipped.png").convert_alpha()
GOLEM_WALK_SPRITES_FLIPPED = get_sprites(sheet=golem_walk_sheet_flipped,
                                         number_sprites=16,
                                         width=GOLEM_SPRITE_WIDTH,
                                         height=GOLEM_SPRITE_HEIGHT,
                                         scale=GOLEM_SIZE,
                                         color=GENERAL["black"])
golem_run_sheet = pygame.image.load(
    "images/enemies/golem/run_sheet.png").convert_alpha()
GOLEM_RUN_SPRITES = get_sprites(sheet=golem_run_sheet,
                                number_sprites=16,
                                width=GOLEM_SPRITE_WIDTH,
                                height=GOLEM_SPRITE_HEIGHT,
                                scale=GOLEM_SIZE,
                                color=GENERAL["black"])
golem_run_sheet_flipped = pygame.image.load(
    "images/enemies/golem/run_sheet_flipped.png").convert_alpha()
GOLEM_RUN_SPRITES_FLIPPED = get_sprites(sheet=golem_run_sheet_flipped,
                                        number_sprites=16,
                                        width=GOLEM_SPRITE_WIDTH,
                                        height=GOLEM_SPRITE_HEIGHT,
                                        scale=GOLEM_SIZE,
                                        color=GENERAL["black"])
golem_strike_sheet = pygame.image.load(
    "images/enemies/golem/jump_sheet.png").convert_alpha()
GOLEM_STRIKE_SPRITES = get_sprites(sheet=golem_strike_sheet,
                                   number_sprites=16,
                                   width=GOLEM_SPRITE_WIDTH,
                                   height=GOLEM_SPRITE_HEIGHT,
                                   scale=GOLEM_SIZE,
                                   color=GENERAL["black"])
golem_strike_sheet_flipped = pygame.image.load(
    "images/enemies/golem/jump_sheet_flipped.png").convert_alpha()
GOLEM_STRIKE_SPRITES_FLIPPED = get_sprites(sheet=golem_strike_sheet_flipped,
                                           number_sprites=16,
                                           width=GOLEM_SPRITE_WIDTH,
                                           height=GOLEM_SPRITE_HEIGHT,
                                           scale=GOLEM_SIZE,
                                           color=GENERAL["black"])

golem_death_sheet = pygame.image.load(
    "images/enemies/golem/jump_sheet_flipped.png").convert_alpha()
GOLEM_DEATH_SPRITES = get_sprites(sheet=golem_death_sheet,
                                  number_sprites=16,
                                  width=GOLEM_SPRITE_WIDTH,
                                  height=GOLEM_SPRITE_HEIGHT,
                                  scale=GOLEM_SIZE,
                                  color=GENERAL["black"])
