import math
import pygame

from projectiles.flaming_skull import FlamingSkull

from utilities.sprite_groups import all_sprites, enemy_sprites
from utilities.game_physics import get_direction


class BaseEnemy(pygame.sprite.Sprite):
    """
    Base class to create an Enemy character.
    Contains all base attributes and methods.
    BaseEnemy instance is added to all_sprites and enemy_sprites ( pygam.sprite.Group() ).
    """
    def __init__(self, player, position, character):
        """
        :param player: Player() instance.
        :param position: Enemy spawn location Tuple(x, y) from settings dictionary.
        :param character: Settings dictionary.
        """
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

        # Sounds
        if character["attack_sound_path"] is not None:
            self.attack_sound = pygame.mixer.Sound(character["attack_sound_path"])
            self.attack_sound.set_volume(0.2)

        self.death_sound = pygame.mixer.Sound(character["death_sound_path"])
        self.death_sound.set_volume(0.2)
        self.played_death_sound = False

        # Offsets
        self.hitbox_offset_x = character["hitbox_offset_x"]
        self.hitbox_offset_y = character["hitbox_offset_y"]
        self.shoot_offset_x = character["shoot_offset_x"]
        self.shoot_offset_y = character["shoot_offset_y"]

        # States (active state)
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

        # State duration (fixed ime in ms, currently not used)
        self.idle_duration = character["idle_duration"]
        self.walk_duration = character["walk_duration"]
        self.run_duration = character["run_duration"]

        # State distance (trigger states by distance to Player)
        self.walk_distance = character["walk_distance"]
        self.run_distance = character["run_distance"]
        self.strike_distance = character["strike_distance"]
        self.shoot_distance = character["shoot_distance"]

        # Frame attributes
        self.frame = character["frame"]                 # current frame
        self.frame_ticks = character["frame_ticks"]     # frame 'clock'
        # How many ticks frames per frame
        self.spawn_ticks = character["spawn_ticks"]
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

        # Properties
        self.name = character["name"]

        self.position = pygame.math.Vector2(position)
        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()

        self.health = character["health"]
        self.damage = character["damage"]
        self.speed = character["speed"]
        self.walk_speed = character["walk_speed"]
        self.run_speed = character["run_speed"]

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

    def manage_idle_state(self):
        """
        Applies Enemy idle state and image properties.
        """
        self.set_idle_image()

    def manage_move_state(self):
        """
        Applies Rusher move state and image properties.
        """
        self.move_to_player()

        if self.walk:
            self.set_walk_image()

        elif self.run:
            self.set_run_image()

    def move_to_player(self):
        """
        Move towards Player by one unit of speed.
        """
        self.direction = get_direction(location_a=self.player.hitbox.center,
                                       location_b=self.rect.center)

        self.velocity = self.direction * self.speed
        self.position += self.velocity

        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def manage_strike_state(self):
        """
        Applies Rusher strike state and image properties.
        """
        if self.is_allowed_to_strike():
            self.strike_player()

        self.set_strike_image()

    def is_allowed_to_strike(self):
        """
        Checks if Rusher is allowed to strike Player depending on self.strike_frame.

        :return: Returns True if conditions are met (bool).
        """
        return self.frame == self.strike_frame\
            and self.frame_ticks == (self.strike_ticks // 2)\
            and not self.player.is_invincible

    def strike_player(self):
        """
        Deal strike damage to Player.
        """
        if self.player.sound_is_on:
            self.attack_sound.play()

        self.player.health -= self.damage

    def manage_shoot_state(self):
        """
        Applies SkullCollector shoot state and image properties.
        """
        if self.is_allowed_to_shoot():
            self.shoot_player()

        self.set_shoot_image()

    def is_allowed_to_shoot(self):
        """
        Checks if SkullCollector is allowed to shoot Player depending on self.shoot_frame.

        :return: Returns True if conditions are met (bool).
        """
        return self.frame == self.shoot_frame\
            and self.frame_ticks == (self.shoot_ticks // 2)

    def shoot_player(self):
        """
        Shoot Projectile towards Player.
        """
        # Set projectile in right spot on the SkullCollector image
        if self.flip_image:
            projectile_x = self.rect.centerx - self.shoot_offset_x

        else:
            projectile_x = self.rect.centerx + self.shoot_offset_x

        projectile_y = self.rect.centery + self.shoot_offset_y

        # Calculate angle to Player
        dx = self.player.rect.centerx - projectile_x
        dy = self.player.rect.centery - projectile_y
        angle = math.degrees(math.atan2(dy, dx))

        # Create projectile
        if self.name == "skull_collector":
            FlamingSkull(player=self.player,
                         x=projectile_x,
                         y=projectile_y,
                         angle=angle,
                         bomb_location=None)

    def play_death_sound(self):
        """
        Played death sound if Player.sound_is_on is True.
        """
        if self.death \
                and self.player.sound_is_on\
                and not self.played_death_sound:

            self.death_sound.play()
            self.played_death_sound = True

    def set_idle_image(self):
        """
        Sets correct image depending on animation length,
            frames per animation and
            self.flip_image.
        """
        # Resetting ticks
        if self.frame_ticks == self.idle_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Resetting animation
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
            self.flip_image.
        """
        # Resetting ticks
        if self.frame_ticks == self.walk_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Resetting animation
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
            self.flip_image.
        """
        # Resetting ticks
        if self.frame_ticks == self.run_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Resetting animation
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
            self.flip_image.
        """
        # Resetting ticks
        if self.frame_ticks == self.strike_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Resetting animation
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
            self.flip_image.
        """
        # Resetting ticks
        if self.frame_ticks == self.shoot_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Resetting animation
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
            self.flip_image.
        """
        if self.flip_image:
            self.image = self.death_sprites_flipped[self.frame]

        else:
            self.image = self.death_sprites[self.frame]
