import pygame

from settings.creeper_settings import BAT, FISH
from settings.projectile_settings import FLAMING_SKULL, BULLET
from settings.enemy_settings import SKULL_COLLECTOR, RUSHER, GOLEM
from settings.general_settings import GENERAL
from settings.interactives_settings import PORTAL, SKULL, ENERGY
from settings.player_settings import PLAYER
from utilities import all_sprites, player_projectile_sprites, enemy_projectile_sprites, \
    portal_sprites, skull_sprites, energy_sprites


class Camera(pygame.sprite.Group):
    def __init__(self, background):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft=GENERAL["origin"])

        self.skull_image = pygame.image.load("images/interactives/skull/skull.png")
        self.energy_image = pygame.image.load("images/interactives/energy/energy2.png")
        self.coin_image = pygame.image.load("images/interactives/coin/coin.png")

        self.font = pygame.font.SysFont("comicsansms", 30)

    def custom_draw(self, screen, background, player):
        self.offset.x = player.rect.centerx - GENERAL["half_width"]
        self.offset.y = player.rect.centery - GENERAL["half_height"]

        # draw the floor
        floor_offset = self.floor_rect.topleft - self.offset
        screen.blit(background, floor_offset)

        for sprite in all_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)

    def show_bars(self, screen, player):
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

        # if skull is not None:
        #     bar_position = (player.rect.centerx - GENERAL["health_bar_x_offset"],
        #                     player.rect.centery - GENERAL["health_bar_y_offset"] + 75)
        #     new_bar_position = bar_position - self.offset
        #     bar_x = new_bar_position[0]
        #     bar_y = new_bar_position[1]
        #     pygame.draw.rect(screen,
        #                      GENERAL["red"],
        #                      (bar_x, bar_y,
        #                       player.skull_level, GENERAL["health_bar_height"]))
        #
        # if energy is not None:
        #     bar_position = (player.rect.centerx - GENERAL["health_bar_x_offset"],
        #                     player.rect.centery - GENERAL["health_bar_y_offset"] + 150)
        #     new_bar_position = bar_position - self.offset
        #     bar_x = new_bar_position[0]
        #     bar_y = new_bar_position[1]
        #     pygame.draw.rect(screen,
        #                      GENERAL["blue"],
        #                      (bar_x, bar_y,
        #                       player.energy_level, GENERAL["health_bar_height"]))

    def show_hitboxes(self, player=None, skull_collector=None, rusher=None, golem=None, bat=None,
                      fish=None, bullet=None, flaming_skull=None, skull=None, energy=None,
                      portal=None):
        """
        Draws hitboxes.
        Player, SkullCollector and Rusher need instances, others only need to be not None.
        """
        if player is not None:
            if not player.shoot:
                player_hitbox = pygame.draw.rect(player.base_image,
                                                 GENERAL["blue"],
                                                 pygame.Rect(PLAYER["hitbox"]),
                                                 2)
                player_hitbox.topleft -= self.offset
            elif player.shoot:
                player_hitbox = pygame.draw.rect(player.base_image_shoot,
                                                 GENERAL["blue"],
                                                 pygame.Rect(PLAYER["hitbox"]),
                                                 2)
                player_hitbox.topleft -= self.offset

        if skull_collector is not None:
            skull_collector_hitbox = pygame.draw.rect(skull_collector.image,
                                                      GENERAL["red"],
                                                      pygame.Rect(SKULL_COLLECTOR["hitbox"]),
                                                      2)
            skull_collector_hitbox.topleft -= self.offset

        if rusher is not None:
            rusher_hitbox = pygame.draw.rect(rusher.image,
                                             GENERAL["red"],
                                             pygame.Rect(RUSHER["hitbox"]),
                                             2)
            rusher_hitbox.topleft -= self.offset

        if golem is not None:
            golem_hitbox = pygame.draw.rect(golem.image,
                                            GENERAL["red"],
                                            pygame.Rect(GOLEM["hitbox"]),
                                            2)
            golem_hitbox.topleft -= self.offset

        if bat is not None:
            bat_hitbox = pygame.draw.rect(bat.image,
                                          GENERAL["red"],
                                          pygame.Rect(BAT["hitbox"]),
                                          2)
            bat_hitbox.topleft -= self.offset

        if fish is not None:
            fish_hitbox = pygame.draw.rect(fish.image,
                                           GENERAL["red"],
                                           pygame.Rect(FISH["hitbox"]),
                                           2)
            fish_hitbox.topleft -= self.offset

        if bullet is not None:
            for bullet in player_projectile_sprites:
                bullet_hitbox = pygame.draw.rect(bullet.image,
                                                 GENERAL["blue"],
                                                 pygame.Rect(BULLET["hitbox"]),
                                                 2)
                bullet_hitbox.topleft -= self.offset

        if flaming_skull is not None:
            for flaming_skull in enemy_projectile_sprites:
                flaming_skull_hitbox = pygame.draw.rect(flaming_skull.image,
                                                        GENERAL["red"],
                                                        pygame.Rect(FLAMING_SKULL["hitbox"]),
                                                        2)
                flaming_skull_hitbox.topleft -= self.offset

        if skull is not None:
            for skull in skull_sprites:
                skull_hitbox = pygame.draw.rect(skull.image,
                                                GENERAL["red"],
                                                pygame.Rect(SKULL["hitbox"]),
                                                2)
                skull_hitbox.topleft -= self.offset

        if energy is not None:
            for energy in energy_sprites:
                energy_hitbox = pygame.draw.rect(energy.image,
                                                 GENERAL["red"],
                                                 pygame.Rect(ENERGY["hitbox"]),
                                                 2)
                energy_hitbox.topleft -= self.offset

        if portal is not None:
            for portal in portal_sprites:
                portal_hitbox = pygame.draw.rect(portal.image,
                                                 GENERAL["blue"],
                                                 pygame.Rect(PORTAL["hitbox"]),
                                                 2)
                portal_hitbox.topleft -= self.offset
