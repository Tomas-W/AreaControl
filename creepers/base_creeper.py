from cmath import sin, cos, pi
from random import choice

import pygame

from utilities import all_sprites, get_distance, get_direction


class Creeper(pygame.sprite.Sprite):
    def __init__(self, player, creeper_name):
        super().__init__(all_sprites)
        # Reference to Player
        self.player = player

        # Sprites
        self.sprites = creeper_name["sprites"]
        self.sprites_flipped = creeper_name["sprites_flipped"]

        # Image
        self.image = creeper_name["image"]
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = choice(creeper_name["start_position"])
        # Hitbox
        self.hitbox = pygame.Rect(creeper_name["hitbox"])
        # Offsets
        self.hitbox_offset_x = creeper_name["hitbox_offset_x"]
        self.hitbox_offset_y = creeper_name["hitbox_offset_y"]

        # States
        self.idle = creeper_name["idle"]
        self.chase = creeper_name["chase"]
        self.strike = creeper_name["strike"]
        self.shoot = creeper_name["shoot"]
        self.death = creeper_name["death"]

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
        self.angle = creeper_name["angle"]

        # State attributes
        self.chase_distance = creeper_name["chase_distance"]
        self.strike_distance = creeper_name["strike_distance"]
        self.shoot_distance = creeper_name["shoot_distance"]

        # Frame attributes
        self.frame = creeper_name["frame"]
        self.frame_ticks = creeper_name["frame_ticks"]
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

    def set_hitbox(self):
        """
        Aligns hitbox with rect.
        """
        self.hitbox.left = self.rect.left + self.hitbox_offset_x
        self.hitbox.top = self.rect.top + self.hitbox_offset_y

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

    def set_state(self):
        distance_to_player = get_distance(location_a=self.player.hitbox.center,
                                          location_b=self.hitbox.center)
        if distance_to_player < 25:
            self.kill()

        if not self.chase:
            distance_to_player = get_distance(location_a=self.player.hitbox.center,
                                              location_b=self.hitbox.center)

            if distance_to_player < self.chase_distance:
                self.chase = True
                self.idle = False
                self.speed = self.chase_speed

    def manage_idle_state(self):
        self.circle_location()
        self.set_idle_image()

    def manage_chase_state(self):
        self.chase_player()
        self.set_chase_image()

    def circle_location(self):

        angle_radians = self.angle * pi / 180

        # Calculate the x and y coordinates of the sprite
        x = self.position[0] + self.circle_radius * cos(angle_radians)
        y = self.position[1] + self.circle_radius * sin(angle_radians)

        self.rect.center = (x.real, y.real)
        self.angle += 1
        if self.angle == 360:
            self.angle = 0

    def chase_player(self):
        """
        Move towards Player by one unit of speed.
        """
        # Get vectors
        self.direction = get_direction(location_a=self.player.hitbox.center,
                                       location_b=self.rect.center)
        # Move SkullCollector
        self.velocity = self.direction * self.speed
        self.position += self.velocity
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def set_idle_image(self):
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
        if self.frame_ticks == self.chase_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.sprites_flipped[self.frame]
        else:
            self.image = self.sprites[self.frame]
