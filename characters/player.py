import math

import pygame

from projectiles.bomb import Bomb
from projectiles.bullet import Bullet

from utilities.sprite_groups import player_sprite, all_sprites

from settings.general_settings import GENERAL, PLAYER_SIZE
from settings.player_settings import PLAYER


class Player(pygame.sprite.Sprite):
    def __init__(self, sound_is_on):
        super().__init__(all_sprites, player_sprite)
        # Starting position
        self.position = pygame.math.Vector2(PLAYER["start_position"])

        # Sprites
        self.image = PLAYER["sprite"]
        self.image_shoot = PLAYER["shoot_sprite"]

        # Base images for rotation purposes
        self.base_image = self.image.copy()
        self.base_image_shoot = self.image_shoot.copy()
        # Hitbox
        self.hitbox = self.base_image.get_rect(center=self.position)
        # Rect
        self.rect = self.hitbox.copy()

        # Sounds
        self.sound_is_on = sound_is_on
        self.hit_sound = pygame.mixer.Sound(PLAYER["hit_sound_path"])
        self.hit_sound.set_volume(0.2)

        self.add_health_sound = pygame.mixer.Sound(PLAYER["add_health_sound_path"])
        self.add_health_sound.set_volume(0.2)

        self.death_sound = pygame.mixer.Sound(PLAYER["death_sound_path"])
        self.death_sound.set_volume(0.2)

        # States
        self.shoot = PLAYER["shoot"]
        self.bomb = PLAYER["bomb"]
        self.is_invincible = PLAYER["is_invincible"]
        # Track states
        self.shoot_cooldown = PLAYER["shoot_cooldown"]
        self.muzzle_flash_cooldown = PLAYER["muzzle_flash_cooldown"]
        self.bomb_cooldown = PLAYER["bomb_cooldown"]
        self.new_location_ticks = 0
        self.invincible_ticks = 0
        self.invincible_image_ticks = 0
        # State attributes
        self.new_location = PLAYER["new_location"]
        self.teleport_location = PLAYER["teleport_location"]

        # Buy menu
        self.buy_multiplier = PLAYER["buy_multiplier"]
        self.buy_multiplier_addition = PLAYER["buy_multiplier_addition"]
        self.bullet_upgrade_cost = PLAYER["bullet_upgrade_cost"]
        self.bomb_upgrade_cost = PLAYER["bomb_upgrade_cost"]
        self.buy_bomb_cost = PLAYER["buy_bomb_cost"]
        self.buy_portal_cost = PLAYER["buy_portal_cost"]

        # Attributes
        self.name = PLAYER["name"]
        self.speed = PLAYER["speed"]
        self.health = PLAYER["health"]
        self.max_health = PLAYER["max_health"]
        self.health_potion_boost = PLAYER["health_potion_boost"]

        self.skull_level = PLAYER["skull_level"]
        self.energy_level = PLAYER["energy_level"]
        self.coin_level = PLAYER["coin_level"]
        self.wave_level = PLAYER["wave_level"]
        self.total_bombs = PLAYER["total_bombs"]
        self.total_portals = PLAYER["total_portals"]
        self.total_health_potions = PLAYER["total_health_potions"]

        # Misc
        self.item_ticks = 0  # To add buy delay
        self.shooting_offset = PLAYER["sprite_width"] * PLAYER_SIZE // 2.5
        self.health_checker = self.health
        self.kills = {
            "skull_collector": 0,
            "rusher": 0,
            "bat": 0,
            "fish": 0,
        }
        self.kill_points = {
            "skull_collector": PLAYER["skull_collector_points"],
            "rusher": PLAYER["rusher_points"],
            "bat": PLAYER["bat_points"],
            "fish": PLAYER["fish_points"],
        }
        self.highscore_name = ""

    # ################################################################ #
    # ############################ MOVING ############################ #
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
        # Get angle
        self.angle = math.degrees(math.atan2(self.dy_mouse_player,  # noqa
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
        if keys[pygame.K_a] and self.hitbox.left > GENERAL["level_left_x"]:
            self.velocity_x = -self.speed

        if keys[pygame.K_d] and self.hitbox.right < GENERAL["level_right_x"]:
            self.velocity_x = self.speed  # noqa

        if keys[pygame.K_w] and self.hitbox.top > GENERAL["level_top_y"]:
            self.velocity_y = -self.speed

        if keys[pygame.K_s] and self.hitbox.bottom < GENERAL["level_bottom_y"]:
            self.velocity_y = self.speed  # noqa

        # Vertical movement adjust
        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x /= math.sqrt(2)
            self.velocity_x /= math.sqrt(2)

    def move_player(self):
        """
        Moves player to new position.
        """
        # Update position
        self.position += pygame.math.Vector2(self.velocity_x,
                                             self.velocity_y)
        # Apply new positioning
        self.hitbox.center = self.position
        self.rect.center = self.hitbox.center

    # ################################################################## #
    # ############################ SHOOTING ############################ #
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
            self.fire_bullet()
        # Update shoot cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        # Update muzzle flash cooldown
        if self.muzzle_flash_cooldown > 0:
            self.muzzle_flash_cooldown -= 1

    def adjust_projectile_position(self):
        """
        Adjusts spawn location of the projectile.
        Aligns bullet spawn location with pistol muzzle.
        First applies coordinate offset and then
            angle offset.

        :return: Projectile spawn position (tuple int).
        """
        # Convert the player angle to radians
        angle_radians = math.radians(self.angle)

        # Calculate the offset position
        offset_x = self.shooting_offset * math.cos(angle_radians)
        offset_y = self.shooting_offset * math.sin(angle_radians)

        # Calculate the spawn position based on the offset
        bullet_spawn_x = self.rect.centerx + offset_x
        bullet_spawn_y = self.rect.centery + offset_y

        # Adjust bullet location depending on angle
        if 120 < self.angle < 180:
            bullet_spawn_y -= abs((120 + self.angle) * 0.05)

        elif 100 < self.angle < 120:
            bullet_spawn_y -= abs((120 + self.angle) * 0.06)

        elif self.angle >= 0:
            bullet_spawn_x -= abs(self.angle // 30)

        elif -120 < self.angle < 0:
            bullet_spawn_x -= abs((120 + self.angle) * 0.15)
            bullet_spawn_y -= abs((120 + self.angle) * 0.05)

        else:
            bullet_spawn_y -= abs(self.angle // 30)

        return bullet_spawn_x, bullet_spawn_y

    def fire_bullet(self):
        """
        Created a Bullet projectile instance and
            gives it an angle.
        """
        self.shoot_cooldown = int(PLAYER["shoot_cooldown"])
        self.muzzle_flash_cooldown = PLAYER["muzzle_flash_cooldown"]

        bullet_start_x, bullet_start_y = self.adjust_projectile_position()

        Bullet(player=self,
               x=bullet_start_x,
               y=bullet_start_y,
               angle=self.angle)

    def get_bomb_input(self):
        """
        Listens for user input and sets Player Bomb properties accordingly.
        """
        if pygame.mouse.get_pressed() == GENERAL["right_mouse_button"]:
            self.bomb = True

        else:
            self.bomb = False

    def manage_bombing(self):
        """
        Checks bombing requirements and
            updates trackers.
        """
        if self.bomb and not self.bomb_cooldown and self.total_bombs > 0:
            self.total_bombs -= 1
            self.bomb_cooldown = PLAYER["bomb_cooldown"]
            self.throw_bomb()

        if self.bomb_cooldown > 0:
            self.bomb_cooldown -= 1

    def throw_bomb(self):
        """
        Created a Bomb projectile instance,
            gives it an angle and
            a location to explode at.
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x, mouse_y = (self.rect.centerx - GENERAL["half_width"] + mouse_x,
                            self.rect.centery - GENERAL["half_height"] + mouse_y)

        bomb_start_x, bomb_start_y = self.adjust_projectile_position()

        Bomb(player=self,
             x=bomb_start_x,
             y=bomb_start_y,
             angle=self.angle,
             bomb_location=(mouse_x, mouse_y))

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

    def manage_health_potions(self):
        keys = pygame.key.get_pressed()
        # Consume health potion
        if keys[pygame.K_q]:
            if self.total_health_potions > 0 and self.item_ticks == 0 and self.health < self.max_health:
                self.total_health_potions -= 1
                self.health = min(self.health + self.health_potion_boost,
                                  self.max_health)
                self.item_ticks = 15

    def manage_hit_sounds(self):
        if self.health < self.health_checker and self.sound_is_on:
            # Player has been hit
            self.hit_sound.play()

        elif self.health > self.health_checker and self.sound_is_on:
            # Player used health potion
            self.add_health_sound.play()

        self.health_checker = self.health

    def get_score(self):
        """
        G
        Returns Players final score after utilities has ended.
        Multiplies Enemy kills with theirs corresponding points.

        :return: Players total score (int).
        """
        player_score = 0
        for (key, val), (key2, val2) in zip(self.kills.items(), self.kill_points.items()):
            player_score += val * val2

        return player_score

    def update(self):
        # Move (do not change order)
        self.rotate_player()
        self.get_move_input()
        self.move_player()

        # Fire Bullet
        self.get_shoot_input()
        self.manage_shooting()
        # Throw Bomb
        self.get_bomb_input()
        self.manage_bombing()

        # Start Teleport counter if Portal used
        self.manage_teleport()
        # Check if Portal is used
        self.use_teleport()
        # Apply invincibility after Portal use
        if self.is_invincible:
            self.set_invincibility_image()
        # Manage invincibility after Portal use
        self.manage_invincibility()

        # Items
        self.manage_health_potions()
        if self.item_ticks > 0:
            self.item_ticks -= 1

        # Sounds
        self.manage_hit_sounds()

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
