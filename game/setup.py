import os
import sys
from random import choice

import pygame
from pygame.locals import *

from settings.general_settings import GENERAL

pygame.init()
screen = pygame.display.set_mode((GENERAL["width"],
                                  GENERAL["height"]),
                                 16)

from game.menus import Button
from game.camera import Camera

from characters.player import Player
from characters.rusher import Rusher
from characters.skull_collector import SkullCollector

from creepers.bat import Bat
from creepers.fish import Fish

from settings.enemy_settings import SKULL_COLLECTOR, RUSHER
from settings.creeper_settings import BAT, FISH
from utilities import handle_incoming_projectiles, handle_outgoing_projectiles, handle_pickups, \
    all_sprites, handle_outgoing_bombs, enemy_sprites, all_creeper_sprites

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


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
        self.small_font = pygame.font.Font(os.path.join(base_dir, "fonts/PublicPixel.ttf"), 15)
        self.medium_font = pygame.font.Font(os.path.join(base_dir, "fonts/PublicPixel.ttf"), 30)
        self.large_font = pygame.font.Font(os.path.join(base_dir, "fonts/PublicPixel.ttf"), 45)
        self.font_color = GENERAL["white"]


        # Menus
        self.first_button_x = 0.62 * GENERAL["width"]
        self.first_button_y = 0.144 * GENERAL["width"]
        self.play_button_image = pygame.image.load(GENERAL["play_btn_img"]).convert_alpha()
        self.play_button = Button(x=self.first_button_x,
                                  y=self.first_button_y,
                                  image=self.play_button_image,
                                  scale=1)

        self.settings_button_image = pygame.image.load(GENERAL["settings_btn_img"]).convert_alpha()
        self.settings_button = Button(x=self.first_button_x,
                                      y=self.first_button_y + 90,
                                      image=self.settings_button_image,
                                      scale=1)

        self.leaderboard_button_image = pygame.image.load(
            GENERAL["leaderboard_btn_img"]).convert_alpha()
        self.leaderboard_button = Button(x=self.first_button_x,
                                         y=self.first_button_y + 180,
                                         image=self.leaderboard_button_image,
                                         scale=1)

        self.credits_button_image = pygame.image.load(
            GENERAL["credits_btn_img"]).convert_alpha()
        self.credits_button = Button(x=self.first_button_x,
                                     y=self.first_button_y + 270,
                                     image=self.credits_button_image,
                                     scale=1)

        self.sounds_on_button_image = pygame.image.load(
            GENERAL["sounds_on_btn_img"]).convert_alpha()
        self.sounds_on_button = Button(x=self.first_button_x,
                                       y=self.first_button_y + 360,
                                       image=self.sounds_on_button_image,
                                       scale=1)

        self.sounds_off_button_image = pygame.image.load(
            GENERAL["sounds_off_btn_img"]).convert_alpha()
        self.sounds_off_button = Button(x=self.first_button_x,
                                        y=self.first_button_y + 360,
                                        image=self.sounds_off_button_image,
                                        scale=1)

        self.main_menu_button_image = pygame.image.load(
            GENERAL["main_menu_btn_img"]).convert_alpha()
        self.main_menu_button = Button(x=self.first_button_x,
                                       y=self.first_button_y + 360,
                                       image=self.main_menu_button_image,
                                       scale=1)

        # Characters
        self.player = Player()

        # Camera
        self.camera = Camera(background=self.background)

        # States
        self.game_is_running = True
        self.is_playing_game = False

        self.main_menu_shown = True
        self.credits_menu_shown = False
        self.pause_menu_shown = False

        self.sound_is_on = False
        # Trackers
        self.tick = 0
        self.wave_pause_ticks = 0
        self.wave_pause = 180

        # Misc
        self.credits = GENERAL["credits"]

    def listen_for_events(self):
        for event in pygame.event.get():

            # Quit with exit window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Quit with escape
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()

            # Pause with space-bar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pause_menu_shown = not self.pause_menu_shown

    def turn_off_menus(self):
        self.main_menu_shown = False
        self.credits_menu_shown = False
        self.pause_menu_shown = False

    def display_main_menu(self):
        self.screen.blit(self.menu_background, (0, 0))

        # Menu buttons
        if self.play_button.draw(self.screen):
            self.is_playing_game = True
            self.turn_off_menus()

        elif self.settings_button.draw(self.screen):
            print("settings menu")

        elif self.leaderboard_button.draw(self.screen):
            print("leaderboard menu")

        elif self.credits_button.draw(self.screen):
            self.turn_off_menus()
            self.credits_menu_shown = True

        elif self.sound_is_on:
            if self.sounds_on_button.draw(self.screen):
                self.sound_is_on = False
                print("turning on")

        else:
            if self.sounds_off_button.draw(self.screen):
                self.sound_is_on = True
                print("turning off")

    def display_credit_menu(self):
        self.screen.blit(self.menu_background, (0, 0))
        for i, credit in enumerate(self.credits):
            text = self.small_font.render(credit, True, self.font_color)
            self.screen.blit(text, (self.first_button_x, self.first_button_y + i * 28))

        if self.main_menu_button.draw(self.screen):
            self.turn_off_menus()
            self.main_menu_shown = True

    def spawn_test_enemies(self):
        if self.tick == 200:
            Bat(player=self.player,
                creeper_name=BAT)
            Fish(player=self.player,
                 creeper_name=FISH)

            SkullCollector(player=self.player,
                           position=choice(SKULL_COLLECTOR["start_position"]),
                           character=SKULL_COLLECTOR)
            Rusher(player=self.player,
                   position=choice(RUSHER["start_position"]),
                   character=RUSHER)
            self.tick = 0

    def spawn_waves(self):
        for _ in range(SKULL_COLLECTOR["wave_spawns"][self.player.wave_level]):
            SkullCollector(player=self.player,
                           position=choice(SKULL_COLLECTOR["start_position"]),
                           character=SKULL_COLLECTOR)

        for _ in range(RUSHER["wave_spawns"][self.player.wave_level]):
            Rusher(player=self.player,
                   position=choice(RUSHER["start_position"]),
                   character=RUSHER)

        for _ in range(BAT["wave_spawns"][self.player.wave_level]):
            Bat(player=self.player,
                creeper_name=BAT)

        for _ in range(FISH["wave_spawns"][self.player.wave_level]):
            Fish(player=self.player,
                 creeper_name=FISH)

    def outline_hitboxes(self):
        # self.camera.show_hitboxes(screen=screen,
        #                           player=self.player)
        self.camera.show_hitboxes(screen=screen,
                                  skull_collector=True)
        self.camera.show_hitboxes(screen=screen,
                                  rusher=True)

        self.camera.show_hitboxes(screen=screen,
                                  skull=True)
        self.camera.show_hitboxes(screen=screen,
                                  energy=True)

        self.camera.show_hitboxes(screen=screen,
                                  bat=True)
        self.camera.show_hitboxes(screen=screen,
                                  fish=True)

        self.camera.show_hitboxes(screen=screen,
                                  bullet=True)
        self.camera.show_hitboxes(screen=screen,
                                  bomb=True)

    def run_game(self):
        while self.game_is_running:
            # Events
            self.listen_for_events()

            # Show pause menu
            if self.pause_menu_shown:
                text = self.medium_font.render("Pause menu", True, self.font_color)
                self.screen.blit(text, (GENERAL["half_width"], GENERAL["half_height"]))

            elif self.credits_menu_shown:
                self.display_credit_menu()

            # Show start screen
            elif self.main_menu_shown:
                self.display_main_menu()

            # Play game
            elif self.is_playing_game:
                self.tick += 1

                # self.spawn_test_enemies()
                if not len(enemy_sprites) and not len(all_creeper_sprites):
                    self.wave_pause_ticks += 1
                    # display buy menu text
                    if self.wave_pause_ticks == self.wave_pause:
                        self.wave_pause_ticks = 0
                        print(f"level: {self.player.wave_level}")
                        self.spawn_waves()
                        self.player.wave_level += 1

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
                self.outline_hitboxes()

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
