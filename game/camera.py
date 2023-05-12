import pygame

from settings.general_settings import GENERAL

from settings.player_settings import PLAYER
from settings.enemy_settings import SKULL_COLLECTOR, RUSHER, GOLEM
from settings.creeper_settings import BAT, FISH

from settings.interactives_settings import PORTAL, SKULL, ENERGY

from settings.projectile_settings import FLAMING_SKULL, BULLET, BOMB

from utilities import all_sprites, player_projectile_sprites, enemy_projectile_sprites, \
    portal_sprites, skull_sprites, energy_sprites, bomb_sprites


class Camera(pygame.sprite.Group):
    """
    Shifts all Sprites by an offset to keep Player centered in Camera.
    Offset is calculated based on screen dimensions.
    """

    def __init__(self, background):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft=GENERAL["origin"])

        self.skull_image = pygame.image.load("./images/interactives/skull/skull.png")
        self.energy_image = pygame.image.load("./images/interactives/energy/energy2.png")
        self.coin_image = pygame.image.load("./images/interactives/coin/coin.png")

        self.font = pygame.font.SysFont("comicsansms", 30)

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
        skull_number = self.font.render(str(player.skull_level), True, GENERAL["white"])
        screen.blit(skull_number, (base_x + 5,
                                   base_y + 100))

        # Energy
        screen.blit(self.energy_image, (base_x + 85,
                                        base_y + 50))
        energy_number = self.font.render(str(player.energy_level), True, GENERAL["white"])
        screen.blit(energy_number, (base_x + 85 + 15,
                                    base_y + 100))

        # Coin
        screen.blit(self.coin_image, (base_x + 185,
                                      base_y + 50))
        coin_number = self.font.render(str(player.coin_level), True, GENERAL["white"])
        screen.blit(coin_number, (base_x + 185 + 5,
                                  base_y + 100))

    def show_hitboxes(self, screen, player=None, skull_collector=None, rusher=None, golem=None,
                      bat=None,
                      fish=None, bullet=None, bomb=None, flaming_skull=None, skull=None,
                      energy=None,
                      portal=None):
        """
        Draws hitboxes.
        Player, SkullCollector and Rusher need instances, others only need to be not None.
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

        if skull_collector is not None:
            pygame.draw.rect(skull_collector.image,
                             GENERAL["red"],
                             pygame.Rect(SKULL_COLLECTOR["hitbox"]),
                             2)

        if rusher is not None:
            pygame.draw.rect(rusher.image,
                             GENERAL["red"],
                             pygame.Rect(RUSHER["hitbox"]),
                             2)

        if golem is not None:
            pygame.draw.rect(golem.image,
                             GENERAL["red"],
                             pygame.Rect(GOLEM["hitbox"]),
                             2)

        if bat is not None:
            pygame.draw.rect(bat.image,
                             GENERAL["red"],
                             pygame.Rect(BAT["hitbox"]),
                             2)

        if fish is not None:
            pygame.draw.rect(fish.image,
                             GENERAL["red"],
                             pygame.Rect(FISH["hitbox"]),
                             2)

        if bullet is not None:
            for bullet in player_projectile_sprites:
                pygame.draw.rect(bullet.image,
                                 GENERAL["blue"],
                                 pygame.Rect(BULLET["hitbox"]),
                                 2)

        if bomb is not None:
            for bomb in bomb_sprites:

                pygame.draw.circle(screen,
                                   GENERAL["blue"],
                                   bomb.bomb_location,
                                   8,
                                   2)

                if not bomb.explode:

                    pygame.draw.rect(bomb.image,
                                     GENERAL["blue"],
                                     pygame.Rect(BOMB["hitbox"]),
                                     2)

                else:
                    # print("***")
                    # print(bomb.bomb_location)
                    # print(bomb.rect.center)
                    # print("***")

                    pygame.draw.circle(bomb.image,
                                       GENERAL["blue"],
                                       bomb.image.get_rect().center,
                                       bomb.image.get_width() // 2,
                                       2)

        if flaming_skull is not None:
            for flaming_skull in enemy_projectile_sprites:
                pygame.draw.rect(flaming_skull.image,
                                 GENERAL["red"],
                                 pygame.Rect(FLAMING_SKULL["hitbox"]),
                                 2)

        if skull is not None:
            for skull in skull_sprites:
                pygame.draw.rect(skull.image,
                                 GENERAL["red"],
                                 pygame.Rect(SKULL["hitbox"]),
                                 2)

        if energy is not None:
            for energy in energy_sprites:
                pygame.draw.rect(energy.image,
                                 GENERAL["red"],
                                 pygame.Rect(ENERGY["hitbox"]),
                                 2)

        if portal is not None:
            for portal in portal_sprites:
                pygame.draw.rect(portal.image,
                                 GENERAL["blue"],
                                 pygame.Rect(PORTAL["hitbox"]),
                                 2)
