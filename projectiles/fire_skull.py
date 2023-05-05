import math

import pygame

from settings.enemy_projectile_settings import FIRE_SKULL
from sprites.projectile_sprites import FIRE_SKULL_SPRITE
from utilities import all_sprites, all_projectile_sprites, enemy_projectile_sprites


class FireSkull(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__(all_sprites, all_projectile_sprites, enemy_projectile_sprites)
        # Image
        self.image = FIRE_SKULL_SPRITE
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # Hitbox
        self.hitbox = pygame.Rect(FIRE_SKULL["hitbox"])
        self.hitbox_x_offset = FIRE_SKULL["hitbox_x_offset"]
        self.hitbox_y_offset = FIRE_SKULL["hitbox_y_offset"]

        # Attributes
        self.angle = angle
        self.speed = FIRE_SKULL["speed"]
        self.y = y
        self.x = x

        self.x_velocity = math.cos(self.angle * (2 * math.pi / 360)) * self.speed
        self.y_velocity = math.sin(self.angle * (2 * math.pi / 360)) * self.speed

        self.damage = FIRE_SKULL["damage"]

    def set_hitbox(self):
        """
        Aligns hitbox with SkullCollector rect.
        """
        self.hitbox.left = self.rect.left + self.hitbox_x_offset
        self.hitbox.top = self.rect.top + self.hitbox_y_offset

    def fire_skull_movement(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.set_hitbox()
        self.fire_skull_movement()
