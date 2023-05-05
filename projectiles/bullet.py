import math

import pygame

from settings.player_settings import BULLET
from sprites.projectile_sprites import BULLET_SPRITE
from utilities import all_sprites, all_projectile_sprites, player_projectile_sprites


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__(all_sprites, all_projectile_sprites, player_projectile_sprites)

        # Image
        self.image = BULLET_SPRITE
        # rect
        self.rect = self.image.get_rect(center=(x, y))
        # self.rect.center = (x, y)
        # Hitbox
        self.hitbox = self.rect.copy()

        # Attributes
        self.angle = angle
        self.speed = BULLET["speed"]
        self.damage = BULLET["damage"]
        self.x = x
        self.y = y

        self.x_velocity = math.cos(self.angle * (2 * math.pi / 360)) * self.speed
        self.y_velocity = math.sin(self.angle * (2 * math.pi / 360)) * self.speed

    def bullet_movement(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.bullet_movement()
        self.hitbox.center = self.rect.center
