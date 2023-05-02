import pygame as pygame

from utilities import all_sprites, enemy_sprites, get_direction


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, position, character):
        super().__init__(all_sprites, enemy_sprites)
        # References
        self.player = player

        # Sprites
        self.idle_sprites = character["idle_sprites"]
        self.idle_sprites_flipped = character["idle_sprites_flipped"]

        self.walk_sprites = character["walk_sprites"]
        self.walk_sprites_flipped = character["walk_sprites_flipped"]

        self.run_sprites = character["run_sprites"]
        self.run_sprites_flipped = character["run_sprites_flipped"]

        self.strike_sprites = character["strike_sprites"]
        self.strike_sprites_flipped = character["strike_sprites_flipped"]

        self.shoot_sprites = character["shoot_sprites"]
        self.shoot_sprites_flipped = character["shoot_sprites"]

        self.death_sprites = character["death_sprites"]

        # Image
        self.image = character["image"]
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = position
        # Hitbox
        self.hitbox = pygame.Rect(character["hitbox"])
        self.hitbox_offset_x = character["hitbox_offset_x"]
        self.hitbox_offset_y = character["hitbox_offset_y"]

        # States
        self.idle = character["idle"]
        self.walk = character["walk"]
        self.run = character["run"]
        self.strike = character["strike"]
        self.shoot = character["shoot"]
        self.death = character["death"]

        # Attributes
        self.position = pygame.math.Vector2(position)
        self.health = character["health"]
        self.damage = character["damage"]
        self.walk_speed = character["walk_speed"]
        self.run_speed = character["run_speed"]
        self.speed = self.walk_speed

        self.walk_duration = character["walk_duration"]
        self.run_duration = character["run_duration"]
        self.walk_distance = character["walk_distance"]
        self.run_distance = character["run_distance"]
        self.strike_distance = character["strike_distance"]
        self.shoot_distance = character["shoot_distance"]

        self.strike_tick = character["strike_tick"]
        self.shoot_tick = character["shoot_tick"]
        self.death_tick = character["death_tick"]

        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()

        self.flip_image = character["flip_image"]

        self.idle_ticks = 0
        self.walk_ticks = 0
        self.run_ticks = 0
        self.strike_ticks = 0
        self.shoot_ticks = 0
        self.death_ticks = 0

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

