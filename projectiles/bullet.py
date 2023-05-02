import math

import pygame

from settings.player_settings import BULLET
from utilities import all_sprites, all_projectile_sprites, player_projectile_sprites


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__(all_sprites, all_projectile_sprites, player_projectile_sprites)

        # Image
        self.image = pygame.image.load("images/projectiles/bullet_blue.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,
                                               False,
                                               BULLET["size"])
        # rect
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # Hitbox
        self.hitbox = self.rect.copy()

        # Attributes
        self.angle = angle
        self.speed = BULLET["speed"]
        self.y = y
        self.x = x

        self.x_velocity = math.cos(self.angle * (2 * math.pi / 360)) * self.speed
        self.y_velocity = math.sin(self.angle * (2 * math.pi / 360)) * self.speed

        self.damage = BULLET["damage"]
        self.spawn_time = pygame.time.get_ticks()
        # To not use bullet offset, need invisibility
        self.is_visible = False
        self.image.set_alpha(0)

    def bullet_movement(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        # Display bullets
        if not self.is_visible:
            if pygame.time.get_ticks() - self.spawn_time > BULLET["invisibility_time"]:
                self.is_visible = True
                self.image.set_alpha(255)

        self.bullet_movement()
        self.hitbox.center = self.rect.center
