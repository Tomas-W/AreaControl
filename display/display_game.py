import os
import pygame
import sys

from utilities.helpers import all_sprites

from settings.general_settings import GENERAL

from settings.player_settings import PLAYER
from settings.enemy_settings import SKULL_COLLECTOR, RUSHER
from settings.creeper_settings import BAT, FISH

from settings.interactives_settings import SKULL, ENERGY, HEALTH_POTION
from settings.projectile_settings import FLAMING_SKULL, BULLET, BOMB


base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


class DisplayGame(pygame.sprite.Group):
    """
    Shifts all Sprites by an offset to keep Player centered in Camera.
    Offset is calculated based on screen dimensions.
    """

    def __init__(self, screen, background, player, sound_is_on):
        super().__init__()
        self.screen = screen
        self.background = background
        self.player = player
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft=GENERAL["origin"])
        self.sound_is_on = sound_is_on

        self.bonus_ticks_list = [2000, 2100, 2600, 3000, 3000, 3500, 4000]  # time per wave

    def blit_all_sprites(self):
        """
        Blits all Sprites to the main screen with an offset so
            player is always centered.
        """
        # Calculate offset
        self.offset.x = self.player.rect.centerx - GENERAL["half_width"]
        self.offset.y = self.player.rect.centery - GENERAL["half_height"]

        # Blit the floor
        floor_offset = self.floor_rect.topleft - self.offset
        self.screen.blit(self.background, floor_offset)

        # Blit all sprites
        for sprite in all_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)

    @staticmethod
    def show_hitboxes(screen, player=None, skull_collector=False, rusher=False,
                      bat=False, fish=False,
                      bullet=False, bomb=False, flaming_skull=False,
                      skull=False, energy=False, health_potion=False):
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

            if health_potion:
                if item.name == "health_potion":
                    pygame.draw.rect(item.image,
                                     GENERAL["blue"],
                                     pygame.Rect(HEALTH_POTION["hitbox"]),
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
