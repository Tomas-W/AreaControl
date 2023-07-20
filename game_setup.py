import time
import random

from settings.general_settings import GENERAL

import pygame

from utilities.game_physics import get_safe_spawn

pygame.init()
from pygame.locals import *

screen = pygame.display.set_mode((GENERAL["width"],
                                  GENERAL["height"]),
                                 16)
pygame.display.set_caption(GENERAL["title"])
pygame.event.set_allowed([QUIT, K_w, K_s, K_a, K_d, MOUSEBUTTONDOWN])

from characters.rusher import Rusher
from characters.skull_collector import SkullCollector
from creepers.bat import Bat
from creepers.fish import Fish
from display.display_game import DisplayGame
from display.display_interfaces import DisplayInterfaces
from display.display_menus import DisplayMenus
from interactives.base_pickup import PickUp

from settings.player_settings import PLAYER
from settings.interactives_settings import HEALTH_POTION
from settings.projectile_settings import BULLET, BOMB
from sprites.camera_sprites import BUTTON_Q_CAMERA_IMAGE, BUTTON_E_CAMERA_IMAGE, \
    BUTTON_W_CAMERA_IMAGE, BUTTON_S_CAMERA_IMAGE, MOUSE_L_CAMERA_IMAGE, BUTTON_A_CAMERA_IMAGE, \
    BUTTON_D_CAMERA_IMAGE, MOUSE_R_CAMERA_IMAGE

from fonts.fonts import *

from characters.player import Player

from settings.enemy_settings import SKULL_COLLECTOR, RUSHER
from settings.creeper_settings import BAT, FISH

from utilities.sprite_groups import all_sprites, enemy_sprites, all_creeper_sprites
from utilities.general import save_player_score
from utilities.game_interactions import handle_incoming_projectiles, handle_outgoing_projectiles, \
    handle_outgoing_bombs
from utilities.player_interactions import buy_bullet_upgrade, buy_bomb, buy_bomb_upgrade, \
    buy_portal, handle_pickups

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


class GameSetup:
    def __init__(self):
        # Characters
        self.player = Player(sound_is_on=False)

        # Screen
        self.screen = screen
        # Backgrounds
        self.background = pygame.image.load(GENERAL["background_path"]).convert_alpha()
        self.menu_background = pygame.image.load(GENERAL["menu_background_path"]).convert_alpha()
        # Display
        self.display_game = DisplayGame(background=self.background,
                                        player=self.player,
                                        screen=self.screen,
                                        sound_is_on=self.player.sound_is_on)
        self.display_menus = DisplayMenus(screen=self.screen,
                                          player=self.player)
        self.display_interfaces = DisplayInterfaces(screen=self.screen,
                                                    background=self.background,
                                                    player=self.player)

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
        self.game_is_over = False

        self.main_menu_shown = True
        self.settings_menu_shown = False
        self.leaderboard_menu_shown = False
        self.credits_menu_shown = False
        self.pause_menu_shown = False

        # Trackers
        self.test_tick = 0
        self.wave_pause_ticks = 0
        self.wave_pause = GENERAL["wave_pause"]  # how long is the buy period
        self.buy_tick = GENERAL["buy_tick"]  # to prevent double buys
        self.bonus_ticks_list = [2000, 2100, 2600, 3000, 3000, 3500, 4000]  # time per wave
        self.bonus_ticks = self.bonus_ticks_list[0]
        self.level_completed = False

        # Misc
        self.credits = GENERAL["credits"]
        self.before_settings_menu = "home"
        self.buy_moment = time.time()
        self.buy_delay = 0.15

    def operate_special_keys(self):
        """
        Listens for key presses while playing utilities.
        User can:
            Pause
            Exit
            Kill all enemies
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                # Quit with exiting window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # Quit with escape key
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                # Pause and resume with space-bar
                if event.key == pygame.K_SPACE and self.is_playing_game:
                    self.is_playing_game = not self.is_playing_game
                    self.pause_menu_shown = not self.pause_menu_shown

                # Kill all enemies with k
                if event.key == pygame.K_k and self.is_playing_game:
                    for sprite in enemy_sprites:
                        sprite.kill()
                    for sprite in all_creeper_sprites:
                        sprite.kill()

    def operate_buy_menu(self):
        """
        Listens for key presses while buy menu is shown inbetween waves.
        Calls function according to the keypress
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1] and time.time() - self.buy_moment > self.buy_delay:
            if buy_bullet_upgrade(game=self,
                                  bullet_stats=BULLET):
                if self.sound_is_on:
                    self.buy_sound.play()

            self.buy_moment = time.time()

        if keys[pygame.K_2] and time.time() - self.buy_moment > self.buy_delay:
            if buy_bomb_upgrade(game=self,
                                bomb_stats=BOMB):
                if self.sound_is_on:
                    self.buy_sound.play()

            self.buy_moment = time.time()

        if keys[pygame.K_3] and time.time() - self.buy_moment > self.buy_delay:
            if buy_bomb(game=self,
                        player=self.player):
                if self.sound_is_on:
                    self.buy_sound.play()

            self.buy_moment = time.time()

        if keys[pygame.K_4] and time.time() - self.buy_moment > self.buy_delay:
            if buy_portal(game=self,
                          player=self.player):
                if self.sound_is_on:
                    self.buy_sound.play()

            self.buy_moment = time.time()

    def get_highscore_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                    self.player.highscore_name = self.player.highscore_name[:-1]

                elif event.key == pygame.K_RETURN:
                    save_player_score(self.player)
                    nickname = self.player.highscore_name
                    self.reset_game()
                    self.player.highscore_name = nickname

                else:
                    if len(self.player.highscore_name) < 11:
                        self.player.highscore_name += event.unicode

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
                           position=random.choice(SKULL_COLLECTOR["start_position"]),
                           character=SKULL_COLLECTOR)
        # Spawn Rushers
        for _ in range(RUSHER["wave_spawns"][self.player.wave_level]):
            spawn_pos = get_safe_spawn(player_loc=self.player.rect.center,
                                       enemy_spawns=RUSHER["start_position"])
            Rusher(player=self.player,
                   position=spawn_pos,
                   character=RUSHER)
        # Spawn Bats
        for _ in range(BAT["wave_spawns"][self.player.wave_level]):
            spawn_pos = get_safe_spawn(player_loc=self.player.rect.center,
                                       enemy_spawns=BAT["start_position"])
            Bat(player=self.player,
                position=spawn_pos,
                creeper_name=BAT)
        # Spawn Fish
        for _ in range(FISH["wave_spawns"][self.player.wave_level]):
            spawn_pos = get_safe_spawn(player_loc=self.player.rect.center,
                                       enemy_spawns=FISH["start_position"])
            Fish(player=self.player,
                 position=spawn_pos,
                 creeper_name=FISH)

    def end_of_wave_spawns(self):
        """
        Spawns PickUps after a wave has been cleared.
        """
        for _ in range(self.player.wave_level):
            PickUp(player=self.player,
                   pickup_name=HEALTH_POTION,
                   position=None)

    def turn_off_menus(self):
        """
        Disables all menu states.
        """
        self.main_menu_shown = False
        self.settings_menu_shown = False
        self.leaderboard_menu_shown = False
        self.credits_menu_shown = False
        self.pause_menu_shown = False

    def reset_player(self):
        # Buy menu
        self.player.buy_multiplier = PLAYER["buy_multiplier"]
        self.player.buy_multiplier_addition = PLAYER["buy_multiplier_addition"]
        self.player.bullet_upgrade_cost = PLAYER["bullet_upgrade_cost"]
        self.player.bomb_upgrade_cost = PLAYER["bomb_upgrade_cost"]
        self.player.buy_bomb_cost = PLAYER["buy_bomb_cost"]
        self.player.buy_portal_cost = PLAYER["buy_portal_cost"]

        # Attributes
        self.player.position = pygame.math.Vector2(PLAYER["start_position"])
        self.player.speed = PLAYER["speed"]
        self.player.health = PLAYER["health"]
        self.player.max_health = PLAYER["max_health"]
        self.player.health_potion_boost = PLAYER["health_potion_boost"]

        self.player.skull_level = PLAYER["skull_level"]
        self.player.energy_level = PLAYER["energy_level"]
        self.player.coin_level = PLAYER["coin_level"]
        self.player.wave_level = PLAYER["wave_level"]
        self.player.total_bombs = PLAYER["total_bombs"]
        self.player.total_portals = PLAYER["total_portals"]
        self.player.total_health_potions = PLAYER["total_health_potions"]

        # Misc
        self.player.health_checker = self.player.health
        self.player.kills = {
            "skull_collector": 0,
            "rusher": 0,
            "bat": 0,
            "fish": 0,
        }
        self.player.kill_points = {
            "skull_collector": PLAYER["skull_collector_points"],
            "rusher": PLAYER["rusher_points"],
            "bat": PLAYER["bat_points"],
            "fish": PLAYER["fish_points"],
        }

    def reset_game(self):
        """
        Removes all sprites and resets all settings.
        """
        for sprite in all_sprites:
            if not sprite.name == "player":
                sprite.kill()
        # all_sprites.empty()

        self.reset_player()
        # States
        self.game_is_over = False
        self.game_is_running = True
        self.is_playing_game = False
        self.main_menu_shown = True
        self.settings_menu_shown = False
        self.credits_menu_shown = False
        self.pause_menu_shown = False

        self.before_settings_menu = "home"

        # Trackers
        self.test_tick = 0
        self.wave_pause_ticks = 0
        self.wave_pause = GENERAL["wave_pause"]
        self.buy_tick = GENERAL["buy_tick"]
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

    def show_menu_screens(self):
        # Main menu
        if self.main_menu_shown:
            self.display_menus.display_main_menu(game_setup=self)

        # Settings menu
        elif self.settings_menu_shown:
            self.display_menus.display_settings_menu(game_setup=self)

        # Leaderboard menu
        elif self.leaderboard_menu_shown:
            self.display_menus.display_leaderboad_menu(game_setup=self)

        # Credits menu
        elif self.credits_menu_shown:
            self.display_menus.display_credit_menu(game_setup=self)

        # Pause menu
        elif self.pause_menu_shown:
            self.display_menus.display_pause_menu(game_setup=self)

    def check_player_death(self):
        if self.player.health < 0 and self.is_playing_game:
            self.game_is_over = True
            self.is_playing_game = False

    def show_game_over_screen(self):
        if self.game_is_over:
            self.display_interfaces.display_game_over()

            # Calculate base position
            base_x = 300
            base_y = 150

            # Enter name
            self.get_highscore_input()

            name_text_render = self.medium_font.render(
                f"{self.player.highscore_name}",
                True, GENERAL["white"])
            screen.blit(name_text_render, (base_x + 575, base_y + 650))

    def check_new_round_start(self):
        if not len(enemy_sprites) and not len(all_creeper_sprites):
            self.wave_pause_ticks += 1

            if self.wave_pause_ticks == self.wave_pause:
                # Start wave after buy phase
                self.bonus_ticks = self.bonus_ticks_list[
                    self.player.wave_level]  # Set bonus timer
                self.wave_pause_ticks = 0
                self.spawn_waves()
                self.level_completed = False
                self.player.wave_level += 1

    def check_time_bonus(self):
        if not len(enemy_sprites) \
                and not len(all_creeper_sprites) \
                and self.wave_pause_ticks == 1 \
                and not self.level_completed \
                and not self.player.wave_level == 0 \
                and self.bonus_ticks > 0:
            print(f"bonus lvl {self.player.wave_level}")
            self.level_completed = True

    def run_game(self):
        """
        Runs the utilities.

        Listens for events.
        Checks if menu's should be displayed.
        Checks if utilities is running.
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
            self.operate_special_keys()

            # Menus
            self.show_menu_screens()

            # Check death
            self.check_player_death()

            # Game over screen
            if self.game_is_over:
                self.show_game_over_screen()

            # Play
            elif self.is_playing_game:
                # Events (key presses)
                self.operate_special_keys()

                # Start wave countdown if no enemies present
                self.check_new_round_start()

                # Spawn items after wave completed
                if self.wave_pause_ticks == 1:
                    self.end_of_wave_spawns()

                # Utility handlers (collisions)
                handle_outgoing_projectiles()
                handle_outgoing_bombs()
                handle_incoming_projectiles()
                handle_pickups()

                # Camera offset
                # self.display_game.blit_level_objects()
                self.display_game.blit_all_sprites()

                # Hitboxes
                # self.display_game.show_hitboxes(screen=self.screen,
                #                                 player=self.player,
                #                                 skull_collector=True,
                #                                 rusher=True,
                #                                 bat=True,
                #                                 fish=True)

                # Screen info (health, items..)
                self.display_interfaces.show_stats()

                # Time bonus
                self.check_time_bonus()

                # Bonus timer
                if self.bonus_ticks > 0 and self.wave_pause_ticks == 0:
                    self.bonus_ticks -= 1

                self.display_interfaces.show_bonus_timer(ticks=self.bonus_ticks)

                # Display buy menu text
                if self.wave_pause_ticks > 0:
                    self.display_interfaces.show_new_wave_info()
                    self.display_interfaces.show_buy_menu()
                    self.display_interfaces.show_buy_menu_countdown(ticks=self.wave_pause_ticks)
                # Let user buy items
                self.operate_buy_menu()

                # Update sprites
                all_sprites.update()

                # Update screen
                self.clock.tick(GENERAL["FPS"])

            pygame.display.update()

        pygame.quit()
        exit()
