import os
import sys

import pygame

from settings.enemy_settings import SKULL_COLLECTOR_SIZE, RUSHER_SIZE, GOLEM_SIZE
from settings.general_settings import GENERAL, SKULL_COLLECTOR_SPRITE_WIDTH, \
    SKULL_COLLECTOR_SPRITE_HEIGHT, RUSHER_SPRITE_WIDTH, RUSHER_SPRITE_HEIGHT, GOLEM_SPRITE_WIDTH, \
    GOLEM_SPRITE_HEIGHT
from utilities.general import get_sprites

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# ######################################################################### #
# ############################ SKULL COLLECTOR ############################ #
skull_collector_spawn_sheet = None
SKULL_COLLECTOR_SPAWN_SPRITES = None

skull_collector_walk_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/skull_collector/skull_collector_walk.png")).convert_alpha()
SKULL_COLLECTOR_WALK_SPRITES = get_sprites(sheet=skull_collector_walk_sheet,
                                           number_sprites=8,
                                           width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                           height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                           scale=SKULL_COLLECTOR_SIZE,
                                           color=GENERAL["black"])
skull_collector_walk_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/skull_collector/skull_collector_walk_flipped.png")).convert_alpha()
SKULL_COLLECTOR_WALK_SPRITES_FLIPPED = get_sprites(sheet=skull_collector_walk_sheet_flipped,
                                                   number_sprites=8,
                                                   width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                                   height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                                   scale=SKULL_COLLECTOR_SIZE,
                                                   color=GENERAL["black"])

skull_collector_shoot_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/skull_collector/skull_collector_shoot.png")).convert_alpha()
SKULL_COLLECTOR_SHOOT_SPRITES = get_sprites(sheet=skull_collector_shoot_sheet,
                                            number_sprites=9,
                                            width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                            height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                            scale=SKULL_COLLECTOR_SIZE,
                                            color=GENERAL["black"])
skull_collector_shoot_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/skull_collector/skull_collector_shoot_flipped.png")).convert_alpha()
SKULL_COLLECTOR_SHOOT_SPRITES_FLIPPED = get_sprites(sheet=skull_collector_shoot_sheet_flipped,
                                                    number_sprites=9,
                                                    width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                                    height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                                    scale=SKULL_COLLECTOR_SIZE,
                                                    color=GENERAL["black"])

skull_collector_death_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/skull_collector/skull_collector_death.png")).convert_alpha()
SKULL_COLLECTOR_DEATH_SPRITES = get_sprites(sheet=skull_collector_death_sheet,
                                            number_sprites=9,
                                            width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                            height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                            scale=SKULL_COLLECTOR_SIZE,
                                            color=GENERAL["black"])
skull_collector_death_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/skull_collector/skull_collector_death_flipped.png")).convert_alpha()
SKULL_COLLECTOR_DEATH_SPRITES_FLIPPED = get_sprites(sheet=skull_collector_death_sheet_flipped,
                                                    number_sprites=9,
                                                    width=SKULL_COLLECTOR_SPRITE_WIDTH,
                                                    height=SKULL_COLLECTOR_SPRITE_HEIGHT,
                                                    scale=SKULL_COLLECTOR_SIZE,
                                                    color=GENERAL["black"])

# ################################################################ #
# ############################ RUSHER ############################ #
rusher_spawn_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/rusher/rusher_spawn.png")).convert_alpha()
RUSHER_SPAWN_SPRITES = get_sprites(sheet=rusher_spawn_sheet,
                                   number_sprites=19,
                                   width=RUSHER_SPRITE_WIDTH,
                                   height=RUSHER_SPRITE_HEIGHT,
                                   scale=RUSHER_SIZE,
                                   color=GENERAL["black"])

rusher_idle_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/rusher/rusher_idle.png")).convert_alpha()
RUSHER_IDLE_SPRITES = get_sprites(sheet=rusher_idle_sheet,
                                  number_sprites=9,
                                  width=RUSHER_SPRITE_WIDTH,
                                  height=RUSHER_SPRITE_HEIGHT,
                                  scale=RUSHER_SIZE,
                                  color=GENERAL["black"])
rusher_idle_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/rusher/rusher_idle_flipped.png")).convert_alpha()
RUSHER_IDLE_SPRITES_FLIPPED = get_sprites(sheet=rusher_idle_sheet_flipped,
                                          number_sprites=9,
                                          width=RUSHER_SPRITE_WIDTH,
                                          height=RUSHER_SPRITE_HEIGHT,
                                          scale=RUSHER_SIZE,
                                          color=GENERAL["black"])

rusher_run_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/rusher/rusher_run.png")).convert_alpha()
RUSHER_RUN_SPRITES = get_sprites(sheet=rusher_run_sheet,
                                 number_sprites=6,
                                 width=RUSHER_SPRITE_WIDTH,
                                 height=RUSHER_SPRITE_HEIGHT,
                                 scale=RUSHER_SIZE,
                                 color=GENERAL["black"])
rusher_run_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/rusher/rusher_run_flipped.png")).convert_alpha()
RUSHER_RUN_SPRITES_FLIPPED = get_sprites(sheet=rusher_run_sheet_flipped,
                                         number_sprites=6,
                                         width=RUSHER_SPRITE_WIDTH,
                                         height=RUSHER_SPRITE_HEIGHT,
                                         scale=RUSHER_SIZE,
                                         color=GENERAL["black"])

rusher_strike_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/rusher/rusher_strike.png")).convert_alpha()
RUSHER_STRIKE_SPRITES = get_sprites(sheet=rusher_strike_sheet,
                                    number_sprites=12,
                                    width=RUSHER_SPRITE_WIDTH,
                                    height=RUSHER_SPRITE_HEIGHT,
                                    scale=RUSHER_SIZE,
                                    color=GENERAL["black"])
rusher_strike_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/rusher/rusher_strike_flipped.png")).convert_alpha()
RUSHER_STRIKE_SPRITES_FLIPPED = get_sprites(sheet=rusher_strike_sheet_flipped,
                                            number_sprites=12,
                                            width=RUSHER_SPRITE_WIDTH,
                                            height=RUSHER_SPRITE_HEIGHT,
                                            scale=RUSHER_SIZE,
                                            color=GENERAL["black"])

rusher_death_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/rusher/rusher_death.png")).convert_alpha()
RUSHER_DEATH_SPRITES = get_sprites(sheet=rusher_death_sheet,
                                   number_sprites=19,
                                   width=RUSHER_SPRITE_WIDTH,
                                   height=RUSHER_SPRITE_HEIGHT,
                                   scale=RUSHER_SIZE,
                                   color=GENERAL["black"])
rusher_death_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/rusher/rusher_death_flipped.png")).convert_alpha()
RUSHER_DEATH_SPRITES_FLIPPED = get_sprites(sheet=rusher_death_sheet_flipped,
                                           number_sprites=19,
                                           width=RUSHER_SPRITE_WIDTH,
                                           height=RUSHER_SPRITE_HEIGHT,
                                           scale=RUSHER_SIZE,
                                           color=GENERAL["black"])

# ############################################################### #
# ############################ GOLEM ############################ #
golem_walk_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/golem/walk_sheet.png")).convert_alpha()
GOLEM_WALK_SPRITES = get_sprites(sheet=golem_walk_sheet,
                                 number_sprites=16,
                                 width=GOLEM_SPRITE_WIDTH,
                                 height=GOLEM_SPRITE_HEIGHT,
                                 scale=GOLEM_SIZE,
                                 color=GENERAL["black"])
golem_walk_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/golem/walk_sheet_flipped.png")).convert_alpha()
GOLEM_WALK_SPRITES_FLIPPED = get_sprites(sheet=golem_walk_sheet_flipped,
                                         number_sprites=16,
                                         width=GOLEM_SPRITE_WIDTH,
                                         height=GOLEM_SPRITE_HEIGHT,
                                         scale=GOLEM_SIZE,
                                         color=GENERAL["black"])
golem_run_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/golem/run_sheet.png")).convert_alpha()
GOLEM_RUN_SPRITES = get_sprites(sheet=golem_run_sheet,
                                number_sprites=16,
                                width=GOLEM_SPRITE_WIDTH,
                                height=GOLEM_SPRITE_HEIGHT,
                                scale=GOLEM_SIZE,
                                color=GENERAL["black"])
golem_run_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/golem/run_sheet_flipped.png")).convert_alpha()
GOLEM_RUN_SPRITES_FLIPPED = get_sprites(sheet=golem_run_sheet_flipped,
                                        number_sprites=16,
                                        width=GOLEM_SPRITE_WIDTH,
                                        height=GOLEM_SPRITE_HEIGHT,
                                        scale=GOLEM_SIZE,
                                        color=GENERAL["black"])
golem_strike_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/golem/jump_sheet.png")).convert_alpha()
GOLEM_STRIKE_SPRITES = get_sprites(sheet=golem_strike_sheet,
                                   number_sprites=16,
                                   width=GOLEM_SPRITE_WIDTH,
                                   height=GOLEM_SPRITE_HEIGHT,
                                   scale=GOLEM_SIZE,
                                   color=GENERAL["black"])
golem_strike_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/golem/jump_sheet_flipped.png")).convert_alpha()
GOLEM_STRIKE_SPRITES_FLIPPED = get_sprites(sheet=golem_strike_sheet_flipped,
                                           number_sprites=16,
                                           width=GOLEM_SPRITE_WIDTH,
                                           height=GOLEM_SPRITE_HEIGHT,
                                           scale=GOLEM_SIZE,
                                           color=GENERAL["black"])

golem_death_sheet = pygame.image.load(
    os.path.join(base_dir, "images/enemies/golem/jump_sheet_flipped.png")).convert_alpha()
GOLEM_DEATH_SPRITES = get_sprites(sheet=golem_death_sheet,
                                  number_sprites=16,
                                  width=GOLEM_SPRITE_WIDTH,
                                  height=GOLEM_SPRITE_HEIGHT,
                                  scale=GOLEM_SIZE,
                                  color=GENERAL["black"])
golem_death_sheet_flipped = pygame.image.load(
    os.path.join(base_dir, "images/enemies/golem/jump_sheet_flipped.png")).convert_alpha()
GOLEM_DEATH_SPRITES_FLIPPED = get_sprites(sheet=golem_death_sheet_flipped,
                                          number_sprites=16,
                                          width=GOLEM_SPRITE_WIDTH,
                                          height=GOLEM_SPRITE_HEIGHT,
                                          scale=GOLEM_SIZE,
                                          color=GENERAL["black"])
