import pygame
from pygame.locals import *

from creepers.fish import Fish
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
from settings.creeper_settings import BAT, FISH

from camera import Camera

# Characters
player = Player()
skull_collector = SkullCollector(player=player,
                                 position=(1400, 1250),
                                 character=SKULL_COLLECTOR)
rusher = Rusher(player=player,
                position=(1400, 1400),
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
    tick += 1
    if tick == 50:
        print(len(all_sprites.sprites()))
        print(clock.get_fps())

        bat = Bat(player=player,
                  creeper_name=BAT)
        fish = Fish(player=player,
                    creeper_name=FISH)

        skull = SkullCollector(player=player,
                               position=(1400, 1250),
                               character=SKULL_COLLECTOR)
        rush = Rusher(player=player,
                      position=(1400, 1400),
                      character=RUSHER)
        tick = 0

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
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
    # camera.show_hitboxes(skull_collector=skull,
    #                      rusher=rush)
    # camera.show_hitboxes(skull=True,
    #                      energy=True)
    # camera.show_hitboxes(fish=fish)

    # Bars
    camera.show_bars(screen=screen,
                     player=player,
                     health=True,
                     skull=True,
                     energy=True)

    # Update sprites
    all_sprites.update()

    # Update screen
    pygame.display.update()
    clock.tick(GENERAL["FPS"])
