import pygame as pygame

from utilities import all_sprites, enemy_sprites, get_direction


class Enemy(pygame.sprite.Sprite):
    """
    Base class to create Enemies.

    Contains all sprites, attributes and trackers.
    To create a new Enemy, pass in a dictionary.
    """
    def __init__(self, player, position, character):
        super().__init__(all_sprites, enemy_sprites)
        # References
        self.player = player

        # Sprites
        self.spawn_sprites = character["spawn_sprites"]

        self.idle_sprites = character["idle_sprites"]
        self.idle_sprites_flipped = character["idle_sprites_flipped"]

        self.walk_sprites = character["walk_sprites"]
        self.walk_sprites_flipped = character["walk_sprites_flipped"]

        self.run_sprites = character["run_sprites"]
        self.run_sprites_flipped = character["run_sprites_flipped"]

        self.strike_sprites = character["strike_sprites"]
        self.strike_sprites_flipped = character["strike_sprites_flipped"]

        self.shoot_sprites = character["shoot_sprites"]
        self.shoot_sprites_flipped = character["shoot_sprites_flipped"]

        self.death_sprites = character["death_sprites"]
        self.death_sprites_flipped = character["death_sprites_flipped"]

        # Image
        self.image = character["image"].copy()
        self.image_opacity = character["spawn_opacity"]
        self.image.set_alpha(self.image_opacity)
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = position
        # Hitbox
        self.hitbox = pygame.Rect(character["hitbox"])

        # Offsets
        self.hitbox_offset_x = character["hitbox_offset_x"]
        self.hitbox_offset_y = character["hitbox_offset_y"]
        self.shoot_offset_x = character["shoot_offset_x"]
        self.shoot_offset_y = character["shoot_offset_y"]

        # States
        self.spawn = character["spawn"]
        self.idle = character["idle"]
        self.walk = character["walk"]
        self.run = character["run"]
        self.strike = character["strike"]
        self.shoot = character["shoot"]
        self.death = character["death"]
        # Track states
        self.current_state = character["current_state"]
        self.last_state = character["last_state"]

        # State attributes
        self.idle_duration = character["idle_duration"]
        self.walk_duration = character["walk_duration"]
        self.run_duration = character["run_duration"]

        self.walk_distance = character["walk_distance"]
        self.run_distance = character["run_distance"]
        self.strike_distance = character["strike_distance"]
        self.shoot_distance = character["shoot_distance"]

        # Frame attributes
        self.frame = character["frame"]
        self.frame_ticks = character["frame_ticks"]
        self.spawn_ticks = character["spawn_ticks"]
        # How many ticks frames per frame
        self.idle_ticks = character["idle_ticks"]
        self.walk_ticks = character["walk_ticks"]
        self.run_ticks = character["run_ticks"]
        self.strike_ticks = character["strike_ticks"]
        self.shoot_ticks = character["shoot_ticks"]
        self.death_ticks = character["death_ticks"]
        # Action at what frame
        self.strike_frame = character["strike_frame"]
        self.shoot_frame = character["shoot_frame"]
        self.death_frame = character["death_frame"]
        self.flip_image = character["flip_image"]

        # Attributes
        self.name = character["name"]
        self.position = pygame.math.Vector2(position)
        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.health = character["health"]
        self.damage = character["damage"]
        self.walk_speed = character["walk_speed"]
        self.run_speed = character["run_speed"]
        self.speed = character["speed"]

    def set_hitbox(self):
        """
        Aligns hitbox with rect.
        """
        self.hitbox.left = self.rect.left + self.hitbox_offset_x
        self.hitbox.top = self.rect.top + self.hitbox_offset_y

    def manage_frames(self):
        """
        Updates frame_ticks and state tracking for animations.
        """
        self.frame_ticks += 1

        # Animation switch
        if self.current_state != self.last_state:
            self.frame_ticks = 0

        self.last_state = self.current_state

    def should_image_flip(self):
        """
        Checks if Player is on the left or right side.
        Sets flip_image to True if player is on the Left.
        """
        if self.rect.centerx > self.player.rect.centerx:
            self.flip_image = True
        else:
            self.flip_image = False

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
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def set_idle_image(self):
        """
        Sets correct image depending on animation length,
            frames per animation and
            flip_image.
        """
        if self.frame_ticks == self.idle_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.idle_sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.idle_sprites_flipped[self.frame]
        else:
            self.image = self.idle_sprites[self.frame]

    def set_walk_image(self):
        """
        Sets correct image depending on animation length,
            frames per animation and
            flip_image.
        """
        if self.frame_ticks == self.walk_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.walk_sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.walk_sprites_flipped[self.frame]
        else:
            self.image = self.walk_sprites[self.frame]

    def set_run_image(self):
        """
        Sets correct image depending on animation length,
            frames per animation and
            flip_image.
        """
        if self.frame_ticks == self.run_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.run_sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.run_sprites_flipped[self.frame]
        else:
            self.image = self.run_sprites[self.frame]

    def set_strike_image(self):
        """
        Sets correct image depending on animation length,
            frames per animation and
            flip_image.
        """
        if self.frame_ticks == self.strike_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.strike_sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.strike_sprites_flipped[self.frame]
        else:
            self.image = self.strike_sprites[self.frame]

    def set_shoot_image(self):
        """
        Sets correct image depending on animation length,
            frames per animation and
            flip_image.
        """
        if self.frame_ticks == self.shoot_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.shoot_sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.shoot_sprites_flipped[self.frame]
        else:
            self.image = self.shoot_sprites[self.frame]

    def set_death_image(self):
        """
        Sets correct image depending on animation length,
            frames per animation and
            flip_image.
        """
        if self.flip_image:
            self.image = self.death_sprites_flipped[self.frame]
        else:
            self.image = self.death_sprites[self.frame]
