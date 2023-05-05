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

from utilities import all_sprites, handle_outgoing_projectiles, handle_incoming_projectiles
from settings.enemy_settings import SKULL_COLLECTOR, RUSHER

from player import Player
from characters.skull_collector import SkullCollector
from characters.rusher import Rusher

from camera import Camera

player = Player()

# skull = SkullCollector(player=player,
#                        position=(1400, 1250),
#                        character=SKULL_COLLECTOR)

rush = Rusher(player=player,
              position=(1400, 1400),
              character=RUSHER)

camera = Camera(background=background)

# Allowed events
pygame.event.set_allowed([QUIT, K_w, K_s, K_a, K_d, MOUSEBUTTONDOWN])

# Clock
clock = pygame.time.Clock()

tick = 0

while True:

    tick += 1
    if tick == 5000:
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

    handle_incoming_projectiles()
    handle_outgoing_projectiles()

    camera.custom_draw(screen=screen,
                       background=background,
                       player=player)

    camera.show_hitboxes(player=player,
                         rusher=rush)

    # Update sprites
    all_sprites.update()

    # Update screen
    pygame.display.update()
    clock.tick(GENERAL["FPS"])
