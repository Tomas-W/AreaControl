import math

import pygame

from utilities.helpers import all_sprites, all_projectile_sprites, player_projectile_sprites, \
    enemy_projectile_sprites, bomb_sprites


class Projectile(pygame.sprite.Sprite):
    """
    Base class for Projectiles.

    Projectile is placed in correct location and
        moves in the shooting direction by its speed.

    A new Projectile can be created by passing in a dictionary.
    """
    def __init__(self, player, x, y, angle, projectile_name, bomb_location):
        super().__init__(all_sprites, all_projectile_sprites)
        # Player reference
        self.player = player

        # Sheet
        self.sprite_sheet = projectile_name["sprite_sheet"]
        # Image
        self.image = projectile_name["sprite"].copy()
        # rect
        self.rect = self.image.get_rect()
        self.rect.bottomright = x, y
        # Hitbox
        self.hitbox = pygame.Rect(projectile_name["hitbox"])
        self.hitbox_x_offset = projectile_name["hitbox_x_offset"]
        self.hitbox_y_offset = projectile_name["hitbox_y_offset"]

        # Sounds
        if projectile_name["spawn_sound_path"] is not None:
            self.spawn_sound = pygame.mixer.Sound(projectile_name["spawn_sound_path"])
            self.spawn_sound.set_volume(0.2)
        else:
            self.spawn_sound = None
        if projectile_name["death_sound_path"] is not None:
            self.death_sound = pygame.mixer.Sound(projectile_name["death_sound_path"])
            self.death_sound.set_volume(0.2)
        else:
            self.death_sound = None

        # Attributes
        self.name = projectile_name["name"]
        self.speed = projectile_name["speed"]
        self.damage = projectile_name["damage"]
        self.angle = angle
        self.x = x
        self.y = y
        self.x_velocity = math.cos(self.angle * (2 * math.pi / 360)) * self.speed
        self.y_velocity = math.sin(self.angle * (2 * math.pi / 360)) * self.speed

        self.bomb_location = bomb_location

        # frame attributes
        self.frame = projectile_name["frame"]
        self.frame_ticks = projectile_name["frame_ticks"]
        # ticks per frame
        self.image_ticks = projectile_name["image_ticks"]

        # PLAY SPAWN SOUND
        if self.spawn_sound is not None and self.player.sound_is_on:
            self.spawn_sound.play()

        # add to correct sprite list
        if self.name == "bullet":
            player_projectile_sprites.add(self)

        elif self.name == "flaming_skull":
            enemy_projectile_sprites.add(self)

        elif self.name == "bomb":
            bomb_sprites.add(self)

    def kill_self(self):
        # bomb has its own death and sound manager because of animation
        # play sound if it exists
        if self.death_sound is not None and not self.name == "bomb" and self.player.sound_is_on:
            self.death_sound.play()

        self.kill()

    def set_hitbox(self):
        """
        Aligns hitbox with SkullCollector rect.
        """
        self.hitbox.x = self.rect.x + self.hitbox_x_offset
        self.hitbox.y = self.rect.y + self.hitbox_y_offset

    def movement(self):
        """
        Updates position based on angle and speed.
        """
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y
