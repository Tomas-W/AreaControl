from random import choice

import pygame
from pygame.locals import *

from settings.general_settings import GENERAL
from sprites.camera_sprites import BUTTON_Q_CAMERA_IMAGE, BUTTON_E_CAMERA_IMAGE, \
    BUTTON_W_CAMERA_IMAGE, BUTTON_S_CAMERA_IMAGE, MOUSE_L_CAMERA_IMAGE, BUTTON_A_CAMERA_IMAGE, \
    BUTTON_D_CAMERA_IMAGE, MOUSE_R_CAMERA_IMAGE

pygame.init()
screen = pygame.display.set_mode((GENERAL["width"],
                                  GENERAL["height"]),
                                 16)
pygame.display.set_caption(GENERAL["title"])
pygame.event.set_allowed([QUIT, K_w, K_s, K_a, K_d, MOUSEBUTTONDOWN])

from game.camera import Camera
from game.buttons import Button
from fonts.fonts import *

from characters.player import Player
from characters.rusher import Rusher
from characters.skull_collector import SkullCollector

from creepers.bat import Bat
from creepers.fish import Fish

from interactives.base_pickup import PickUp

from settings.menu_settings import DISPLAY
from settings.enemy_settings import SKULL_COLLECTOR, RUSHER
from settings.creeper_settings import BAT, FISH
from settings.interactives_settings import HEALTH_POTION
from settings.projectile_settings import BULLET, BOMB

from utilities import handle_incoming_projectiles, handle_outgoing_projectiles, handle_pickups, \
    all_sprites, handle_outgoing_bombs, enemy_sprites, all_creeper_sprites, buy_bullet_upgrade, \
    buy_bomb_upgrade, buy_bomb, buy_portal

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


class Game:
    def __init__(self):
        # Characters
        self.player = Player(sound_is_on=False)

        # Screen
        self.screen = screen
        # Backgrounds
        self.background = pygame.image.load(GENERAL["background_path"]).convert_alpha()
        self.menu_background = pygame.image.load(GENERAL["menu_background_path"]).convert_alpha()
        # Camera
        self.camera = Camera(background=self.background)
        # Clock
        self.clock = pygame.time.Clock()
        # Fonts
        self.tiny_font = TINY_FONT
        self.small_font = SMALL_FONT
        self.medium_font = MEDIUM_FONT
        self.large_font = LARGE_FONT
        self.font_color = FONT_COLOR

        # Buttons
        self.first_menu_button_x = 0.62 * GENERAL["width"]
        self.first_menu_button_y = 0.144 * GENERAL["width"]

        self.play_button_image = pygame.image.load(DISPLAY["play_btn_img"]).convert_alpha()
        self.play_button = Button(x=self.first_menu_button_x,
                                  y=self.first_menu_button_y,
                                  image=self.play_button_image,
                                  scale=1,
                                  name="play",
                                  player=self.player)

        self.settings_button_image = pygame.image.load(DISPLAY["settings_btn_img"]).convert_alpha()
        self.settings_button = Button(x=self.first_menu_button_x,
                                      y=self.first_menu_button_y + 90,
                                      image=self.settings_button_image,
                                      scale=1,
                                      name="settings",
                                      player=self.player)

        self.leaderboard_button_image = pygame.image.load(
            DISPLAY["leaderboard_btn_img"]).convert_alpha()
        self.leaderboard_button = Button(x=self.first_menu_button_x,
                                         y=self.first_menu_button_y + 180,
                                         image=self.leaderboard_button_image,
                                         scale=1,
                                         name="leaderboard",
                                         player=self.player)

        self.credits_button_image = pygame.image.load(
            DISPLAY["credits_btn_img"]).convert_alpha()
        self.credits_button = Button(x=self.first_menu_button_x,
                                     y=self.first_menu_button_y + 270,
                                     image=self.credits_button_image,
                                     scale=1,
                                     name="credits",
                                     player=self.player)

        self.sounds_on_button_image = pygame.image.load(
            DISPLAY["sounds_on_btn_img"]).convert_alpha()
        self.sounds_on_button = Button(x=self.first_menu_button_x,
                                       y=self.first_menu_button_y + 360,
                                       image=self.sounds_on_button_image,
                                       scale=1,
                                       name="sounds_on",
                                       player=self.player)

        self.sounds_off_button_image = pygame.image.load(
            DISPLAY["sounds_off_btn_img"]).convert_alpha()
        self.sounds_off_button = Button(x=self.first_menu_button_x,
                                        y=self.first_menu_button_y + 360,
                                        image=self.sounds_off_button_image,
                                        scale=1,
                                        name="sounds_off",
                                        player=self.player)

        self.main_menu_button_image = pygame.image.load(
            DISPLAY["main_menu_btn_img"]).convert_alpha()
        self.main_menu_button = Button(x=self.first_menu_button_x,
                                       y=self.first_menu_button_y + 360,
                                       image=self.main_menu_button_image,
                                       scale=1,
                                       name="main",
                                       player=self.player)

        self.continue_button_image = pygame.image.load(
            DISPLAY["continue_btn_img"]).convert_alpha()
        self.continue_button = Button(x=self.first_menu_button_x,
                                      y=self.first_menu_button_y,
                                      image=self.continue_button_image,
                                      scale=1,
                                      name="continue",
                                      player=self.player)

        self.restart_button_image = pygame.image.load(
            DISPLAY["restart_btn_img"]).convert_alpha()
        self.restart_button = Button(x=self.first_menu_button_x,
                                     y=self.first_menu_button_y + 180,
                                     image=self.restart_button_image,
                                     scale=1,
                                     name="restart",
                                     player=self.player)

        self.back_button_image = pygame.image.load(
            DISPLAY["back_btn_img"]).convert_alpha()
        self.back_button = Button(x=self.first_menu_button_x,
                                  y=self.first_menu_button_y + 360,
                                  image=self.back_button_image,
                                  scale=1,
                                  name="return",
                                  player=self.player)

        # Settings button images
        self.btn_q = BUTTON_Q_CAMERA_IMAGE
        self.btn_w = BUTTON_W_CAMERA_IMAGE
        self.btn_e = BUTTON_E_CAMERA_IMAGE
        self.btn_a = BUTTON_A_CAMERA_IMAGE
        self.btn_s = BUTTON_S_CAMERA_IMAGE
        self.btn_d = BUTTON_D_CAMERA_IMAGE
        self.mouse_l = MOUSE_L_CAMERA_IMAGE
        self.mouse_r = MOUSE_R_CAMERA_IMAGE

        # Sounds
        self.sound_is_on = False
        self.buy_sound = pygame.mixer.Sound(GENERAL["buy_sound_path"])
        self.buy_sound.set_volume(0.2)

        # States
        self.game_is_running = True
        self.is_playing_game = False

        self.main_menu_shown = True
        self.settings_menu_shown = False
        self.credits_menu_shown = False
        self.pause_menu_shown = False

        self.game_is_over = False

        # Trackers
        self.test_tick = 0
        self.wave_pause_ticks = 0
        self.wave_pause = GENERAL["wave_pause"]  # how long is the buy period
        self.buy_tick = GENERAL["buy_tick"]  # to prevent double buys
        self.bonus_ticks_list = [2000, 2100, 2600, 3000, 3000, 3500, 4000]
        self.bonus_ticks = self.bonus_ticks_list[0]

        # Misc
        self.credits = GENERAL["credits"]
        self.before_settings_menu = "home"

    def reset_game(self):
        """
        Removes all sprites and resets all settings.
        """
        for sprite in all_sprites:
            sprite.kill()
        all_sprites.empty()

        self.player = Player(sound_is_on=self.player.sound_is_on)
        # States
        self.game_is_running = True
        self.is_playing_game = False
        self.main_menu_shown = True
        self.settings_menu_shown = False
        self.credits_menu_shown = False
        self.pause_menu_shown = False
        self.sound_is_on = False

        # Trackers
        self.test_tick = 0
        self.wave_pause_ticks = 0
        self.wave_pause = GENERAL["wave_pause"]  # how long is the buy period
        self.buy_tick = GENERAL["buy_tick"]  # to prevent double buys
        self.bonus_ticks = self.bonus_ticks_list[0]

        # Settings
        SKULL_COLLECTOR["health"] = 260
        RUSHER["health"] = 105
        BAT["health"] = 60
        FISH["health"] = 60

        RUSHER["damage"] = 40
        BAT["damage"] = 50
        FISH["damage"] = 50

        SKULL_COLLECTOR["speed"] = 3

    def listen_for_events(self):
        """
        Active keys:
            'escape': closes game.
            'space-bar': pauses game.
            '1': buy option.
            '2': buy option.
            '3': buy option.
            '4': buy option.
        """
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.game_is_over = not self.game_is_over

                # Pause and resume with space-bar
                if event.key == pygame.K_SPACE and self.is_playing_game:
                    self.pause_menu_shown = True

                # Kill all enemies with k
                if event.key == pygame.K_k and self.is_playing_game:
                    for enemy in enemy_sprites:
                        enemy.kill()
                    for creeper in all_creeper_sprites:
                        creeper.kill()

            # Operate buy menu
            if self.wave_pause_ticks > 0:
                if event.type == pygame.KEYDOWN:

                    # Buy Bullet upgrade with '1'
                    if event.key == K_1:
                        if buy_bullet_upgrade(game=self,
                                              bullet_stats=BULLET):
                            if self.sound_is_on:
                                self.buy_sound.play()

                    # Buy Bomb upgrade with '2'
                    elif event.key == K_2:
                        if buy_bomb_upgrade(game=self,
                                            bomb_stats=BOMB):
                            if self.sound_is_on:
                                self.buy_sound.play()

                    # Buy Bomb with '3'
                    elif event.key == K_3:
                        if buy_bomb(game=self,
                                    player=self.player):
                            if self.sound_is_on:
                                self.buy_sound.play()

                    # Buy Teleport with '4'
                    elif event.key == K_4:
                        if buy_portal(game=self,
                                      player=self.player):
                            if self.sound_is_on:
                                self.buy_sound.play()

    def turn_off_menus(self):
        """
        Disables all menu states.
        """
        self.main_menu_shown = False
        self.settings_menu_shown = False
        self.credits_menu_shown = False
        self.pause_menu_shown = False

    def display_main_menu(self):
        """
        Displays main menu on screen.
        """
        self.screen.blit(self.menu_background, (0, 0))

        # Menu buttons
        if self.play_button.draw(self.screen):
            self.turn_off_menus()
            self.is_playing_game = True

        elif self.settings_button.draw(self.screen):
            self.turn_off_menus()
            self.settings_menu_shown = True
            self.before_settings_menu = "home"

        elif self.leaderboard_button.draw(self.screen):
            print(": test")

        elif self.credits_button.draw(self.screen):
            self.turn_off_menus()
            self.credits_menu_shown = True

        if not self.sound_is_on:
            if self.sounds_off_button.draw(self.screen):
                self.sound_is_on = True
                self.player.sound_is_on = True

        elif self.sound_is_on:
            if self.sounds_on_button.draw(self.screen):
                self.sound_is_on = False
                self.player.sound_is_on = False

    def display_pause_menu(self):
        """
        Displays pause menu on screen.
        """
        self.screen.blit(self.menu_background, (0, 0))

        # Menu buttons
        if self.continue_button.draw(self.screen):
            self.turn_off_menus()
            self.is_playing_game = True
            self.pause_menu_shown = False

        elif self.settings_button.draw(self.screen):
            self.turn_off_menus()
            self.settings_menu_shown = True
            self.before_settings_menu = "pause"

        elif self.restart_button.draw(self.screen):
            self.reset_game()
            self.turn_off_menus()
            self.is_playing_game = True

        elif self.main_menu_button.draw(self.screen):
            self.reset_game()
            self.turn_off_menus()
            self.main_menu_shown = True

    def display_settings_menu(self):
        self.screen.blit(self.menu_background, (0, 0))
        # Forwards
        screen.blit(self.btn_w,
                    (self.first_menu_button_x - 0.02 * GENERAL["width"], self.first_menu_button_y))
        text = self.small_font.render("forwards", True, self.font_color)
        self.screen.blit(text, (
            self.first_menu_button_x - 0.02 * GENERAL["width"] + 75, self.first_menu_button_y + 10))
        # Backwards
        screen.blit(self.btn_s,
                    (self.first_menu_button_x - 0.02 * GENERAL["width"],
                     self.first_menu_button_y + 40))
        text = self.small_font.render("backwards", True, self.font_color)
        self.screen.blit(text, (
            self.first_menu_button_x - 0.02 * GENERAL["width"] + 75, self.first_menu_button_y + 50))
        # Left
        screen.blit(self.btn_a,
                    (self.first_menu_button_x - 0.02 * GENERAL["width"],
                     self.first_menu_button_y + 80))
        text = self.small_font.render("left", True, self.font_color)
        self.screen.blit(text, (
            self.first_menu_button_x - 0.02 * GENERAL["width"] + 75, self.first_menu_button_y + 90))
        # Right
        screen.blit(self.btn_d,
                    (self.first_menu_button_x - 0.02 * GENERAL["width"],
                     self.first_menu_button_y + 120))
        text = self.small_font.render("right", True, self.font_color)
        self.screen.blit(text, (
            self.first_menu_button_x - 0.02 * GENERAL["width"] + 75,
            self.first_menu_button_y + 130))
        # Use Health potion
        screen.blit(self.btn_q,
                    (self.first_menu_button_x - 0.02 * GENERAL["width"],
                     self.first_menu_button_y + 160))
        text = self.small_font.render("use potion", True, self.font_color)
        self.screen.blit(text, (
            self.first_menu_button_x - 0.02 * GENERAL["width"] + 75,
            self.first_menu_button_y + 170))
        # Use Portal
        screen.blit(self.btn_e,
                    (self.first_menu_button_x - 0.02 * GENERAL["width"],
                     self.first_menu_button_y + 200))
        text = self.small_font.render("use portal", True, self.font_color)
        self.screen.blit(text, (
            self.first_menu_button_x - 0.02 * GENERAL["width"] + 75,
            self.first_menu_button_y + 210))
        # Shoot Bullet
        screen.blit(self.mouse_l,
                    (self.first_menu_button_x - 0.02 * GENERAL["width"],
                     self.first_menu_button_y + 250))
        text = self.small_font.render("shoot bullet", True, self.font_color)
        self.screen.blit(text, (
            self.first_menu_button_x - 0.02 * GENERAL["width"] + 75,
            self.first_menu_button_y + 260))
        # Throw Bomb
        screen.blit(self.mouse_r,
                    (self.first_menu_button_x - 0.02 * GENERAL["width"],
                     self.first_menu_button_y + 300))
        text = self.small_font.render("throw bomb", True, self.font_color)
        self.screen.blit(text, (
            self.first_menu_button_x - 0.02 * GENERAL["width"] + 75,
            self.first_menu_button_y + 310))

        # Back Button
        if self.back_button.draw(self.screen):
            if self.before_settings_menu == "pause":
                self.turn_off_menus()
                self.pause_menu_shown = True

            elif self.before_settings_menu == "home":
                self.turn_off_menus()
                self.main_menu_shown = True

    def display_credit_menu(self):
        """
        Displays credit menu with credits and a Main Menu button.
        """
        self.screen.blit(self.menu_background, (0, 0))
        # Loop over credits and blit them
        for i, credit in enumerate(self.credits):
            text = self.tiny_font.render(credit, True, self.font_color)
            self.screen.blit(text, (
                self.first_menu_button_x - 0.02 * GENERAL["width"],
                self.first_menu_button_y + i * 18))

        # Blit Main Menu button
        if self.back_button.draw(self.screen):
            self.turn_off_menus()
            self.main_menu_shown = True

    def spawn_test_enemies(self, ticks):
        """
        Spawns Enemies and Creepers after given ticks.

        :param ticks: Number of game ticks after which Enemies and Creepers are spawned (int).
        """
        self.test_tick += 1
        if self.test_tick == ticks:
            # Bat(player=self.player,
            #     creeper_name=BAT)
            # Fish(player=self.player,
            #      creeper_name=FISH)
            #
            # SkullCollector(player=self.player,
            #                position=choice(SKULL_COLLECTOR["start_position"]),
            #                character=SKULL_COLLECTOR)
            # Rusher(player=self.player,
            #        position=choice(RUSHER["start_position"]),
            #        character=RUSHER)
            print(self.clock.get_fps())
            self.test_tick = 0

    def spawn_waves(self):
        """
        Updates Enemy and Creeper stats based on wave number.
        Spawns new wave based on wave_spawn settings.
        """
        SKULL_COLLECTOR["health"] *= 1.1
        RUSHER["health"] *= 1.2
        BAT["health"] *= 1.1
        FISH["health"] *= 1.1

        RUSHER["damage"] *= 1.2
        BAT["damage"] *= 1.1
        FISH["damage"] *= 1.1

        SKULL_COLLECTOR["speed"] *= 1.05

        # Spawn SkullCollectors
        for _ in range(SKULL_COLLECTOR["wave_spawns"][self.player.wave_level]):
            SkullCollector(player=self.player,
                           position=choice(SKULL_COLLECTOR["start_position"]),
                           character=SKULL_COLLECTOR)
        # Spawn Rushers
        for _ in range(RUSHER["wave_spawns"][self.player.wave_level]):
            Rusher(player=self.player,
                   position=choice(RUSHER["start_position"]),
                   character=RUSHER)
        # Spawn Bats
        for _ in range(BAT["wave_spawns"][self.player.wave_level]):
            Bat(player=self.player,
                creeper_name=BAT)
        # Spawn Fish
        for _ in range(FISH["wave_spawns"][self.player.wave_level]):
            Fish(player=self.player,
                 creeper_name=FISH)

    def end_of_wave_spawns(self):
        """
        Spawns PickUps after a wave has been cleared.
        """
        for _ in range(self.player.wave_level):
            PickUp(player=self.player,
                   pickup_name=HEALTH_POTION,
                   position=None)

    def outline_hitboxes(self):
        """
        Draws outline around Sprite hitboxes.
        """
        # Characters
        self.camera.show_hitboxes(screen=screen,
                                  player=self.player)
        # self.camera.show_hitboxes(screen=screen,
        #                           skull_collector=True)
        # self.camera.show_hitboxes(screen=screen,
        #                           rusher=True)
        # # Creepers
        # self.camera.show_hitboxes(screen=screen,
        #                           bat=True)
        # self.camera.show_hitboxes(screen=screen,
        #                           fish=True)
        # # PickUps
        # self.camera.show_hitboxes(screen=screen,
        #                           skull=True)
        # self.camera.show_hitboxes(screen=screen,
        #                           energy=True)
        # self.camera.show_hitboxes(screen=screen,
        #                           health_potion=True)
        # # Projectiles
        # self.camera.show_hitboxes(screen=screen,
        #                           bullet=True)
        # self.camera.show_hitboxes(screen=screen,
        #                           bomb=True)

    def run_game(self):
        """
        Runs the game.

        Listens for events.
        Checks if menu's should be displayed.
        Checks if game is running.
        Checks wave spawns.
        Calls utility handlers.
        Draws sprites.
        Draws hitboxes.
        Checks if wave and buy info should be displayed.
        Updates sprites.
        Updates clock.
        """
        while self.game_is_running:
            # Events (key presses)
            self.listen_for_events()

            if self.game_is_over:
                self.camera.display_game_over(screen=self.screen,
                                              player=self.player)

            # Pause menu
            elif self.pause_menu_shown:
                self.display_pause_menu()

            # Settings menu
            elif self.settings_menu_shown:
                self.display_settings_menu()

            # Credits menu
            elif self.credits_menu_shown:
                self.display_credit_menu()

            # Main menu
            elif self.main_menu_shown:
                self.display_main_menu()

            # Play game
            elif self.is_playing_game:

                # Start wave countdown when al enemies are killed
                if not len(enemy_sprites) and not len(all_creeper_sprites):
                    self.wave_pause_ticks += 1

                    if self.wave_pause_ticks == self.wave_pause:
                        self.bonus_ticks = self.bonus_ticks_list[
                            self.player.wave_level]  # Set bonus timer
                        self.wave_pause_ticks = 0
                        self.spawn_waves()
                        self.player.wave_level += 1

                # Spawn items after wave completed
                if self.wave_pause_ticks == 1:
                    self.end_of_wave_spawns()

                # Tests
                # self.spawn_test_enemies(30)

                # Utility handlers (collisions)
                handle_outgoing_projectiles()
                handle_outgoing_bombs()
                handle_incoming_projectiles()
                handle_pickups()

                # Camera offset
                self.camera.blit_all_sprites(screen=self.screen,
                                             background=self.background,
                                             player=self.player)

                # Hitboxes
                # self.outline_hitboxes()

                # Screen info
                self.camera.show_stats(screen=self.screen,
                                       player=self.player)

                # Bonus timer
                if self.bonus_ticks > 0:
                    self.bonus_ticks -= 1

                self.camera.show_bonus_timer(screen=self.screen,
                                             player=self.player,
                                             ticks=self.bonus_ticks)

                # Display buy menu text
                if self.wave_pause_ticks > 0:
                    self.camera.show_new_wave_info(screen=screen,
                                                   player=self.player)
                    self.camera.show_buy_menu(screen=screen,
                                              player=self.player)
                    self.camera.show_buy_menu_countdown(screen=screen,
                                                        player=self.player,
                                                        ticks=self.wave_pause_ticks)

                # Update sprites
                all_sprites.update()

                # Update screen
                self.clock.tick(GENERAL["FPS"])

            pygame.display.update()

        pygame.quit()
        exit()
