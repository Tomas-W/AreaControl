from random import choice

import pygame
from pygame.locals import *

from settings.general_settings import GENERAL

pygame.init()
screen = pygame.display.set_mode((GENERAL["width"],
                                  GENERAL["height"]),
                                 16)

from game.menus import start_button, exit_button
from game.camera import Camera

from characters.player import Player
from characters.rusher import Rusher
from characters.skull_collector import SkullCollector

from creepers.bat import Bat
from creepers.fish import Fish

from settings.enemy_settings import SKULL_COLLECTOR, RUSHER
from settings.creeper_settings import BAT, FISH
from utilities import handle_incoming_projectiles, handle_outgoing_projectiles, handle_pickups, \
    all_sprites, handle_outgoing_bombs


class Game:
    pygame.display.set_caption(GENERAL["title"])
    pygame.event.set_allowed([QUIT, K_w, K_s, K_a, K_d, MOUSEBUTTONDOWN])

    def __init__(self):
        # Screen
        self.screen = screen

        # Backgrounds
        self.background = pygame.image.load(GENERAL["background_path"]).convert_alpha()
        self.menu_background = pygame.image.load(GENERAL["menu_background_path"]).convert_alpha()

        # Clock
        self.clock = pygame.time.Clock()

        # Fonts
        self.pause_font = pygame.font.SysFont("comicsansms", 75)
        self.pause_font_color = GENERAL["white"]

        # Menus
        self.start_button = start_button
        self.exit_button = exit_button

        # Characters
        self.player = Player()
        self.skull_collector = SkullCollector(player=self.player,
                                              position=(choice(SKULL_COLLECTOR["start_position"])),
                                              character=SKULL_COLLECTOR)
        self.rusher = Rusher(player=self.player,
                             position=choice(RUSHER["start_position"]),
                             character=RUSHER)
        # Creepers
        self.bat = Bat(player=self.player,
                       creeper_name=BAT)
        self.fish = Fish(player=self.player,
                         creeper_name=FISH)

        # Camera
        self.camera = Camera(background=self.background)

        # States
        self.game_is_running = True
        self.game_has_started = False
        self.game_is_paused = False

        # Trackers
        self.tick = 0

    def run_game(self):
        while self.game_is_running:
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
                        self.game_is_paused = not self.game_is_paused

            # Show pause menu
            if self.game_is_paused:
                text = self.pause_font.render("Pause menu", True, self.pause_font_color)
                self.screen.blit(text, (GENERAL["half_width"], GENERAL["half_height"]))

            else:

                # Show start screen
                if not self.game_has_started:
                    self.screen.blit(self.menu_background, (0, 0))
                    if self.start_button.draw(self.screen):
                        self.game_has_started = True
                    if self.exit_button.draw(self.screen):
                        pygame.quit()
                        exit()

                # Run the game
                else:

                    self.tick += 1
                    if self.tick == 150:
                        # Bat(player=self.player,
                        #     creeper_name=BAT)
                        # Fish(player=self.player,
                        #      creeper_name=FISH)

                        SkullCollector(player=self.player,
                                       position=choice(SKULL_COLLECTOR["start_position"]),
                                       character=SKULL_COLLECTOR)
                        # Rusher(player=self.player,
                        #        position=choice(RUSHER["start_position"]),
                        #        character=RUSHER)
                        self.tick = 0

                    # Utility handlers
                    handle_outgoing_projectiles()
                    handle_outgoing_bombs()
                    handle_incoming_projectiles()
                    handle_pickups()

                    # Camera offset
                    self.camera.custom_draw(screen=self.screen,
                                            background=self.background,
                                            player=self.player)

                    # Hitboxes
                    # self.camera.show_hitboxes(screen=screen,
                    #                           player=self.player)
                    self.camera.show_hitboxes(screen=screen,
                                              skull_collector=self.skull_collector)
                    self.camera.show_hitboxes(screen=screen,
                                              rusher=self.rusher)

                    # self.camera.show_hitboxes(screen=screen,
                    #                           skull=True)
                    # self.camera.show_hitboxes(screen=screen,
                    #                           energy=True)

                    # self.camera.show_hitboxes(screen=screen,
                    #                           bat=self.bat)
                    # self.camera.show_hitboxes(screen=screen,
                    #                           fish=self.fish)

                    # self.camera.show_hitboxes(screen=screen,
                    #                           bullet=True)
                    self.camera.show_hitboxes(screen=screen,
                                              bomb=True)

                    # Bars
                    self.camera.show_stats(screen=self.screen,
                                           player=self.player)

                    # Update sprites
                    all_sprites.update()

                    # Update screen
                    self.clock.tick(GENERAL["FPS"])

            pygame.display.update()

        pygame.quit()
        exit()
