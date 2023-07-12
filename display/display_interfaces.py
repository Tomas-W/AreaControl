from settings.general_settings import GENERAL
from settings.menu_settings import DISPLAY
from settings.enemy_settings import SKULL_COLLECTOR, RUSHER
from settings.creeper_settings import BAT, FISH


from sprites.camera_sprites import *
from fonts.fonts import *

from utilities.general import get_health_color_list

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


class DisplayInterfaces(pygame.sprite.Group):
    """
    Blits in-utilities information to screen e.g.
        items, wave info, buy info
    """

    def __init__(self, screen, background, player):
        super().__init__()
        self.screen = screen
        self.offset = pygame.math.Vector2()
        self.offset.x = player.rect.centerx - GENERAL["half_width"]
        self.offset.y = player.rect.centery - GENERAL["half_height"]
        self.floor_rect = background.get_rect(topleft=GENERAL["origin"])
        self.player = player

        # Character images
        self.skull_collector_image = SKULL_COLLECTOR_CAMERA_IMAGE
        self.rusher_image = RUSHER_CAMERA_IMAGE
        # Creeper images
        self.bat_image = BAT_CAMERA_IMAGE
        self.fish_image = FISH_CAMERA_IMAGE
        # PickUp images
        self.skull_image = SKULL_CAMERA_IMAGE
        self.energy_image = ENERGY_CAMERA_IMAGE
        self.coin_image = COIN_CAMERA_IMAGE
        # Item images
        self.bomb_image = BOMB_CAMERA_IMAGE
        self.portal_image = PORTAL_CAMERA_IMAGE
        self.health_potion_image = HEALTH_POTION_CAMERA_IMAGE
        # Button images
        self.btn_1 = BUTTON_1_CAMERA_IMAGE
        self.btn_2 = BUTTON_2_CAMERA_IMAGE
        self.btn_3 = BUTTON_3_CAMERA_IMAGE
        self.btn_4 = BUTTON_4_CAMERA_IMAGE

        # Fonts
        self.small_font = SMALL_FONT
        self.medium_font = MEDIUM_FONT
        self.large_font = LARGE_FONT
        self.font_color = FONT_COLOR

        # Misc
        self.health_color_list = get_health_color_list()

    def show_stats(self):
        """
        Displays player attributes to the screen.
        Includes health and skill utilities.
        """
        # Calculate base position (health-bar)
        base_position = (self.player.rect.centerx - DISPLAY["health_bar_x_offset"] ,
                         self.player.rect.centery - DISPLAY["health_bar_y_offset"])

        # Calculate offset
        self.offset.x = self.player.rect.centerx - GENERAL["half_width"]
        self.offset.y = self.player.rect.centery - GENERAL["half_height"]

        new_base_position = base_position - self.offset
        base_x = new_base_position[0]
        base_y = new_base_position[1]

        # Health-bar
        pygame.draw.rect(self.screen,
                         self.health_color_list[max(int(self.player.health / 10), 0)],
                         (base_x, base_y,
                          self.player.health, DISPLAY["health_bar_height"]))
        # Health-bar outline
        pygame.draw.rect(self.screen,
                         GENERAL["black"],
                         (base_x, base_y,
                          self.player.max_health, DISPLAY["health_bar_height"]),
                         2)

        # Health-bar text
        health_number = self.small_font.render(f"{int(max(0, self.player.health))}", True,
                                               GENERAL["white"])
        self.screen.blit(health_number, (base_x + 10,
                                    base_y + 6))

        # Skulls
        self.screen.blit(self.skull_image, (base_x,
                                       base_y + 50))
        skull_number = self.small_font.render(f"{self.player.skull_level:02}", True, GENERAL["white"])
        self.screen.blit(skull_number, (base_x + 10,
                                   base_y + 110))

        # Energy
        self.screen.blit(self.energy_image, (base_x + 85,
                                        base_y + 50))
        energy_number = self.small_font.render(f"{self.player.energy_level:02}", True, GENERAL["white"])
        self.screen.blit(energy_number, (base_x + 104,
                                    base_y + 110))

        # Coin
        self.screen.blit(self.coin_image, (base_x + 185,
                                      base_y + 50))
        coin_number = self.small_font.render(f"{self.player.coin_level:02}", True, GENERAL["white"])
        self.screen.blit(coin_number, (base_x + 195,
                                  base_y + 110))

        # Health potion
        self.screen.blit(self.health_potion_image, (base_x + 1220,
                                               base_y + 45))
        health_potion_number = self.small_font.render(f"{self.player.total_health_potions:02}", True,
                                                      GENERAL["white"])
        self.screen.blit(health_potion_number, (base_x + 1233,
                                           base_y + 110))

        # Bomb
        self.screen.blit(self.bomb_image, (base_x + 1320,
                                      base_y + 35))
        bomb_number = self.small_font.render(f"{self.player.total_bombs:02}", True, GENERAL["white"])
        self.screen.blit(bomb_number, (base_x + 1340,
                                  base_y + 110))

        # Portal
        self.screen.blit(self.portal_image, (base_x + 1440,
                                        base_y + 35))
        bomb_number = self.small_font.render(f"{self.player.total_portals:02}", True, GENERAL["white"])
        self.screen.blit(bomb_number, (base_x + 1460,
                                  base_y + 110))

    def show_new_wave_info(self):
        """
        Displays wave count and total Enemies in wave.
        """
        # Calculate base position
        base_position = (self.player.rect.centerx - DISPLAY["wave_text_x_offset"],
                         self.player.rect.centery - DISPLAY["wave_text_y_offset"])
        new_base_position = base_position - self.offset
        base_x = new_base_position[0]
        base_y = new_base_position[1]

        # Wave text
        wave_text = self.medium_font.render(f"Prepare for wave {self.player.wave_level + 1}", True,
                                            GENERAL["white"])
        self.screen.blit(wave_text, (base_x,
                                base_y))

        # SkullCollectors
        self.screen.blit(self.skull_collector_image, (base_x,
                                                 base_y + 50))
        skull_collector_number = self.small_font.render(
            f"{SKULL_COLLECTOR['wave_spawns'][self.player.wave_level]:02}", True,
            GENERAL["white"])
        self.screen.blit(skull_collector_number, (base_x + 10,
                                             base_y + 150))

        # Rushers
        self.screen.blit(self.rusher_image, (base_x + 160,
                                        base_y + 50))
        rusher_number = self.small_font.render(
            f"{RUSHER['wave_spawns'][self.player.wave_level]:02}", True,
            GENERAL["white"])
        self.screen.blit(rusher_number, (base_x + 150 + 37,
                                    base_y + 150))

        # Bats
        self.screen.blit(self.bat_image, (base_x + 310,
                                     base_y + 50))
        bat_number = self.small_font.render(
            f"{BAT['wave_spawns'][self.player.wave_level]:02}", True,
            GENERAL["white"])
        self.screen.blit(bat_number, (base_x + 300 + 37,
                                 base_y + 150))

        # Fish
        self.screen.blit(self.fish_image, (base_x + 460,
                                      base_y + 50))
        fish_number = self.small_font.render(
            f"{FISH['wave_spawns'][self.player.wave_level]:02}", True,
            GENERAL["white"])
        self.screen.blit(fish_number, (base_x + 450 + 37,
                                  base_y + 150))

    def show_buy_menu_countdown(self, ticks):
        """
        Displays buy menu in-between waves.

        :param ticks: Current wave tick (int).
        """
        # Calculate base position
        base_position = (self.player.rect.centerx - DISPLAY["countdown_x_offset"],
                         self.player.rect.centery - DISPLAY["countdown_y_offset"])
        new_base_position = base_position - self.offset
        base_x = new_base_position[0]
        base_y = new_base_position[1]

        if 0 < ticks < 60:
            number = "03"
        elif ticks < 120:
            number = "02"
        elif ticks < 180:
            number = "01"
        else:
            number = "GO"

        countdown = self.large_font.render(number, True,
                                           GENERAL["white"])
        self.screen.blit(countdown, (base_x,
                                base_y))

    def show_buy_menu(self):
        """
        Displays wave buy menu.
        """
        # Calculate base position
        base_position = (self.player.rect.centerx - DISPLAY["buy_menu_x_offset"],
                         self.player.rect.centery - DISPLAY["buy_menu_y_offset"])
        new_base_position = base_position - self.offset
        base_x = new_base_position[0]
        base_y = new_base_position[1]

        # UPGRADE BULLETS
        # Button image
        self.screen.blit(self.btn_1, (base_x,
                                 base_y))
        # Buy text
        btn_1_text_a = self.small_font.render("Upgrade", True,
                                              GENERAL["white"])
        self.screen.blit(btn_1_text_a, (base_x,
                                   base_y + 65))
        btn_1_text_b = self.small_font.render("Bullets", True,
                                              GENERAL["white"])
        self.screen.blit(btn_1_text_b, (base_x,
                                   base_y + 95))
        # Coin image
        self.screen.blit(self.coin_image, (base_x,
                                      base_y + 120))
        # Coin cost
        bullet_coin_cost = self.small_font.render(
            str(int(self.player.buy_multiplier * self.player.bullet_upgrade_cost)), True,
            GENERAL["white"])
        self.screen.blit(bullet_coin_cost, (base_x + 65,
                                       base_y + 135))
        # Upgrade amount
        bullet_upgrade_amount = self.small_font.render(
            "+ 5%", True,
            GENERAL["white"])
        self.screen.blit(bullet_upgrade_amount, (base_x,
                                            base_y + 185))

        # UPGRADE BOMBS
        # Button image
        self.screen.blit(self.btn_2, (base_x + 150,
                                 base_y))
        # Buy text
        btn_2_text_a = self.small_font.render("Upgrade", True,
                                              GENERAL["white"])
        self.screen.blit(btn_2_text_a, (base_x + 150,
                                   base_y + 65))
        btn_2_text_b = self.small_font.render("Bombs", True,
                                              GENERAL["white"])
        self.screen.blit(btn_2_text_b, (base_x + 150,
                                   base_y + 95))
        # Coin image
        self.screen.blit(self.coin_image, (base_x + 150,
                                      base_y + 120))
        # Coin cost
        bomb_coin_cost = self.small_font.render(
            str(int(self.player.buy_multiplier * self.player.bomb_upgrade_cost)), True,
            GENERAL["white"])
        self.screen.blit(bomb_coin_cost, (base_x + 150 + 65,
                                     base_y + 135))
        # Upgrade amount
        bomb_upgrade_amount = self.small_font.render(
            "+ 7%", True,
            GENERAL["white"])
        self.screen.blit(bomb_upgrade_amount, (base_x + 150,
                                          base_y + 185))

        # BUY BOMB
        # Button image
        self.screen.blit(self.btn_3, (base_x + 300,
                                 base_y))
        # Buy text
        btn_3_text_a = self.small_font.render("Buy", True,
                                              GENERAL["white"])
        self.screen.blit(btn_3_text_a, (base_x + 300,
                                   base_y + 65))
        btn_3_text_b = self.small_font.render("Bomb", True,
                                              GENERAL["white"])
        self.screen.blit(btn_3_text_b, (base_x + 300,
                                   base_y + 95))
        # Skull image
        self.screen.blit(self.skull_image, (base_x + 300,
                                       base_y + 120))
        # Skull cost
        bomb_skull_cost = self.small_font.render(
            str(int(self.player.buy_multiplier * self.player.buy_bomb_cost)), True,
            GENERAL["white"])
        self.screen.blit(bomb_skull_cost, (base_x + 300 + 65,
                                      base_y + 135))

        # BUY TELEPORT
        # Button image
        self.screen.blit(self.btn_4, (base_x + 450,
                                 base_y))
        # Buy text
        btn_4_text_a = self.small_font.render("Buy", True,
                                              GENERAL["white"])
        self.screen.blit(btn_4_text_a, (base_x + 450,
                                   base_y + 65))
        btn_4_text_b = self.small_font.render("Portal", True,
                                              GENERAL["white"])
        self.screen.blit(btn_4_text_b, (base_x + 450,
                                   base_y + 95))
        # Energy image
        self.screen.blit(self.energy_image, (base_x + 450,
                                        base_y + 120))
        # Energy cost
        teleport_energy_cost = self.small_font.render(
            str(int(self.player.buy_multiplier * self.player.buy_portal_cost)), True,
            GENERAL["white"])
        self.screen.blit(teleport_energy_cost, (base_x + 450 + 70,
                                           base_y + 135))

    def show_hud(self):
        """
        Displays player attributes to the screen.
        Includes health and skill utilities.
        """
        # Calculate base position (health-bar)
        base_position = (self.player.rect.centerx - DISPLAY["health_bar_x_offset"],
                         self.player.rect.centery - DISPLAY["health_bar_y_offset"])
        new_base_position = base_position - self.offset
        base_x = new_base_position[0]
        base_y = new_base_position[1]

        # Health-bar
        pygame.draw.rect(self.screen,
                         self.health_color_list[max(int(self.player.health / 10), 0)],
                         (base_x, base_y,
                          self.player.health, DISPLAY["health_bar_height"]))
        # Health-bar outline
        pygame.draw.rect(self.screen,
                         GENERAL["black"],
                         (base_x, base_y,
                          self.player.max_health, DISPLAY["health_bar_height"]),
                         2)

        # Health-bar text
        health_number = self.small_font.render(f"{int(max(0, self.player.health))}", True,
                                               GENERAL["white"])
        self.screen.blit(health_number, (base_x + 10,
                                    base_y + 6))

        # Skulls
        self.screen.blit(self.skull_image, (base_x,
                                       base_y + 50))
        skull_number = self.small_font.render(f"{self.player.skull_level:02}", True, GENERAL["white"])
        self.screen.blit(skull_number, (base_x + 10,
                                   base_y + 110))

        # Energy
        self.screen.blit(self.energy_image, (base_x + 85,
                                        base_y + 50))
        energy_number = self.small_font.render(f"{self.player.energy_level:02}", True, GENERAL["white"])
        self.screen.blit(energy_number, (base_x + 104,
                                    base_y + 110))

        # Coin
        self.screen.blit(self.coin_image, (base_x + 185,
                                      base_y + 50))
        coin_number = self.small_font.render(f"{self.player.coin_level:02}", True, GENERAL["white"])
        self.screen.blit(coin_number, (base_x + 195,
                                  base_y + 110))

        # Health potion
        self.screen.blit(self.health_potion_image, (base_x + 1220,
                                               base_y + 45))
        health_potion_number = self.small_font.render(f"{self.player.total_health_potions:02}", True,
                                                      GENERAL["white"])
        self.screen.blit(health_potion_number, (base_x + 1233,
                                           base_y + 110))

        # Bomb
        self.screen.blit(self.bomb_image, (base_x + 1320,
                                      base_y + 35))
        bomb_number = self.small_font.render(f"{self.player.total_bombs:02}", True, GENERAL["white"])
        self.screen.blit(bomb_number, (base_x + 1340,
                                  base_y + 110))

        # Portal
        self.screen.blit(self.portal_image, (base_x + 1440,
                                        base_y + 35))
        bomb_number = self.small_font.render(f"{self.player.total_portals:02}", True, GENERAL["white"])
        self.screen.blit(bomb_number, (base_x + 1460,
                                  base_y + 110))

    def show_bonus_timer(self, ticks):
        # Calculate base position (health-bar)
        base_position = (self.player.rect.centerx - DISPLAY["health_bar_x_offset"],
                         self.player.rect.centery - DISPLAY["health_bar_y_offset"])
        new_base_position = base_position - self.offset
        base_x = new_base_position[0]
        base_y = new_base_position[1]

        bonus_timer_text = self.small_font.render(f"Earn bonus {ticks // 60}", True,
                                                  GENERAL["white"])
        self.screen.blit(bonus_timer_text, (base_x + 650,
                                       base_y + 50))

    def display_game_over(self):
        self.screen.fill((35, 35, 35))

        # Calculate base position
        base_position = (self.player.rect.centerx - DISPLAY["game_over_x_offset"],
                         self.player.rect.centery - DISPLAY["game_over_y_offset"])
        new_base_position = base_position - self.offset
        base_x = new_base_position[0]
        base_y = new_base_position[1]

        # Game over text
        game_over_text = self.large_font.render("Game Over", True,
                                                GENERAL["white"])
        self.screen.blit(game_over_text, (base_x + 300,
                                     base_y - 50))

        # Continue text
        continue_text = self.small_font.render("press 'enter' to continue'", True,
                                               GENERAL["white"])
        self.screen.blit(continue_text, (base_x + 303,
                                    base_y + 25))

        # SkullCollector image
        self.screen.blit(self.skull_collector_image, (base_x + 250,
                                                 base_y + 100))
        # SkullCollectors killed
        skull_collectors_killed_text = self.small_font.render(
            f"{self.player.kills['skull_collector']}", True, GENERAL["white"])
        self.screen.blit(skull_collectors_killed_text, (base_x + 350,
                                                   base_y + 135))
        # SkullCollectors points
        skull_collectors_killed_text = self.small_font.render(
            f"=  {self.player.kill_points['skull_collector'] * self.player.kills['skull_collector']}", True,
            GENERAL["white"])
        self.screen.blit(skull_collectors_killed_text, (base_x + 650,
                                                   base_y + 135))

        # Rusher image
        self.screen.blit(self.rusher_image, (base_x + 250,
                                        base_y + 200))
        # Rushers killed
        rushers_killed_text = self.small_font.render(
            f"{self.player.kills['rusher']}", True, GENERAL["white"])
        self.screen.blit(rushers_killed_text, (base_x + 350,
                                          base_y + 235))
        # Rusher points
        rushers_killed_text = self.small_font.render(
            f"=  {self.player.kill_points['rusher'] * self.player.kills['rusher']}", True, GENERAL["white"])
        self.screen.blit(rushers_killed_text, (base_x + 650,
                                          base_y + 235))

        # Bat image
        self.screen.blit(self.bat_image, (base_x + 250,
                                     base_y + 300))
        # Bats killed
        bats_killed_text = self.small_font.render(
            f"{self.player.kills['bat']}", True, GENERAL["white"])
        self.screen.blit(bats_killed_text, (base_x + 350,
                                       base_y + 355))
        # Bat points
        bats_killed_text = self.small_font.render(
            f"=  {self.player.kill_points['bat'] * self.player.kills['bat']}", True, GENERAL["white"])
        self.screen.blit(bats_killed_text, (base_x + 650,
                                       base_y + 355))

        # Fish image
        self.screen.blit(self.fish_image, (base_x + 250,
                                      base_y + 400))
        # Fish killed
        fish_killed_text = self.small_font.render(
            f"{self.player.kills['fish']}", True, GENERAL["white"])
        self.screen.blit(fish_killed_text, (base_x + 350,
                                       base_y + 455))
        # Fish points
        fish_killed_text = self.small_font.render(
            f"=  {self.player.kill_points['fish'] * self.player.kills['fish']}", True, GENERAL["white"])
        self.screen.blit(fish_killed_text, (base_x + 650,
                                       base_y + 455))

        # Divider
        pygame.draw.rect(self.screen,
                         GENERAL["white"],
                         (base_x + 650, base_y + 510,
                          125, 4))

        # Total text
        total_text = self.medium_font.render("Total", True,
                                             GENERAL["white"])
        self.screen.blit(total_text, (base_x + 250,
                                 base_y + 575))
        # Total points
        total_points = self.medium_font.render(
            f"=  {(self.player.kill_points['skull_collector'] * self.player.kills['skull_collector']) + (self.player.kill_points['rusher'] * self.player.kills['rusher']) + (self.player.kill_points['bat'] * self.player.kills['bat']) + (self.player.kill_points['fish'] * self.player.kills['fish'])}",
            True, GENERAL["white"])
        self.screen.blit(total_points, (base_x + 575,
                                   base_y + 575))

        # Enter name text
        enter_name_text = self.medium_font.render("Name:", True,
                                                  GENERAL["white"])
        self.screen.blit(enter_name_text, (base_x + 255,
                                      base_y + 650))

        digits = int(str(pygame.time.get_ticks())[-3:-1])
        border_color = (255 - digits,
                        255 - digits,
                        255 - digits)

        pygame.draw.rect(self.screen,
                         border_color,
                         (base_x + 560, base_y + 640, 357, 53),
                         2)
