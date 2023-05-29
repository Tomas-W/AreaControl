from cmath import sin, cos, pi
from random import choice

import pygame

from interactives.base_pickup import PickUp
from settings.interactives_settings import COIN
from utilities import all_sprites, get_distance, get_direction, bat_sprites, fish_sprites, \
    all_creeper_sprites


class Creeper(pygame.sprite.Sprite):
    """
    Base class to create Creepers.
    Creepers spawn and rotate around their spawn point.
    When Player is in range, they go in chase mode and deal damage when colliding.
    If Player kills a Creeper, it drops a coin. Not when it suicides.
    """
    def __init__(self, player, creeper_name):
        super().__init__(all_sprites, all_creeper_sprites)
        # Reference to Player
        self.player = player

        # Sprites
        self.sprites = creeper_name["sprites"]
        self.sprites_flipped = creeper_name["sprites_flipped"]

        # Image
        self.image = creeper_name["image"].copy()
        self.image.set_alpha(0)
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = choice(creeper_name["start_position"])
        # Hitbox
        self.hitbox = pygame.Rect(creeper_name["hitbox"])

        # Sounds
        self.death_sound = pygame.mixer.Sound(creeper_name["death_sound_path"])
        self.death_sound.set_volume(0.2)
        self.played_death_sound = False

        # Offsets
        self.hitbox_offset_x = creeper_name["hitbox_offset_x"]
        self.hitbox_offset_y = creeper_name["hitbox_offset_y"]

        # States
        self.spawn = creeper_name["spawn"]
        self.idle = creeper_name["idle"]
        self.chase = creeper_name["chase"]
        self.strike = creeper_name["strike"]
        self.shoot = creeper_name["shoot"]
        self.death = creeper_name["death"]

        # State attributes
        self.chase_distance = creeper_name["chase_distance"]
        self.strike_distance = creeper_name["strike_distance"]
        self.shoot_distance = creeper_name["shoot_distance"]

        # Frame attributes
        self.frame = creeper_name["frame"]
        self.frame_ticks = creeper_name["frame_ticks"]
        self.spawn_ticks = creeper_name["spawn_ticks"]
        # how ticks frames per frame
        self.idle_ticks = creeper_name["idle_ticks"]
        self.chase_ticks = creeper_name["chase_ticks"]
        self.strike_ticks = creeper_name["strike_ticks"]
        self.shoot_ticks = creeper_name["shoot_ticks"]
        self.death_ticks = creeper_name["death_ticks"]
        # Action at what frame
        self.strike_frame = creeper_name["strike_frame"]
        self.shoot_frame = creeper_name["shoot_frame"]
        self.death_frame = creeper_name["death_frame"]

        self.flip_image = creeper_name["flip_image"]

        # Attributes
        self.position = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.name = creeper_name["name"]
        self.health = creeper_name["health"]
        self.damage = creeper_name["damage"]
        self.speed = creeper_name["speed"]
        self.idle_speed = creeper_name["idle_speed"]
        self.chase_speed = creeper_name["chase_speed"]
        self.circle_radius = creeper_name["circle_radius"]
        self.angle = choice(creeper_name["angle"])
        self.angle_adjustment = creeper_name["angle_adjustment"]
        self.spawn_opacity = creeper_name["spawn_opacity"]

        if self.name == "bat":
            bat_sprites.add(self)
        elif self.name == "fish":
            fish_sprites.add(self)

        # Misc
        self.spawned = True

    def set_hitbox(self):
        """
        Aligns hitbox with rect.
        """
        self.hitbox.left = self.rect.left + self.hitbox_offset_x
        self.hitbox.top = self.rect.top + self.hitbox_offset_y

    def set_state(self):
        # Hide in first frame to allow setting position
        if not self.spawned:
            self.image.set_alpha(255)
        if self.spawned:
            self.spawned = False

        if self.health <= 0:
            self.kill_self()

        # Once a Creeper chases, it chases indefinitely
        if not self.chase:
            distance_to_player = get_distance(location_a=self.player.hitbox.center,
                                              location_b=self.hitbox.center)

            if distance_to_player < self.chase_distance:
                self.chase = True
                self.idle = False
                self.frame_ticks = 0
                self.position = self.rect.center
                self.speed = self.chase_speed

    def manage_frames(self):
        """
        Updates frame_ticks and state tracking for animations.
        """
        self.frame_ticks += 1

    def should_image_flip(self):
        """
        Checks if Player is on the left or right side.
        Sets flip_image to True if player is on the Left.
        """
        if self.idle:
            if 0 < self.angle < 180:
                self.flip_image = True
            else:
                self.flip_image = False

        elif self.chase:
            if self.rect.centerx > self.player.rect.centerx:
                self.flip_image = True
            else:
                self.flip_image = False

    def manage_idle_state(self):
        self.circle_location()
        self.set_idle_image()

    def circle_location(self):
        """
        Moves Creeper in circular motion around its spawn position.
        """
        angle_radians = self.angle * pi / 180

        # Calculate the x and y coordinates of the sprite
        x = self.position[0] + self.circle_radius * cos(angle_radians)
        y = self.position[1] + self.circle_radius * sin(angle_radians)

        # Shift Creeper
        self.rect.center = (x.real, y.real)
        self.angle += self.angle_adjustment
        if self.angle == 360:
            self.angle = 0

    def manage_chase_state(self):
        self.move_to_player()

        if self.is_allowed_to_strike():
            self.strike_player()

        self.set_chase_image()

    def is_allowed_to_strike(self):
        """
        Checks if Creeper is allowed to strike Player.

        :return: Returns True if conditions are met (bool).
        """
        return self.hitbox.colliderect(self.player.hitbox) and not self.player.is_invincible

    def strike_player(self):
        # No points when Player kills Creeper
        self.player.health -= self.damage
        self.kill()

    def kill_self(self):
        # Play sound
        if not self.played_death_sound and self.player.sound_is_on:
            self.death_sound.play()

        # Spawn PickUp
        PickUp(player=self.player,
               position=self.rect.center,
               pickup_name=COIN)

        # Update Player kills
        self.player.kills[self.name] += 1
        self.kill()

    def move_to_player(self):
        """
        Move towards Player by one unit of speed.
        """
        # Get vectors
        self.direction = get_direction(location_a=self.player.hitbox.center,
                                       location_b=self.rect.center)
        # Move SkullCollector
        self.velocity = self.direction * self.speed
        self.position += self.velocity
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def set_idle_image(self):
        """
        Sets correct image depending on animation length,
            frames per animation and
            flip_image.
        """
        if self.frame_ticks == self.idle_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.sprites_flipped[self.frame]
        else:
            self.image = self.sprites[self.frame]

    def set_chase_image(self):
        """
        Sets correct image depending on animation length,
            frames per animation and
            flip_image.
        """
        if self.frame_ticks == self.chase_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.sprites_flipped[self.frame]
        else:
            self.image = self.sprites[self.frame]
