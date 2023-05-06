import math

import pygame

from utilities import all_sprites, all_projectile_sprites, player_projectile_sprites, \
    enemy_projectile_sprites


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, projectile_name):
        super().__init__(all_sprites, all_projectile_sprites)

        # Image
        self.image = projectile_name["sprite"]
        # rect
        self.rect = self.image.get_rect(center=(x, y))
        # Hitbox
        self.hitbox = projectile_name["hitbox"]
        self.hitbox_x_offset = projectile_name["hitbox_x_offset"]
        self.hitbox_y_offset = projectile_name["hitbox_y_offset"]

        # Attributes
        self.name = projectile_name["name"]
        self.speed = projectile_name["speed"]
        self.damage = projectile_name["damage"]
        self.angle = angle
        self.x = x
        self.y = y
        self.x_velocity = math.cos(self.angle * (2 * math.pi / 360)) * self.speed
        self.y_velocity = math.sin(self.angle * (2 * math.pi / 360)) * self.speed

        # add to correct sprite list
        if self.name == "bullet":
            player_projectile_sprites.add(self)
        elif self.name == "fire_skull":
            enemy_projectile_sprites.add(self)

    def set_hitbox(self):
        """
        Aligns hitbox with SkullCollector rect.
        """
        print(self.hitbox.left)
        self.hitbox.x = self.rect.x + self.hitbox_x_offset
        self.hitbox.y = self.rect.y + self.hitbox_y_offset

    def movement(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        # self.set_hitbox()
        self.movement()
