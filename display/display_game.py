import os
import pygame
import sys

from sprites.interactives_sprites import DOOR_RED_SPRITES, DOOR_BLUE_SPRITES, DOOR_GREEN_SPRITES, \
    DOOR_YELLOW_SPRITES
from utilities.sprite_groups import all_sprites

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
        self.floor_rect = background.get_rect(topleft=GENERAL["origin"])
        self.offset = pygame.math.Vector2()

        self.door_red_sprites = DOOR_RED_SPRITES
        self.door_red_image = self.door_red_sprites[0]
        self.door_red_rect = self.door_red_image.get_rect()
        self.door_red_rect.bottom = GENERAL["y_min"] - 50
        self.door_red_rect.left = GENERAL["left_x_min"] + 250

        self.door_blue_sprites = DOOR_BLUE_SPRITES
        self.door_blue_image = self.door_blue_sprites[0]
        self.door_blue_rect = self.door_blue_image.get_rect()
        self.door_blue_rect.bottom = GENERAL["y_min"] - 50
        self.door_blue_rect.right = GENERAL["right_x_max"] - 250

        self.door_green_sprites = DOOR_GREEN_SPRITES
        self.door_green_image = self.door_green_sprites[0]
        self.door_green_rect = self.door_green_image.get_rect()
        self.door_green_rect.top = GENERAL["y_max"] + 50
        self.door_green_rect.left = GENERAL["left_x_min"] + 250

        self.door_yellow_sprites = DOOR_YELLOW_SPRITES
        self.door_yellow_image = self.door_yellow_sprites[0]
        self.door_yellow_rect = self.door_yellow_image.get_rect()
        self.door_yellow_rect.top = GENERAL["y_max"] + 50
        self.door_yellow_rect.right = GENERAL["right_x_max"] - 250

        self.door_group = [(self.door_red_image, self.door_red_rect),
                            (self.door_blue_image, self.door_blue_rect),
                            (self.door_green_image, self.door_green_rect),
                            (self.door_yellow_image, self.door_yellow_rect)]

        self.player = player

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

        # Blit doors
        for door in self.door_group:
            offset_pos = door[1].topleft - self.offset
            self.screen.blit(door[0], offset_pos)

        # Blit all sprites
        for sprite in all_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)

    def blit_level_objects(self):
        # Calculate offset
        self.offset.x = self.player.rect.centerx - GENERAL["half_width"]
        self.offset.y = self.player.rect.centery - GENERAL["half_height"]

        for door in self.door_group:
            offset_pos = door[1].topleft - self.offset
            self.screen.blit(door[0], offset_pos)



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
