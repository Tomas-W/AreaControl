import pygame

from settings.projectile_settings import FIRE_SKULL, BULLET
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

    def custom_draw(self, screen, background, player):
        self.offset.x = player.rect.centerx - GENERAL["half_width"]
        self.offset.y = player.rect.centery - GENERAL["half_height"]

        # draw the floor
        floor_offset = self.floor_rect.topleft - self.offset
        screen.blit(background, floor_offset)

        for sprite in all_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)

    def show_bars(self, screen, player=None, health=None, skull=None, energy=None):
        if health is not None:
            bar_position = (player.rect.centerx - GENERAL["health_bar_x_offset"],
                            player.rect.centery - GENERAL["health_bar_y_offset"])
            new_bar_position = bar_position - self.offset
            bar_x = new_bar_position[0]
            bar_y = new_bar_position[1]
            pygame.draw.rect(screen,
                             GENERAL["green"],
                             (bar_x, bar_y,
                              player.health, GENERAL["health_bar_height"]))

        if skull is not None:
            bar_position = (player.rect.centerx - GENERAL["health_bar_x_offset"],
                            player.rect.centery - GENERAL["health_bar_y_offset"] + 75)
            new_bar_position = bar_position - self.offset
            bar_x = new_bar_position[0]
            bar_y = new_bar_position[1]
            pygame.draw.rect(screen,
                             GENERAL["red"],
                             (bar_x, bar_y,
                              player.skull_level, GENERAL["health_bar_height"]))

        if energy is not None:
            bar_position = (player.rect.centerx - GENERAL["health_bar_x_offset"],
                            player.rect.centery - GENERAL["health_bar_y_offset"] + 150)
            new_bar_position = bar_position - self.offset
            bar_x = new_bar_position[0]
            bar_y = new_bar_position[1]
            pygame.draw.rect(screen,
                             GENERAL["blue"],
                             (bar_x, bar_y,
                              player.energy_level, GENERAL["health_bar_height"]))

    def show_hitboxes(self, player=None, skull_collector=None, rusher=None, golem=None,
                      bullet=None, fire_skull=None, skull=None, energy=None, portal=None):
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

        if bullet is not None:
            for bullet in player_projectile_sprites:
                bullet_hitbox = pygame.draw.rect(bullet.image,
                                                 GENERAL["blue"],
                                                 pygame.Rect(BULLET["hitbox"]),
                                                 2)
                bullet_hitbox.topleft -= self.offset

        if fire_skull is not None:
            for fire_skull in enemy_projectile_sprites:
                fire_skull_hitbox = pygame.draw.rect(fire_skull.image,
                                                     GENERAL["red"],
                                                     pygame.Rect(FIRE_SKULL["hitbox"]),
                                                     2)
                fire_skull_hitbox.topleft -= self.offset

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
