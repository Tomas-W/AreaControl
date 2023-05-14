import os
import sys

import pygame

from settings.general_settings import GENERAL

from settings.player_settings import PLAYER
from settings.enemy_settings import SKULL_COLLECTOR, RUSHER
from settings.creeper_settings import BAT, FISH

from settings.interactives_settings import SKULL, ENERGY

from settings.projectile_settings import FLAMING_SKULL, BULLET, BOMB

from utilities import all_sprites

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


class Camera(pygame.sprite.Group):
    """
    Shifts all Sprites by an offset to keep Player centered in Camera.
    Offset is calculated based on screen dimensions.
    """

    def __init__(self, background):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft=GENERAL["origin"])

        self.skull_collector_image = pygame.image.load(
            os.path.join(base_dir, "./images/camera/skull_collector.png"))
        self.rusher_image = pygame.image.load(
            os.path.join(base_dir, "./images/camera/rusher.png"))
        self.bat_image = pygame.image.load(
            os.path.join(base_dir, "./images/camera/bat.png"))
        self.fish_image = pygame.image.load(
            os.path.join(base_dir, "./images/camera/fish.png"))

        self.skull_image = pygame.image.load(
            os.path.join(base_dir, "./images/camera/skull.png"))
        self.energy_image = pygame.image.load(
            os.path.join(base_dir, "./images/camera/energy.png"))
        self.coin_image = pygame.image.load(
            os.path.join(base_dir, "./images/camera/coin.png"))
        self.bomb_image = pygame.image.load(
            os.path.join(base_dir, "./images/camera/bomb.png"))
        self.portal_image = pygame.image.load(
            os.path.join(base_dir, "./images/camera/portal.png"))

        self.btn_1 = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_1.png"))
        self.btn_2 = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_2.png"))
        self.btn_3 = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_3.png"))
        self.btn_4 = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_4.png"))

        # Fonts
        self.small_font = pygame.font.Font(os.path.join(base_dir, "fonts/PublicPixel.ttf"), 15)
        self.medium_font = pygame.font.Font(os.path.join(base_dir, "fonts/PublicPixel.ttf"), 30)
        self.large_font = pygame.font.Font(os.path.join(base_dir, "fonts/PublicPixel.ttf"), 60)
        self.font_color = GENERAL["white"]

    def custom_draw(self, screen, background, player):
        """
        Blits all Sprites to the main screen.

        :param screen: Display to blit Sprites to (obj).
        :param background: Level image (png).
        :param player: Player instance (obj).
        """
        # Calculate offset
        self.offset.x = player.rect.centerx - GENERAL["half_width"]
        self.offset.y = player.rect.centery - GENERAL["half_height"]

        # draw the floor
        floor_offset = self.floor_rect.topleft - self.offset
        screen.blit(background, floor_offset)

        for sprite in all_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)

    def show_new_wave_info(self, screen, player):
        """
        Displays wave count and total Enemies in wave.

        :param screen: Display to blit Sprites to (obj).
        :param player: Player instance (obj).
        """
        # Calculate base position
        base_position = (player.rect.centerx - GENERAL["wave_text_x_offset"],
                         player.rect.centery - GENERAL["wave_text_y_offset"])
        new_base_position = base_position - self.offset
        base_x = new_base_position[0]
        base_y = new_base_position[1]

        # Wave text
        wave_text = self.medium_font.render(f"Prepare for wave {player.wave_level + 1}", True,
                                            GENERAL["white"])
        screen.blit(wave_text, (base_x,
                                base_y))

        # SkullCollectors
        screen.blit(self.skull_collector_image, (base_x,
                                                 base_y + 50))
        skull_collector_number = self.small_font.render(
            f"{SKULL_COLLECTOR['wave_spawns'][player.wave_level]:02}", True,
            GENERAL["white"])
        screen.blit(skull_collector_number, (base_x + 10,
                                             base_y + 150))

        # Rushers
        screen.blit(self.rusher_image, (base_x + 160,
                                        base_y + 50))
        rusher_number = self.small_font.render(
            f"{RUSHER['wave_spawns'][player.wave_level]:02}", True,
            GENERAL["white"])
        screen.blit(rusher_number, (base_x + 150 + 37,
                                    base_y + 150))

        # Bats
        screen.blit(self.bat_image, (base_x + 310,
                                     base_y + 50))
        bat_number = self.small_font.render(
            f"{BAT['wave_spawns'][player.wave_level]:02}", True,
            GENERAL["white"])
        screen.blit(bat_number, (base_x + 300 + 37,
                                 base_y + 150))

        # Fishes
        screen.blit(self.fish_image, (base_x + 460,
                                      base_y + 50))
        fish_number = self.small_font.render(
            f"{FISH['wave_spawns'][player.wave_level]:02}", True,
            GENERAL["white"])
        screen.blit(fish_number, (base_x + 450 + 37,
                                  base_y + 150))

    def show_buy_menu_countdown(self, screen, player, ticks):
        # Calculate base position
        base_position = (player.rect.centerx - GENERAL["countdown_x_offset"],
                         player.rect.centery - GENERAL["countdown_y_offset"])
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
        screen.blit(countdown, (base_x,
                                base_y))

    def show_buy_menu(self, screen, player):
        """
        Displays wave buy menu.

        :param screen: Display to blit Sprites to (obj).
        :param player: Player instance (obj).
        """
        # Calculate base position
        base_position = (player.rect.centerx - GENERAL["buy_menu_x_offset"],
                         player.rect.centery - GENERAL["buy_menu_y_offset"])
        new_base_position = base_position - self.offset
        base_x = new_base_position[0]
        base_y = new_base_position[1]

        # Upgrade bullets
        # Button image
        screen.blit(self.btn_1, (base_x,
                                 base_y))
        # Buy text
        btn_1_text_a = self.small_font.render("Upgrade", True,
                                              GENERAL["white"])
        screen.blit(btn_1_text_a, (base_x,
                                   base_y + 65))
        btn_1_text_b = self.small_font.render("Bullets", True,
                                              GENERAL["white"])
        screen.blit(btn_1_text_b, (base_x,
                                   base_y + 95))
        # Coin image
        screen.blit(self.coin_image, (base_x,
                                      base_y + 120))
        # Coin cost
        bullet_coin_cost = self.small_font.render(
            str(int(player.buy_multiplier * player.bullet_upgrade_cost)), True,
            GENERAL["white"])
        screen.blit(bullet_coin_cost, (base_x + 65,
                                       base_y + 135))
        # Upgrade amount
        bullet_upgrade_amount = self.small_font.render(
            "+ 5%", True,
            GENERAL["white"])
        screen.blit(bullet_upgrade_amount, (base_x,
                                            base_y + 185))

        # Upgrade bombs
        # Button image
        screen.blit(self.btn_2, (base_x + 150,
                                 base_y))
        # Buy text
        btn_2_text_a = self.small_font.render("Upgrade", True,
                                              GENERAL["white"])
        screen.blit(btn_2_text_a, (base_x + 150,
                                   base_y + 65))
        btn_2_text_b = self.small_font.render("Bombs", True,
                                              GENERAL["white"])
        screen.blit(btn_2_text_b, (base_x + 150,
                                   base_y + 95))
        # Coin image
        screen.blit(self.coin_image, (base_x + 150,
                                      base_y + 120))
        # Coin cost
        bomb_coin_cost = self.small_font.render(
            str(int(player.buy_multiplier * player.bomb_upgrade_cost)), True,
            GENERAL["white"])
        screen.blit(bomb_coin_cost, (base_x + 150 + 65,
                                     base_y + 135))
        # Upgrade amount
        bomb_upgrade_amount = self.small_font.render(
            "+ 7%", True,
            GENERAL["white"])
        screen.blit(bomb_upgrade_amount, (base_x + 150,
                                          base_y + 185))

        # Buy bombs
        # Button image
        screen.blit(self.btn_3, (base_x + 300,
                                 base_y))
        # Buy text
        btn_3_text_a = self.small_font.render("Buy", True,
                                              GENERAL["white"])
        screen.blit(btn_3_text_a, (base_x + 300,
                                   base_y + 65))
        btn_3_text_b = self.small_font.render("Bombs", True,
                                              GENERAL["white"])
        screen.blit(btn_3_text_b, (base_x + 300,
                                   base_y + 95))
        # Skull image
        screen.blit(self.skull_image, (base_x + 300,
                                       base_y + 120))
        # Skull cost
        bomb_skull_cost = self.small_font.render(
            str(int(player.buy_multiplier * player.buy_bomb_cost)), True,
            GENERAL["white"])
        screen.blit(bomb_skull_cost, (base_x + 300 + 65,
                                      base_y + 135))

        # Buy teleport
        # Key image
        screen.blit(self.btn_4, (base_x + 450,
                                 base_y))
        # Buy text
        btn_4_text_a = self.small_font.render("Buy", True,
                                              GENERAL["white"])
        screen.blit(btn_4_text_a, (base_x + 450,
                                   base_y + 65))
        btn_4_text_b = self.small_font.render("Portals", True,
                                              GENERAL["white"])
        screen.blit(btn_4_text_b, (base_x + 450,
                                   base_y + 95))
        # Energy image
        screen.blit(self.energy_image, (base_x + 450,
                                        base_y + 120))
        # Energy cost
        teleport_energy_cost = self.small_font.render(
            str(int(player.buy_multiplier * player.buy_portal_cost)), True,
            GENERAL["white"])
        screen.blit(teleport_energy_cost, (base_x + 450 + 65,
                                           base_y + 135))

    def show_stats(self, screen, player):
        """
        Displays player attributes to the screen.
        Includes health and skill game.

        :param screen: Display to blit Sprites to (obj).
        :param player: Player instance (obj).
        """
        # Calculate base position (health-bar)
        base_position = (player.rect.centerx - GENERAL["health_bar_x_offset"],
                         player.rect.centery - GENERAL["health_bar_y_offset"])
        new_base_position = base_position - self.offset
        base_x = new_base_position[0]
        base_y = new_base_position[1]

        # Health
        pygame.draw.rect(screen,
                         GENERAL["green"],
                         (base_x, base_y,
                          player.health, GENERAL["health_bar_height"]))

        # Skulls
        screen.blit(self.skull_image, (base_x,
                                       base_y + 50))
        skull_number = self.small_font.render(f"{player.skull_level:02}", True, GENERAL["white"])
        screen.blit(skull_number, (base_x + 10,
                                   base_y + 110))

        # Energy
        screen.blit(self.energy_image, (base_x + 85,
                                        base_y + 50))
        energy_number = self.small_font.render(f"{player.energy_level:02}", True, GENERAL["white"])
        screen.blit(energy_number, (base_x + 104,
                                    base_y + 110))

        # Coin
        screen.blit(self.coin_image, (base_x + 185,
                                      base_y + 50))
        coin_number = self.small_font.render(f"{player.coin_level:02}", True, GENERAL["white"])
        screen.blit(coin_number, (base_x + 195,
                                  base_y + 110))

        # Bomb
        screen.blit(self.bomb_image, (base_x + 1320,
                                      base_y + 35))
        bomb_number = self.small_font.render(f"{player.total_bombs:02}", True, GENERAL["white"])
        screen.blit(bomb_number, (base_x + 1340,
                                  base_y + 110))

        # Portal
        screen.blit(self.portal_image, (base_x + 1440,
                                        base_y + 35))
        bomb_number = self.small_font.render(f"{player.total_bombs:02}", True, GENERAL["white"])
        screen.blit(bomb_number, (base_x + 1460,
                                  base_y + 110))

    @staticmethod
    def show_hitboxes(screen, player=None, skull_collector=False, rusher=False,
                      bat=False, fish=False,
                      bullet=False, bomb=False, flaming_skull=False,
                      skull=False, energy=False):
        """
        Draws hitboxes if True.
        Player needs instance.
        """
        if player is not None:
            if not player.shoot:
                pygame.draw.rect(player.base_image,
                                 GENERAL["blue"],
                                 pygame.Rect(PLAYER["hitbox"]),
                                 2)
            elif player.shoot:
                pygame.draw.rect(player.base_image_shoot,
                                 GENERAL["blue"],
                                 pygame.Rect(PLAYER["hitbox"]),
                                 2)

        for item in all_sprites:
            if skull_collector:
                if item.name == "skull_collector":
                    pygame.draw.rect(item.image,
                                     GENERAL["red"],
                                     pygame.Rect(SKULL_COLLECTOR["hitbox"]),
                                     2)

            if rusher:
                if item.name == "rusher":
                    pygame.draw.rect(item.image,
                                     GENERAL["red"],
                                     pygame.Rect(RUSHER["hitbox"]),
                                     2)

            if bat:
                if item.name == "bat":
                    pygame.draw.rect(item.image,
                                     GENERAL["red"],
                                     pygame.Rect(BAT["hitbox"]),
                                     2)

            if fish:
                if item.name == "fish":
                    pygame.draw.rect(item.image,
                                     GENERAL["red"],
                                     pygame.Rect(FISH["hitbox"]),
                                     2)

            if skull:
                if item.name == "skull":
                    pygame.draw.rect(item.image,
                                     GENERAL["blue"],
                                     pygame.Rect(SKULL["hitbox"]),
                                     2)

            if energy:
                if item.name == "energy":
                    pygame.draw.rect(item.image,
                                     GENERAL["blue"],
                                     pygame.Rect(ENERGY["hitbox"]),
                                     2)

            if bullet:
                if item.name == "bullet":
                    pygame.draw.rect(item.image,
                                     GENERAL["green"],
                                     pygame.Rect(BULLET["hitbox"]),
                                     2)

            if bomb:
                if item.name == "bomb":
                    if not item.explode:

                        pygame.draw.rect(item.image,
                                         GENERAL["blue"],
                                         pygame.Rect(BOMB["hitbox"]),
                                         2)
                    else:
                        pygame.draw.circle(screen,
                                           GENERAL["blue"],
                                           item.image.get_rect().center,
                                           item.image.get_width() // 2,
                                           2)

            if flaming_skull:
                if item.name == "flaming_skull":
                    pygame.draw.rect(item.image,
                                     GENERAL["red"],
                                     pygame.Rect(FLAMING_SKULL["hitbox"]),
                                     2)
