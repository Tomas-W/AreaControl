import math
from math import atan2, sqrt, degrees

import pygame

from projectiles.bullet import Bullet

from utilities import player_sprite, all_sprites

from settings.general_settings import GENERAL
from settings.player_settings import PLAYER


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, player_sprite)
        # Starting position
        self.position = pygame.math.Vector2(PLAYER["start_position"])

        # Create sprites
        self.image = pygame.transform.rotozoom(
            pygame.image.load("images/player/player_pistol.png").convert_alpha(),
            False,
            PLAYER["size"])
        self.image_shoot = pygame.transform.rotozoom(
            pygame.image.load("images/player/player_pistol_fire.png").convert_alpha(),
            False,
            PLAYER["size"])

        # Base images for rotation purposes
        self.base_image = self.image.copy()
        self.base_image_shoot = self.image_shoot.copy()
        # Hitbox
        self.hitbox = self.base_image.get_rect(center=self.position)
        # Rect
        self.rect = self.hitbox.copy()

        # Attributes
        self.health = PLAYER["health"]
        self.speed = PLAYER["speed"]
        self.shoot = False
        self.new_location = None
        self.teleport_location = None
        self.is_invincible = False

        # Trackers
        self.shoot_cooldown = 0
        self.muzzle_flash_cooldown = 0
        self.new_location_ticks = 0
        self.invincible_ticks = 0
        self.invincible_image_ticks = 0

    def rotate_player(self):
        """
        Keeps player image directed at mouse position.
        """
        self.get_rotation_angle()

        self.rotate_player_image()

        self.rect = self.image.get_rect(center=self.hitbox.center)

    def get_rotation_angle(self):
        """
        Calculates and sets angle towards mouse.
        """
        self.mouse_position = pygame.mouse.get_pos()  # noqa
        # Distance between player and mouse
        self.dx_mouse_player = (self.mouse_position[0] - GENERAL["half_width"])  # noqa
        self.dy_mouse_player = (self.mouse_position[1] - GENERAL["half_height"])  # noqa
        # Pythagoras to get angle
        self.angle = degrees(atan2(self.dy_mouse_player,  # noqa
                                   self.dx_mouse_player))

    def rotate_player_image(self):
        """
        Rotates Player image towards mouse.
        """
        if self.muzzle_flash_cooldown == 0:
            # Normal image
            self.image = pygame.transform.rotate(self.base_image,
                                                 -self.angle)
        else:
            # Shooting image
            self.image = pygame.transform.rotate(self.base_image_shoot,
                                                 -self.angle)

    def get_move_input(self):
        """
        Listens for user inputs and sets Player direction and velocity.
        """
        # No movement when nothing pressed
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()
        # Axial movement and wall collision
        if keys[pygame.K_a]:
            # Detect walls
            if self.hitbox.left > GENERAL["level_left_x"]:
                self.velocity_x = -self.speed
        if keys[pygame.K_d]:
            # Detect walls
            if self.hitbox.right < GENERAL["level_right_x"]:
                self.velocity_x = self.speed  # noqa
        if keys[pygame.K_w]:
            if self.hitbox.top > GENERAL["level_top_y"]:
                self.velocity_y = -self.speed
        if keys[pygame.K_s]:
            # Detect walls
            if self.hitbox.bottom < GENERAL["level_bottom_y"]:
                self.velocity_y = self.speed  # noqa

        # Vertical movement adjust with Pythagoras
        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x /= sqrt(2)
            self.velocity_x /= sqrt(2)

    def move_player(self):
        """
        Moves player to new place.
        """
        # Update position
        self.position += pygame.math.Vector2(self.velocity_x,
                                             self.velocity_y)
        # Apply new positioning
        self.hitbox.center = self.position
        self.rect.center = self.hitbox.center

    def get_shoot_input(self):
        """
        Listens for user input and sets Player shoot property accordingly.
        """
        if pygame.mouse.get_pressed() == GENERAL["left_mouse_button"]:
            self.shoot = True
        else:
            self.shoot = False

    def manage_shooting(self):
        """
        Checks shooting requirements and
            updates trackers.
        """
        if self.shoot and not self.shoot_cooldown:
            self.shoot_projectile()
        # Update shoot cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        # Update muzzle flash cooldown
        if self.muzzle_flash_cooldown > 0:
            self.muzzle_flash_cooldown -= 1

    def shoot_projectile(self):
        """
        Created a Bullet projectile instance and
            gives it an angle.
        """
        self.shoot_cooldown = PLAYER["shoot_cooldown"]
        self.muzzle_flash_cooldown = PLAYER["muzzle_flash_cooldown"]

        # Calculate the starting position of the bullet based on the player rect and direction
        bullet_start_x = self.hitbox.centerx + ((214 * 0.4) / 2) * math.cos(
            self.angle * math.pi / 180)
        bullet_start_y = self.hitbox.centery + ((174 * 0.4) / 2) * math.sin(
            self.angle * math.pi / 180)

        # Adjust bullet location
        if 120 < self.angle < 180:
            bullet_start_y -= abs((120 + self.angle) * 0.03)

        if -120 < self.angle < 0:
            bullet_start_x -= abs((120 + self.angle) * 0.15)
            bullet_start_y -= abs((120 + self.angle) * 0.05)

        elif self.angle >= 0:
            bullet_start_x -= abs(self.angle // 30)
        else:
            bullet_start_y -= abs(self.angle // 30)

        # Create projectile
        Bullet(x=bullet_start_x,
               y=bullet_start_y,
               angle=self.angle)

    def manage_teleport(self):
        """
        Manages teleport trackers and sets Player's teleport location.
        """
        if self.new_location_ticks > 0:
            self.new_location_ticks += 1
            # Teleport Player
            if self.new_location_ticks == PLAYER["new_location_tick"]:
                self.rect.center = self.teleport_location
                self.hitbox.center = self.teleport_location
                self.position = pygame.Vector2(self.rect.center)
                self.new_location_ticks = 0

    def use_teleport(self):
        """
        Checks is Player used portal and updates attributes accordingly.
        """
        if self.new_location is not None:
            # Start countdown
            self.new_location_ticks += 1
            self.teleport_location = self.new_location
            self.new_location = None
            # Set invincibility
            self.is_invincible = True
            self.invincible_ticks += 1

    def manage_invincibility(self):
        """
        Manages Player invincibility after Portal used.
        """
        if self.invincible_ticks > 0:
            self.invincible_ticks += 1

            # Control Player image flickering
            self.invincible_image_ticks += 1
            if self.invincible_image_ticks == GENERAL["FPS"]:
                self.invincible_image_ticks = 0

            # Check is invincibility still lasts
            if self.invincible_ticks == PLAYER["invincibility_ticks"]:
                self.is_invincible = False
                self.invincible_ticks = 0

    def update(self):
        # Move (do not change order)
        self.rotate_player()
        self.get_move_input()
        self.move_player()

        # Shoot
        self.get_shoot_input()
        self.manage_shooting()

        # Start Teleport counter if Portal used
        self.manage_teleport()

        # Check if Portal is used
        self.use_teleport()

        # Apply invincibility after Portal use
        if self.is_invincible:
            self.set_invincibility_image()

        # Manage invincibility after Portal use
        self.manage_invincibility()

    def set_invincibility_image(self):
        """
        Checks self.invincible_image_ticks value and loads corresponding image.
        """
        if self.invincible_image_ticks < 5:
            self.image.set_alpha(225)
        elif self.invincible_image_ticks < 10:
            self.image.set_alpha(195)
        elif self.invincible_image_ticks < 15:
            self.image.set_alpha(165)
        elif self.invincible_image_ticks < 20:
            self.image.set_alpha(135)
        elif self.invincible_image_ticks < 25:
            self.image.set_alpha(105)
        elif self.invincible_image_ticks < 30:
            self.image.set_alpha(85)
        elif self.invincible_image_ticks < 35:
            self.image.set_alpha(105)
        elif self.invincible_image_ticks < 45:
            self.image.set_alpha(135)
        elif self.invincible_image_ticks < 45:
            self.image.set_alpha(165)
        elif self.invincible_image_ticks < 50:
            self.image.set_alpha(195)
        else:
            self.image.set_alpha(225)
