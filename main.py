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
menu_background = pygame.image.load(GENERAL["menu_background_path"]).convert_alpha()

pygame.display.set_caption(GENERAL["title"])
pygame.event.set_allowed([QUIT, K_w, K_s, K_a, K_d, MOUSEBUTTONDOWN])
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

from menus import start_button, exit_button

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

# Fonts
pause_font = pygame.font.SysFont("comicsansms", 75)
pause_color = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

tick = 0

game_has_started = False
game_is_paused = False
while True:
    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Quit with escape
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

        # Pause menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_is_paused = not game_is_paused

    # Show pause menu
    if game_is_paused:
        text = pause_font.render("Pause menu", True, pause_color)
        screen.blit(text, (GENERAL["half_width"], GENERAL["half_height"]))

    else:

        # Show start screen
        if not game_has_started:
            screen.blit(menu_background, (0, 0))
            if start_button.draw(screen):
                game_has_started = True
            if exit_button.draw(screen):
                pygame.quit()
                exit()

        # Run the game
        else:

            tick += 1
            if tick == 100:

                Bat(player=player,
                    creeper_name=BAT)
                Fish(player=player,
                     creeper_name=FISH)

                SkullCollector(player=player,
                               position=choice(SKULL_COLLECTOR["start_position"]),
                               character=SKULL_COLLECTOR)
                Rusher(player=player,
                       position=choice(RUSHER["start_position"]),
                       character=RUSHER)
                tick = 0

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
            # camera.show_hitboxes(rusher=rusher)
            #
            # camera.show_hitboxes(skull=True)
            # camera.show_hitboxes(energy=True)
            #
            # camera.show_hitboxes(bat=bat)
            # camera.show_hitboxes(fish=fish)

            # Bars
            camera.show_bars(screen=screen,
                             player=player)

            # Update sprites
            all_sprites.update()

            # Update screen
            clock.tick(GENERAL["FPS"])

    pygame.display.update()

