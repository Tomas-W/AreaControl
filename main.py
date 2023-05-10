from random import choice

import pygame
from pygame.locals import *

from settings.general_settings import GENERAL

# INIT PYGAME #
pygame.init()
screen = pygame.display.set_mode((GENERAL["width"],
                                  GENERAL["height"]),
                                 16)
background = pygame.image.load(GENERAL["background_path"]).convert_alpha()
pygame.display.set_caption(GENERAL["title"])
# INIT PYGAME #

from utilities import all_sprites, handle_outgoing_projectiles, handle_incoming_projectiles, \
    handle_pickups
from settings.enemy_settings import SKULL_COLLECTOR, RUSHER

from characters.player import Player
from characters.skull_collector import SkullCollector
from characters.rusher import Rusher
from creepers.bat import Bat
from creepers.fish import Fish
from settings.creeper_settings import BAT, FISH

from camera import Camera


from settings.player_settings import PLAYER
from settings.projectile_settings import BULLET

# Characters
player = Player()
skull_collector = SkullCollector(player=player,
                                 position=(choice(SKULL_COLLECTOR["start_position"])),
                                 character=SKULL_COLLECTOR)
rusher = Rusher(player=player,
                position=choice(RUSHER["start_position"]),
                character=RUSHER)

# Creepers
bat = Bat(player=player,
          creeper_name=BAT)
fish = Fish(player=player,
            creeper_name=FISH)

# Camera
camera = Camera(background=background)

# Allowed events
pygame.event.set_allowed([QUIT, K_w, K_s, K_a, K_d, MOUSEBUTTONDOWN])

# Clock
clock = pygame.time.Clock()

tick = 0
while True:
    if player.skull_level > 10:
        player.health = 1000
        player.skull_level = 0

    if player.energy_level > 10:
        player.speed *= 1.5
        player.energy_level = 0

    if player.coin_level > 10:
        BULLET["speed"] *= 1.5
        BULLET["damage"] *= 1.5
        if PLAYER["shoot_cooldown"] > 5:
            PLAYER["shoot_cooldown"] -= 4
        player.coin_level = 0

    tick += 1
    if tick == 120:
        print(len(all_sprites.sprites()))
        print(clock.get_fps())

        Bat(player=player,
            creeper_name=BAT)
        Fish(player=player,
             creeper_name=FISH)

        SkullCollector(player=player,
                       position=(choice(SKULL_COLLECTOR["start_position"])),
                       character=SKULL_COLLECTOR)
        Rusher(player=player,
               position=choice(RUSHER["start_position"]),
               character=RUSHER)
        tick = 0

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    # Utility handlers
    handle_incoming_projectiles()
    handle_outgoing_projectiles()
    handle_pickups()

    # Camera offset
    camera.custom_draw(screen=screen,
                       background=background,
                       player=player)

    # Hitboxes
    # camera.show_hitboxes(player=player)
    # camera.show_hitboxes(skull_collector=skull_collector)
    # camera.show_hitboxes(skull=True,
    #                      energy=True)
    # camera.show_hitboxes(fish=fish)

    # Bars
    camera.show_bars(screen=screen,
                     player=player)

    # Update sprites
    all_sprites.update()

    # Update screen
    pygame.display.update()
    clock.tick(GENERAL["FPS"])
